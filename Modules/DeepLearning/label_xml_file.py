from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement
from lxml import etree

from PyQt5.QtGui import QImage
from CONSTANT.constant import XML_EXT
import json
from pathlib import Path
from CONSTANT.constant import DEFAULT_ENCODING
import os
from xml.dom import minidom
# from View.MainView.main_window import MainWindow


class LabelXmlFile(object):
    suffix = XML_EXT

    def __init__(self, main_window, filename=None):
        self.main_window: MainWindow = main_window
        self.shapes = ()
        self.image_path = None
        self.image_data = None
        self.verified = False

    def save_create_xml_format(self, output_file_name, shapes, image_path):
        # duong dan image
        image_path = image_path
        # folder
        image_folder_name = os.path.basename(os.path.dirname(image_path))
        # file name image
        image_file_name = os.path.basename(image_path)
        # shapes: list_label_info
        shapes = shapes
        # shape image
        image = QImage()
        image.load(image_path)
        image_shape = [image.height(), image.width(),
                       1 if image.isGrayscale() else 3]
        # write
        writer = CreateMLWriter(folder_name=image_folder_name, image_name=image_file_name,
                                img_size=image_shape, shapes=shapes, output_file=output_file_name,
                                local_img_path=image_path)
        writer.verified = self.verified
        writer.write_xml()
        writer.write_json()

    def load_xml_format(self, xml_path):
        try:
            self.main_window.middle_view.main_show.rectangele_process.delete_all_label()
            self.main_window.middle_view.main_show.rectangele_process.khoi_tao()
        except Exception as er:
            return
        xml_reader = LoadMLReader(file_path=xml_path)
        shapes = xml_reader.get_shapes()
        for label_info in shapes:
            label_info[2] = self.convert_coordinate_on_real_image_to_on_view_label(point_real_image=label_info[2])
            label_info[2] = self.convert_tuple_qpoint_to_tuple_scale(label_info[2])
            print(label_info)
        print(shapes)
        self.main_window.middle_view.main_show.rectangele_process.load_labels(list_info_label=shapes)

    def convert_list_label_info_scale_to_point(self, list_label):
        print(f"tesst{list_label}")
        list_label_with_coor_is_point = []
        for label_info in list_label:
            print(label_info)
            tmp = label_info.copy()
            coordinate_on_show_label = self.convert_tuple_scale_to_tuple_qpoint(label_info[2])
            print("point on window:: ", coordinate_on_show_label)
            coordinate_on_real_image = self.convert_coordinate_on_view_label_to_on_real_image(
                point_on_window=coordinate_on_show_label)
            tmp[2] = coordinate_on_real_image
            list_label_with_coor_is_point.append(tmp)
        return list_label_with_coor_is_point

    # write
    def convert_tuple_scale_to_tuple_qpoint(self, tuple_coordinate_scale: tuple):
        width_pixel_view = self.main_window.middle_view.main_show.show_image_label.width()
        height_pixel_view = self.main_window.middle_view.main_show.show_image_label.height()
        print(width_pixel_view)
        print((height_pixel_view))
        list_coordinate = list(tuple_coordinate_scale)
        list_corr = list_coordinate.copy()
        try:
            tuple_coordinate_qpoint = (
                int(list_corr[0] * width_pixel_view), int(list_corr[1] * height_pixel_view),
                int(list_corr[2] * width_pixel_view), int(list_corr[3] * height_pixel_view)
            )
        except:
            return
        # self.top_left, self.bottom_right = self.convert_tuple_to_two_qpoint(tuple_coordinate_current)
        return tuple_coordinate_qpoint

    def convert_coordinate_on_view_label_to_on_real_image(self, point_on_window):
        current_width_label_show = self.main_window.middle_view.main_show.show_image_label.width()
        current_height_label_show = self.main_window.middle_view.main_show.show_image_label.height()
        width, height, depth = self.main_window.middle_view.main_show.shapes_image

        print("window:: ", current_width_label_show, current_height_label_show)
        print("image:: ", width, height)

        point = point_on_window
        point_start_x = int(point[0] / current_width_label_show * width)
        point_start_y = int(point[1] / current_height_label_show * height)
        point_end_x = int(point[2] / current_width_label_show * width)
        point_end_y = int(point[3] / current_height_label_show * height)

        new_point_in_real_image = (point_start_x, point_start_y, point_end_x, point_end_y)
        return new_point_in_real_image

    # read
    def convert_coordinate_on_real_image_to_on_view_label(self, point_real_image):
        current_width_label_show = self.main_window.middle_view.main_show.show_image_label.width()
        current_height_label_show = self.main_window.middle_view.main_show.show_image_label.height()
        width, height, depth = self.main_window.middle_view.main_show.shapes_image

        print("window:: ", current_width_label_show, current_height_label_show)
        print("image:: ", width, height)

        point = point_real_image
        point_start_x = int(point[0] * current_width_label_show / width)
        point_start_y = int(point[1] * current_height_label_show / height)
        point_end_x = int(point[2] * current_width_label_show / width)
        point_end_y = int(point[3] * current_height_label_show / height)

        new_point_on_window = (point_start_x, point_start_y, point_end_x, point_end_y)
        return new_point_on_window

    def convert_tuple_qpoint_to_tuple_scale(self, tuple_qpoint_coordinate: tuple):
        width_pixel_view = self.main_window.middle_view.main_show.show_image_label.width()
        height_pixel_view = self.main_window.middle_view.main_show.show_image_label.height()
        list_coordinate = list(tuple_qpoint_coordinate)
        try:
            list_coordinate_scale = [
                list_coordinate[0] / width_pixel_view, list_coordinate[1] / height_pixel_view,
                list_coordinate[2] / width_pixel_view, list_coordinate[3] / height_pixel_view
            ]
        except:
            return
        return tuple(list_coordinate_scale)

    def toggle_verify(self):
        self.verified = not self.verified

    ''' ttf is disable
    def load(self, filename):
        import json
        with open(filename, 'rb') as f:
                data = json.load(f)
                imagePath = data['imagePath']
                imageData = b64decode(data['imageData'])
                lineColor = data['lineColor']
                fillColor = data['fillColor']
                shapes = ((s['label'], s['points'], s['line_color'], s['fill_color'])\
                        for s in data['shapes'])
                # Only replace data after everything is loaded.
                self.shapes = shapes
                self.imagePath = imagePath
                self.imageData = imageData
                self.lineColor = lineColor
                self.fillColor = fillColor

    def save(self, filename, shapes, imagePath, imageData, lineColor=None, fillColor=None):
        import json
        with open(filename, 'wb') as f:
                json.dump(dict(
                    shapes=shapes,
                    lineColor=lineColor, fillColor=fillColor,
                    imagePath=imagePath,
                    imageData=b64encode(imageData)),
                    f, ensure_ascii=True, indent=2)
    '''

    @staticmethod
    def is_label_file(filename):
        file_suffix = os.path.splitext(filename)[1].lower()
        return file_suffix == LabelXmlFile.suffix

    @staticmethod
    def convert_points_to_bnd_box(points):
        x_min = float('inf')
        y_min = float('inf')
        x_max = float('-inf')
        y_max = float('-inf')
        for p in points:
            x = p[0]
            y = p[1]
            x_min = min(x, x_min)
            y_min = min(y, y_min)
            x_max = max(x, x_max)
            y_max = max(y, y_max)
        if x_min < 1:
            x_min = 1

        if y_min < 1:
            y_min = 1

        return int(x_min), int(y_min), int(x_max), int(y_max)


