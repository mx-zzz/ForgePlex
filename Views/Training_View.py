from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QFileDialog



# View
class Training_View(QMainWindow):
    def init_ui(self, TrainingMenu):
        TrainingMenu.setObjectName("TrainingMenu")
        TrainingMenu.resize(534, 1115)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TrainingMenu.sizePolicy().hasHeightForWidth())
        TrainingMenu.setSizePolicy(sizePolicy)
        TrainingMenu.setMinimumSize(QtCore.QSize(509, 1115))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        TrainingMenu.setFont(font)
        TrainingMenu.setStyleSheet("/* General Styles */\n"
                                   "QWidget {\n"
                                   "    font:  \"Segoe UI Semibold\";\n"
                                   "}\n"
                                   "\n"
                                   "/* Labels */\n"
                                   "QLabel {\n"
                                   "    font-size: 10.5pt;\n"
                                   "    color: #333333; /* Dark gray text color */\n"
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
                                   "#training_label {\n"
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
                                   "#train_button {\n"
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
                                   "#train_button:pressed {\n"
                                   "    background-color: #dadbde; /* Light gray when pressed */\n"
                                   "}\n"
                                   "\n"
                                   "#train_button:hover {\n"
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
                                   "\n"
                                   "\n"
                                   "")
        self.centralwidget = QtWidgets.QWidget(parent=TrainingMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(509, 0))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 471, 1021))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.training_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.training_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.training_layout.setContentsMargins(10, 10, 10, 0)
        self.training_layout.setObjectName("training_layout")
        self.training_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.training_label.sizePolicy().hasHeightForWidth())
        self.training_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        self.training_label.setFont(font)
        self.training_label.setLineWidth(0)
        self.training_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.training_label.setObjectName("training_label")
        self.training_layout.addWidget(self.training_label)
        self.training_frame = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.training_frame.sizePolicy().hasHeightForWidth())
        self.training_frame.setSizePolicy(sizePolicy)
        self.training_frame.setAutoFillBackground(True)
        self.training_frame.setStyleSheet("fields_frame:Qframe {\n"
                                          "\n"
                                          "background: rgb(249, 249, 249)\n"
                                          "}")
        self.training_frame.setObjectName("training_frame")
        self.layers_tab = QtWidgets.QTabWidget(parent=self.training_frame)
        self.layers_tab.setGeometry(QtCore.QRect(0, 560, 451, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.layers_tab.sizePolicy().hasHeightForWidth())
        self.layers_tab.setSizePolicy(sizePolicy)
        self.layers_tab.setMinimumSize(QtCore.QSize(450, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        self.layers_tab.setFont(font)
        self.layers_tab.setStyleSheet("")
        self.layers_tab.setDocumentMode(False)
        self.layers_tab.setTabsClosable(False)
        self.layers_tab.setTabBarAutoHide(True)
        self.layers_tab.setObjectName("layers_tab")
        self.general_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_tab.sizePolicy().hasHeightForWidth())
        self.general_tab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.general_tab.setFont(font)
        self.general_tab.setObjectName("general_tab")
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.general_tab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(40, 10, 691, 235))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.general_form = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.general_form.setContentsMargins(10, 10, 10, 10)
        self.general_form.setHorizontalSpacing(20)
        self.general_form.setVerticalSpacing(30)
        self.general_form.setObjectName("general_form")
        self.epochs_label = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.epochs_label.setFont(font)
        self.epochs_label.setObjectName("epochs_label")
        self.general_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.epochs_label)
        self.verbiose_label = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.verbiose_label.setFont(font)
        self.verbiose_label.setObjectName("verbiose_label")
        self.general_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.verbiose_label)
        self.batch_size_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batch_size_box.sizePolicy().hasHeightForWidth())
        self.batch_size_box.setSizePolicy(sizePolicy)
        self.batch_size_box.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.batch_size_box.setFont(font)
        self.batch_size_box.setObjectName("batch_size_box")
        self.general_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.batch_size_box)
        self.epochs_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.epochs_box.sizePolicy().hasHeightForWidth())
        self.epochs_box.setSizePolicy(sizePolicy)
        self.epochs_box.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.epochs_box.setFont(font)
        self.epochs_box.setObjectName("epochs_box")
        self.general_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.epochs_box)
        self.lrate_box = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lrate_box.sizePolicy().hasHeightForWidth())
        self.lrate_box.setSizePolicy(sizePolicy)
        self.lrate_box.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.lrate_box.setFont(font)
        self.lrate_box.setObjectName("lrate_box")
        self.general_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lrate_box)
        self.lrate_label = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.lrate_label.setFont(font)
        self.lrate_label.setObjectName("lrate_label")
        self.general_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lrate_label)
        self.batch_size_label = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.batch_size_label.setFont(font)
        self.batch_size_label.setObjectName("batch_size_label")
        self.general_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.batch_size_label)
        self.verbiose_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verbiose_box.sizePolicy().hasHeightForWidth())
        self.verbiose_box.setSizePolicy(sizePolicy)
        self.verbiose_box.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.verbiose_box.setFont(font)
        self.verbiose_box.setObjectName("verbiose_box")
        self.general_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.verbiose_box)
        self.layers_tab.addTab(self.general_tab, "")
        self.early_stop_tab = QtWidgets.QWidget()
        self.early_stop_tab.setObjectName("early_stop_tab")
        self.formLayoutWidget_4 = QtWidgets.QWidget(parent=self.early_stop_tab)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(40, 10, 471, 284))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.early_stop_form = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.early_stop_form.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.early_stop_form.setContentsMargins(10, 10, 10, 10)
        self.early_stop_form.setHorizontalSpacing(20)
        self.early_stop_form.setVerticalSpacing(30)
        self.early_stop_form.setObjectName("early_stop_form")
        self.enable_stop_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.enable_stop_label.setFont(font)
        self.enable_stop_label.setObjectName("enable_stop_label")
        self.early_stop_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.enable_stop_label)
        self.enable_stop_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_4)
        self.enable_stop_box.setText("")
        self.enable_stop_box.setObjectName("enable_stop_box")
        self.early_stop_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.enable_stop_box)
        self.monitor_var_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.monitor_var_label.setFont(font)
        self.monitor_var_label.setObjectName("monitor_var_label")
        self.early_stop_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.monitor_var_label)
        self.monitor_var_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monitor_var_box.sizePolicy().hasHeightForWidth())
        self.monitor_var_box.setSizePolicy(sizePolicy)
        self.monitor_var_box.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.monitor_var_box.setFont(font)
        self.monitor_var_box.setObjectName("monitor_var_box")
        self.monitor_var_box.addItem("")
        self.monitor_var_box.setItemText(0, "")
        self.early_stop_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.monitor_var_box)
        self.till_stop_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.till_stop_label.setFont(font)
        self.till_stop_label.setObjectName("till_stop_label")
        self.early_stop_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.till_stop_label)
        self.tilll_stop_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tilll_stop_box.sizePolicy().hasHeightForWidth())
        self.tilll_stop_box.setSizePolicy(sizePolicy)
        self.tilll_stop_box.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.tilll_stop_box.setFont(font)
        self.tilll_stop_box.setObjectName("tilll_stop_box")
        self.early_stop_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tilll_stop_box)
        self.trigger_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.trigger_label.setFont(font)
        self.trigger_label.setObjectName("trigger_label")
        self.early_stop_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.trigger_label)
        self.trigger_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trigger_box.sizePolicy().hasHeightForWidth())
        self.trigger_box.setSizePolicy(sizePolicy)
        self.trigger_box.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.trigger_box.setFont(font)
        self.trigger_box.setObjectName("trigger_box")
        self.early_stop_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.trigger_box)
        self.restore_weights_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_4)
        self.restore_weights_box.setText("")
        self.restore_weights_box.setObjectName("restore_weights_box")
        self.early_stop_form.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.restore_weights_box)
        self.restore_weight_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.restore_weight_label.setFont(font)
        self.restore_weight_label.setObjectName("restore_weight_label")
        self.early_stop_form.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.restore_weight_label)
        self.layers_tab.addTab(self.early_stop_tab, "")
        self.lrate_scheduler_tab = QtWidgets.QWidget()
        self.lrate_scheduler_tab.setObjectName("lrate_scheduler_tab")
        self.formLayoutWidget_5 = QtWidgets.QWidget(parent=self.lrate_scheduler_tab)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(40, 10, 426, 311))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.lrate_scheduler_form = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.lrate_scheduler_form.setContentsMargins(10, 10, 10, 10)
        self.lrate_scheduler_form.setHorizontalSpacing(20)
        self.lrate_scheduler_form.setVerticalSpacing(30)
        self.lrate_scheduler_form.setObjectName("lrate_scheduler_form")
        self.type_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.type_label.setFont(font)
        self.type_label.setObjectName("type_label")
        self.lrate_scheduler_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.type_label)
        self.rate_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.rate_label.setFont(font)
        self.rate_label.setObjectName("rate_label")
        self.lrate_scheduler_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.rate_label)
        self.rate_box = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rate_box.sizePolicy().hasHeightForWidth())
        self.rate_box.setSizePolicy(sizePolicy)
        self.rate_box.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.rate_box.setFont(font)
        self.rate_box.setMaximum(1.0)
        self.rate_box.setSingleStep(0.1)
        self.rate_box.setProperty("value", 0.9)
        self.rate_box.setObjectName("rate_box")
        self.lrate_scheduler_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.rate_box)
        self.decay_start_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.decay_start_label.setFont(font)
        self.decay_start_label.setObjectName("decay_start_label")
        self.lrate_scheduler_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.decay_start_label)
        self.decay_type_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decay_type_box.sizePolicy().hasHeightForWidth())
        self.decay_type_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.decay_type_box.setFont(font)
        self.decay_type_box.setObjectName("decay_type_box")
        self.lrate_scheduler_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.decay_type_box)
        self.decay_start_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decay_start_box.sizePolicy().hasHeightForWidth())
        self.decay_start_box.setSizePolicy(sizePolicy)
        self.decay_start_box.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.decay_start_box.setFont(font)
        self.decay_start_box.setMinimum(0)
        self.decay_start_box.setMaximum(1000)
        self.decay_start_box.setProperty("value", 5)
        self.decay_start_box.setObjectName("decay_start_box")
        self.lrate_scheduler_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.decay_start_box)
        self.enable_scheduler_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.enable_scheduler_label.setFont(font)
        self.enable_scheduler_label.setObjectName("enable_scheduler_label")
        self.lrate_scheduler_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.enable_scheduler_label)
        self.enable_scheduler_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_5)
        self.enable_scheduler_box.setText("")
        self.enable_scheduler_box.setObjectName("enable_scheduler_box")
        self.lrate_scheduler_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.enable_scheduler_box)
        self.layers_tab.addTab(self.lrate_scheduler_tab, "")
        self.groupBox = QtWidgets.QGroupBox(parent=self.training_frame)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 451, 531))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget_7 = QtWidgets.QWidget(parent=self.groupBox)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(30, 190, 391, 231))
        self.formLayoutWidget_7.setObjectName("formLayoutWidget_7")
        self.source_form = QtWidgets.QFormLayout(self.formLayoutWidget_7)
        self.source_form.setContentsMargins(5, 0, 5, 0)
        self.source_form.setHorizontalSpacing(20)
        self.source_form.setVerticalSpacing(30)
        self.source_form.setObjectName("source_form")
        self.train_data_path_label = QtWidgets.QLabel(parent=self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.train_data_path_label.setFont(font)
        self.train_data_path_label.setObjectName("train_data_path_label")
        self.source_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.train_data_path_label)
        self.train_path_hbox = QtWidgets.QHBoxLayout()
        self.train_path_hbox.setSpacing(15)
        self.train_path_hbox.setObjectName("train_path_hbox")
        self.train_path_entry = QtWidgets.QLineEdit(parent=self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.train_path_entry.setFont(font)
        self.train_path_entry.setObjectName("train_path_entry")
        self.train_path_hbox.addWidget(self.train_path_entry)
        self.train_path_button = QtWidgets.QPushButton(parent=self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.train_path_button.setFont(font)
        self.train_path_button.setObjectName("train_path_button")
        self.train_path_hbox.addWidget(self.train_path_button)
        self.source_form.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.train_path_hbox)
        self.valid_data_path_label = QtWidgets.QLabel(parent=self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.valid_data_path_label.setFont(font)
        self.valid_data_path_label.setObjectName("valid_data_path_label")
        self.source_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.valid_data_path_label)
        self.valid_path_hbox = QtWidgets.QHBoxLayout()
        self.valid_path_hbox.setSpacing(15)
        self.valid_path_hbox.setObjectName("valid_path_hbox")
        self.valid_path_entry = QtWidgets.QLineEdit(parent=self.formLayoutWidget_7)
        self.valid_path_entry.setObjectName("valid_path_entry")
        self.valid_path_hbox.addWidget(self.valid_path_entry)
        self.valid_path_button = QtWidgets.QPushButton(parent=self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.valid_path_button.setFont(font)
        self.valid_path_button.setObjectName("valid_path_button")
        self.valid_path_hbox.addWidget(self.valid_path_button)
        self.source_form.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.valid_path_hbox)
        self.valid_split_label = QtWidgets.QLabel(parent=self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.valid_split_label.setFont(font)
        self.valid_split_label.setObjectName("valid_split_label")
        self.source_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.valid_split_label)
        self.split_layout = QtWidgets.QHBoxLayout()
        self.split_layout.setSpacing(30)
        self.split_layout.setObjectName("split_layout")
        self.valid_split_slider = QtWidgets.QSlider(parent=self.formLayoutWidget_7)
        self.valid_split_slider.setMaximumSize(QtCore.QSize(400, 26))
        self.valid_split_slider.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        self.valid_split_slider.setFont(font)
        self.valid_split_slider.setMaximum(100)
        self.valid_split_slider.setSingleStep(5)
        self.valid_split_slider.setPageStep(5)
        self.valid_split_slider.setSliderPosition(10)
        self.valid_split_slider.setTracking(True)
        self.valid_split_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.valid_split_slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.valid_split_slider.setTickInterval(5)
        self.valid_split_slider.setObjectName("valid_split_slider")
        self.split_layout.addWidget(self.valid_split_slider)
        self.valid_split_perc = QtWidgets.QLabel(parent=self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.valid_split_perc.setFont(font)
        self.valid_split_perc.setObjectName("valid_split_perc")
        self.split_layout.addWidget(self.valid_split_perc)
        self.source_form.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.split_layout)
        self.folds_label = QtWidgets.QLabel(parent=self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.folds_label.setFont(font)
        self.folds_label.setObjectName("folds_label")
        self.source_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.folds_label)
        self.folds_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folds_box.sizePolicy().hasHeightForWidth())
        self.folds_box.setSizePolicy(sizePolicy)
        self.folds_box.setMinimumSize(QtCore.QSize(50, 20))
        self.folds_box.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.folds_box.setFont(font)
        self.folds_box.setStyleSheet("")
        self.folds_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.folds_box.setAccelerated(False)
        self.folds_box.setProperty("showGroupSeparator", False)
        self.folds_box.setObjectName("folds_box")
        self.source_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.folds_box)
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 470, 191, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.optional_form1 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.optional_form1.setContentsMargins(5, 0, 5, 0)
        self.optional_form1.setHorizontalSpacing(20)
        self.optional_form1.setVerticalSpacing(30)
        self.optional_form1.setObjectName("optional_form1")
        self.datasets_label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.datasets_label.setFont(font)
        self.datasets_label.setObjectName("datasets_label")
        self.optional_form1.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.datasets_label)
        self.datasets_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datasets_box.sizePolicy().hasHeightForWidth())
        self.datasets_box.setSizePolicy(sizePolicy)
        self.datasets_box.setMinimumSize(QtCore.QSize(50, 20))
        self.datasets_box.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.datasets_box.setFont(font)
        self.datasets_box.setStyleSheet("")
        self.datasets_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.datasets_box.setAccelerated(False)
        self.datasets_box.setProperty("showGroupSeparator", False)
        self.datasets_box.setObjectName("datasets_box")
        self.optional_form1.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.datasets_box)
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(240, 470, 192, 101))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.optional_form2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.optional_form2.setContentsMargins(5, 0, 5, 0)
        self.optional_form2.setHorizontalSpacing(20)
        self.optional_form2.setVerticalSpacing(30)
        self.optional_form2.setObjectName("optional_form2")
        self.subfolders_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_2)
        self.subfolders_box.setEnabled(False)
        self.subfolders_box.setText("")
        self.subfolders_box.setObjectName("subfolders_box")
        self.optional_form2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.subfolders_box)
        self.subfolders_label = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.subfolders_label.setFont(font)
        self.subfolders_label.setObjectName("subfolders_label")
        self.optional_form2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.subfolders_label)
        self.formLayoutWidget_6 = QtWidgets.QWidget(parent=self.groupBox)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(30, 40, 391, 101))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.general_form_1 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.general_form_1.setContentsMargins(5, 0, 5, 0)
        self.general_form_1.setSpacing(30)
        self.general_form_1.setObjectName("general_form_1")
        self.valid_method_label = QtWidgets.QLabel(parent=self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.valid_method_label.setFont(font)
        self.valid_method_label.setObjectName("valid_method_label")
        self.general_form_1.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.valid_method_label)
        self.valid_method_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valid_method_box.sizePolicy().hasHeightForWidth())
        self.valid_method_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.valid_method_box.setFont(font)
        self.valid_method_box.setObjectName("valid_method_box")
        self.general_form_1.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.valid_method_box)
        self.data_source_label = QtWidgets.QLabel(parent=self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.data_source_label.setFont(font)
        self.data_source_label.setObjectName("data_source_label")
        self.general_form_1.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.data_source_label)
        self.data_source_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_source_box.sizePolicy().hasHeightForWidth())
        self.data_source_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.data_source_box.setFont(font)
        self.data_source_box.setObjectName("data_source_box")
        self.general_form_1.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.data_source_box)
        self.training_layout.addWidget(self.training_frame)
        self.train_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.train_button.setEnabled(True)
        self.train_button.setGeometry(QtCore.QRect(80, 1040, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.train_button.setFont(font)
        self.train_button.setStyleSheet("")
        self.train_button.setObjectName("train_button")
        TrainingMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=TrainingMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 22))
        self.menubar.setObjectName("menubar")
        TrainingMenu.setMenuBar(self.menubar)
        self.training_status = QtWidgets.QStatusBar(parent=TrainingMenu)
        self.training_status.setObjectName("training_status")
        TrainingMenu.setStatusBar(self.training_status)

        self.retranslateUi(TrainingMenu)
        self.layers_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TrainingMenu)


    def __init__(self):
        super().__init__()

    def retranslateUi(self, TrainingMenu):
        _translate = QtCore.QCoreApplication.translate
        TrainingMenu.setWindowTitle(_translate("TrainingMenu", " Training Menu"))
        self.training_label.setText(_translate("TrainingMenu", "Train Network"))
        self.epochs_label.setText(_translate("TrainingMenu", "Epochs"))
        self.verbiose_label.setText(_translate("TrainingMenu", "Verbiose Mode"))
        self.lrate_label.setText(_translate("TrainingMenu", "Initial Learning Rate       "))
        self.batch_size_label.setText(_translate("TrainingMenu", "Batch Size"))
        self.layers_tab.setTabText(self.layers_tab.indexOf(self.general_tab), _translate("TrainingMenu", "General"))
        self.enable_stop_label.setText(_translate("TrainingMenu", "Enable Stopping"))
        self.monitor_var_label.setText(_translate("TrainingMenu", "Monitored Variable        "))
        self.till_stop_label.setText(_translate("TrainingMenu", "Epochs Till Stop"))
        self.trigger_label.setText(_translate("TrainingMenu", "Stop Trigger"))
        self.restore_weight_label.setText(_translate("TrainingMenu", "Restore Weights"))
        self.layers_tab.setTabText(self.layers_tab.indexOf(self.early_stop_tab), _translate("TrainingMenu", "Stopping"))
        self.type_label.setText(_translate("TrainingMenu", "Decay Type                     "))
        self.rate_label.setText(_translate("TrainingMenu", "Decay Rate"))
        self.decay_start_label.setText(_translate("TrainingMenu", "Decay Start (Epochs)"))
        self.enable_scheduler_label.setText(_translate("TrainingMenu", "Enable Scheduler"))
        self.layers_tab.setTabText(self.layers_tab.indexOf(self.lrate_scheduler_tab),
                                   _translate("TrainingMenu", "Scheduler"))
        self.train_data_path_label.setText(_translate("TrainingMenu", "Training Data Path"))
        self.train_path_button.setText(_translate("TrainingMenu", "Select Folder"))
        self.valid_data_path_label.setText(_translate("TrainingMenu", "Validation Data Path"))
        self.valid_path_button.setText(_translate("TrainingMenu", "Select Folder"))
        self.valid_split_label.setText(_translate("TrainingMenu", "Validation Split"))
        self.valid_split_perc.setText(_translate("TrainingMenu", "0%"))
        self.folds_label.setText(_translate("TrainingMenu", "Number of Folds"))
        self.datasets_label.setText(_translate("TrainingMenu", "Max Samples"))
        self.subfolders_label.setText(_translate("TrainingMenu", "Include Subfolders"))
        self.valid_method_label.setText(_translate("TrainingMenu", "Validation Method"))
        self.data_source_label.setText(_translate("TrainingMenu", "Data Source"))
        self.train_button.setText(_translate("TrainingMenu", "Train"))




    def handle_train_btn(self):
        self.controller.handle_train_btn(self.collect_training_data())

    def set_training_source(self):

        sourceIndex = self.data_source_box.currentIndex()
        if sourceIndex == 0:

            self.hideWidgets(self.valid_path_entry, self.valid_data_path_label,self.valid_path_button,self.train_path_button)

            self.showWidgets(self.valid_split_slider, self.valid_split_label,self.train_path_button,self.valid_split_perc,self.folds_box,self.folds_label)

        if sourceIndex == 1:

            self.showWidgets(self.valid_path_entry, self.valid_data_path_label,self.valid_path_button,self.train_path_button,self.folds_box,self.folds_label)


            self.hideWidgets(self.valid_split_slider, self.valid_split_label,self.valid_split_perc)



    def set_train_method(self):

        method_index = self.valid_method_box.currentIndex()
        if method_index == 0:
            self.showWidgets(self.folds_box, self.folds_label)



        if method_index == 1:




            self.hideWidgets(self.folds_box,self.folds_label)

    def init_values(self):

        # hide split options when in select validation data option, opposite for split validation data option



        self.datasets_box.setValue(500)
        self.valid_split_slider.setValue(0.2)


        # set to open on general tab
        self.layers_tab.setCurrentIndex(0)


        self.epochs_box.setValue(5)


        self.lrate_box.setValue(0.01)
        self.lrate_box.setDecimals(4)  # Set the number of decimal places
        self.lrate_box.setRange(0.0001, 0.99)  # Set the initial range
        self.lrate_box.setSingleStep(0.0001)  # Set the step size




        self.verbiose_box.setCurrentIndex(1)
        self.batch_size_box.setValue(32)

        self.enable_stop_box.setChecked(False)
        self.monitor_var_box.setCurrentIndex(0)
        self.trigger_box.setCurrentIndex(0)
        self.tilll_stop_box.setValue(5)


        self.enable_stop_box.setChecked(False)
        self.decay_type_box.setCurrentIndex(0)
        self.rate_box.setValue(0.9)
        self.decay_start_box.setValue(5)



        self.subfolders_box.setCheckable(True)
        self.subfolders_box.setEnabled(True)
        self.subfolders_box.setChecked(True)

        self.restore_weights_box.setCheckable(True)
        self.restore_weights_box.setEnabled(True)
        self.restore_weights_box.setChecked(True)

        self.datasets_box.setRange(1,10000)
        self.datasets_box.setValue(100)


        self.valid_method_box.addItem("K Fold Training")
        self.valid_method_box.addItem("Single Training Set")
        self.valid_method_box.setCurrentIndex(0)
        self.valid_method_box.show()

        self.train_path_entry.setText(r"TrainingData\Training")
        self.valid_path_entry.setText(r"TrainingData\Testing")

        self.data_source_box.addItem("Split Existing Data")
        self.data_source_box.addItem("Use Seperate Test Data")
        self.data_source_box.setCurrentIndex(1)

        self.decay_type_box.addItem("Linear Decay")
        self.decay_type_box.addItem("Exponential Decay")
        self.decay_type_box.setCurrentIndex(0)

        self.monitor_var_box.addItem("Loss")
        self.monitor_var_box.addItem("Accuracy")
        self.monitor_var_box.setCurrentIndex(1)

        self.verbiose_box.addItem("Silent")
        self.verbiose_box.addItem("Show Epochs")
        self.verbiose_box.addItem("Show Epochs Progress")
        self.verbiose_box.setCurrentIndex(2)

        self.trigger_box.setCurrentIndex(0)
        self.trigger_box.addItem("Increase (Does not Decrease)")
        self.trigger_box.addItem("Plateau (Does not Increase)")





        self.set_train_method()
        self.set_training_source()



        self.folds_box.setValue(5)





    def hideWidgets(self, *widgets):

        for widget in widgets:
            widget.hide()

    def showWidgets(self, *widgets):

        for widget in widgets:
            widget.show()

    def collect_training_data(self):


        data = {
            "general": {
                "epochs": self.epochs_box.value(),
                "initial_learning_rate": self.lrate_box.value(),
                "batch_size": self.batch_size_box.value(),
                "data_source": self.data_source_box.currentIndex(),
                "training_dir": self.train_path_entry.text(),
                "testing_dir": self.train_path_entry.text(),
                "split": self.valid_split_slider.value(),
                "method": self.valid_method_box.currentIndex(),
                "datasets": self.datasets_box.value(),
                "folds": self.folds_box.value(),
                "subfolders": self.subfolders_box.isChecked(),
                "verbiose": self.verbiose_box.currentIndex()
            },
            "early_stopping": {
                "enable_stopping": self.enable_stop_box.isChecked(),
                "monitored_variable": self.monitor_var_box.currentText(),
                "epochs_till_stop": self.tilll_stop_box.value(),
                "stop_trigger": self.trigger_box.currentIndex(),
                "restore_weights": self.restore_weights_box.isChecked(),
            },
            "learning_rate_scheduler": {
                "type": self.decay_type_box.currentText(),
                "params": {
                    "decay_rate": self.rate_box.value(),
                    "decay_steps": self.decay_start_box.value(),
                    # Add other parameters as needed
                } if self.enable_scheduler_box.isChecked() else {}
            }
        }

        return data

    def restrictions(self):

        pass

    def set_bindings(self):
        self.data_source_box.currentIndexChanged.connect(self.set_training_source)

        self.valid_method_box.currentIndexChanged.connect(self.set_train_method)

        self.train_path_button.clicked.connect(self.open_training_folder_selector)

        self.valid_path_button.clicked.connect(self.open_validation_folder_selector)

        self.train_button.clicked.connect(self.handle_train_btn)

    def open_training_folder_selector(self):
        folder_path = self.select_folder()
        if folder_path:
            self.train_path_entry.setText(folder_path)

    def open_validation_folder_selector(self):
        folder_path = self.select_folder()
        if folder_path:
            self.valid_path_entry.setText(folder_path)

    def select_folder(self):
        options = QFileDialog.Option.ShowDirsOnly
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "", options)
        return folder_path

    def select_training_data(self):
        pass

    def set_controller(self, controller):
        self.controller = controller
        self.init_ui(self)
        self.retranslateUi(self)
        self.set_bindings()
        self.init_values()





