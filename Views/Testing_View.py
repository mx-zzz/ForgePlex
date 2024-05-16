
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow


# View
class Testing_View(QMainWindow):
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
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
        self.general_box = QtWidgets.QGroupBox(parent=self.fields_frame)
        self.general_box.setGeometry(QtCore.QRect(10, 20, 491, 141))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.general_box.setFont(font)
        self.general_box.setObjectName("general_box")
        self.formLayoutWidget_14 = QtWidgets.QWidget(parent=self.general_box)
        self.formLayoutWidget_14.setGeometry(QtCore.QRect(0, 30, 491, 101))
        self.formLayoutWidget_14.setObjectName("formLayoutWidget_14")
        self.general_form_3 = QtWidgets.QFormLayout(self.formLayoutWidget_14)
        self.general_form_3.setContentsMargins(20, 20, 20, 20)
        self.general_form_3.setVerticalSpacing(15)
        self.general_form_3.setObjectName("general_form_3")
        self.path_label = QtWidgets.QLabel(parent=self.formLayoutWidget_14)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.path_label.setFont(font)
        self.path_label.setObjectName("path_label")
        self.general_form_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.path_label)
        self.data_label = QtWidgets.QLabel(parent=self.formLayoutWidget_14)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.data_label.setFont(font)
        self.data_label.setObjectName("data_label")
        self.general_form_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.data_label)
        self.path_box = QtWidgets.QHBoxLayout()
        self.path_box.setObjectName("path_box")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget_14)
        self.lineEdit.setObjectName("lineEdit")
        self.path_box.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(parent=self.formLayoutWidget_14)
        self.pushButton.setObjectName("pushButton")
        self.path_box.addWidget(self.pushButton)
        self.general_form_3.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.path_box)
        self.data_entry = QtWidgets.QSpinBox(parent=self.formLayoutWidget_14)
        self.data_entry.setObjectName("data_entry")
        self.general_form_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.data_entry)
        self.test_button = QtWidgets.QPushButton(parent=self.fields_frame)
        self.test_button.setEnabled(True)
        self.test_button.setGeometry(QtCore.QRect(30, 670, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        self.test_button.setFont(font)
        self.test_button.setStyleSheet("QPushButton {\n"
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
        self.test_button.setObjectName("test_button")
        self.output_box = QtWidgets.QGroupBox(parent=self.fields_frame)
        self.output_box.setGeometry(QtCore.QRect(10, 180, 491, 201))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.output_box.setFont(font)
        self.output_box.setObjectName("output_box")
        self.formLayoutWidget_13 = QtWidgets.QWidget(parent=self.output_box)
        self.formLayoutWidget_13.setGeometry(QtCore.QRect(0, 20, 491, 181))
        self.formLayoutWidget_13.setObjectName("formLayoutWidget_13")
        self.output_form = QtWidgets.QFormLayout(self.formLayoutWidget_13)
        self.output_form.setContentsMargins(20, 20, 20, 20)
        self.output_form.setVerticalSpacing(15)
        self.output_form.setObjectName("output_form")
        self.sample_label = QtWidgets.QLabel(parent=self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.sample_label.setFont(font)
        self.sample_label.setObjectName("sample_label")
        self.output_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.sample_label)
        self.samples_entry = QtWidgets.QSpinBox(parent=self.formLayoutWidget_13)
        self.samples_entry.setObjectName("samples_entry")
        self.output_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.samples_entry)
        self.samplesize_label = QtWidgets.QLabel(parent=self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.samplesize_label.setFont(font)
        self.samplesize_label.setObjectName("samplesize_label")
        self.output_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.samplesize_label)
        self.samplesize_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_13)
        self.samplesize_box.setText("")
        self.samplesize_box.setObjectName("samplesize_box")
        self.output_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.samplesize_box)
        self.rand_label = QtWidgets.QLabel(parent=self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.rand_label.setFont(font)
        self.rand_label.setObjectName("rand_label")
        self.output_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.rand_label)
        self.rand_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_13)
        self.rand_box.setText("")
        self.rand_box.setObjectName("rand_box")
        self.output_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.rand_box)
        self.zero_label = QtWidgets.QLabel(parent=self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.zero_label.setFont(font)
        self.zero_label.setObjectName("zero_label")
        self.output_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.zero_label)
        self.zero_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_13)
        self.zero_box.setText("")
        self.zero_box.setObjectName("zero_box")
        self.output_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.zero_box)
        self.mse_label = QtWidgets.QLabel(parent=self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.mse_label.setFont(font)
        self.mse_label.setObjectName("mse_label")
        self.output_form.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.mse_label)
        self.mse_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_13)
        self.mse_box.setText("")
        self.mse_box.setObjectName("mse_box")
        self.output_form.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.mse_box)
        self.console_box = QtWidgets.QGroupBox(parent=self.fields_frame)
        self.console_box.setGeometry(QtCore.QRect(10, 400, 491, 171))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.console_box.setFont(font)
        self.console_box.setObjectName("console_box")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.console_box)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 471, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(parent=self.fields_frame)
        self.progressBar.setGeometry(QtCore.QRect(30, 600, 471, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.time_elapsed_label = QtWidgets.QLabel(parent=self.fields_frame)
        self.time_elapsed_label.setGeometry(QtCore.QRect(170, 630, 221, 16))
        self.time_elapsed_label.setObjectName("time_elapsed_label")
        self.fields_layout.addWidget(self.fields_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "Test Network"))
        self.general_box.setTitle(_translate("MainWindow", "General Setting"))
        self.path_label.setText(_translate("MainWindow", "Path"))
        self.data_label.setText(_translate("MainWindow", "Dataset Size"))
        self.pushButton.setText(_translate("MainWindow", "Select Folder"))
        self.test_button.setText(_translate("MainWindow", "Create"))
        self.output_box.setTitle(_translate("MainWindow", "Output Settings"))
        self.sample_label.setText(_translate("MainWindow", "Samples Shown"))
        self.samplesize_label.setText(_translate("MainWindow", "Sample Size"))
        self.rand_label.setText(_translate("MainWindow", "Random Control"))
        self.zero_label.setText(_translate("MainWindow", "Zero Control"))
        self.mse_label.setText(_translate("MainWindow", "Mean Squared Error"))
        self.console_box.setTitle(_translate("MainWindow", "Console"))
        self.time_elapsed_label.setText(_translate("MainWindow", "Time Elapsed : "))
        self.test_button.setText(_translate("MainWindow", "Test"))


    def handle_test_btn(self):
        pass


    def set_controller(self, controller):

        self.controller = controller
        self.init_ui(self)










