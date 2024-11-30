import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QFileDialog


# View
class Testing_View(QMainWindow):
    def __init__(self):
        super().__init__()

    def init_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 797)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 741, 751))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.fields_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.fields_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.fields_layout.setContentsMargins(10, 10, 10, 0)
        self.fields_layout.setObjectName("fields_layout")
        self.title_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("/* General Styles */\n"
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
        self.title_label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.fields_layout.addWidget(self.title_label)
        self.fields_frame = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.fields_frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fields_frame.sizePolicy().hasHeightForWidth())
        self.fields_frame.setSizePolicy(sizePolicy)
        self.fields_frame.setMinimumSize(QtCore.QSize(200, 200))
        self.fields_frame.setAutoFillBackground(True)
        self.fields_frame.setStyleSheet("fields_frame:Qframe {\n"
                                        "\n"
                                        "background: rgb(249, 249, 249)\n"
                                        "}")
        self.fields_frame.setObjectName("fields_frame")
        self.general_box = QtWidgets.QGroupBox(parent=self.fields_frame)
        self.general_box.setGeometry(QtCore.QRect(10, 20, 591, 651))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.general_box.setFont(font)
        self.general_box.setTitle("")
        self.general_box.setObjectName("general_box")
        self.formLayoutWidget_14 = QtWidgets.QWidget(parent=self.general_box)
        self.formLayoutWidget_14.setGeometry(QtCore.QRect(60, 50, 498, 121))
        self.formLayoutWidget_14.setObjectName("formLayoutWidget_14")
        self.general_form = QtWidgets.QFormLayout(self.formLayoutWidget_14)
        self.general_form.setContentsMargins(5, 0, 5, 0)
        self.general_form.setHorizontalSpacing(20)
        self.general_form.setVerticalSpacing(30)
        self.general_form.setObjectName("general_form")
        self.path_label = QtWidgets.QLabel(parent=self.formLayoutWidget_14)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.path_label.setFont(font)
        self.path_label.setObjectName("path_label")
        self.general_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.path_label)
        self.path_box = QtWidgets.QHBoxLayout()
        self.path_box.setObjectName("path_box")
        self.path_entry = QtWidgets.QLineEdit(parent=self.formLayoutWidget_14)
        self.path_entry.setObjectName("path_entry")
        self.path_box.addWidget(self.path_entry)
        self.select_button = QtWidgets.QPushButton(parent=self.formLayoutWidget_14)
        self.select_button.setObjectName("select_button")
        self.path_box.addWidget(self.select_button)
        self.general_form.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.path_box)
        self.data_label = QtWidgets.QLabel(parent=self.formLayoutWidget_14)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.data_label.setFont(font)
        self.data_label.setObjectName("data_label")
        self.general_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.data_label)
        self.data_entry = QtWidgets.QSpinBox(parent=self.formLayoutWidget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_entry.sizePolicy().hasHeightForWidth())
        self.data_entry.setSizePolicy(sizePolicy)
        self.data_entry.setMinimumSize(QtCore.QSize(70, 0))
        self.data_entry.setObjectName("data_entry")
        self.general_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.data_entry)
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.general_box)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 230, 531, 321))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.visuals_form = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.visuals_form.setContentsMargins(5, 0, 5, 0)
        self.visuals_form.setHorizontalSpacing(20)
        self.visuals_form.setVerticalSpacing(30)
        self.visuals_form.setObjectName("visuals_form")
        self.sample_label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.sample_label.setFont(font)
        self.sample_label.setObjectName("sample_label")
        self.visuals_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.sample_label)
        self.samples_entry = QtWidgets.QSpinBox(parent=self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.samples_entry.sizePolicy().hasHeightForWidth())
        self.samples_entry.setSizePolicy(sizePolicy)
        self.samples_entry.setMinimumSize(QtCore.QSize(70, 0))
        self.samples_entry.setObjectName("samples_entry")
        self.visuals_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.samples_entry)
        self.conmat_label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.conmat_label.setFont(font)
        self.conmat_label.setObjectName("conmat_label")
        self.visuals_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.conmat_label)
        self.auc_label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.auc_label.setFont(font)
        self.auc_label.setObjectName("auc_label")
        self.visuals_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.auc_label)
        self.conmat_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        self.conmat_box.setText("")
        self.conmat_box.setObjectName("conmat_box")
        self.visuals_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.conmat_box)
        self.auc_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        self.auc_box.setText("")
        self.auc_box.setObjectName("auc_box")
        self.visuals_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.auc_box)
        self.time_elapsed_label = QtWidgets.QLabel(parent=self.fields_frame)
        self.time_elapsed_label.setGeometry(QtCore.QRect(170, 790, 221, 16))
        self.time_elapsed_label.setObjectName("time_elapsed_label")
        self.main_button = QtWidgets.QPushButton(parent=self.fields_frame)
        self.main_button.setEnabled(True)
        self.main_button.setGeometry(QtCore.QRect(80, 630, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.main_button.setFont(font)
        self.main_button.setStyleSheet("")
        self.main_button.setObjectName("main_button")
        self.fields_layout.addWidget(self.fields_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #temproarily hiden till implemented
        self.samples_entry.hide()
        self.sample_label.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Testing Menu"))
        self.title_label.setText(_translate("MainWindow", "Test Network"))
        self.path_label.setText(_translate("MainWindow", "Test Data Path"))
        self.select_button.setText(_translate("MainWindow", "Select Folder"))
        self.data_label.setText(_translate("MainWindow", "Dataset Size"))
        self.sample_label.setText(_translate("MainWindow", "Samples Shown"))
        self.conmat_label.setText(_translate("MainWindow", "Show Confusion Matrix"))
        self.auc_label.setText(_translate("MainWindow", "Show AUC Curve"))
        self.time_elapsed_label.setText(_translate("MainWindow", "Time Elapsed : "))
        self.main_button.setText(_translate("MainWindow", "Test"))


    def handle_test_btn(self):
        options = self.get_testing_options()
        self.controller.handle_test_btn(options)


    def get_testing_options(self):
        options = {
            'conmat_box': self.conmat_box.isChecked(),
            'auc_box': self.auc_box.isChecked()
        }


    def set_controller(self, controller):

        self.controller = controller
        self.init_ui(self)

    def get_testing_data_size(self):
        return self.data_entry.value()



    def set_bindings(self):
        self.select_button.clicked.connect(self.handle_select_button)
        self.main_button.clicked.connect(self.handle_test_btn)

    def handle_select_button(self):
        folder_path = self.select_folder()
        if folder_path:
            self.path_entry.setText(folder_path)

    def select_folder(self):
        options = QFileDialog.Option.ShowDirsOnly
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "", options)
        return folder_path

    def get_test_path(self):
        if self.path_entry :
            return self.path_entry.text()
        pass


    def set_controller(self, controller):
        self.controller = controller
        self.init_ui(self)
        self.retranslateUi(self)
        self.set_bindings()
        self.init_values()

    def init_values(self):
        pass















