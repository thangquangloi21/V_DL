from PyQt5.QtWidgets import QGridLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import QSize
from View.TopView.MenuBar.menu_bar import MenuBar
from View.TopView.LogoVision.logo_vision import LogoVision
from View.TopView.TabBar.tab_bar import TabBar
from View.TopView.ToolBar.tool_bar import ToolBar
from View.MainView.main_window import MainWindow
from View.common_view.vision_frame import VisionFrame


class TopView(VisionFrame):
    logo_vision: LogoVision = None
    tabBar: TabBar = None
    toolBar: ToolBar = None
    tool_bar = None
    menu_bar: MenuBar = None
    horizontalSp: QSpacerItem
    grid_topView: QGridLayout

    def __init__(self, parent, main_window, camera_manager):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.camera_manager = camera_manager
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("background: transparent")  # rgb(179,179,179);")# '''border: 1px solid blue;
        self.setMinimumSize(QSize(0, 95))
        self.grid_topView = QGridLayout(self)

    def setup_view(self):
        self.setup_logo_vision()
        self.setup_menu_bar()
        self.setup_tool_bar()
        self.setup_tab_bar()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_topView.addWidget(self.logo_vision, 0, 0, 2, 1)
        self.grid_topView.addWidget(self.menu_bar, 0, 1, 1, 2)
        self.grid_topView.addWidget(self.toolBar, 1, 1, 1, 1)
        self.grid_topView.addWidget(self.tabBar, 0, 3, 2, 1)

        # Hàng
        self.grid_topView.setRowStretch(0, 1)
        self.grid_topView.setRowStretch(1, 1)

        # Cột
        self.grid_topView.setColumnStretch(0, 1)
        self.grid_topView.setColumnStretch(1, 1)
        self.grid_topView.setColumnStretch(2, 1)

    def setup_logo_vision(self):
        self.logo_vision = LogoVision(parent=self)

    def setup_menu_bar(self):
        self.menu_bar = MenuBar(parent=self, main_window=self.main_window, camera_manager=self.camera_manager)

    def setup_tab_bar(self):
        self.tabBar = TabBar(parent=self, main_window=self.main_window)

    def setup_tool_bar(self):
        self.toolBar = ToolBar(parent=self, main_window=self.main_window)
