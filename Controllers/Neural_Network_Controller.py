
from PyQt6.QtWidgets import QMessageBox, QSlider
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QRegularExpression, pyqtSignal
from PyQt6.QtGui import QIntValidator, QRegularExpressionValidator, QIcon
from PyQt6.QtWidgets import QMainWindow, QSlider, QWidget


class Neural_Network_Controller:
    network_created = pyqtSignal()
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.window = QMainWindow()
        self.view.setupUi(self.window)

        self.set_default_settings()
        self.connect_signals()










    def set_default_settings(self):

        regex = QRegularExpression("[a-zA-Z0-9 ]+")
        self.view.name_entry.setValidator(QRegularExpressionValidator(regex))
        self.view.name_entry.setEnabled(True)

        # Optionally, set the range if needed
        self.view.time_entry.setMinimum(1)  # Set the minimum value
        self.view.time_entry.setMaximum(1000)  # Set the maximum value

        self.view.type_entry_1.addItems(["Conv"])
        self.view.kernel_entry_1.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.view.layers_entry.addItems(["1 layer", "2 layers", "3 layers"])  # Correct grammar
        self.view.filters_entry_1.setMinimum(1)  # Set the minimum value
        self.view.filters_entry_1.setMaximum(1000)  # Set the maximum value
        self.view.pool_entry_1.addItems(["None","1", "2", "3"])
        self.view.activation_entry_1.addItems(["Tanh", "Relu"])

        self.view.drop_slider_1.setTickInterval(10)
        self.view.drop_slider_1.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.view.l1_slider_1.setTickInterval(10)
        self.view.l1_slider_1.setTickPosition(QSlider.TickPosition.TicksBelow)  # Correct method and enum
        self.view.l2_slider_1.setTickInterval(10)
        self.view.l2_slider_1.setTickPosition(QSlider.TickPosition.TicksBelow)  # Correct method and enum



        self.view.type_entry_2.addItems(["Conv", "Dense"])
        self.view.kernel_entry_2.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.view.filters_entry_2.setMinimum(1)  # Set the minimum value
        self.view.filters_entry_2.setMaximum(1000)  # Set the maximum value
        self.view.pool_entry_2.addItems(["None","1", "2", "3"])
        self.view.activation_entry_2.addItems(["Tanh", "Relu"])
        self.view.drop_slider_2.setTickInterval(10)  # Sets the interval between ticks
        self.view.drop_slider_2.setTickPosition(
            QSlider.TickPosition.TicksBelow)  # Correct method call with enum for tick position

        self.view.l1_slider_2.setTickInterval(10)
        self.view.l1_slider_2.setTickPosition(QSlider.TickPosition.TicksBelow)  # Correct method and enum
        self.view.l2_slider_2.setTickInterval(10)
        self.view.l2_slider_2.setTickPosition(QSlider.TickPosition.TicksBelow)  # Correct method and enum


        self.view.type_entry_3.addItems(["Conv", "Dense"])
        self.view.kernel_entry_3.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.view.filters_entry_3.setMinimum(1)  # Set minimum value
        self.view.filters_entry_3.setMaximum(1000)  # Set maximum value
        self.view.pool_entry_3.addItems(["None","1", "2", "3"])
        self.view.activation_entry_3.addItems(["Tanh", "Relu"])
        self.view.drop_slider_3.setTickInterval(10)  # Set interval between ticks
        self.view.drop_slider_3.setTickPosition(QSlider.TickPosition.TicksBelow)


        self.view.compiler_entry.addItems(["Adam", "RMSprop", "SGD"])
        self.view.compiler_entry.setCurrentIndex(0)  # Set default optimizer for compile_box


        self.view.task_entry.addItems(["Classification", "Regression"])

        # set default layer types


        self.view.type_entry_1.setCurrentIndex(0)
        self.view.type_entry_2.setCurrentIndex(0)
        self.view.type_entry_3.setCurrentIndex(1)





        # Update the layer types to default types
        self.on_type_change(1)
        self.on_type_change(2)
        self.on_type_change(3)

        self.view.name_entry.setText("Untitled Network")
        self.view.time_entry.setValue(100)  # Set the default value to 64
        self.view.layers_entry.setCurrentIndex(2)  # 3rd option, zero-based index
        self.view.categories_entry.setValue(7)

        self.view.kernel_entry_1.setCurrentIndex(2)  # Corrected to affect kernel_entry1
        self.view.filters_entry_1.setValue(32)  # Set the default value to 64
        self.view.pool_entry_1.setCurrentIndex(0)
        self.view.activation_entry_1.setCurrentIndex(0)
        self.view.drop_slider_1.setValue(20)
        self.view.l1_slider_1.setValue(0)
        self.view.l2_slider_1.setValue(0)
        self.view.batch_entry_1.setChecked(False)  # Assuming self.batch_entry1 is a QCheckBox or similar'
        self.view.dense_entry_1.setValue(100)
        self.view.flat_box_2.setChecked(False)  # Assuming self.

        self.view.kernel_entry_2.setCurrentIndex(2)  # Now correctly referring to kernel_entry2
        self.view.filters_entry_2.setValue(64)  # Set the default value to 64
        self.view.pool_entry_2.setCurrentIndex(2)  # Sets the default pooling size for pool_entry2
        self.view.activation_entry_2.setCurrentIndex(0)  # Sets the default activation function for activation_entry2
        self.view.drop_slider_2.setValue(0)  # Sets the initial value for dropout
        self.view.batch_entry_2.setChecked(False)  # Assuming self.batch_entry1 is a QCheckBox or similar
        self.view.flat_box_2.setChecked(True) # Assuming self.
        self.view.dense_entry_2.setValue(100)
        self.view.l1_slider_2.setValue(0)
        self.view.l2_slider_2.setValue(0)

        self.view.kernel_entry_3.setCurrentIndex(2)  # Set default kernel size for kernel_entry3
        self.view.filters_entry_3.setValue(64)  # Set default value to 64
        self.view.pool_entry_3.setCurrentIndex(0)  # Set default pooling size for pool_entry3
        self.view.activation_entry_3.setCurrentIndex(0)  # Set default activation function for activation_entry3
        self.view.drop_slider_3.setValue(0)  # Set initial value for dropout
        self.view.batch_entry_3.setChecked(False)  # Assuming self.batch_entry1 is a QCheckBox or similar
        self.view.dense_entry_3.setValue(100)
        self.view.l1_slider_3.setValue(0)
        self.view.l2_slider_3.setValue(0)

    def pass_menu_controller(self, controller):
        self.menu_controller = controller

    def connect_signals(self):
        self.view.task_entry.currentIndexChanged.connect(self.update_task_type_visibility)
        self.view.type_entry_1.currentIndexChanged.connect(lambda: self.on_type_change(1))
        self.view.type_entry_2.currentIndexChanged.connect(lambda: self.on_type_change(2))
        self.view.type_entry_3.currentIndexChanged.connect(lambda: self.on_type_change(3))

        self.view.layers_entry.currentIndexChanged.connect(self.on_layer_box_change)
        self.view.main_button.clicked.connect(self.handle_create_btn)

    def handle_create_btn(self):
        data = self.collect_ui_data()
        if self.validate_name(data):
            print("set network data")
            self.model.set_data(data)
            print("creating network")
            self.model.handle_create_btn()

            self.model.save_metadata(data)
            if hasattr(self, "menu_controller"):
                self.menu_controller.update_network_list()


            self.window.close()

    def collect_ui_data(self):
        data = {
            "general": {
                "name": self.view.name_entry.text(),
                "time_steps": self.view.time_entry.value(),
                "layers": self.view.layers_entry.currentText(),
                "categories": self.view.categories_entry.value(),
                "task_type": self.view.task_entry.currentText(),
            },
            "compile": {
                "compiler": self.view.compiler_entry.currentText(),
            },
            "layers": []
        }

        for i in range(self.view.layers_tab.count()):
            tab = self.view.layers_tab.widget(i)

            layer = {
                "type": tab.findChild(QtWidgets.QComboBox, f"type_entry_{i + 1}").currentText(),
                "kernel": tab.findChild(QtWidgets.QComboBox, f"kernel_entry_{i + 1}").currentText(),
                "filters": tab.findChild(QtWidgets.QSpinBox, f"filters_entry_{i + 1}").value(),
                "dense_units": tab.findChild(QtWidgets.QSpinBox, f"dense_entry_{i + 1}").value(),
                "pooling": tab.findChild(QtWidgets.QComboBox, f"pool_entry_{i + 1}").currentText(),
                "activation": tab.findChild(QtWidgets.QComboBox, f"activation_entry_{i + 1}").currentText(),
                "dropout_rate": tab.findChild(QtWidgets.QSlider, f"drop_slider_{i + 1}").value() / 100.0,
                "batch_normalization": tab.findChild(QtWidgets.QCheckBox, f"batch_entry_{i + 1}").isChecked(),
                "flatten": tab.findChild(QtWidgets.QCheckBox, f"flat_box_{i + 1}").isChecked(),
                "l1_reg": tab.findChild(QtWidgets.QSlider, f"l1_slider_{i + 1}").value() / 100.0,
                "l2_reg": tab.findChild(QtWidgets.QSlider, f"l2_slider_{i + 1}").value() / 100.0,
            }

            data["layers"].append(layer)

        return data

    def update_value_label(self, label_widget, value):
        label_widget.setText(str(value))



    def validate_name(self, data):

        if self.null_check(data['general']['name']):
            return False
        else:
            return True

    def nullError(self, input):
        QMessageBox.critical(self, "Error", input + " is empty or null")

    def null_check(self, s) -> str:
        return s == "" or s.isspace()

    def typeToIndex(self, type_str):
        # Define a dictionary mapping type strings to their corresponding indexes
        type_to_index = {"Conv": 0, "Dense": 1}

        # Use the dictionary to return the corresponding index
        # If type_str is not found, return a default value, e.g., -1 or None
        return type_to_index.get(type_str, -1)

    def on_type_change(self, layer):

        print("layer type changed")

        if layer == 1:
            self.model.layer_types['layer1Type'] = self.view.type_entry_1.currentText()
            print(self.view.type_entry_1.currentText())
            self.update_layer_type(layer, self.model.layer_types['layer1Type'])

        if layer == 2:
            self.model.layer_types['layer2Type'] = self.view.type_entry_2.currentText()
            self.update_layer_type(layer, self.model.layer_types['layer2Type'])

        if layer == 3:
            self.model.layer_types['layer3Type'] = self.view.type_entry_3.currentText()
            self.update_layer_type(layer, self.model.layer_types['layer3Type'])

    def update_layer_type(self, layer, type):

        print("updating layer type")

        print(layer)
        print(type)

        cnn_settings = ['kernel_entry_', 'kernel_label_', 'filters_label_', 'pool_label_', 'pool_entry_',
                        'filters_entry_', 'flat_box_', 'flat_label_']
        dense_settings = ['dense_entry_', 'dense_label_']
        try:
            if type == "Dense":
                for widget in cnn_settings:
                    att_name = widget + str(layer)
                    print(f"updating {widget}")
                    getattr(self.view, att_name).hide()
                    getattr(self.view, att_name).setEnabled(False)

                for widget in dense_settings:
                    att_name = widget + str(layer)
                    print(f"updating {widget}")
                    getattr(self.view, att_name).show()
                    getattr(self.view, att_name).setEnabled(True)

            if type == "Conv":
                for widget in cnn_settings:
                    att_name = widget + str(layer)
                    getattr(self.view, att_name).show()
                    getattr(self.view, att_name).setEnabled(True)

                for widget in dense_settings:
                    att_name = widget + str(layer)
                    print(f"updating {widget}")
                    getattr(self.view, att_name).hide()
                    getattr(self.view, att_name).setEnabled(False)


        except Exception as e:
            print(e)

    def on_layer_box_change(self, event=None):
        print("layer box changed")
        layers = int(self.view.layers_entry.currentIndex()) + 1

        print("layers amount selected: %d" % layers)

        if layers != self.model.number_of_layers:
            print("layers are to be changed to %d" % layers)
            self.model.number_of_layers = layers
            self.update_layers()

    def update_layers(self):

        print("Updating Layers")

        # Clear all existing tabs
        while self.view.layers_tab.count() > 0:
            self.view.layers_tab.removeTab(0)

        print("deleted layers")

        try:

            if self.model.number_of_layers == 1:
                self.view.layers_tab.addTab(self.view.tabReference1, "Layer 1")

            if self.model.number_of_layers == 2:
                self.view.layers_tab.addTab(self.view.tabReference1, "Layer 1")
                self.view.layers_tab.addTab(self.view.tabReference2, "Layer 2")

            if self.model.number_of_layers == 3:
                self.view.layers.addTab(self.view.tabReference1, "Layer 1")
                self.view.layers_tab.addTab(self.view.tabReference2, "Layer 2")
                self.view.layers_tab.addTab(self.view.tabReference3, "Layer 3")

            # Your existing logic to clear and add tabs...
        except Exception as e:
            print(f"Error updating layers: {e}")


    def update_task_type_visibility(self):
        task_type = self.view.task_entry.currentText().lower()
        if task_type == "classification":
            self.view.categories_entry.setVisible(True)
            self.view.categories_label.setVisible(True)

        if task_type == "regression":
            self.view.categories_entry.setVisible(False)
            self.view.categories_label.setVisible(False)

