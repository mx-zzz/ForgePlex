from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QFileDialog



# View
class Training_View(QMainWindow):

    def __init__(self):
        super().__init__()

    def retranslateUi(self, TrainingMenu):
        _translate = QtCore.QCoreApplication.translate
        TrainingMenu.setWindowTitle(_translate("TrainingMenu", "MainWindow"))
        self.training_label.setText(_translate("TrainingMenu", "Train Network"))
        self.epochs_label.setText(_translate("TrainingMenu", "Epochs"))
        self.verbiose_label.setText(_translate("TrainingMenu", "Verbiose Mode"))
        self.lrate_label.setText(_translate("TrainingMenu", "Initial Learning Rate"))
        self.batch_size_label.setText(_translate("TrainingMenu", "Batch Size"))
        self.verbiose_box.setItemText(0, _translate("TrainingMenu", "Silent"))
        self.verbiose_box.setItemText(1, _translate("TrainingMenu", "Progress Bar"))
        self.verbiose_box.setItemText(2, _translate("TrainingMenu", "One Line Per Epoch"))
        self.layers_tab.setTabText(self.layers_tab.indexOf(self.general_tab), _translate("TrainingMenu", "General"))
        self.enable_stop_label.setText(_translate("TrainingMenu", "Enable Stopping"))
        self.monitor_var_label.setText(_translate("TrainingMenu", "Monitored Variable"))
        self.monitor_var_box.setItemText(0, _translate("TrainingMenu", "Validation Loss"))
        self.monitor_var_box.setItemText(1, _translate("TrainingMenu", "Validation Accuracy"))
        self.till_stop_label.setText(_translate("TrainingMenu", "Epochs Till Stop"))
        self.trigger_label.setText(_translate("TrainingMenu", "Stop Trigger"))
        self.trigger_box.setItemText(0, _translate("TrainingMenu", "Increase (Does not Decrease)"))
        self.trigger_box.setItemText(1, _translate("TrainingMenu", "Plateau (Does not Increase)"))
        self.restore_weight_label.setText(_translate("TrainingMenu", "Restore Weights"))
        self.layers_tab.setTabText(self.layers_tab.indexOf(self.early_stop_tab), _translate("TrainingMenu", "Early Stopping"))
        self.type_label.setText(_translate("TrainingMenu", "Decay Type"))
        self.rate_label.setText(_translate("TrainingMenu", "Decay Rate"))
        self.decay_start_label.setText(_translate("TrainingMenu", "Decay Start (Epochs)"))
        self.decay_type_box.setItemText(0, _translate("TrainingMenu", "Linear Decay"))
        self.decay_type_box.setItemText(1, _translate("TrainingMenu", "Exponential Decay"))
        self.layers_tab.setTabText(self.layers_tab.indexOf(self.lrate_scheduler_tab), _translate("TrainingMenu", "Learning Rate Scheduler"))
        self.data_settings_group.setTitle(_translate("TrainingMenu", "Data Settings"))
        self.train_data_path_label.setText(_translate("TrainingMenu", "Training Data Path"))
        self.train_path_button.setText(_translate("TrainingMenu", "Select Folder"))
        self.valid_data_path_label.setText(_translate("TrainingMenu", "Validation Data Path"))
        self.valid_path_button.setText(_translate("TrainingMenu", "Select Folder"))
        self.datasets_label.setText(_translate("TrainingMenu", "Total Datasets"))
        self.data_source_label.setText(_translate("TrainingMenu", "Validation Data Source"))
        self.valid_split_label.setText(_translate("TrainingMenu", "Validation Split"))
        self.zero_label.setText(_translate("TrainingMenu", "0%"))
        self.fifty_label.setText(_translate("TrainingMenu", "50%"))
        self.hund_label.setText(_translate("TrainingMenu", "100%"))
        self.train_button.setText(_translate("TrainingMenu", "Train"))
        self.console_box.setTitle(_translate("TrainingMenu", "Console"))
        self.time_elapsed_label.setText(_translate("TrainingMenu", "Time Elapsed : 00:00:00"))
        self.enable_scheduler_label.setText(_translate("TrainingMenu", "Enable Scheduler"))

    def init_ui(self, TrainingMenu):
        TrainingMenu.setObjectName("TrainingMenu")
        TrainingMenu.resize(509, 908)
        self.centralwidget = QtWidgets.QWidget(parent=TrainingMenu)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 861))
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
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        self.training_label.setFont(font)
        self.training_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.training_label.setObjectName("training_label")
        self.training_layout.addWidget(self.training_label)
        self.training_frame = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.training_frame.sizePolicy().hasHeightForWidth())
        self.training_frame.setSizePolicy(sizePolicy)
        self.training_frame.setAutoFillBackground(True)
        self.training_frame.setStyleSheet("fields_frame:Qframe {\n"
                                          "background: rgb(249, 249, 249)\n"
                                          "}")
        self.training_frame.setObjectName("training_frame")
        self.layers_tab = QtWidgets.QTabWidget(parent=self.training_frame)
        self.layers_tab.setGeometry(QtCore.QRect(10, 280, 441, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
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
                                      "/* Style for the selected tab */\n"
                                      "QTabBar::tab:selected {\n"
                                      "    background: #a0a0a0; /* Darker background for the selected tab */\n"
                                      "    border-color: #444; /* Darker border color for the selected tab */\n"
                                      "}\n"
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
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 421, 151))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.general_form = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.general_form.setContentsMargins(10, 10, 10, 10)
        self.general_form.setHorizontalSpacing(4)
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
        self.lrate_box = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_3)
        self.lrate_box.setObjectName("lrate_box")
        self.general_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lrate_box)
        self.lrate_label = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.lrate_label.setFont(font)
        self.lrate_label.setObjectName("lrate_label")
        self.general_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lrate_label)
        self.batch_size_label = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.batch_size_label.setFont(font)
        self.batch_size_label.setObjectName("batch_size_label")
        self.general_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.batch_size_label)
        self.verbiose_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        self.verbiose_box.setObjectName("verbiose_box")
        self.verbiose_box.addItem("")
        self.verbiose_box.addItem("")
        self.verbiose_box.addItem("")
        self.general_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.verbiose_box)
        self.layers_tab.addTab(self.general_tab, "")
        self.early_stop_tab = QtWidgets.QWidget()
        self.early_stop_tab.setObjectName("early_stop_tab")
        self.formLayoutWidget_4 = QtWidgets.QWidget(parent=self.early_stop_tab)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 411, 181))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.early_stop_form = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.early_stop_form.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.early_stop_form.setContentsMargins(10, 10, 10, 10)
        self.early_stop_form.setVerticalSpacing(15)
        self.early_stop_form.setObjectName("early_stop_form")
        self.enable_stop_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.enable_stop_label.setFont(font)
        self.enable_stop_label.setObjectName("enable_stop_label")
        self.early_stop_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.enable_stop_label)
        self.enable_stop_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_4)
        self.enable_stop_box.setText("")
        self.enable_stop_box.setObjectName("enable_stop_box")
        self.early_stop_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.enable_stop_box)
        self.monitor_var_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.monitor_var_label.setFont(font)
        self.monitor_var_label.setObjectName("monitor_var_label")
        self.early_stop_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.monitor_var_label)
        self.monitor_var_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.monitor_var_box.setObjectName("monitor_var_box")
        self.monitor_var_box.addItem("")
        self.monitor_var_box.addItem("")
        self.monitor_var_box.addItem("")
        self.monitor_var_box.setItemText(2, "")
        self.early_stop_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.monitor_var_box)
        self.till_stop_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.till_stop_label.setFont(font)
        self.till_stop_label.setObjectName("till_stop_label")
        self.early_stop_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.till_stop_label)
        self.tilll_stop_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_4)
        self.tilll_stop_box.setObjectName("tilll_stop_box")
        self.early_stop_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tilll_stop_box)
        self.trigger_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.trigger_label.setFont(font)
        self.trigger_label.setObjectName("trigger_label")
        self.early_stop_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.trigger_label)
        self.trigger_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.trigger_box.setObjectName("trigger_box")
        self.trigger_box.addItem("")
        self.trigger_box.addItem("")
        self.early_stop_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.trigger_box)
        self.restore_weights_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_4)
        self.restore_weights_box.setText("")
        self.restore_weights_box.setObjectName("restore_weights_box")
        self.early_stop_form.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.restore_weights_box)
        self.restore_weight_label = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.restore_weight_label.setFont(font)
        self.restore_weight_label.setObjectName("restore_weight_label")
        self.early_stop_form.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.restore_weight_label)
        self.layers_tab.addTab(self.early_stop_tab, "")
        self.lrate_scheduler_tab = QtWidgets.QWidget()
        self.lrate_scheduler_tab.setObjectName("lrate_scheduler_tab")
        self.formLayoutWidget_5 = QtWidgets.QWidget(parent=self.lrate_scheduler_tab)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 421, 151))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.lrate_scheduler_form = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.lrate_scheduler_form.setContentsMargins(10, 10, 10, 10)
        self.lrate_scheduler_form.setVerticalSpacing(15)
        self.lrate_scheduler_form.setObjectName("lrate_scheduler_form")
        self.type_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.type_label.setFont(font)
        self.type_label.setObjectName("type_label")
        self.lrate_scheduler_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.type_label)
        self.rate_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.rate_label.setFont(font)
        self.rate_label.setObjectName("rate_label")
        self.lrate_scheduler_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.rate_label)
        self.rate_box = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget_5)
        self.rate_box.setMaximum(1.0)
        self.rate_box.setSingleStep(0.1)
        self.rate_box.setProperty("value", 0.9)
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
        self.decay_start_box.setMinimum(0)
        self.decay_start_box.setMaximum(1000)
        self.decay_start_box.setProperty("value", 5)
        self.decay_start_box.setObjectName("decay_start_box")
        self.lrate_scheduler_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.decay_start_box)


        self.enable_scheduler_label = QtWidgets.QLabel(parent=self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.enable_scheduler_label.setFont(font)
        self.enable_scheduler_label.setObjectName("enable_scheduler_label")
        self.lrate_scheduler_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.enable_scheduler_label)
        self.enable_scheduler_box = QtWidgets.QCheckBox(parent=self.formLayoutWidget_5)
        self.enable_scheduler_box.setText("")
        self.enable_scheduler_box.setObjectName("enable_scheduler_box")
        self.lrate_scheduler_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.enable_scheduler_box)



        self.layers_tab.addTab(self.lrate_scheduler_tab, "")
        self.data_settings_group = QtWidgets.QGroupBox(parent=self.training_frame)
        self.data_settings_group.setGeometry(QtCore.QRect(10, 20, 441, 241))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.data_settings_group.setFont(font)
        self.data_settings_group.setObjectName("data_settings_group")
        self.formLayoutWidget_12 = QtWidgets.QWidget(parent=self.data_settings_group)
        self.formLayoutWidget_12.setGeometry(QtCore.QRect(0, 20, 441, 350))
        self.formLayoutWidget_12.setObjectName("formLayoutWidget_12")
        self.data_settings_form = QtWidgets.QFormLayout(self.formLayoutWidget_12)
        self.data_settings_form.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.data_settings_form.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.data_settings_form.setContentsMargins(20, 20, 20, 20)
        self.data_settings_form.setVerticalSpacing(15)
        self.data_settings_form.setObjectName("data_settings_form")
        self.train_data_path_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.train_data_path_label.setFont(font)
        self.train_data_path_label.setObjectName("train_data_path_label")
        self.data_settings_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.train_data_path_label)
        self.train_path_hbox = QtWidgets.QHBoxLayout()
        self.train_path_hbox.setObjectName("train_path_hbox")
        self.train_path_entry = QtWidgets.QLineEdit(parent=self.formLayoutWidget_12)
        self.train_path_entry.setObjectName("train_path_entry")
        self.train_path_hbox.addWidget(self.train_path_entry)
        self.train_path_button = QtWidgets.QPushButton(parent=self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.train_path_button.setFont(font)
        self.train_path_button.setObjectName("train_path_button")
        self.train_path_hbox.addWidget(self.train_path_button)
        self.data_settings_form.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.train_path_hbox)
        self.valid_data_path_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.valid_data_path_label.setFont(font)
        self.valid_data_path_label.setObjectName("valid_data_path_label")
        self.data_settings_form.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.valid_data_path_label)
        self.valid_path_hbox = QtWidgets.QHBoxLayout()
        self.valid_path_hbox.setObjectName("valid_path_hbox")
        self.valid_path_entry = QtWidgets.QLineEdit(parent=self.formLayoutWidget_12)
        self.valid_path_entry.setObjectName("valid_path_entry")
        self.valid_path_hbox.addWidget(self.valid_path_entry)
        self.valid_path_button = QtWidgets.QPushButton(parent=self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.valid_path_button.setFont(font)
        self.valid_path_button.setObjectName("valid_path_button")
        self.valid_path_hbox.addWidget(self.valid_path_button)
        self.data_settings_form.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.valid_path_hbox)
        self.datasets_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.datasets_label.setFont(font)
        self.datasets_label.setObjectName("datasets_label")
        self.data_settings_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.datasets_label)
        self.datasets_box = QtWidgets.QSpinBox(parent=self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.datasets_box.setFont(font)
        self.datasets_box.setObjectName("datasets_box")
        self.data_settings_form.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.datasets_box)
        self.data_source_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.data_source_label.setFont(font)
        self.data_source_label.setObjectName("data_source_label")
        self.data_settings_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.data_source_label)
        self.data_source_box = QtWidgets.QComboBox(parent=self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.data_source_box.setFont(font)





        self.data_settings_form.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.data_source_box)
        self.valid_split_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.valid_split_label.setFont(font)
        self.valid_split_label.setObjectName("valid_split_label")
        self.data_settings_form.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.valid_split_label)
        self.valid_split_slider = QtWidgets.QSlider(parent=self.formLayoutWidget_12)
        self.valid_split_slider.setMaximumSize(QtCore.QSize(400, 16777215))
        self.valid_split_slider.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
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
        self.data_settings_form.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.valid_split_slider)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.zero_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
        self.zero_label.setObjectName("zero_label")
        self.horizontalLayout.addWidget(self.zero_label)
        self.fifty_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
        self.fifty_label.setObjectName("fifty_label")
        self.horizontalLayout.addWidget(self.fifty_label)
        self.hund_label = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
        self.hund_label.setObjectName("hund_label")
        self.horizontalLayout.addWidget(self.hund_label)
        self.data_settings_form.setLayout(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout)
        self.spacer = QtWidgets.QLabel(parent=self.formLayoutWidget_12)
        self.spacer.setText("")
        self.spacer.setObjectName("spacer")
        self.data_settings_form.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.spacer)
        self.train_button = QtWidgets.QPushButton(parent=self.training_frame)
        self.train_button.setEnabled(True)
        self.train_button.setGeometry(QtCore.QRect(40, 780, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.train_button.setFont(font)
        self.train_button.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid #8f8f8f;\n"
                                        "    border-radius: 2px;\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                        "    padding: 5px;\n"
                                        "    font-size: 14px;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    border: 2px solid #3daee9;\n"
                                        "}\n"
                                        "")
        self.train_button.setObjectName("train_button")
        self.console_box = QtWidgets.QGroupBox(parent=self.training_frame)
        self.console_box.setGeometry(QtCore.QRect(10, 530, 441, 171))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.console_box.setFont(font)
        self.console_box.setObjectName("console_box")
        self.console_output = QtWidgets.QTextBrowser(parent=self.console_box)
        self.console_output.setGeometry(QtCore.QRect(10, 20, 421, 141))
        self.console_output.setObjectName("console_output")
        self.training_progress_bar = QtWidgets.QProgressBar(parent=self.training_frame)
        self.training_progress_bar.setGeometry(QtCore.QRect(30, 720, 411, 20))
        self.training_progress_bar.setProperty("value", 24)
        self.training_progress_bar.setObjectName("training_progress_bar")
        self.time_elapsed_label = QtWidgets.QLabel(parent=self.training_frame)
        self.time_elapsed_label.setGeometry(QtCore.QRect(190, 750, 221, 16))
        self.time_elapsed_label.setObjectName("time_elapsed_label")
        self.training_layout.addWidget(self.training_frame)
        TrainingMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=TrainingMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 22))
        self.menubar.setObjectName("menubar")
        TrainingMenu.setMenuBar(self.menubar)
        self.training_status = QtWidgets.QStatusBar(parent=TrainingMenu)
        self.training_status.setObjectName("training_status")
        TrainingMenu.setStatusBar(self.training_status)

        self.retranslateUi(TrainingMenu)
        QtCore.QMetaObject.connectSlotsByName(TrainingMenu)

    def handle_train_btn(self):
        pass

    def set_training_source(self):

        sourceIndex = self.data_source_box.currentIndex()
        if sourceIndex == 0:

            self.hideWidgets(self.valid_path_entry, self.valid_data_path_label,self.valid_path_button,self.train_path_button)

            self.showWidgets(self.valid_split_slider, self.valid_split_label,self.train_path_button,
                             self.zero_label, self.fifty_label, self.hund_label)

        if sourceIndex == 1:

            self.showWidgets(self.valid_path_entry, self.valid_data_path_label,self.valid_path_button,self.train_path_button)


            self.hideWidgets(self.valid_split_slider, self.valid_split_label,self.zero_label,
                             self.fifty_label, self.hund_label)

    def init_values(self):

        # hide split options when in select validation data option, opposite for split validation data option

        sources = ["Split Validation Data","Select Valdiation Data"]
        self.data_source_box.addItems(sources)
        self.data_source_box.setCurrentIndex(0)

        self.datasets_box.setValue(500)
        self.valid_split_slider.setValue(0.1)


        # set to open on general tab
        self.layers_tab.setCurrentIndex(0)


        self.epochs_box.setValue(10)
        self.lrate_box.setValue(0.001)
        self.verbiose_box.setCurrentIndex(1)
        self.batch_size_box.setValue(32)

        self.enable_stop_box.setChecked(False)
        self.monitor_var_box.setCurrentIndex(0)
        self.trigger_box.setCurrentIndex(0)
        self.restore_weights_box.setDisabled(True)
        self.tilll_stop_box.setValue(5)


        self.enable_stop_box.setChecked(False)
        self.decay_type_box.setCurrentIndex(0)
        self.rate_box.setValue(0.9)
        self.decay_start_box.setValue(5)





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
                "verbose_mode": self.verbiose_box.currentText(),
                "initial_learning_rate": self.lrate_box.value(),
                "batch_size": self.batch_size_box.value(),
            },
            "early_stopping": {
                "enable_stopping": self.enable_stop_box.isChecked(),
                "monitored_variable": self.monitor_var_box.currentText(),
                "epochs_till_stop": self.tilll_stop_box.value(),
                "stop_trigger": self.trigger_box.currentText(),
                "restore_weights": self.restore_weights_box.isChecked(),
            },
            "learning_rate_scheduler": {
                "type": self.decay_type_box.currentText(),
                "params": {
                    "decay_rate": self.rate_box.value(),
                    "decay_steps": self.decay_start_box.value(),
                    # Add other parameters as needed
                } if self.scheduler_enabled_box.isChecked() else {}
            }
        }

        return data

    def restrictions(self):

        pass

    def set_bindings(self):
        self.data_source_box.currentIndexChanged.connect(self.set_training_source)

        self.train_path_button.clicked.connect(self.open_training_folder_selector)

        self.valid_path_button.clicked.connect(self.open_validation_folder_selector)

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





