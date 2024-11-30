import sys


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QIntValidator, QRegularExpressionValidator, QIcon
from PyQt6.QtWidgets import QMainWindow, QSlider, QWidget


class Neural_Network_View(QMainWindow):
    def __init__(self):
        super().__init__()




    def init_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 1055)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(535, 1055))
        MainWindow.setMaximumSize(QtCore.QSize(535, 1055))
        MainWindow.setStyleSheet("/* General Styles */\n"
                                 "QWidget {\n"
                                 "    font:  \"Segoe UI Semibold\";\n"
                                 "}\n"
                                 "\n"
                                 "/* Labels */\n"
                                 "QLabel {\n"
                                 "    font-size: 10pt;\n"
                                 "    color: rgb(99, 99, 99);\n"
                                 "font-weight: bold;\n"
                                 "}\n"
                                 "/* Combo Boxes */\n"
                                 "QComboBox {\n"
                                 "    font-size: 10pt;\n"
                                 "    padding: 5px 10px; /* Increased padding */\n"
                                 "    qproperty-alignment: \'AlignCenter\'; /* This may not work in some versions of Qt */\n"
                                 "    background-color: #ffffff; /* White background */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "    border-radius: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::drop-down {\n"
                                 "    subcontrol-origin: padding;\n"
                                 "    subcontrol-position: top right;\n"
                                 "    width: 15px;\n"
                                 "    border-left-width: 1px;\n"
                                 "    border-left-color: darkgray;\n"
                                 "    border-left-style: solid; /* just a single line */\n"
                                 "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                 "    border-bottom-right-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox QAbstractItemView {\n"
                                 "    text-align: center;\n"
                                 "    background-color: #ffffff; /* White background */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "}\n"
                                 "\n"
                                 "/* Push Buttons */\n"
                                 "QPushButton {\n"
                                 "    font-size: 10pt; /* Increased font size */\n"
                                 "    padding: 4px 4px; /* Increased padding */\n"
                                 "    background-color: #ffffff; /* White background */\n"
                                 "    color: #333333; /* Dark gray text color */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "    border-radius: 4px;\n"
                                 "    transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effects */\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #dadbde; /* Light gray when pressed */\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #3daee9; /* Primary accent color */\n"
                                 "    color: #ffffff; /* White text color when hovered */\n"
                                 "    border: 1px solid #3daee9; /* Blue border when hovered */\n"
                                 "}\n"
                                 "\n"
                                 "/* Text Browser */\n"
                                 "QTextBrowser {\n"
                                 "    font-size: 10pt;\n"
                                 "    color: #333333; /* Dark gray text color */\n"
                                 "    background-color: #ffffff; /* White background */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "}\n"
                                 "\n"
                                 "/* Group Boxes */\n"
                                 "QGroupBox {\n"
                                 "    font-size: 10pt;\n"
                                 "    background-color: #f2f2f2; /* Light gray background for the tab content area */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "    border-radius: 4px;\n"
                                 "    margin-top: 15px; /* Add margin between group boxes */\n"
                                 "}\n"
                                 "\n"
                                 "/* Line Edits */\n"
                                 "QLineEdit {\n"
                                 "    font-size: 10pt;\n"
                                 "    padding: 5px 10px; /* Increased padding */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "    border-radius: 4px;\n"
                                 "    background-color: #ffffff; /* White background */\n"
                                 "}\n"
                                 "\n"
                                 "/* Spin Boxes */\n"
                                 "QSpinBox, QDoubleSpinBox {\n"
                                 "    font-size: 10pt;\n"
                                 "    padding: 5px 10px; /* Increased padding */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "    border-radius: 4px;\n"
                                 "    background-color: #ffffff; /* White background */\n"
                                 "}\n"
                                 "\n"
                                 "QSpinBox::up-button, QDoubleSpinBox::up-button {\n"
                                 "    width: 20px; /* Adjusted width */\n"
                                 "    height: 14px; /* Adjusted height */\n"
                                 "    padding: 0px; /* Removed padding */\n"
                                 "    margin: 0px; /* Ensure no margins are applied */\n"
                                 "    background-color: #dcdcdc; /* Slightly lighter gray background */\n"
                                 "    border-radius: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QSpinBox::down-button, QDoubleSpinBox::down-button {\n"
                                 "    width: 20px; /* Adjusted width */\n"
                                 "    height: 14px; /* Adjusted height */\n"
                                 "    padding: 0px; /* Removed padding */\n"
                                 "    margin: 0px; /* Ensure no margins are applied */\n"
                                 "    background-color: #e0e0e0; /* Light gray background */\n"
                                 "    border-radius: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover,\n"
                                 "QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover {\n"
                                 "    background-color: #3daee9; /* Primary accent color */\n"
                                 "    color: #ffffff; /* White text color when hovered */\n"
                                 "    border: 1px solid #3daee9; /* Blue border when hovered */\n"
                                 "}\n"
                                 "\n"
                                 "QSpinBox::up-arrow, QDoubleSpinBox::up-arrow {\n"
                                 "    image: url(:/icons/up-arrow.png); /* Path to your custom up arrow icon */\n"
                                 "    width: 8px; /* Adjusted width */\n"
                                 "    height: 8px; /* Adjusted height */\n"
                                 "    margin: auto;\n"
                                 "}\n"
                                 "\n"
                                 "QSpinBox::down-arrow, QDoubleSpinBox::down-arrow {\n"
                                 "    image: url(:/icons/down-arrow.png); /* Path to your custom down arrow icon */\n"
                                 "    width: 8px; /* Adjusted width */\n"
                                 "    height: 8px; /* Adjusted height */\n"
                                 "    margin: auto;\n"
                                 "}\n"
                                 "\n"
                                 "/* Check Boxes */\n"
                                 "QCheckBox {\n"
                                 "    font-size: 10pt;\n"
                                 "    padding: 3px 8px; /* Adjusted padding to be more consistent */\n"
                                 "    spacing: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator {\n"
                                 "    width: 16px;\n"
                                 "    height: 16px;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:checked {\n"
                                 "    background-color: #3daee9; /* Primary accent color */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:unchecked {\n"
                                 "    background-color: #ffffff; /* White background */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:hover {\n"
                                 "    border: 1px solid #3daee9;\n"
                                 "}\n"
                                 "\n"
                                 "/* Sliders */\n"
                                 "QSlider {\n"
                                 "    min-height: 20px;\n"
                                 "    max-height: 20px;\n"
                                 "    margin: 3px 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::groove:horizontal {\n"
                                 "    border: 1px solid #bbb; /* Light gray border */\n"
                                 "    background-color: #f2f2f2; /* Light gray background */\n"
                                 "    height: 6px;\n"
                                 "    border-radius: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle:horizontal {\n"
                                 "    background-color: #3daee9; /* Primary accent color */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "    width: 15px;\n"
                                 "    height: 15px;\n"
                                 "    margin: -5px 0;\n"
                                 "    border-radius: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle:horizontal:hover {\n"
                                 "    background-color: #5dc0ef; /* Lighter blue */\n"
                                 "    border: 1px solid #3daee9;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::sub-page:horizontal {\n"
                                 "    background-color: #3daee9; /* Primary accent color */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "    height: 6px;\n"
                                 "    border-radius: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "/* Specific Element Styles */\n"
                                 "#title_label {\n"
                                 "    font-size: 25pt;\n"
                                 "    font-weight: bold;\n"
                                 "    color: #333333; /* Dark gray text color */\n"
                                 "    padding: 10px;\n"
                                 "    background-color: #f2f2f2; /* Light gray background */\n"
                                 "    border: 0px solid #c0c0c0; /* Light gray border */\n"
                                 "    border-radius: 5px;\n"
                                 "    text-align: center; /* Centered text */\n"
                                 "}\n"
                                 "\n"
                                 "#layers_tab::pane {\n"
                                 "    background-color: #f2f2f2; /* Light gray background for the tab content area */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "}\n"
                                 "\n"
                                 "#main_button {\n"
                                 "    font-size: 12pt;\n"
                                 "font-weight: bold;\n"
                                 "    padding: 8px 16px; /* Increased padding */\n"
                                 "    background-color: #ffffff; /* White background */\n"
                                 "    color: #333333; /* Dark gray text color */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "    border-radius: 4px;\n"
                                 "    transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effects */\n"
                                 "}\n"
                                 "\n"
                                 "#main_button:pressed {\n"
                                 "    background-color: #dadbde; /* Light gray when pressed */\n"
                                 "}\n"
                                 "\n"
                                 "#main_button:hover {\n"
                                 "    background-color: #3daee9; /* Primary accent color */\n"
                                 "    color: #ffffff; /* White text color when hovered */\n"
                                 "    border: 1px solid #3daee9; /* Blue border when hovered */\n"
                                 "}\n"
                                 "\n"
                                 "/* Tab Bar Styles */\n"
                                 "QTabBar::tab {\n"
                                 "    background-color: white; /* Light blue background */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "    border-bottom-color: transparent; /* Makes the bottom border invisible */\n"
                                 "    border-top-left-radius: 4px; /* Rounded corners on the top-left */\n"
                                 "    border-top-right-radius: 4px; /* Rounded corners on the top-right */\n"
                                 "    padding: 8px 15px; /* Increased padding to make tabs bigger */\n"
                                 "    margin-right: 2px; /* Space between tabs */\n"
                                 "    font-size: 10pt; /* Increased font size */\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:selected {\n"
                                 "    background-color: #5dc0ef; /* Lighter blue */\n"
                                 "    color: #ffffff; /* White text color for selected tab */\n"
                                 "    border-color: #3daee9; /* Darker border color for the selected tab */\n"
                                 "    border-bottom-color: #ffffff; /* Light gray background for the tab content area */\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:hover {\n"
                                 "    background-color: #3daee9; /* Primary accent color */\n"
                                 "    color: #ffffff; /* White text color for hovered tab */\n"
                                 "}\n"
                                 "\n"
                                 "QTabWidget::pane {\n"
                                 "    background-color: #ffffff; /* White background for the tab content area */\n"
                                 "    border: 1px solid #c0c0c0; /* Light gray border */\n"
                                 "    border-radius: 4px;\n"
                                 "    padding: 10px; /* Padding inside the tab content area */\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 520, 1151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.fields_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.fields_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.fields_layout.setContentsMargins(10, 10, 10, 0)
        self.fields_layout.setObjectName("fields_layout")
        self.title_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.fields_layout.addWidget(self.title_label)
        self.fields_frame = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fields_frame.sizePolicy().hasHeightForWidth())
        self.fields_frame.setSizePolicy(sizePolicy)
        self.fields_frame.setAutoFillBackground(True)
        self.fields_frame.setStyleSheet("fields_frame:Qframe {\n"
                                        "\n"
                                        "background: rgb(249, 249, 249)\n"
                                        "}")
        self.fields_frame.setObjectName("fields_frame")
        self.layers_tab = QtWidgets.QTabWidget(parent=self.fields_frame)
        self.layers_tab.setGeometry(QtCore.QRect(30, 280, 431, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layers_tab.sizePolicy().hasHeightForWidth())
        self.layers_tab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.layers_tab.setFont(font)
        self.layers_tab.setStyleSheet("")
        self.layers_tab.setDocumentMode(False)
        self.layers_tab.setTabsClosable(False)
        self.layers_tab.setObjectName("layers_tab")
        self.layer1 = QtWidgets.QWidget()
        self.layer1.setObjectName("layer1")
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.layer1)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(30, 10, 401, 368))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.arch_form1 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.arch_form1.setContentsMargins(0, 5, 0, 5)
        self.arch_form1.setHorizontalSpacing(30)
        self.arch_form1.setVerticalSpacing(20)
        self.arch_form1.setObjectName("arch_form1")
        self.type_label_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.type_label_1.setFont(font)
        self.type_label_1.setObjectName("type_label_1")
        self.arch_form1.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.type_label_1)
        self.type_entry_1 = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_entry_1.sizePolicy().hasHeightForWidth())
        self.type_entry_1.setSizePolicy(sizePolicy)
        self.type_entry_1.setObjectName("type_entry_1")
        self.arch_form1.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.type_entry_1)
        self.activation_label_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.activation_label_1.setFont(font)
        self.activation_label_1.setObjectName("activation_label_1")
        self.arch_form1.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.activation_label_1)
        self.activation_entry_1 = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.activation_entry_1.sizePolicy().hasHeightForWidth())
        self.activation_entry_1.setSizePolicy(sizePolicy)
        self.activation_entry_1.setMinimumSize(QtCore.QSize(100, 0))
        self.activation_entry_1.setObjectName("activation_entry_1")
        self.arch_form1.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.activation_entry_1)
        self.kernel_label_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.kernel_label_1.setFont(font)
        self.kernel_label_1.setObjectName("kernel_label_1")
        self.arch_form1.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.kernel_label_1)
        self.kernel_entry_1 = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kernel_entry_1.sizePolicy().hasHeightForWidth())
        self.kernel_entry_1.setSizePolicy(sizePolicy)
        self.kernel_entry_1.setObjectName("kernel_entry_1")
        self.arch_form1.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.kernel_entry_1)
        self.filters_label_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.filters_label_1.setFont(font)
        self.filters_label_1.setObjectName("filters_label_1")
        self.arch_form1.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.filters_label_1)
        self.filters_entry_1 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filters_entry_1.sizePolicy().hasHeightForWidth())
        self.filters_entry_1.setSizePolicy(sizePolicy)
        self.filters_entry_1.setObjectName("filters_entry_1")
        self.arch_form1.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.filters_entry_1)
        self.pool_label_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.pool_label_1.setFont(font)
        self.pool_label_1.setObjectName("pool_label_1")
        self.arch_form1.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pool_label_1)
        self.pool_entry_1 = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pool_entry_1.sizePolicy().hasHeightForWidth())
        self.pool_entry_1.setSizePolicy(sizePolicy)
        self.pool_entry_1.setObjectName("pool_entry_1")
        self.arch_form1.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pool_entry_1)
        self.dense_label_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.dense_label_1.setFont(font)
        self.dense_label_1.setObjectName("dense_label_1")
        self.arch_form1.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dense_label_1)
        self.flat_label_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.flat_label_1.setFont(font)
        self.flat_label_1.setObjectName("flat_label_1")
        self.arch_form1.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.flat_label_1)
        self.flat_box_1 = QtWidgets.QCheckBox(parent=self.formLayoutWidget_3)
        self.flat_box_1.setText("")
        self.flat_box_1.setObjectName("flat_box_1")
        self.arch_form1.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.flat_box_1)
        self.dense_entry_1 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dense_entry_1.sizePolicy().hasHeightForWidth())
        self.dense_entry_1.setSizePolicy(sizePolicy)
        self.dense_entry_1.setObjectName("dense_entry_1")
        self.arch_form1.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dense_entry_1)
        self.formLayoutWidget_11 = QtWidgets.QWidget(parent=self.layer1)
        self.formLayoutWidget_11.setGeometry(QtCore.QRect(20, 320, 381, 221))
        self.formLayoutWidget_11.setObjectName("formLayoutWidget_11")
        self.reg_form_1 = QtWidgets.QFormLayout(self.formLayoutWidget_11)
        self.reg_form_1.setContentsMargins(10, 10, 10, 10)
        self.reg_form_1.setHorizontalSpacing(30)
        self.reg_form_1.setVerticalSpacing(20)
        self.reg_form_1.setObjectName("reg_form_1")
        self.dropout_label_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.dropout_label_1.setFont(font)
        self.dropout_label_1.setObjectName("dropout_label_1")
        self.reg_form_1.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dropout_label_1)
        self.drop_box_1 = QtWidgets.QHBoxLayout()
        self.drop_box_1.setSpacing(30)
        self.drop_box_1.setObjectName("drop_box_1")
        self.drop_slider_1 = QtWidgets.QSlider(parent=self.formLayoutWidget_11)
        self.drop_slider_1.setMaximumSize(QtCore.QSize(400, 26))
        self.drop_slider_1.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        self.drop_slider_1.setFont(font)
        self.drop_slider_1.setMaximum(100)
        self.drop_slider_1.setSingleStep(5)
        self.drop_slider_1.setPageStep(5)
        self.drop_slider_1.setSliderPosition(10)
        self.drop_slider_1.setTracking(True)
        self.drop_slider_1.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.drop_slider_1.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.drop_slider_1.setTickInterval(5)
        self.drop_slider_1.setObjectName("drop_slider_1")
        self.drop_box_1.addWidget(self.drop_slider_1)
        self.drop_perc_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.drop_perc_1.setFont(font)
        self.drop_perc_1.setObjectName("drop_perc_1")
        self.drop_box_1.addWidget(self.drop_perc_1)
        self.reg_form_1.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.drop_box_1)
        self.l1_label_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.l1_label_1.setFont(font)
        self.l1_label_1.setObjectName("l1_label_1")
        self.reg_form_1.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l1_label_1)
        self.l1_box_1 = QtWidgets.QHBoxLayout()
        self.l1_box_1.setSpacing(30)
        self.l1_box_1.setObjectName("l1_box_1")
        self.l1_slider_1 = QtWidgets.QSlider(parent=self.formLayoutWidget_11)
        self.l1_slider_1.setMaximumSize(QtCore.QSize(400, 26))
        self.l1_slider_1.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        self.l1_slider_1.setFont(font)
        self.l1_slider_1.setMaximum(100)
        self.l1_slider_1.setSingleStep(5)
        self.l1_slider_1.setPageStep(5)
        self.l1_slider_1.setSliderPosition(10)
        self.l1_slider_1.setTracking(True)
        self.l1_slider_1.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.l1_slider_1.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.l1_slider_1.setTickInterval(5)
        self.l1_slider_1.setObjectName("l1_slider_1")
        self.l1_box_1.addWidget(self.l1_slider_1)
        self.l1_perc_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.l1_perc_1.setFont(font)
        self.l1_perc_1.setObjectName("l1_perc_1")
        self.l1_box_1.addWidget(self.l1_perc_1)
        self.reg_form_1.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.l1_box_1)
        self.l2_label_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.l2_label_1.setFont(font)
        self.l2_label_1.setObjectName("l2_label_1")
        self.reg_form_1.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l2_label_1)
        self.l2_box_1 = QtWidgets.QHBoxLayout()
        self.l2_box_1.setSpacing(30)
        self.l2_box_1.setObjectName("l2_box_1")
        self.l2_slider_1 = QtWidgets.QSlider(parent=self.formLayoutWidget_11)
        self.l2_slider_1.setMaximumSize(QtCore.QSize(400, 26))
        self.l2_slider_1.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        self.l2_slider_1.setFont(font)
        self.l2_slider_1.setMaximum(100)
        self.l2_slider_1.setSingleStep(5)
        self.l2_slider_1.setPageStep(5)
        self.l2_slider_1.setSliderPosition(10)
        self.l2_slider_1.setTracking(True)
        self.l2_slider_1.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.l2_slider_1.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.l2_slider_1.setTickInterval(5)
        self.l2_slider_1.setObjectName("l2_slider_1")
        self.l2_box_1.addWidget(self.l2_slider_1)
        self.l2_perc_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.l2_perc_1.setFont(font)
        self.l2_perc_1.setObjectName("l2_perc_1")
        self.l2_box_1.addWidget(self.l2_perc_1)
        self.reg_form_1.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.l2_box_1)
        self.batch_label_1 = QtWidgets.QLabel(parent=self.formLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.batch_label_1.setFont(font)
        self.batch_label_1.setObjectName("batch_label_1")
        self.reg_form_1.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.batch_label_1)
        self.batch_entry_1 = QtWidgets.QCheckBox(parent=self.formLayoutWidget_11)
        self.batch_entry_1.setText("")
        self.batch_entry_1.setObjectName("batch_entry_1")
        self.reg_form_1.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.batch_entry_1)
        self.layers_tab.addTab(self.layer1, "")
        self.layer2 = QtWidgets.QWidget()
        self.layer2.setObjectName("layer2")
        self.formLayoutWidget_13 = QtWidgets.QWidget(parent=self.layer2)
        self.formLayoutWidget_13.setGeometry(QtCore.QRect(20, 320, 381, 210))
        self.formLayoutWidget_13.setObjectName("formLayoutWidget_13")
        self.reg_form_2 = QtWidgets.QFormLayout(self.formLayoutWidget_13)
        self.reg_form_2.setContentsMargins(10, 10, 10, 10)
        self.reg_form_2.setHorizontalSpacing(30)
        self.reg_form_2.setVerticalSpacing(20)
        self.reg_form_2.setObjectName("reg_form_2")
        self.dropout_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.dropout_label_2.setFont(font)
        self.dropout_label_2.setObjectName("dropout_label_2")
        self.reg_form_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dropout_label_2)
        self.drop_box_2 = QtWidgets.QHBoxLayout()
        self.drop_box_2.setSpacing(30)
        self.drop_box_2.setObjectName("drop_box_2")
        self.drop_slider_2 = QtWidgets.QSlider(parent=self.formLayoutWidget_13)
        self.drop_slider_2.setMaximumSize(QtCore.QSize(400, 26))
        self.drop_slider_2.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        self.drop_slider_2.setFont(font)
        self.drop_slider_2.setMaximum(100)
        self.drop_slider_2.setSingleStep(5)
        self.drop_slider_2.setPageStep(5)
        self.drop_slider_2.setSliderPosition(10)
        self.drop_slider_2.setTracking(True)
        self.drop_slider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.drop_slider_2.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.drop_slider_2.setTickInterval(5)
        self.drop_slider_2.setObjectName("drop_slider_2")
        self.drop_box_2.addWidget(self.drop_slider_2)
        self.drop_perc_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.drop_perc_2.setFont(font)
        self.drop_perc_2.setObjectName("drop_perc_2")
        self.drop_box_2.addWidget(self.drop_perc_2)
        self.reg_form_2.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.drop_box_2)
        self.l1_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.l1_label_2.setFont(font)
        self.l1_label_2.setObjectName("l1_label_2")
        self.reg_form_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l1_label_2)
        self.l2_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.l2_label_2.setFont(font)
        self.l2_label_2.setObjectName("l2_label_2")
        self.reg_form_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l2_label_2)
        self.batch_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.batch_label_2.setFont(font)
        self.batch_label_2.setObjectName("batch_label_2")
        self.reg_form_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.batch_label_2)
        self.batch_entry_2 = QtWidgets.QCheckBox(parent=self.formLayoutWidget_13)
        self.batch_entry_2.setText("")
        self.batch_entry_2.setObjectName("batch_entry_2")
        self.reg_form_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.batch_entry_2)
        self.l1_box_2 = QtWidgets.QHBoxLayout()
        self.l1_box_2.setSpacing(30)
        self.l1_box_2.setObjectName("l1_box_2")
        self.l1_slider_2 = QtWidgets.QSlider(parent=self.formLayoutWidget_13)
        self.l1_slider_2.setMaximumSize(QtCore.QSize(400, 26))
        self.l1_slider_2.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        self.l1_slider_2.setFont(font)
        self.l1_slider_2.setMaximum(100)
        self.l1_slider_2.setSingleStep(5)
        self.l1_slider_2.setPageStep(5)
        self.l1_slider_2.setSliderPosition(10)
        self.l1_slider_2.setTracking(True)
        self.l1_slider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.l1_slider_2.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.l1_slider_2.setTickInterval(5)
        self.l1_slider_2.setObjectName("l1_slider_2")
        self.l1_box_2.addWidget(self.l1_slider_2)
        self.l1_perc_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.l1_perc_2.setFont(font)
        self.l1_perc_2.setObjectName("l1_perc_2")
        self.l1_box_2.addWidget(self.l1_perc_2)
        self.reg_form_2.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.l1_box_2)
        self.l2_box_2 = QtWidgets.QHBoxLayout()
        self.l2_box_2.setSpacing(30)
        self.l2_box_2.setObjectName("l2_box_2")
        self.l2_slider_2 = QtWidgets.QSlider(parent=self.formLayoutWidget_13)
        self.l2_slider_2.setMaximumSize(QtCore.QSize(400, 26))
        self.l2_slider_2.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        self.l2_slider_2.setFont(font)
        self.l2_slider_2.setMaximum(100)
        self.l2_slider_2.setSingleStep(5)
        self.l2_slider_2.setPageStep(5)
        self.l2_slider_2.setSliderPosition(10)
        self.l2_slider_2.setTracking(True)
        self.l2_slider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.l2_slider_2.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.l2_slider_2.setTickInterval(5)
        self.l2_slider_2.setObjectName("l2_slider_2")
        self.l2_box_2.addWidget(self.l2_slider_2)
        self.l2_perc_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.l2_perc_2.setFont(font)
        self.l2_perc_2.setObjectName("l2_perc_2")
        self.l2_box_2.addWidget(self.l2_perc_2)
        self.reg_form_2.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.l2_box_2)
        self.formLayoutWidget_4 = QtWidgets.QWidget(parent=self.layer2)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(30, 10, 321, 344))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.arch_form_2 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.arch_form_2.setContentsMargins(0, 5, 0, 5)
        self.arch_form_2.setHorizontalSpacing(30)
        self.arch_form_2.setVerticalSpacing(20)
        self.arch_form_2.setObjectName("arch_form_2")
        self.type_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.type_label_2.setFont(font)
        self.type_label_2.setObjectName("type_label_2")
        self.arch_form_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.type_label_2)
        self.type_entry_2 = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_entry_2.sizePolicy().hasHeightForWidth())
        self.type_entry_2.setSizePolicy(sizePolicy)
        self.type_entry_2.setObjectName("type_entry_2")
        self.arch_form_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.type_entry_2)
        self.kernel_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.kernel_label_2.setFont(font)
        self.kernel_label_2.setObjectName("kernel_label_2")
        self.arch_form_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.kernel_label_2)
        self.kernel_entry_2 = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kernel_entry_2.sizePolicy().hasHeightForWidth())
        self.kernel_entry_2.setSizePolicy(sizePolicy)
        self.kernel_entry_2.setObjectName("kernel_entry_2")
        self.arch_form_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.kernel_entry_2)
        self.filters_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.filters_label_2.setFont(font)
        self.filters_label_2.setObjectName("filters_label_2")
        self.arch_form_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.filters_label_2)
        self.filters_entry_2 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filters_entry_2.sizePolicy().hasHeightForWidth())
        self.filters_entry_2.setSizePolicy(sizePolicy)
        self.filters_entry_2.setObjectName("filters_entry_2")
        self.arch_form_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.filters_entry_2)
        self.pool_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.pool_label_2.setFont(font)
        self.pool_label_2.setObjectName("pool_label_2")
        self.arch_form_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pool_label_2)
        self.pool_entry_2 = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pool_entry_2.sizePolicy().hasHeightForWidth())
        self.pool_entry_2.setSizePolicy(sizePolicy)
        self.pool_entry_2.setObjectName("pool_entry_2")
        self.arch_form_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pool_entry_2)
        self.dense_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.dense_label_2.setFont(font)
        self.dense_label_2.setObjectName("dense_label_2")
        self.arch_form_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dense_label_2)
        self.dense_entry_2 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dense_entry_2.sizePolicy().hasHeightForWidth())
        self.dense_entry_2.setSizePolicy(sizePolicy)
        self.dense_entry_2.setObjectName("dense_entry_2")
        self.arch_form_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dense_entry_2)
        self.activation_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.activation_label_2.setFont(font)
        self.activation_label_2.setObjectName("activation_label_2")
        self.arch_form_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.activation_label_2)
        self.activation_entry_2 = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.activation_entry_2.sizePolicy().hasHeightForWidth())
        self.activation_entry_2.setSizePolicy(sizePolicy)
        self.activation_entry_2.setMinimumSize(QtCore.QSize(100, 0))
        self.activation_entry_2.setObjectName("activation_entry_2")
        self.arch_form_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.activation_entry_2)
        self.flat_label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.flat_label_2.setFont(font)
        self.flat_label_2.setObjectName("flat_label_2")
        self.arch_form_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.flat_label_2)
        self.flat_box_2 = QtWidgets.QCheckBox(parent=self.formLayoutWidget_4)
        self.flat_box_2.setText("")
        self.flat_box_2.setObjectName("flat_box_2")
        self.arch_form_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.flat_box_2)
        self.layers_tab.addTab(self.layer2, "")
        self.layer3 = QtWidgets.QWidget()
        self.layer3.setObjectName("layer3")
        self.formLayoutWidget_5 = QtWidgets.QWidget(parent=self.layer3)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(30, 10, 401, 344))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.arch_form_3 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.arch_form_3.setContentsMargins(0, 5, 0, 5)
        self.arch_form_3.setHorizontalSpacing(30)
        self.arch_form_3.setVerticalSpacing(20)
        self.arch_form_3.setObjectName("arch_form_3")
        self.type_label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.type_label_3.setFont(font)
        self.type_label_3.setObjectName("type_label_3")
        self.arch_form_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.type_label_3)
        self.type_entry_3 = QtWidgets.QComboBox(parent=self.formLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_entry_3.sizePolicy().hasHeightForWidth())
        self.type_entry_3.setSizePolicy(sizePolicy)
        self.type_entry_3.setObjectName("type_entry_3")
        self.arch_form_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.type_entry_3)
        self.kernel_label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.kernel_label_3.setFont(font)
        self.kernel_label_3.setObjectName("kernel_label_3")
        self.arch_form_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.kernel_label_3)
        self.kernel_entry_3 = QtWidgets.QComboBox(parent=self.formLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kernel_entry_3.sizePolicy().hasHeightForWidth())
        self.kernel_entry_3.setSizePolicy(sizePolicy)
        self.kernel_entry_3.setObjectName("kernel_entry_3")
        self.arch_form_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.kernel_entry_3)
        self.filters_label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.filters_label_3.setFont(font)
        self.filters_label_3.setObjectName("filters_label_3")
        self.arch_form_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.filters_label_3)
        self.filters_entry_3 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filters_entry_3.sizePolicy().hasHeightForWidth())
        self.filters_entry_3.setSizePolicy(sizePolicy)
        self.filters_entry_3.setObjectName("filters_entry_3")
        self.arch_form_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.filters_entry_3)
        self.pool_label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.pool_label_3.setFont(font)
        self.pool_label_3.setObjectName("pool_label_3")
        self.arch_form_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pool_label_3)
        self.pool_entry_3 = QtWidgets.QComboBox(parent=self.formLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pool_entry_3.sizePolicy().hasHeightForWidth())
        self.pool_entry_3.setSizePolicy(sizePolicy)
        self.pool_entry_3.setObjectName("pool_entry_3")
        self.arch_form_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pool_entry_3)
        self.dense_label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        self.dense_label_3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.dense_label_3.setFont(font)
        self.dense_label_3.setObjectName("dense_label_3")
        self.arch_form_3.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dense_label_3)
        self.dense_entry_3 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dense_entry_3.sizePolicy().hasHeightForWidth())
        self.dense_entry_3.setSizePolicy(sizePolicy)
        self.dense_entry_3.setObjectName("dense_entry_3")
        self.arch_form_3.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dense_entry_3)
        self.activation_label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.activation_label_3.setFont(font)
        self.activation_label_3.setObjectName("activation_label_3")
        self.arch_form_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.activation_label_3)
        self.activation_entry_3 = QtWidgets.QComboBox(parent=self.formLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.activation_entry_3.sizePolicy().hasHeightForWidth())
        self.activation_entry_3.setSizePolicy(sizePolicy)
        self.activation_entry_3.setMinimumSize(QtCore.QSize(100, 0))
        self.activation_entry_3.setObjectName("activation_entry_3")
        self.arch_form_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.activation_entry_3)
        self.flat_box_3 = QtWidgets.QCheckBox(parent=self.formLayoutWidget_5)
        self.flat_box_3.setText("")
        self.flat_box_3.setObjectName("flat_box_3")
        self.arch_form_3.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.flat_box_3)
        self.flat_label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.flat_label_3.setFont(font)
        self.flat_label_3.setObjectName("flat_label_3")
        self.arch_form_3.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.flat_label_3)
        self.formLayoutWidget_14 = QtWidgets.QWidget(parent=self.layer3)
        self.formLayoutWidget_14.setGeometry(QtCore.QRect(20, 320, 381, 210))
        self.formLayoutWidget_14.setObjectName("formLayoutWidget_14")
        self.reg_form_3 = QtWidgets.QFormLayout(self.formLayoutWidget_14)
        self.reg_form_3.setContentsMargins(10, 10, 10, 10)
        self.reg_form_3.setHorizontalSpacing(30)
        self.reg_form_3.setVerticalSpacing(20)
        self.reg_form_3.setObjectName("reg_form_3")
        self.dropout_label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.dropout_label_3.setFont(font)
        self.dropout_label_3.setObjectName("dropout_label_3")
        self.reg_form_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dropout_label_3)
        self.drop_box_3 = QtWidgets.QHBoxLayout()
        self.drop_box_3.setSpacing(30)
        self.drop_box_3.setObjectName("drop_box_3")
        self.drop_slider_3 = QtWidgets.QSlider(parent=self.formLayoutWidget_14)
        self.drop_slider_3.setMaximumSize(QtCore.QSize(400, 26))
        self.drop_slider_3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        self.drop_slider_3.setFont(font)
        self.drop_slider_3.setMaximum(100)
        self.drop_slider_3.setSingleStep(5)
        self.drop_slider_3.setPageStep(5)
        self.drop_slider_3.setSliderPosition(10)
        self.drop_slider_3.setTracking(True)
        self.drop_slider_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.drop_slider_3.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.drop_slider_3.setTickInterval(5)
        self.drop_slider_3.setObjectName("drop_slider_3")
        self.drop_box_3.addWidget(self.drop_slider_3)
        self.drop_perc_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.drop_perc_3.setFont(font)
        self.drop_perc_3.setObjectName("drop_perc_3")
        self.drop_box_3.addWidget(self.drop_perc_3)
        self.reg_form_3.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.drop_box_3)
        self.l1_label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.l1_label_3.setFont(font)
        self.l1_label_3.setObjectName("l1_label_3")
        self.reg_form_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l1_label_3)
        self.l2_label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.l2_label_3.setFont(font)
        self.l2_label_3.setObjectName("l2_label_3")
        self.reg_form_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l2_label_3)
        self.batch_label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.batch_label_3.setFont(font)
        self.batch_label_3.setObjectName("batch_label_3")
        self.reg_form_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.batch_label_3)
        self.batch_entry_3 = QtWidgets.QCheckBox(parent=self.formLayoutWidget_14)
        self.batch_entry_3.setText("")
        self.batch_entry_3.setObjectName("batch_entry_3")
        self.reg_form_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.batch_entry_3)
        self.l1_box_3 = QtWidgets.QHBoxLayout()
        self.l1_box_3.setSpacing(30)
        self.l1_box_3.setObjectName("l1_box_3")
        self.l1_slider_3 = QtWidgets.QSlider(parent=self.formLayoutWidget_14)
        self.l1_slider_3.setMaximumSize(QtCore.QSize(400, 26))
        self.l1_slider_3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        self.l1_slider_3.setFont(font)
        self.l1_slider_3.setMaximum(100)
        self.l1_slider_3.setSingleStep(5)
        self.l1_slider_3.setPageStep(5)
        self.l1_slider_3.setSliderPosition(10)
        self.l1_slider_3.setTracking(True)
        self.l1_slider_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.l1_slider_3.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.l1_slider_3.setTickInterval(5)
        self.l1_slider_3.setObjectName("l1_slider_3")
        self.l1_box_3.addWidget(self.l1_slider_3)
        self.l1_perc_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.l1_perc_3.setFont(font)
        self.l1_perc_3.setObjectName("l1_perc_3")
        self.l1_box_3.addWidget(self.l1_perc_3)
        self.reg_form_3.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.l1_box_3)
        self.l2_box_3 = QtWidgets.QHBoxLayout()
        self.l2_box_3.setSpacing(30)
        self.l2_box_3.setObjectName("l2_box_3")
        self.l2_slider_3 = QtWidgets.QSlider(parent=self.formLayoutWidget_14)
        self.l2_slider_3.setMaximumSize(QtCore.QSize(400, 26))
        self.l2_slider_3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        self.l2_slider_3.setFont(font)
        self.l2_slider_3.setMaximum(100)
        self.l2_slider_3.setSingleStep(5)
        self.l2_slider_3.setPageStep(5)
        self.l2_slider_3.setSliderPosition(10)
        self.l2_slider_3.setTracking(True)
        self.l2_slider_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.l2_slider_3.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.l2_slider_3.setTickInterval(5)
        self.l2_slider_3.setObjectName("l2_slider_3")
        self.l2_box_3.addWidget(self.l2_slider_3)
        self.l2_perc_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.l2_perc_3.setFont(font)
        self.l2_perc_3.setObjectName("l2_perc_3")
        self.l2_box_3.addWidget(self.l2_perc_3)
        self.reg_form_3.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.l2_box_3)
        self.layers_tab.addTab(self.layer3, "")
        self.general_group = QtWidgets.QGroupBox(parent=self.fields_frame)
        self.general_group.setGeometry(QtCore.QRect(20, 0, 431, 261))
        self.general_group.setTitle("")
        self.general_group.setObjectName("general_group")
        self.formLayoutWidget_12 = QtWidgets.QWidget(parent=self.general_group)
        self.formLayoutWidget_12.setGeometry(QtCore.QRect(30, 120, 301, 141))
        self.formLayoutWidget_12.setObjectName("formLayoutWidget_12")
        self.general_form = QtWidgets.QFormLayout(self.formLayoutWidget_12)
        self.general_form.setContentsMargins(5, 0, 5, 0)
        self.general_form.setHorizontalSpacing(20)
        self.general_form.setVerticalSpacing(30)
        self.general_form.setObjectName("general_form")
        self.time_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
        self.time_label.setObjectName("time_label")
        self.general_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.time_label)
        self.time_entry = QtWidgets.QSpinBox(parent=self.formLayoutWidget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_entry.sizePolicy().hasHeightForWidth())
        self.time_entry.setSizePolicy(sizePolicy)
        self.time_entry.setMinimumSize(QtCore.QSize(70, 0))
        self.time_entry.setObjectName("time_entry")
        self.general_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.time_entry)
        self.layers_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
        self.layers_label.setObjectName("layers_label")
        self.general_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.layers_label)
        self.layers_entry = QtWidgets.QComboBox(parent=self.formLayoutWidget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layers_entry.sizePolicy().hasHeightForWidth())
        self.layers_entry.setSizePolicy(sizePolicy)
        self.layers_entry.setObjectName("layers_entry")
        self.general_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.layers_entry)
        self.name_label = QtWidgets.QLabel(parent=self.general_group)
        self.name_label.setGeometry(QtCore.QRect(100, 50, 101, 31))
        self.name_label.setObjectName("name_label")
        self.name_entry = QtWidgets.QLineEdit(parent=self.general_group)
        self.name_entry.setGeometry(QtCore.QRect(200, 50, 90, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_entry.sizePolicy().hasHeightForWidth())
        self.name_entry.setSizePolicy(sizePolicy)
        self.name_entry.setMaximumSize(QtCore.QSize(90, 16777215))
        self.name_entry.setObjectName("name_entry")
        self.formLayoutWidget_15 = QtWidgets.QWidget(parent=self.general_group)
        self.formLayoutWidget_15.setGeometry(QtCore.QRect(240, 120, 301, 141))
        self.formLayoutWidget_15.setObjectName("formLayoutWidget_15")
        self.general_form_2 = QtWidgets.QFormLayout(self.formLayoutWidget_15)
        self.general_form_2.setContentsMargins(5, 0, 5, 0)
        self.general_form_2.setHorizontalSpacing(20)
        self.general_form_2.setVerticalSpacing(30)
        self.general_form_2.setObjectName("general_form_2")
        self.categories_label = QtWidgets.QLabel(parent=self.formLayoutWidget_15)
        self.categories_label.setObjectName("categories_label")
        self.general_form_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.categories_label)
        self.categories_entry = QtWidgets.QSpinBox(parent=self.formLayoutWidget_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categories_entry.sizePolicy().hasHeightForWidth())
        self.categories_entry.setSizePolicy(sizePolicy)
        self.categories_entry.setMinimumSize(QtCore.QSize(70, 0))
        self.categories_entry.setObjectName("categories_entry")
        self.general_form_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.categories_entry)
        self.compiler_label = QtWidgets.QLabel(parent=self.formLayoutWidget_15)
        self.compiler_label.setObjectName("compiler_label")
        self.general_form_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.compiler_label)
        self.compiler_entry = QtWidgets.QComboBox(parent=self.formLayoutWidget_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compiler_entry.sizePolicy().hasHeightForWidth())
        self.compiler_entry.setSizePolicy(sizePolicy)
        self.compiler_entry.setObjectName("compiler_entry")
        self.general_form_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.compiler_entry)
        self.main_button = QtWidgets.QPushButton(parent=self.fields_frame)
        self.main_button.setEnabled(True)
        self.main_button.setGeometry(QtCore.QRect(70, 890, 351, 31))
        self.main_button.setObjectName("main_button")
        self.fields_layout.addWidget(self.fields_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(self)
        self.restrictions()
        self.set_default_settings()

        self.layers_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tabReference1 = self.layers_tab.widget(0)
        self.tabReference2 = self.layers_tab.widget(1)
        self.tabReference3 = self.layers_tab.widget(2)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "New Network"))
        self.title_label.setText(_translate("MainWindow", "New Neural Nework"))
        self.type_label_1.setText(_translate("MainWindow", "Layer Type"))
        self.activation_label_1.setText(_translate("MainWindow", "Activation Function"))
        self.kernel_label_1.setText(_translate("MainWindow", "Kernel Size"))
        self.filters_label_1.setText(_translate("MainWindow", "Filters"))
        self.pool_label_1.setText(_translate("MainWindow", "1D Pooling Size"))
        self.dense_label_1.setText(_translate("MainWindow", "Dense Size"))
        self.flat_label_1.setText(_translate("MainWindow", "Flatten"))
        self.dropout_label_1.setText(_translate("MainWindow", "Drop Out"))
        self.drop_perc_1.setText(_translate("MainWindow", "10%"))
        self.l1_label_1.setText(_translate("MainWindow", "L1 Regularization "))
        self.l1_perc_1.setText(_translate("MainWindow", "10%"))
        self.l2_label_1.setText(_translate("MainWindow", "L2 Regularization "))
        self.l2_perc_1.setText(_translate("MainWindow", "10%"))
        self.batch_label_1.setText(_translate("MainWindow", "Batch Normalization"))
        self.layers_tab.setTabText(self.layers_tab.indexOf(self.layer1), _translate("MainWindow", "Layer 1"))
        self.dropout_label_2.setText(_translate("MainWindow", "Drop Out"))
        self.drop_perc_2.setText(_translate("MainWindow", "10%"))
        self.l1_label_2.setText(_translate("MainWindow", "L1 Regularization "))
        self.l2_label_2.setText(_translate("MainWindow", "L2 Regularization "))
        self.batch_label_2.setText(_translate("MainWindow", "Batch Normalization"))
        self.l1_perc_2.setText(_translate("MainWindow", "10%"))
        self.l2_perc_2.setText(_translate("MainWindow", "10%"))
        self.type_label_2.setText(_translate("MainWindow", "Layer Type"))
        self.kernel_label_2.setText(_translate("MainWindow", "Kernel Size"))
        self.filters_label_2.setText(_translate("MainWindow", "Filters"))
        self.pool_label_2.setText(_translate("MainWindow", "1D Pooling Size"))
        self.dense_label_2.setText(_translate("MainWindow", "Dense Size"))
        self.activation_label_2.setText(_translate("MainWindow", "Activation Function"))
        self.flat_label_2.setText(_translate("MainWindow", "Flatten"))
        self.layers_tab.setTabText(self.layers_tab.indexOf(self.layer2), _translate("MainWindow", "Layer 2"))
        self.type_label_3.setText(_translate("MainWindow", "Layer Type"))
        self.kernel_label_3.setText(_translate("MainWindow", "Kernel Size"))
        self.filters_label_3.setText(_translate("MainWindow", "Filters"))
        self.pool_label_3.setText(_translate("MainWindow", "1D Pooling Size"))
        self.dense_label_3.setText(_translate("MainWindow", "Dense Size"))
        self.activation_label_3.setText(_translate("MainWindow", "Activation Function"))
        self.flat_label_3.setText(_translate("MainWindow", "Flatten"))
        self.dropout_label_3.setText(_translate("MainWindow", "Drop Out"))
        self.drop_perc_3.setText(_translate("MainWindow", "10%"))
        self.l1_label_3.setText(_translate("MainWindow", "L1 Regularization "))
        self.l2_label_3.setText(_translate("MainWindow", "L2 Regularization "))
        self.batch_label_3.setText(_translate("MainWindow", "Batch Normalization"))
        self.l1_perc_3.setText(_translate("MainWindow", "10%"))
        self.l2_perc_3.setText(_translate("MainWindow", "10%"))
        self.layers_tab.setTabText(self.layers_tab.indexOf(self.layer3), _translate("MainWindow", "Layer 3"))
        self.time_label.setText(_translate("MainWindow", "Time Step"))
        self.layers_label.setText(_translate("MainWindow", "Layers"))
        self.name_label.setText(_translate("MainWindow", "Model Name"))
        self.categories_label.setText(_translate("MainWindow", "Categories"))
        self.compiler_label.setText(_translate("MainWindow", "Compiler"))
        self.main_button.setText(_translate("MainWindow", "Create"))


    def set_default_settings(self):
        self.name_entry.setText("Untitled Network")
        self.time_entry.setValue(100)  # Set the default value to 64
        self.layers_entry.setCurrentIndex(2)  # 3rd option, zero-based index
        self.categories_entry.setValue(7)

        self.kernel_entry_1.setCurrentIndex(2)  # Corrected to affect kernel_entry1
        self.filters_entry_1.setValue(32)  # Set the default value to 64
        self.pool_entry_1.setCurrentIndex(0)
        self.activation_entry_1.setCurrentIndex(0)
        self.drop_slider_1.setValue(20)
        self.l1_slider_1.setValue(0)
        self.l2_slider_1.setValue(0)
        self.batch_entry_1.setChecked(False)  # Assuming self.batch_entry1 is a QCheckBox or similar'
        self.dense_entry_1.setValue(100)
        self.flat_box_2.setChecked(False)  # Assuming self.

        self.kernel_entry_2.setCurrentIndex(2)  # Now correctly referring to kernel_entry2
        self.filters_entry_2.setValue(64)  # Set the default value to 64
        self.pool_entry_2.setCurrentIndex(2)  # Sets the default pooling size for pool_entry2
        self.activation_entry_2.setCurrentIndex(0)  # Sets the default activation function for activation_entry2
        self.drop_slider_2.setValue(0)  # Sets the initial value for dropout
        self.batch_entry_2.setChecked(False)  # Assuming self.batch_entry1 is a QCheckBox or similar
        self.flat_box_2.setChecked(True) # Assuming self.
        self.dense_entry_2.setValue(100)
        self.l1_slider_2.setValue(0)
        self.l2_slider_2.setValue(0)

        self.kernel_entry_3.setCurrentIndex(2)  # Set default kernel size for kernel_entry3
        self.filters_entry_3.setValue(64)  # Set default value to 64
        self.pool_entry_3.setCurrentIndex(0)  # Set default pooling size for pool_entry3
        self.activation_entry_3.setCurrentIndex(0)  # Set default activation function for activation_entry3
        self.drop_slider_3.setValue(0)  # Set initial value for dropout
        self.batch_entry_3.setChecked(False)  # Assuming self.batch_entry1 is a QCheckBox or similar
        self.dense_entry_3.setValue(100)
        self.l1_slider_3.setValue(0)
        self.l2_slider_3.setValue(0)





    def restrictions(self):


        regex = QRegularExpression("[a-zA-Z0-9 ]+")
        self.name_entry.setValidator(QRegularExpressionValidator(regex))
        self.name_entry.setEnabled(True)

        # Optionally, set the range if needed
        self.time_entry.setMinimum(1)  # Set the minimum value
        self.time_entry.setMaximum(1000)  # Set the maximum value

        self.type_entry_1.addItems(["Conv"])
        self.kernel_entry_1.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.layers_entry.addItems(["1 layer", "2 layers", "3 layers"])  # Correct grammar
        self.filters_entry_1.setMinimum(1)  # Set the minimum value
        self.filters_entry_1.setMaximum(1000)  # Set the maximum value
        self.pool_entry_1.addItems(["None","1", "2", "3"])
        self.activation_entry_1.addItems(["Tanh", "Relu"])

        self.drop_slider_1.setTickInterval(10)
        self.drop_slider_1.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.l1_slider_1.setTickInterval(10)
        self.l1_slider_1.setTickPosition(QSlider.TickPosition.TicksBelow)  # Correct method and enum
        self.l2_slider_1.setTickInterval(10)
        self.l2_slider_1.setTickPosition(QSlider.TickPosition.TicksBelow)  # Correct method and enum



        self.type_entry_2.addItems(["Conv", "Dense"])
        self.kernel_entry_2.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.filters_entry_2.setMinimum(1)  # Set the minimum value
        self.filters_entry_2.setMaximum(1000)  # Set the maximum value
        self.pool_entry_2.addItems(["None","1", "2", "3"])
        self.activation_entry_2.addItems(["Tanh", "Relu"])
        self.drop_slider_2.setTickInterval(10)  # Sets the interval between ticks
        self.drop_slider_2.setTickPosition(
            QSlider.TickPosition.TicksBelow)  # Correct method call with enum for tick position

        self.l1_slider_2.setTickInterval(10)
        self.l1_slider_2.setTickPosition(QSlider.TickPosition.TicksBelow)  # Correct method and enum
        self.l2_slider_2.setTickInterval(10)
        self.l2_slider_2.setTickPosition(QSlider.TickPosition.TicksBelow)  # Correct method and enum


        self.type_entry_3.addItems(["Conv", "Dense"])
        self.kernel_entry_3.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.filters_entry_3.setMinimum(1)  # Set minimum value
        self.filters_entry_3.setMaximum(1000)  # Set maximum value
        self.pool_entry_3.addItems(["None","1", "2", "3"])
        self.activation_entry_3.addItems(["Tanh", "Relu"])
        self.drop_slider_3.setTickInterval(10)  # Set interval between ticks
        self.drop_slider_3.setTickPosition(QSlider.TickPosition.TicksBelow)


        self.compiler_entry.addItems(["Adam", "RMSprop", "SGD"])
        self.compiler_entry.setCurrentIndex(0)  # Set default optimizer for compile_box

        # set default layer types


        self.type_entry_1.setCurrentIndex(0)
        self.type_entry_2.setCurrentIndex(0)
        self.type_entry_3.setCurrentIndex(1)





        # Update the layer types to default types
        self.controller.on_type_change(1)
        self.controller.on_type_change(2)
        self.controller.on_type_change(3)

        self.type_entry_1.currentIndexChanged.connect(lambda: self.controller.on_type_change(1))
        self.type_entry_2.currentIndexChanged.connect(lambda: self.controller.on_type_change(2))
        self.type_entry_3.currentIndexChanged.connect(lambda: self.controller.on_type_change(3))



        self.layers_entry.currentIndexChanged.connect(self.controller.on_layer_box_change)

        self.main_button.clicked.connect(self.handle_create_btn)











    def updateValueLabel(self, value):
        self.valueLabel.setText(str(value))


    def closeEvent(self, event):
         event.accept()

    def close(self):
        super().close()





    def handle_create_btn(self):
        data = self.collect_ui_data()
        if self.controller.validate_name(data):
            self.controller.create_network(data)





    def collect_ui_data(self):
        data = {
            "general": {
                "name": self.name_entry.text(),
                "time_steps": self.time_entry.value(),
                "layers": self.layers_entry.currentText(),
                "categories": self.categories_entry.value(),
            },
            "compile": {
                "compiler": self.compiler_entry.currentText(),
            },
            "layers": []
        }

        # Collect layer-specific configurations
        for i in range(self.layers_tab.count()):
            layer = {
                "type": self.layers_tab.widget(i).findChild(QtWidgets.QComboBox,
                                                            f"type_entry_{i + 1}").currentText(),
                "kernel": self.layers_tab.widget(i).findChild(QtWidgets.QComboBox,
                                                              f"kernel_entry_{i + 1}").currentText(),
                "filters": self.layers_tab.widget(i).findChild(QtWidgets.QSpinBox,
                                                               f"filters_entry_{i + 1}").value(),
                "dense_units": self.layers_tab.widget(i).findChild(QtWidgets.QSpinBox,
                                                                   f"dense_entry_{i + 1}").value(),
                "pooling": self.layers_tab.widget(i).findChild(QtWidgets.QComboBox,
                                                               f"pool_entry_{i + 1}").currentText(),
                "activation": self.layers_tab.widget(i).findChild(QtWidgets.QComboBox,
                                                                  f"activation_entry_{i + 1}").currentText(),
                "dropout_rate": self.layers_tab.widget(i).findChild(QtWidgets.QSlider,
                                                                    f"drop_slider_{i + 1}").value() / 100.0,
                "batch_normalization": self.layers_tab.widget(i).findChild(QtWidgets.QCheckBox,
                                                                           f"batch_entry_{i + 1}").isChecked(),
                "flatten": self.layers_tab.widget(i).findChild(QtWidgets.QCheckBox,
                                                               f"flat_box_{i + 1}").isChecked(),
                "l1_reg": self.layers_tab.widget(i).findChild(QtWidgets.QSlider,
                                                              f"l1_slider_{i + 1}").value() / 100.0,
                "l2_reg": self.layers_tab.widget(i).findChild(QtWidgets.QSlider,
                                                              f"l2_slider_{i + 1}").value() / 100.0
            }

            data["layers"].append(layer)
            # Add the layer configuration to your desired data structure here

        return data

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

        self.init_ui(self)


