ENCODE_METHOD = DEFAULT_ENCODING


class CreateMLWriter:
    def __init__(self, folder_name, image_name, img_size, shapes, output_file, segmented=0, database_src='Unknown',
                 local_img_path=None):
        self.folder_name = folder_name
        self.image_name = image_name
        self.local_img_path = local_img_path
        self.database_src = database_src
        self.img_size = img_size
        self.segmented = segmented
        self.box_list = []
        self.shapes = shapes
        self.output_file = output_file
        self.verified = False

    def write_xml(self):
        # print(self.shapes)
        # create a xml document
        root = minidom.Document()
        # create data tag as root tag
        annotation = root.createElement('annotation')
        root.appendChild(annotation)
        # create child tag of data tag
        folder = root.createElement('folder')
        annotation.appendChild(folder)
        filename = root.createElement("filename")
        annotation.appendChild(filename)
        path = root.createElement('path')
        annotation.appendChild(path)
        source = root.createElement('source')
        annotation.appendChild(source)
        size = root.createElement('size')
        annotation.appendChild(size)
        segmented = root.createElement('segmented')
        annotation.appendChild(segmented)

        # create child tag of items
        folder_text = root.createTextNode(f'{self.folder_name}')  # name_folder
        folder.appendChild(folder_text)
        filename_text = root.createTextNode(f'{self.image_name}')  # name_file
        filename.appendChild(filename_text)
        path_Text = root.createTextNode(f'{self.local_img_path}')
        path.appendChild(path_Text)
        # source
        database = root.createElement("database")
        database_text = root.createTextNode(f'{self.database_src}')
        database.appendChild(database_text)
        source.appendChild(database)
        # size
        width = root.createElement("width")
        width_text = root.createTextNode(f'{self.img_size[1]}')  # width image
        width.appendChild(width_text)
        size.appendChild(width)

        height = root.createElement("height")
        height_text = root.createTextNode(f'{self.img_size[0]}')  # width image
        height.appendChild(height_text)
        size.appendChild(height)

        depth = root.createElement("depth")
        depth_text = root.createTextNode(f'{self.img_size[2]}')  # width image
        depth.appendChild(depth_text)
        size.appendChild(depth)
        # segmented
        segmented_text = root.createTextNode(f'{self.segmented}')
        segmented.appendChild(segmented_text)
        # object
        # [['soup', True, (104, 88, 216, 221), None, None], ['chicken', True, (309, 148, 393, 305), None, None]]
        for label in self.shapes:
            object_ = root.createElement('object')

            name_label = root.createElement('name')
            name_label_text = root.createTextNode(f'{label[0]}')
            name_label.appendChild(name_label_text)
            object_.appendChild(name_label)

            pose = root.createElement("pose")
            pose_text = root.createTextNode('Unspecified')
            pose.appendChild(pose_text)
            object_.appendChild(pose)

            truncated = root.createElement('truncated')
            truncated_text = root.createTextNode('0')
            truncated.appendChild(truncated_text)
            object_.appendChild(truncated)

            difficult = root.createElement('difficult')
            difficult_text = root.createTextNode('0')
            difficult.appendChild(difficult_text)
            object_.appendChild(difficult)
            # bnd_box
            bnd_box = root.createElement('bndbox')

            x_min = root.createElement('xmin')
            x_min_text = root.createTextNode(f'{label[2][0]}')
            x_min.appendChild(x_min_text)
            bnd_box.appendChild(x_min)

            y_min = root.createElement('ymin')
            y_min_text = root.createTextNode(f'{label[2][1]}')
            y_min.appendChild(y_min_text)
            bnd_box.appendChild(y_min)

            x_max = root.createElement('xmax')
            x_max_text = root.createTextNode(f'{label[2][2]}')
            x_max.appendChild(x_max_text)
            bnd_box.appendChild(x_max)

            y_max = root.createElement('ymax')
            y_max_text = root.createTextNode(f'{label[2][3]}')
            y_max.appendChild(y_max_text)
            bnd_box.appendChild(y_max)

            object_.appendChild(bnd_box)
            # color
            color = root.createElement('color')
            color_text = root.createTextNode(label[3])
            color.appendChild(color_text)
            object_.appendChild(color)

            annotation.appendChild(object_)
        # create a new XML file
        mydata = root.toprettyxml(indent="\t")
        output_file = self.output_file + '.xml'
        with open(output_file, "w", encoding='utf-8') as file:
            file.write(mydata)
            file.close()

    def write_json(self):
        output_file = self.output_file + '.json'
        if os.path.isfile(output_file):
            with open(output_file, "r") as file:
                input_data = file.read()
                output_dict = json.loads(input_data)
        else:
            output_dict = []

        output_image_dict = {
            "image": self.image_name,
            "annotations": []
        }

        for shape in self.shapes:
            # points = shape["points"]
            points = shape[2]

            x1 = points[0]
            y1 = points[1]
            x2 = points[2]
            y2 = points[3]

            height, width, x, y = self.calculate_coordinates(x1, x2, y1, y2)

            shape_dict = {
                # "label": shape["label"],
                "label": shape[0],
                "color": shape[3],
                "coordinates": {
                    "x": x,
                    "y": y,
                    "width": width,
                    "height": height
                }
            }
            output_image_dict["annotations"].append(shape_dict)

        # check if image already in output
        exists = False
        for i in range(0, len(output_dict)):
            if output_dict[i]["image"] == output_image_dict["image"]:
                exists = True
                output_dict[i] = output_image_dict
                break

        if not exists:
            output_dict.append(output_image_dict)

        Path(output_file).write_text(json.dumps(output_dict), ENCODE_METHOD)

    def calculate_coordinates(self, x1, x2, y1, y2):
        if x1 < x2:
            x_min = x1
            x_max = x2
        else:
            x_min = x2
            x_max = x1
        if y1 < y2:
            y_min = y1
            y_max = y2
        else:
            y_min = y2
            y_max = y1
        width = x_max - x_min
        if width < 0:
            width = width * -1
        height = y_max - y_min
        # x and y from center of rect
        x = x_min + width / 2
        y = y_min + height / 2
        return height, width, x, y


