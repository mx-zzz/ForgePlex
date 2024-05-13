import tkinter as tk
# Model
from tkinter import font as tkfont

from PyQt6.QtWidgets import QMainWindow


from PyQt6 import QtCore, QtGui, QtWidgets
# View
class Training_View(QMainWindow):
    def __init__(self):
        super().__init__()


    def init_ui(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(553, 908)
            self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
            self.centralwidget.setAutoFillBackground(False)
            self.centralwidget.setStyleSheet("")
            self.centralwidget.setObjectName("centralwidget")
            self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
            self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 531, 861))
            self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
            self.training_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
            self.training_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
            self.training_layout.setContentsMargins(10, 10, 10, 0)
            self.training_layout.setObjectName("training_layout")
            self.training_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.training_label.sizePolicy().hasHeightForWidth())
            self.training_label.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            self.training_label.setFont(font)
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
            self.layers_tab.setGeometry(QtCore.QRect(10, 270, 491, 241))
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
            self.layers_tab.setObjectName("layers_tab")
            self.general_tab = QtWidgets.QWidget()
            self.general_tab.setObjectName("general_tab")
            self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.general_tab)
            self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 40, 461, 161))
            self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
            self.general_form = QtWidgets.QFormLayout(self.formLayoutWidget_3)
            self.general_form.setContentsMargins(10, 10, 10, 10)
            self.general_form.setVerticalSpacing(15)
            self.general_form.setObjectName("general_form")
            self.epochs_label = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.epochs_label.setFont(font)
            self.epochs_label.setObjectName("epochs_label")
            self.general_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.epochs_label)
            self.verbiose_label = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.verbiose_label.setFont(font)
            self.verbiose_label.setObjectName("verbiose_label")
            self.general_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.verbiose_label)
            self.batch_size_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
            self.batch_size_box.setObjectName("batch_size_box")
            self.general_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.batch_size_box)
            self.epochs_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
            self.epochs_box.setObjectName("epochs_box")
            self.general_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.epochs_box)
            self.doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_3)
            self.doubleSpinBox.setObjectName("doubleSpinBox")
            self.general_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.doubleSpinBox)
            self.lrate_label = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.lrate_label.setFont(font)
            self.lrate_label.setObjectName("lrate_label")
            self.general_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lrate_label)
            self.batch_size_label = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
            self.batch_size_label.setObjectName("batch_size_label")
            self.general_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.batch_size_label)
            self.verbiose_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
            self.verbiose_box.setObjectName("verbiose_box")
            self.general_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.verbiose_box)
            self.general_label = QtWidgets.QLabel(parent=self.general_tab)
            self.general_label.setGeometry(QtCore.QRect(210, 10, 51, 16))
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.general_label.setFont(font)
            self.general_label.setObjectName("general_label")
            self.layers_tab.addTab(self.general_tab, "")
            self.early_stop_tab = QtWidgets.QWidget()
            self.early_stop_tab.setObjectName("early_stop_tab")
            self.early_stop_label = QtWidgets.QLabel(parent=self.early_stop_tab)
            self.early_stop_label.setGeometry(QtCore.QRect(210, 10, 71, 16))
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setBold(True)
            font.setWeight(75)
            self.early_stop_label.setFont(font)
            self.early_stop_label.setObjectName("early_stop_label")
            self.formLayoutWidget_4 = QtWidgets.QWidget(parent=self.early_stop_tab)
            self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 40, 461, 181))
            self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
            self.early_stop_form = QtWidgets.QFormLayout(self.formLayoutWidget_4)
            self.early_stop_form.setContentsMargins(10, 10, 10, 10)
            self.early_stop_form.setVerticalSpacing(15)
            self.early_stop_form.setObjectName("early_stop_form")
            self.enable_stop_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.enable_stop_label.setFont(font)
            self.enable_stop_label.setObjectName("enable_stop_label")
            self.early_stop_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.enable_stop_label)
            self.monitor_var_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.monitor_var_label.setFont(font)
            self.monitor_var_label.setObjectName("monitor_var_label")
            self.early_stop_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.monitor_var_label)
            self.monitor_var_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
            self.monitor_var_box.setObjectName("monitor_var_box")
            self.early_stop_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.monitor_var_box)
            self.till_stop_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.till_stop_label.setFont(font)
            self.till_stop_label.setObjectName("till_stop_label")
            self.early_stop_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.till_stop_label)
            self.filters_entry1_4 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_4)
            self.filters_entry1_4.setObjectName("filters_entry1_4")
            self.early_stop_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.filters_entry1_4)
            self.trigger_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.trigger_label.setFont(font)
            self.trigger_label.setObjectName("trigger_label")
            self.early_stop_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.trigger_label)
            self.trigger_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
            self.trigger_box.setObjectName("trigger_box")
            self.early_stop_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.trigger_box)
            self.restore_weight_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.restore_weight_label.setFont(font)
            self.restore_weight_label.setObjectName("restore_weight_label")
            self.early_stop_form.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.restore_weight_label)
            self.restore_weights_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_4)
            self.restore_weights_box.setText("")
            self.restore_weights_box.setObjectName("restore_weights_box")
            self.early_stop_form.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.restore_weights_box)
            self.enable_stop_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_4)
            self.enable_stop_box.setText("")
            self.enable_stop_box.setObjectName("enable_stop_box")
            self.early_stop_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.enable_stop_box)
            self.layers_tab.addTab(self.early_stop_tab, "")
            self.lrate_scheduler_tab = QtWidgets.QWidget()
            self.lrate_scheduler_tab.setObjectName("lrate_scheduler_tab")
            self.lrate_scheduler_label = QtWidgets.QLabel(parent=self.lrate_scheduler_tab)
            self.lrate_scheduler_label.setGeometry(QtCore.QRect(200, 10, 121, 20))
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setBold(True)
            font.setWeight(75)
            self.lrate_scheduler_label.setFont(font)
            self.lrate_scheduler_label.setObjectName("lrate_scheduler_label")
            self.formLayoutWidget_5 = QtWidgets.QWidget(parent=self.lrate_scheduler_tab)
            self.formLayoutWidget_5.setGeometry(QtCore.QRect(10, 40, 461, 171))
            self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
            self.lrate_scheduler_form = QtWidgets.QFormLayout(self.formLayoutWidget_5)
            self.lrate_scheduler_form.setContentsMargins(10, 10, 10, 10)
            self.lrate_scheduler_form.setVerticalSpacing(15)
            self.lrate_scheduler_form.setObjectName("lrate_scheduler_form")
            self.min_lrate_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.min_lrate_label.setFont(font)
            self.min_lrate_label.setObjectName("min_lrate_label")
            self.lrate_scheduler_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.min_lrate_label)
            self.min_lrate_box = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_5)
            self.min_lrate_box.setObjectName("min_lrate_box")
            self.lrate_scheduler_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.min_lrate_box)
            self.type_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.type_label.setFont(font)
            self.type_label.setObjectName("type_label")
            self.lrate_scheduler_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.type_label)
            self.rate_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
            self.rate_label.setObjectName("rate_label")
            self.lrate_scheduler_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.rate_label)
            self.rate_box = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_5)
            self.rate_box.setMaximum(1.0)
            self.rate_box.setSingleStep(0.1)
            self.rate_box.setProperty("value", 0.85)
            self.rate_box.setObjectName("rate_box")
            self.lrate_scheduler_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.rate_box)
            self.decay_start_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.decay_start_label.setFont(font)
            self.decay_start_label.setObjectName("decay_start_label")
            self.lrate_scheduler_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.decay_start_label)
            self.decay_type_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_5)
            self.decay_type_box.setObjectName("decay_type_box")
            self.decay_type_box.addItem("")
            self.decay_type_box.addItem("")
            self.lrate_scheduler_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.decay_type_box)
            self.decay_start_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_5)
            self.decay_start_box.setObjectName("decay_start_box")
            self.lrate_scheduler_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.decay_start_box)
            self.layers_tab.addTab(self.lrate_scheduler_tab, "")
            self.data_settings_group = QtWidgets.QGroupBox(parent=self.training_frame)
            self.data_settings_group.setGeometry(QtCore.QRect(10, 20, 491, 241))
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.data_settings_group.setFont(font)
            self.data_settings_group.setObjectName("data_settings_group")
            self.formLayoutWidget_12 = QtWidgets.QWidget(parent=self.data_settings_group)
            self.formLayoutWidget_12.setGeometry(QtCore.QRect(0, 20, 491, 216))
            self.formLayoutWidget_12.setObjectName("formLayoutWidget_12")
            self.data_settings_form = QtWidgets.QFormLayout(self.formLayoutWidget_12)
            self.data_settings_form.setContentsMargins(20, 20, 20, 20)
            self.data_settings_form.setVerticalSpacing(15)
            self.data_settings_form.setObjectName("data_settings_form")
            self.train_data_path_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.train_data_path_label.setFont(font)
            self.train_data_path_label.setObjectName("train_data_path_label")
            self.data_settings_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.train_data_path_label)
            self.valid_data_path_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.valid_data_path_label.setFont(font)
            self.valid_data_path_label.setObjectName("valid_data_path_label")
            self.data_settings_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.valid_data_path_label)
            self.valid_data_path_hbox = QtWidgets.QHBoxLayout()
            self.valid_data_path_hbox.setObjectName("valid_data_path_hbox")
            self.valid_data_path_line = QtWidgets.QLineEdit(parent=self.formLayoutWidget_12)
            self.valid_data_path_line.setObjectName("valid_data_path_line")
            self.valid_data_path_hbox.addWidget(self.valid_data_path_line)
            self.data_select_folder = QtWidgets.QPushButton(parent=self.formLayoutWidget_12)
            self.data_select_folder.setObjectName("data_select_folder")
            self.valid_data_path_hbox.addWidget(self.data_select_folder)
            self.data_settings_form.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.valid_data_path_hbox)
            self.valid_path_hbox = QtWidgets.QHBoxLayout()
            self.valid_path_hbox.setObjectName("valid_path_hbox")
            self.valid_path_line = QtWidgets.QLineEdit(parent=self.formLayoutWidget_12)
            self.valid_path_line.setObjectName("valid_path_line")
            self.valid_path_hbox.addWidget(self.valid_path_line)
            self.pushButton_3 = QtWidgets.QPushButton(parent=self.formLayoutWidget_12)
            self.pushButton_3.setObjectName("pushButton_3")
            self.valid_path_hbox.addWidget(self.pushButton_3)
            self.data_settings_form.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.valid_path_hbox)
            self.valid_split_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
            self.valid_split_label.setObjectName("valid_split_label")
            self.data_settings_form.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.valid_split_label)
            self.datasets_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.datasets_label.setFont(font)
            self.datasets_label.setObjectName("datasets_label")
            self.data_settings_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.datasets_label)
            self.datasets_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_12)
            self.datasets_box.setObjectName("datasets_box")
            self.data_settings_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.datasets_box)
            self.data_source_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_12)
            self.data_source_box.setObjectName("data_source_box")
            self.data_source_box.addItem("")
            self.data_source_box.addItem("")
            self.data_settings_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.data_source_box)
            self.data_source_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.data_source_label.setFont(font)
            self.data_source_label.setObjectName("data_source_label")
            self.data_settings_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.data_source_label)
            self.valid_split_slider = QtWidgets.QSlider(parent=self.formLayoutWidget_12)
            self.valid_split_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
            self.valid_split_slider.setObjectName("valid_split_slider")
            self.data_settings_form.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.valid_split_slider)
            self.train_button = QtWidgets.QPushButton(parent=self.training_frame)
            self.train_button.setEnabled(True)
            self.train_button.setGeometry(QtCore.QRect(40, 780, 441, 31))
            font = QtGui.QFont()
            font.setPointSize(-1)
            self.train_button.setFont(font)
            self.train_button.setStyleSheet("QPushButton {\n"
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
            self.train_button.setObjectName("train_button")
            self.console_box = QtWidgets.QGroupBox(parent=self.training_frame)
            self.console_box.setGeometry(QtCore.QRect(10, 530, 491, 171))
            font = QtGui.QFont()
            font.setFamily("Calibri")
            self.console_box.setFont(font)
            self.console_box.setObjectName("console_box")
            self.console_output = QtWidgets.QTextBrowser(parent=self.console_box)
            self.console_output.setGeometry(QtCore.QRect(10, 20, 471, 141))
            self.console_output.setObjectName("console_output")
            self.training_progress_bar = QtWidgets.QProgressBar(parent=self.training_frame)
            self.training_progress_bar.setGeometry(QtCore.QRect(30, 720, 471, 20))
            self.training_progress_bar.setProperty("value", 24)
            self.training_progress_bar.setObjectName("training_progress_bar")
            self.time_elapsed_label = QtWidgets.QLabel(parent=self.training_frame)
            self.time_elapsed_label.setGeometry(QtCore.QRect(190, 750, 221, 16))
            self.time_elapsed_label.setObjectName("time_elapsed_label")
            self.training_layout.addWidget(self.training_frame)
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 18))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.training_status = QtWidgets.QStatusBar(parent=MainWindow)
            self.training_status.setObjectName("training_status")
            MainWindow.setStatusBar(self.training_status)

            self.retranslateUi(MainWindow)
            self.layers_tab.setCurrentIndex(2)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.training_label.setText(_translate("MainWindow", "Train Network"))
            self.epochs_label.setText(_translate("MainWindow", "Epochs"))
            self.verbiose_label.setText(_translate("MainWindow", "Verbiose"))
            self.lrate_label.setText(_translate("MainWindow", "Learning Rate"))
            self.batch_size_label.setText(_translate("MainWindow", "Batch Size"))
            self.general_label.setText(_translate("MainWindow", "General"))
            self.layers_tab.setTabText(self.layers_tab.indexOf(self.general_tab), _translate("MainWindow", "General"))
            self.early_stop_label.setText(_translate("MainWindow", "Early Stopping"))
            self.enable_stop_label.setText(_translate("MainWindow", "Enable Early Stopping"))
            self.monitor_var_label.setText(_translate("MainWindow", "Monitored Variable"))
            self.till_stop_label.setText(_translate("MainWindow", "Epochs Till Stop"))
            self.trigger_label.setText(_translate("MainWindow", "Stop Trigger"))
            self.restore_weight_label.setText(_translate("MainWindow", "Restore Best Weights"))
            self.layers_tab.setTabText(self.layers_tab.indexOf(self.early_stop_tab),
                                       _translate("MainWindow", "Early Stopping"))
            self.lrate_scheduler_label.setText(_translate("MainWindow", "Learning Rate Scheduler"))
            self.min_lrate_label.setText(_translate("MainWindow", "Minimum Learning Rate"))
            self.type_label.setText(_translate("MainWindow", "Decay Type"))
            self.rate_label.setText(_translate("MainWindow", "Decay Rate"))
            self.decay_start_label.setText(_translate("MainWindow", "Decay Start (Epochs)"))
            self.decay_type_box.setItemText(0, _translate("MainWindow", "Linear Decay"))
            self.decay_type_box.setItemText(1, _translate("MainWindow", "Exponential Decay"))
            self.layers_tab.setTabText(self.layers_tab.indexOf(self.lrate_scheduler_tab),
                                       _translate("MainWindow", "Learning Rate Scheduler"))
            self.data_settings_group.setTitle(_translate("MainWindow", "Data Settings"))
            self.train_data_path_label.setText(_translate("MainWindow", "Training Data Path"))
            self.valid_data_path_label.setText(_translate("MainWindow", "Validation Data Path"))
            self.data_select_folder.setText(_translate("MainWindow", "Select Folder"))
            self.pushButton_3.setText(_translate("MainWindow", "Select Folder"))
            self.valid_split_label.setText(_translate("MainWindow", "Validation Split"))
            self.datasets_label.setText(_translate("MainWindow", "Total Datasets"))
            self.data_source_box.setItemText(0, _translate("MainWindow", "Split Training Data"))
            self.data_source_box.setItemText(1, _translate("MainWindow", "Data From Seperate Path"))
            self.data_source_label.setText(_translate("MainWindow", "Validation Data Source"))
            self.train_button.setText(_translate("MainWindow", "Train"))
            self.console_box.setTitle(_translate("MainWindow", "Console"))
            self.time_elapsed_label.setText(_translate("MainWindow", "Time Elapsed : 00:00:00"))

    def handle_train_btn(self):
        pass


    def restrictions(self):
            pass


    def select_training_data(self):
            pass





    def set_controller(self, controller):

        self.controller = controller
        self.init_ui(self)
        self.retranslateUi(self)















