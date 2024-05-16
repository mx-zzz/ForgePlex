import sys


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QIntValidator, QRegularExpressionValidator, QIcon
from PyQt6.QtWidgets import QMainWindow, QSlider, QWidget


class Neural_Network_View(QMainWindow):
    def __init__(self):
        super().__init__()




    def init_ui(self, MainWindow):


        # Resize the main window


        self.resize(553, 908)
        self.setFixedWidth(550)
        self.setFixedHeight(900)

        # Create and set the central widget

        # Set the window title
        self.setWindowTitle("Neural Network Viewer")

        # Set the window icon
        self.setWindowIcon(QIcon('Icons\\Icon1.png'))
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 531, 851))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.fields_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.fields_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.fields_layout.setContentsMargins(10, 10, 10, 0)
        self.fields_layout.setObjectName("fields_layout")
        self.title_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
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
        self.layers_tab.setGeometry(QtCore.QRect(10, 180, 491, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layers_tab.sizePolicy().hasHeightForWidth())
        self.layers_tab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.layers_tab.setFont(font)
        self.layers_tab.setStyleSheet("/* Style for all tabs */\n"
                                      "QTabBar::tab {\n"
                                      "    background: #f0f0f0; /* Light gray background */\n"
                                      "    border: 2px solid #555; /* Gray border */\n"
                                      "    border-bottom-color: transparent; /* Makes the bottom border invisible */\n"
                                      "    border-top-left-radius: 4px; /* Rounded corners on the top-left */\n"
                                      "    border-top-right-radius: 4px; /* Rounded corners on the top-right */\n"
                                      "    padding: 5px; /* Space between the text and the border */\n"
                                      "    margin-right: 2px; /* Space between tabs */\n"
                                      "}\n"
                                      "\n"
                                      "/* Style for the selected tab */\n"
                                      "QTabBar::tab:selected {\n"
                                      "    background: #a0a0a0; /* Darker background for the selected tab */\n"
                                      "    border-color: #444; /* Darker border color for the selected tab */\n"
                                      "}\n"
                                      "\n"
                                      "/* Style for a tab when the mouse hovers over it */\n"
                                      "QTabBar::tab:hover {\n"
                                      "    background: #b0b0b0; /* Slightly darker background on hover */\n"
                                      "}\n"
                                      "QTabWidget::pane {\n"
                                      "    background: #f2f2f2; /* Light gray background for the tab content area */\n"
                                      "    border: 1px solid #c0c0c0; /* Optional: Add a border around the content area */\n"
                                      "}\n"
                                      "")
        self.layers_tab.setDocumentMode(False)
        self.layers_tab.setTabsClosable(False)
        self.layers_tab.setObjectName("general_tab")



        self.layer1 = QtWidgets.QWidget()
        self.layer1.setObjectName("layer1")
        self.formLayoutarch1 = QtWidgets.QWidget(parent=self.layer1)
        self.formLayoutarch1.setGeometry(QtCore.QRect(10, 37, 461, 250))
        self.formLayoutarch1.setObjectName("formLayoutarch1")
        self.arch_form1 = QtWidgets.QFormLayout(self.formLayoutarch1)
        self.arch_form1.setContentsMargins(10, 10, 10, 10)
        self.arch_form1.setVerticalSpacing(15)
        self.arch_form1.setObjectName("arch_form1")
        self.type_label1 = QtWidgets.QLabel(parent=self.formLayoutarch1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.type_label1.setFont(font)
        self.type_label1.setObjectName("epochs_label")
        self.arch_form1.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.type_label1)
        self.type_entry1 = QtWidgets.QComboBox(parent=self.formLayoutarch1)
        self.type_entry1.setObjectName("type_entry1")
        self.arch_form1.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.type_entry1)
        self.kernal_label1 = QtWidgets.QLabel(parent=self.formLayoutarch1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.kernal_label1.setFont(font)
        self.kernal_label1.setObjectName("kernal_label1")
        self.arch_form1.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.kernal_label1)
        self.filters_label1 = QtWidgets.QLabel(parent=self.formLayoutarch1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.filters_label1.setFont(font)
        self.filters_label1.setObjectName("verbiose_label")
        self.arch_form1.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.filters_label1)
        self.pool_label1 = QtWidgets.QLabel(parent=self.formLayoutarch1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pool_label1.setFont(font)
        self.pool_label1.setObjectName("pool_label1")
        self.arch_form1.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pool_label1)
        self.activation_label1 = QtWidgets.QLabel(parent=self.formLayoutarch1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.activation_label1.setFont(font)
        self.activation_label1.setObjectName("activation_label1")
        self.arch_form1.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.activation_label1)
        self.kernal_entry1 = QtWidgets.QComboBox(parent=self.formLayoutarch1)
        self.kernal_entry1.setObjectName("kernal_entry1")
        self.arch_form1.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.kernal_entry1)
        self.filters_entry1 = QtWidgets.QSpinBox(parent=self.formLayoutarch1)
        self.filters_entry1.setObjectName("filters_entry1")
        self.arch_form1.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.filters_entry1)

        self.dense_entry1 = QtWidgets.QSpinBox(parent=self.formLayoutarch1)
        self.dense_entry1.setObjectName("dense_entry1")
        self.arch_form1.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dense_entry1)

        self.dense_label1 = QtWidgets.QLabel(parent=self.formLayoutarch1)
        self.dense_label1.setObjectName("dense_label1")

        self.flatten_label1 = QtWidgets.QLabel("Flatten", parent=self.formLayoutarch1)
        self.flatten_label1.setObjectName("flatten_label1")
        self.arch_form1.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.flatten_label1)
        self.flatten_entry1 = QtWidgets.QCheckBox(parent=self.formLayoutarch1)
        self.flatten_entry1.setText("")
        self.flatten_entry1.setObjectName("flatten_entry1")
        self.arch_form1.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.flatten_entry1)


        self.arch_form1.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dense_label1)


        self.pool_entry1 = QtWidgets.QComboBox(parent=self.formLayoutarch1)
        self.pool_entry1.setObjectName("pool_entry1")
        self.arch_form1.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pool_entry1)
        self.activation_entry1 = QtWidgets.QComboBox(parent=self.formLayoutarch1)
        self.activation_entry1.setObjectName("activation_entry1")
        self.arch_form1.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.activation_entry1)
        self.formLayoutreg1 = QtWidgets.QWidget(parent=self.layer1)
        self.formLayoutreg1.setGeometry(QtCore.QRect(10, 260, 461, 162))
        self.formLayoutreg1.setObjectName("formLayoutreg1")
        self.reg_form1 = QtWidgets.QFormLayout(self.formLayoutreg1)
        self.reg_form1.setContentsMargins(10, 10, 10, 10)
        self.reg_form1.setHorizontalSpacing(10)
        self.reg_form1.setVerticalSpacing(15)
        self.reg_form1.setObjectName("reg_form1")
        self.dropout_label1 = QtWidgets.QLabel(parent=self.formLayoutreg1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.dropout_label1.setFont(font)
        self.dropout_label1.setObjectName("dropout_label1")
        self.reg_form1.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dropout_label1)
        self.dropout_entry1 = QtWidgets.QSlider(parent=self.formLayoutreg1)
        self.dropout_entry1.setAutoFillBackground(False)
        self.dropout_entry1.setMaximum(100)
        self.dropout_entry1.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dropout_entry1.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.dropout_entry1.setTickInterval(5)
        self.dropout_entry1.setObjectName("dropout_entry1")
        self.reg_form1.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dropout_entry1)
        self.l1_label1 = QtWidgets.QLabel(parent=self.formLayoutreg1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.l1_label1.setFont(font)
        self.l1_label1.setObjectName("l1_label1")
        self.reg_form1.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l1_label1)
        self.l1_entry1 = QtWidgets.QSlider(parent=self.formLayoutreg1)
        self.l1_entry1.setMaximum(100)
        self.l1_entry1.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.l1_entry1.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.l1_entry1.setTickInterval(5)
        self.l1_entry1.setObjectName("l1_entry1")
        self.reg_form1.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.l1_entry1)
        self.l2_label1 = QtWidgets.QLabel(parent=self.formLayoutreg1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.l2_label1.setFont(font)
        self.l2_label1.setObjectName("l2_label1")
        self.reg_form1.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.l2_label1)
        self.l2_entry1 = QtWidgets.QSlider(parent=self.formLayoutreg1)
        self.l2_entry1.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.l2_entry1.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.l2_entry1.setTickInterval(5)
        self.l2_entry1.setObjectName("l2_entry1")
        self.reg_form1.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.l2_entry1)
        self.batch_label1 = QtWidgets.QLabel(parent=self.formLayoutreg1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.batch_label1.setFont(font)
        self.batch_label1.setObjectName("batch_label1")
        self.reg_form1.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.batch_label1)
        self.batch_entry1 = QtWidgets.QCheckBox(parent=self.formLayoutreg1)
        self.batch_entry1.setText("")
        self.batch_entry1.setObjectName("batch_entry1")
        self.reg_form1.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.batch_entry1)
        self.reg_label1 = QtWidgets.QLabel(parent=self.layer1)
        self.reg_label1.setGeometry(QtCore.QRect(200, 240, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        self.reg_label1.setFont(font)
        self.reg_label1.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.reg_label1.setObjectName("reg_label1")
        self.arch_label1 = QtWidgets.QLabel(parent=self.layer1)
        self.arch_label1.setGeometry(QtCore.QRect(200, 10, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        self.arch_label1.setFont(font)
        self.arch_label1.setObjectName("arch_label1")
        self.layers_tab.addTab(self.layer1, "")




        self.layer2 = QtWidgets.QWidget()
        self.layer2.setObjectName("layer2")
        self.formLayoutarch2 = QtWidgets.QWidget(parent=self.layer2)
        self.formLayoutarch2.setGeometry(QtCore.QRect(10, 37, 461, 250))
        self.formLayoutarch2.setObjectName("formLayoutarch2")
        self.arch_label2 = QtWidgets.QLabel(parent=self.layer2)
        self.arch_label2.setGeometry(QtCore.QRect(200, 10, 251, 16))
        self.arch_label2.setObjectName("arch_label2")
        self.arch_label2.setFont(font)

        font.setBold(False)
        self.arch_form2 = QtWidgets.QFormLayout(self.formLayoutarch2)
        self.arch_form2.setContentsMargins(10, 10, 10, 10)
        self.arch_form2.setVerticalSpacing(15)
        self.arch_form2.setObjectName("arch_form2")



        self.type_label2 = QtWidgets.QLabel(parent=self.formLayoutarch2)
        self.type_label2.setObjectName("type_label2")
        self.type_label2.setFont(font)
        self.arch_form2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.type_label2)


        self.type_entry2 = QtWidgets.QComboBox(parent=self.formLayoutarch2)
        self.type_entry2.setObjectName("type_entry2")
        self.arch_form2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.type_entry2)


        self.kernal_label2 = QtWidgets.QLabel(parent=self.formLayoutarch2)
        self.kernal_label2.setObjectName("kernal_label2")
        self.kernal_label2.setFont(font)
        self.arch_form2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.kernal_label2)

        self.filters_label2 = QtWidgets.QLabel(parent=self.formLayoutarch2)
        self.filters_label2.setObjectName("filters_label2")
        self.filters_label2.setFont(font)
        self.arch_form2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.filters_label2)

        self.dense_entry2 = QtWidgets.QSpinBox(parent=self.formLayoutarch2)
        self.dense_entry2.setObjectName("dense_entry2")
        self.arch_form2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dense_entry2)

        self.dense_label2 = QtWidgets.QLabel(parent=self.formLayoutarch2)
        self.dense_label2.setObjectName("dense_label2")
        self.dense_label2.setFont(font)
        self.arch_form2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dense_label2)

        self.arch_form2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.filters_label2)
        self.pool_label2 = QtWidgets.QLabel(parent=self.formLayoutarch2)
        self.pool_label2.setObjectName("pool_label2")
        self.pool_label2.setFont(font)

        self.arch_form2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pool_label2)
        self.activation_label2 = QtWidgets.QLabel(parent=self.formLayoutarch2)
        self.activation_label2.setObjectName("activation_label2")
        self.activation_label2.setFont(font)

        self.arch_form2.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.activation_label2)
        self.kernal_entry2 = QtWidgets.QComboBox(parent=self.formLayoutarch2)
        self.kernal_entry2.setObjectName("kernal_entry2")
        self.arch_form2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.kernal_entry2)
        self.filters_entry2 = QtWidgets.QSpinBox(parent=self.formLayoutarch2)
        self.filters_entry2.setObjectName("filters_entry2")
        self.arch_form2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.filters_entry2)
        self.pool_entry2 = QtWidgets.QComboBox(parent=self.formLayoutarch2)
        self.pool_entry2.setObjectName("pool_entry2")

        self.flatten_label2 = QtWidgets.QLabel("Flatten", parent=self.formLayoutarch2)
        self.flatten_label2.setObjectName("flatten_label2")
        self.flatten_label2.setFont(font)
        self.arch_form2.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.flatten_label2)
        self.flatten_entry2 = QtWidgets.QCheckBox(parent=self.formLayoutarch2)
        self.flatten_entry2.setText("")
        self.flatten_entry2.setObjectName("flatten_entry2")
        self.arch_form2.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.flatten_entry2)

        self.arch_form2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pool_entry2)

        self.activation_entry2 = QtWidgets.QComboBox(parent=self.formLayoutarch2)
        self.activation_entry2.setObjectName("activation_entry2")
        self.arch_form2.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.activation_entry2)
        self.reg_label2 = QtWidgets.QLabel(parent=self.layer2)
        self.reg_label2.setGeometry(QtCore.QRect(200, 240, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.reg_label2.setFont(font)
        self.reg_label2.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.reg_label2.setObjectName("reg_label2")
        self.formLayoutreg2 = QtWidgets.QWidget(parent=self.layer2)
        self.formLayoutreg2.setGeometry(QtCore.QRect(10, 260, 461, 81))
        self.formLayoutreg2.setObjectName("formLayoutreg2")
        self.reg_form2 = QtWidgets.QFormLayout(self.formLayoutreg2)
        self.reg_form2.setContentsMargins(10, 10, 10, 10)
        self.reg_form2.setHorizontalSpacing(10)
        self.reg_form2.setVerticalSpacing(15)
        self.reg_form2.setObjectName("reg_form2")
        self.dropout_label2 = QtWidgets.QLabel(parent=self.formLayoutreg2)
        self.dropout_label2.setObjectName("dropout_label2")
        self.reg_form2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dropout_label2)
        self.dropout_entry2 = QtWidgets.QSlider(parent=self.formLayoutreg2)
        self.dropout_entry2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dropout_entry2.setObjectName("dropout_entry2")
        self.reg_form2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dropout_entry2)
        self.batch_label2 = QtWidgets.QLabel(parent=self.formLayoutreg2)
        self.batch_label2.setObjectName("batch_label2")
        self.reg_form2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.batch_label2)
        self.batch_entry2 = QtWidgets.QCheckBox(parent=self.formLayoutreg2)
        self.batch_entry2.setText("")
        self.batch_entry2.setObjectName("batch_entry2")
        self.reg_form2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.batch_entry2)
        self.layers_tab.addTab(self.layer2, "")

        self.layer3 = QtWidgets.QWidget()
        self.layer3.setObjectName("layer3")
        self.arch_label3 = QtWidgets.QLabel(parent=self.layer3)
        self.arch_label3.setGeometry(QtCore.QRect(200, 10, 251, 16))
        self.arch_label3.setObjectName("arch_label3")
        font.setBold(True)
        self.arch_label3.setFont(font)
        font.setBold(False)

        self.formLayoutarch3 = QtWidgets.QWidget(parent=self.layer3)
        self.formLayoutarch3.setGeometry(QtCore.QRect(10, 37, 461, 250))
        self.formLayoutarch3.setObjectName("formLayoutarch3")
        self.arch_form3 = QtWidgets.QFormLayout(self.formLayoutarch3)
        self.arch_form3.setContentsMargins(10, 10, 10, 10)
        self.arch_form3.setVerticalSpacing(15)
        self.arch_form3.setObjectName("arch_form3")
        self.type_label3 = QtWidgets.QLabel(parent=self.formLayoutarch3)
        self.type_label3.setObjectName("type_label3")
        self.type_label3.setFont(font)
        self.arch_form3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.type_label3)
        self.type_entry3 = QtWidgets.QComboBox(parent=self.formLayoutarch3)
        self.type_entry3.setObjectName("type_entry3")
        self.arch_form3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.type_entry3)
        self.kernal_label3 = QtWidgets.QLabel(parent=self.formLayoutarch3)
        self.kernal_label3.setObjectName("kernal_label3")
        self.arch_form3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.kernal_label3)
        self.kernal_label3.setFont(font)

        self.filters_label3 = QtWidgets.QLabel(parent=self.formLayoutarch3)
        self.filters_label3.setObjectName("filters_label3")
        self.filters_label3.setFont(font)

        self.dense_entry3 = QtWidgets.QSpinBox(parent=self.formLayoutarch3)
        self.dense_entry3.setObjectName("dense_entry3")
        self.arch_form3.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dense_entry3)

        self.dense_label3 = QtWidgets.QLabel(parent=self.formLayoutarch3)
        self.dense_label3.setObjectName("dense_label3")
        self.dense_label3.setFont(font)
        self.arch_form3.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dense_label3)

        self.arch_form3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.filters_label3)
        self.pool_label3 = QtWidgets.QLabel(parent=self.formLayoutarch3)
        self.pool_label3.setObjectName("pool_label3")
        self.pool_label3.setFont(font)

        self.arch_form3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pool_label3)
        self.activation_label3 = QtWidgets.QLabel(parent=self.formLayoutarch3)
        self.activation_label3.setObjectName("activation_label3")
        self.activation_label3.setFont(font)

        self.arch_form3.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.activation_label3)
        self.kernal_entry3 = QtWidgets.QComboBox(parent=self.formLayoutarch3)
        self.kernal_entry3.setObjectName("kernal_entry3")
        self.arch_form3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.kernal_entry3)
        self.filters_entry3 = QtWidgets.QSpinBox(parent=self.formLayoutarch3)
        self.filters_entry3.setObjectName("filters_entry3")
        self.arch_form3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.filters_entry3)
        self.pool_entry3 = QtWidgets.QComboBox(parent=self.formLayoutarch3)
        self.pool_entry3.setObjectName("pool_entry3")
        self.arch_form3.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pool_entry3)
        self.activation_entry3 = QtWidgets.QComboBox(parent=self.formLayoutarch3)
        self.activation_entry3.setObjectName("activation_entry3")
        self.arch_form3.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.activation_entry3)

        self.flatten_label3 = QtWidgets.QLabel("Flatten", parent=self.formLayoutarch3)
        self.flatten_label3.setObjectName("flatten_label3")
        self.arch_form3.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.flatten_label3)
        self.flatten_entry3 = QtWidgets.QCheckBox(parent=self.formLayoutarch3)
        self.flatten_entry3.setText("")
        self.flatten_entry3.setObjectName("flatten_entry3")
        self.arch_form3.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.flatten_entry3)

        self.reg_label3 = QtWidgets.QLabel(parent=self.layer3)
        self.reg_label3.setGeometry(QtCore.QRect(200, 240, 251, 16))



        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.reg_label3.setFont(font)
        self.reg_label3.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.reg_label3.setObjectName("reg_label3")
        self.formLayoutreg3 = QtWidgets.QWidget(parent=self.layer3)
        self.formLayoutreg3.setGeometry(QtCore.QRect(10, 260, 461, 81))
        self.formLayoutreg3.setObjectName("formLayoutreg3")
        self.reg_form3 = QtWidgets.QFormLayout(self.formLayoutreg3)
        self.reg_form3.setContentsMargins(10, 10, 10, 10)
        self.reg_form3.setHorizontalSpacing(10)
        self.reg_form3.setVerticalSpacing(15)
        self.reg_form3.setObjectName("reg_form3")
        self.dropout_label3 = QtWidgets.QLabel(parent=self.formLayoutreg3)
        self.dropout_label3.setObjectName("dropout_label3")
        self.reg_form3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dropout_label3)
        self.dropout_entry3 = QtWidgets.QSlider(parent=self.formLayoutreg3)
        self.dropout_entry3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dropout_entry3.setObjectName("dropout_entry3")
        self.reg_form3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dropout_entry3)
        self.batch_label3 = QtWidgets.QLabel(parent=self.formLayoutreg3)
        self.batch_label3.setObjectName("batch_label3")
        self.reg_form3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.batch_label3)
        self.batch_entry3 = QtWidgets.QCheckBox(parent=self.formLayoutreg3)
        self.batch_entry3.setText("")
        self.batch_entry3.setObjectName("batch_entry3")
        self.reg_form3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.batch_entry3)
        self.layers_tab.addTab(self.layer3, "")





        self.compile_box = QtWidgets.QGroupBox(parent=self.fields_frame)
        self.compile_box.setGeometry(QtCore.QRect(10, 660, 491, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.compile_box.sizePolicy().hasHeightForWidth())
        self.compile_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.compile_box.setFont(font)
        self.compile_box.setObjectName("compile_box")
        self.formLayout_compile = QtWidgets.QWidget(parent=self.compile_box)
        self.formLayout_compile.setGeometry(QtCore.QRect(10, 20, 471, 77))
        self.formLayout_compile.setObjectName("formLayout_compile")
        self.compile_form = QtWidgets.QFormLayout(self.formLayout_compile)
        self.compile_form.setContentsMargins(10, 10, 10, 10)
        self.compile_form.setVerticalSpacing(15)
        self.compile_form.setObjectName("compile_form")
        self.lrate_label = QtWidgets.QLabel(parent=self.formLayout_compile)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.lrate_label.setFont(font)
        self.lrate_label.setObjectName("lrate_label")
        self.compile_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lrate_label)
        self.lrate_entry = QtWidgets.QDoubleSpinBox(parent=self.formLayout_compile)
        self.lrate_entry.setObjectName("lrate_entry")
        self.compile_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lrate_entry)
        self.compiler_label = QtWidgets.QLabel(parent=self.formLayout_compile)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.compiler_label.setFont(font)
        self.compiler_label.setObjectName("compiler_label")
        self.compile_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.compiler_label)
        self.compiler_entry = QtWidgets.QComboBox(parent=self.formLayout_compile)
        self.compiler_entry.setObjectName("compiler_entry")
        self.compile_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.compiler_entry)

        self.general_box = QtWidgets.QGroupBox(parent=self.fields_frame)
        self.general_box.setGeometry(QtCore.QRect(10, 20, 491, 141))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.general_box.setFont(font)
        self.general_box.setObjectName("general_box")

        # Create a container widget for the form inside the group box
        self.general_form_widget = QtWidgets.QWidget(parent=self.general_box)
        self.general_form_widget.setGeometry(QtCore.QRect(0, 20, 491, 134))
        self.general_form_widget.setObjectName("general_form_widget")

        # Create a form layout and set it to the container widget
        self.general_form_layout = QtWidgets.QFormLayout(self.general_form_widget)
        self.general_form_layout.setContentsMargins(20, 20, 20, 20)
        self.general_form_layout.setVerticalSpacing(15)
        self.general_form_layout.setObjectName("general_form_layout")

        # Create and add widgets to the form layout
        self.name_label = QtWidgets.QLabel("Name", parent=self.general_form_widget)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.general_form_layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.name_label)

        self.name_entry = QtWidgets.QLineEdit(parent=self.general_form_widget)
        self.name_entry.setObjectName("name_entry")
        self.general_form_layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.name_entry)

        self.time_label = QtWidgets.QLabel("Time Step", parent=self.general_form_widget)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.general_form_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.time_label)

        self.time_entry = QtWidgets.QSpinBox(parent=self.general_form_widget)
        self.time_entry.setObjectName("time_entry")
        self.general_form_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.time_entry)

        self.layers_label = QtWidgets.QLabel("Layers", parent=self.general_form_widget)
        self.layers_label.setFont(font)
        self.layers_label.setObjectName("layers_label")
        self.general_form_layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.layers_label)

        self.layers_entry = QtWidgets.QComboBox(parent=self.general_form_widget)
        self.layers_entry.setObjectName("layers_entry")


        self.general_form_layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.layers_entry)

        self.create_button = QtWidgets.QPushButton(parent=self.fields_frame)
        self.create_button.setEnabled(True)
        self.create_button.setGeometry(QtCore.QRect(30, 780, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.create_button.setFont(font)
        self.create_button.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid #8f8f8f;\n"
                                         "    border-radius: 2px;\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                         "    padding: 5px;\n"
                                         "    font-size: 14px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    border: 2px solid #3daee9;\n"
                                         "}\n"
                                         "")
        self.create_button.setObjectName("create_button")
        self.fields_layout.addWidget(self.fields_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 22))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "New Neural Network"))  # Corrected "Nework" to "Network"

        # Layer 1
        self.type_label1.setText(_translate("MainWindow", "Layer Type"))
        self.kernal_label1.setText(
            _translate("MainWindow", "Kernel Size"))  # Consider renaming to kernel_label1 if it's a typo
        self.filters_label1.setText(_translate("MainWindow", "Filters"))
        self.dense_label1.setText(_translate("MainWindow", "Dense size"))
        self.pool_label1.setText(_translate("MainWindow", "1D Pooling Size"))
        self.activation_label1.setText(_translate("MainWindow", "Activation Function"))
        self.dropout_label1.setText(_translate("MainWindow", "Drop Out"))
        self.l1_label1.setText(_translate("MainWindow", "L1 Regularization"))
        self.l2_label1.setText(_translate("MainWindow", "L2 Regularization"))
        self.batch_label1.setText(_translate("MainWindow", "Batch Normalization"))
        self.reg_label1.setText(_translate("MainWindow", "Regularization"))
        self.arch_label1.setText(
            _translate("MainWindow", "Architecture"))  # Corrected "Architechture" to "Architecture"
        self.layers_tab.setTabText(self.layers_tab.indexOf(self.layer1), _translate("MainWindow", "Layer 1"))

        # Layer 2 - Ensure consistency in naming and corrections
        self.arch_label2.setText(_translate("MainWindow", "Architecture"))
        self.type_label2.setText(_translate("MainWindow", "Layer Type"))
        self.kernal_label2.setText(
            _translate("MainWindow", "Kernel Size"))  # Corrected to kernal_label2 from kernal_label1_2 for consistency
        self.filters_label2.setText(_translate("MainWindow", "Filters"))
        self.dense_label2.setText(_translate("MainWindow", "Dense size"))
        self.pool_label2.setText(_translate("MainWindow", "1D Pooling Size"))
        self.activation_label2.setText(_translate("MainWindow", "Activation Function"))
        self.dropout_label2.setText(_translate("MainWindow", "Drop Out"))
        self.batch_label2.setText(_translate("MainWindow", "Batch Normalization"))
        self.reg_label2.setText(_translate("MainWindow", "Regularization"))
        self.layers_tab.setTabText(self.layers_tab.indexOf(self.layer2), _translate("MainWindow", "Layer 2"))

        # Layer 3 - Ensure naming consistency
        self.arch_label3.setText(_translate("MainWindow", "Architecture"))  # Corrected variable name to arch_label3
        self.type_label3.setText(_translate("MainWindow", "Layer Type"))  # Corrected variable name to type_label3
        self.kernal_label3.setText(_translate("MainWindow", "Kernel Size"))  # Corrected variable name to kernal_label3
        self.filters_label3.setText(_translate("MainWindow", "Filters"))  # Corrected variable name to filters_label3
        self.dense_label3.setText(_translate("MainWindow", "Dense size"))  # Corrected variable name to filters_label3
        self.pool_label3.setText(_translate("MainWindow", "1D Pooling Size"))  # Corrected variable name to pool_label3
        self.activation_label3.setText(
            _translate("MainWindow", "Activation Function"))  # Corrected variable name to activation_label3
        self.dropout_label3.setText(_translate("MainWindow", "Drop Out"))  # Corrected variable name to dropout_label3
        self.batch_label3.setText(
            _translate("MainWindow", "Batch Normalization"))  # Corrected variable name to batch_label3
        self.reg_label3.setText(_translate("MainWindow", "Regularization"))  # Corrected variable name to reg_label3
        self.layers_tab.setTabText(self.layers_tab.indexOf(self.layer3), _translate("MainWindow", "Layer 3"))



        # Compile and General Settings
        self.compile_box.setTitle(_translate("MainWindow", "Compile Settings"))
        self.lrate_label.setText(_translate("MainWindow", "Learning Rate"))
        self.compiler_label.setText(_translate("MainWindow", "Compiler"))
        self.general_box.setTitle(_translate("MainWindow", "General Settings"))  # Added 's' to "Setting"
        self.name_label.setText(_translate("MainWindow", "Name"))
        self.layers_label.setText(_translate("MainWindow", "Layers"))
        self.time_label.setText(
            _translate("MainWindow", "Time Step"))  # Corrected variable name to time_label for consistency
        self.create_button.setText(_translate("MainWindow", "Create"))



    def set_default_settings(self):
        self.name_entry.setText("Untitled Network")
        self.time_entry.setValue(100)  # Set the default value to 64
        self.layers_entry.setCurrentIndex(2)  # 3rd option, zero-based index

        self.kernal_entry1.setCurrentIndex(2)  # Corrected to affect kernal_entry1
        self.filters_entry1.setValue(32)  # Set the default value to 64
        self.pool_entry1.setCurrentIndex(0)
        self.activation_entry1.setCurrentIndex(0)
        self.dropout_entry1.setValue(20)
        self.l1_entry1.setValue(20)
        self.l2_entry1.setValue(20)
        self.batch_entry1.setChecked(True)  # Assuming self.batch_entry1 is a QCheckBox or similar'
        self.dense_entry1.setValue(100)

        self.kernal_entry2.setCurrentIndex(2)  # Now correctly referring to kernal_entry2
        self.filters_entry2.setValue(64)  # Set the default value to 64
        self.pool_entry2.setCurrentIndex(2)  # Sets the default pooling size for pool_entry2
        self.activation_entry2.setCurrentIndex(0)  # Sets the default activation function for activation_entry2
        self.dropout_entry2.setValue(20)  # Sets the initial value for dropout
        self.batch_entry2.setChecked(True)  # Assuming self.batch_entry1 is a QCheckBox or similar
        self.flatten_entry2.setChecked(True) # Assuming self.
        self.dense_entry2.setValue(100)

        self.kernal_entry3.setCurrentIndex(2)  # Set default kernel size for kernal_entry3
        self.filters_entry3.setValue(64)  # Set default value to 64
        self.pool_entry3.setCurrentIndex(0)  # Set default pooling size for pool_entry3
        self.activation_entry3.setCurrentIndex(0)  # Set default activation function for activation_entry3
        self.dropout_entry3.setValue(20)  # Set initial value for dropout
        self.batch_entry3.setChecked(True)  # Assuming self.batch_entry1 is a QCheckBox or similar
        self.dense_entry3.setValue(100)


        self.lrate_entry.setRange(0.0001, 1)
        self.lrate_entry.setValue(0.0001)
        self.lrate_entry.setSingleStep(0.0001)
        self.lrate_entry.setDecimals(4)
        self.compiler_entry.setCurrentIndex(0)  # Set the default value to 0


    def restrictions(self):


        regex = QRegularExpression("[a-zA-Z0-9 ]+")
        self.name_entry.setValidator(QRegularExpressionValidator(regex))
        self.name_entry.setEnabled(True)

        # Optionally, set the range if needed
        self.time_entry.setMinimum(1)  # Set the minimum value
        self.time_entry.setMaximum(1000)  # Set the maximum value

        self.type_entry1.addItems(["Conv"])
        self.kernal_entry1.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.layers_entry.addItems(["1 layer", "2 layers", "3 layers"])  # Correct grammar
        self.filters_entry1.setMinimum(1)  # Set the minimum value
        self.filters_entry1.setMaximum(1000)  # Set the maximum value
        self.pool_entry1.addItems(["None","1", "2", "3"])
        self.activation_entry1.addItems(["Tanh", "Relu"])

        self.dropout_entry1.setTickInterval(10)
        self.dropout_entry1.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.l1_entry1.setTickInterval(10)
        self.l1_entry1.setTickPosition(QSlider.TickPosition.TicksBelow)  # Correct method and enum
        self.l2_entry1.setTickInterval(10)
        self.l2_entry1.setTickPosition(QSlider.TickPosition.TicksBelow)  # Correct method and enum



        self.type_entry2.addItems(["Conv", "Dense"])
        self.kernal_entry2.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.filters_entry2.setMinimum(1)  # Set the minimum value
        self.filters_entry2.setMaximum(1000)  # Set the maximum value
        self.pool_entry2.addItems(["None","1", "2", "3"])
        self.activation_entry2.addItems(["Tanh", "Relu"])
        self.dropout_entry2.setTickInterval(10)  # Sets the interval between ticks
        self.dropout_entry2.setTickPosition(
            QSlider.TickPosition.TicksBelow)  # Correct method call with enum for tick position


        self.type_entry3.addItems(["Conv", "Dense"])
        self.kernal_entry3.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.filters_entry3.setMinimum(1)  # Set minimum value
        self.filters_entry3.setMaximum(1000)  # Set maximum value
        self.pool_entry3.addItems(["None","1", "2", "3"])
        self.activation_entry3.addItems(["Tanh", "Relu"])
        self.dropout_entry3.setTickInterval(10)  # Set interval between ticks
        self.dropout_entry3.setTickPosition(QSlider.TickPosition.TicksBelow)


        self.compiler_entry.addItems(["Adam", "RMSprop", "SGD"])
        self.compiler_entry.setCurrentIndex(0)  # Set default optimizer for compile_box

        # set default layer types


        self.type_entry1.setCurrentIndex(0)
        self.type_entry2.setCurrentIndex(0)
        self.type_entry3.setCurrentIndex(1)


        # Update the layer types to default types
        self.controller.on_type_change(1)
        self.controller.on_type_change(2)
        self.controller.on_type_change(3)

        self.type_entry1.currentIndexChanged.connect(lambda: self.controller.on_type_change(1))
        self.type_entry2.currentIndexChanged.connect(lambda: self.controller.on_type_change(2))
        self.type_entry3.currentIndexChanged.connect(lambda: self.controller.on_type_change(3))



        self.layers_entry.currentIndexChanged.connect(self.controller.on_layer_box_change)

        self.create_button.clicked.connect(self.handle_create_btn)









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
            },
            "compile": {
                "learning_rate": self.lrate_entry.value(),
                "compiler": self.compiler_entry.currentText(),
            },
            "layers": []
        }

        # Collect layer-specific configurations
        for i in range(self.layers_tab.count()):
            layer = {
                "type": self.layers_tab.widget(i).findChild(QtWidgets.QComboBox, f"type_entry{i + 1}").currentText(),
                "kernel": self.layers_tab.widget(i).findChild(QtWidgets.QComboBox,
                                                              f"kernal_entry{i + 1}").currentText(),
                "filters": self.layers_tab.widget(i).findChild(QtWidgets.QSpinBox, f"filters_entry{i + 1}").value(),
                "dense_units": self.layers_tab.widget(i).findChild(QtWidgets.QSpinBox, f"dense_entry{i + 1}").value(),
                "pooling": self.layers_tab.widget(i).findChild(QtWidgets.QComboBox, f"pool_entry{i + 1}").currentText(),
                "activation": self.layers_tab.widget(i).findChild(QtWidgets.QComboBox,
                                                                  f"activation_entry{i + 1}").currentText(),
                "dropout_rate": self.layers_tab.widget(i).findChild(QtWidgets.QSlider,
                                                                    f"dropout_entry{i + 1}").value() / 100.0,
                "batch_normalization": self.layers_tab.widget(i).findChild(QtWidgets.QCheckBox,
                                                                           f"batch_entry{i + 1}").isChecked(),
                "flatten": self.layers_tab.widget(i).findChild(QtWidgets.QCheckBox,f"flatten_entry{i + 1}").isChecked()
            }

            if i == 0:
                print("l1 entry is here")

                # Assuming `layer` is already defined as a dictionary
                # Update or add the new key-value pair
                layer[f"l1_reg"] = self.layers_tab.widget(i).findChild(QtWidgets.QSlider,
                                                                                f"l1_entry{i + 1}").value() / 100.0

                layer[f"l2_reg"] = self.layers_tab.widget(i).findChild(QtWidgets.QSlider,
                                                                                f"l2_entry{i + 1}").value() / 100.0



            data["layers"].append(layer)

        return data

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

        self.init_ui(self)































