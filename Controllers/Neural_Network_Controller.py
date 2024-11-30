from PyQt6.QtWidgets import QMessageBox


class Neural_Network_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def pass_menu_controller(self, menu_controller):
        self.menu_controller = menu_controller

    def create_network(self, data):
        print("set network data")
        self.model.set_data(data)
        print("creating network")
        self.model.handle_create_btn()
        self.menu_controller.update_network_list()
        self.view.close()

        # Update other model fields as required
        # After updating the model, you can perform the network creation logic

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
        while self.view.general_tab.count() > 0:
            self.view.general_tab.removeTab(0)

        print("deleted layers")

        try:

            if self.model.number_of_layers == 1:
                self.view.general_tab.addTab(self.view.tabReference1, "Layer 1")

            if self.model.number_of_layers == 2:
                self.view.general_tab.addTab(self.view.tabReference1, "Layer 1")
                self.view.general_tab.addTab(self.view.tabReference2, "Layer 2")

            if self.model.number_of_layers == 3:
                self.view.general_tab.addTab(self.view.tabReference1, "Layer 1")
                self.view.general_tab.addTab(self.view.tabReference2, "Layer 2")
                self.view.general_tab.addTab(self.view.tabReference3, "Layer 3")

            # Your existing logic to clear and add tabs...
        except Exception as e:
            print(f"Error updating layers: {e}")
