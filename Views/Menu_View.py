from PyQt6.QtGui import QIcon

from PySide6.QtCore import Qt

from Views.Neural_Network_View import Neural_Network_View
from Views.Testing_View import Testing_View
from Views.Training_View import Training_View
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QListWidget, QPushButton, QMainWindow,QHBoxLayout
from PySide6.QtGui import QIcon

class Menu_View(QMainWindow):
    def __init__(self):
        super().__init__()
        print("init view")

    def init_ui(self):
        # Set window title and size
        self.setWindowTitle('ForgePlex')
        self.resize(500, 300)
        self.setFixedWidth(500)
        self.setFixedHeight(300)
        self.setWindowIcon(QIcon('Icons\\Icon1.png'))

        # Create central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)  # This is the main layout

        # Create and style widgets
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Search...')
        self.search_bar.setStyleSheet('padding: 5px; font-size: 16px;')

        self.list_widget = QListWidget()
        self.list_widget.setAlternatingRowColors(True)
        self.list_widget.setStyleSheet("""
            QListWidget {
                font-size: 16px; 
                background-color: #ffffff; 
                border: 1px solid #cccccc; 
                color: #333333;
            }
            QListWidget::item:alternate {
                background: #f9f9f9;
            }
            QListWidget::item:selected {
                background-color: #e1e1e1;
            }
            QListWidget::item:hover {
                background-color: #f5f5f5;
            }
        """)

        # Button Styling and Horizontal Layout
        button_layout = QHBoxLayout()  # This is the horizontal layout for buttons
        button_style = 'QPushButton {padding: 8px; font-size: 14px; margin: 2px;}'  # Slightly smaller buttons

        self.train_button = QPushButton('Train Existing')
        self.train_button.setStyleSheet(button_style)
        self.create_button = QPushButton('Create New')
        self.create_button.setStyleSheet(button_style)
        self.test_button = QPushButton('Test')
        self.test_button.setStyleSheet(button_style)
        self.options_button = QPushButton('Options')
        self.options_button.setStyleSheet(button_style)

        # Adding buttons to the horizontal layout
        button_layout.addWidget(self.create_button)
        button_layout.addWidget(self.test_button)
        button_layout.addWidget(self.train_button)
        button_layout.addWidget(self.options_button)

        # Add widgets to the main layout
        main_layout.addWidget(self.search_bar, alignment=Qt.AlignTop)
        main_layout.addWidget(self.list_widget)
        main_layout.addLayout(button_layout)  # Add the horizontal layout of buttons to the main layout

        # Connect buttons
        self.create_button.clicked.connect(self.handle_neural_network_menu_btn)
        self.test_button.clicked.connect(self.handle_testing_menu_btn)
        self.train_button.clicked.connect(self.handle_training_menu_btn)

        # UI setup code...
        if self.controller:
            self.controller.update_network_list()
        else:
            print('Controller not set, unable to populate network list.')

    def handle_training_menu_btn(self):
        selected_network = self.get_selected_network()
        if selected_network is not None:
            self.controller.open_training_menu(selected_network)

    def handle_neural_network_menu_btn(self):
        self.controller.open_network_menu()

    def handle_testing_menu_btn(self):
        selected_network = self.get_selected_network()
        if selected_network is not None:
            self.controller.open_testing_menu()

    def set_controller(self, controller):
        self.controller = controller
        # Now that the controller is set, call init_ui or any setup that depends on the controller.
        self.init_ui()


    def handle_options_btn(self):
        pass






    def get_selected_network(self):
        selected_items = self.list_widget.selectedItems()
        if selected_items:  # Check if the list is not empty
            selected_item = selected_items[0].text()
            print("Selected item:", selected_item)
            return selected_item