class LoadMLReader:
    def __init__(self, file_path):
        # shapes type:
        # [label, (x_start, y_start, x_end, y_end), color, matrix]
        self.shapes = []
        self.file_path = file_path
        self.verified = False
        try:
            self.parse_xml()
        except:
            pass

    def get_shapes(self):
        return self.shapes

    def add_shape_xml(self, label, bnd_box, difficult, color):
        x_min = int(float(bnd_box.find('xmin').text))
        y_min = int(float(bnd_box.find('ymin').text))
        x_max = int(float(bnd_box.find('xmax').text))
        y_max = int(float(bnd_box.find('ymax').text))
        points = (x_min, y_min, x_max, y_max)
        color = color
        self.shapes.append([label, True, points, color, None, difficult])

    def parse_xml(self):
        assert self.file_path.endswith(XML_EXT), "Unsupported file format"
        parser = etree.XMLParser(encoding=ENCODE_METHOD)
        xml_tree = ElementTree.parse(self.file_path, parser=parser).getroot()
        filename = xml_tree.find('filename').text
        try:
            verified = xml_tree.attrib['verified']
            if verified == 'yes':
                self.verified = True
        except KeyError:
            self.verified = False

        for object_iter in xml_tree.findall('object'):
            bnd_box = object_iter.find("bndbox")
            label = object_iter.find('name').text
            color = object_iter.find('color').text
            # Add chris
            difficult = False
            if object_iter.find('difficult') is not None:
                difficult = bool(int(object_iter.find('difficult').text))
            self.add_shape_xml(label, bnd_box, difficult, color)
        return True
