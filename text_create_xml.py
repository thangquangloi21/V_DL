from xml.dom import minidom
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
object_ = root.createElement('object')
annotation.appendChild(object_)

# create child tag of items
folder_text = root.createTextNode('2022_09_06')  # name_folder
folder.appendChild(folder_text)
filename_text = root.createTextNode('2022_09_06_00_04_16-Roto_weighing.jpg')  # name_file
filename.appendChild(filename_text)
path_Text = root.createTextNode('./2022_09_06_00_04_16-Roto_weighing.jpg')
path.appendChild(path_Text)
# source
database = root.createElement("database")
database_text = root.createTextNode('Unknown')
database.appendChild(database_text)
source.appendChild(database)
# size
width = root.createElement("width")
width_text = root.createTextNode('2592')    # width image
width.appendChild(width_text)
size.appendChild(width)

height = root.createElement("height")
height_text = root.createTextNode('1944')    # width image
height.appendChild(height_text)
size.appendChild(height)

depth = root.createElement("depth")
depth_text = root.createTextNode('1')    # width image
depth.appendChild(depth_text)
size.appendChild(depth)
# segmented
segmented_text = root.createTextNode('0')
segmented.appendChild(segmented_text)
# object
name_label = root.createElement('name_label')
name_label_text = root.createTextNode('input_name_label')
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
bnd_box = root.createElement('bnd_box')

x_min = root.createElement('xmin')
x_min_text = root.createTextNode('32')
x_min.appendChild(x_min_text)
bnd_box.appendChild(x_min)

y_min = root.createElement('ymin')
y_min_text = root.createTextNode('26')
y_min.appendChild(y_min_text)
bnd_box.appendChild(y_min)

x_max = root.createElement('xmax')
x_max_text = root.createTextNode('2436')
x_max.appendChild(x_max_text)
bnd_box.appendChild(x_max)

y_max = root.createElement('ymax')
y_max_text = root.createTextNode('1849')
y_max.appendChild(y_max_text)
bnd_box.appendChild(y_max)

object_.appendChild(bnd_box)
# create a new XML file
mydata = root.toprettyxml(indent ="\t")
myxmlfile = open("items2.xml", "w")
myxmlfile.write(mydata)
myxmlfile.close()