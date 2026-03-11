# Controller
from PyQt6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem, QDialog

from Controllers.Dataset_Controller import Dataset_Controller
from Controllers.Testing_Controller import Testing_Controller
from Controllers.Training_Controller import Training_Controller
from Models.Neural_Network_Menu import Neural_Network_Menu
from Models.Testing_Menu import Testing_Menu
from Models.Training_Menu import Training_Menu
from Models.Dataset_Menu import Dataset_Menu
from Views.Neural_Network_View import Neural_Network_View
from Views.Testing_View import Testing_View
from Views.Dataset_View import Dataset_View

from Views.Training_View import Training_View




from Controllers.Neural_Network_Controller import Neural_Network_Controller
class Menu_Controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view

        self.secondary_window = None


        self.last_window = None


    def open_secondary_window(self, secondary_window):


        if self.last_window is None or not self.last_window.isVisible():
            self.secondary_window = secondary_window
            self.secondary_window.show()
            self.last_window = self.secondary_window



    def open_network_menu(self):


        self.network_model = Neural_Network_Menu()
        self.network_view = Neural_Network_View()
        self.network_controller = Neural_Network_Controller(self.network_model,self.network_view)
        self.network_view.set_controller(self.network_controller)
        self.network_controller.pass_menu_controller(self)

        self.open_secondary_window(self.network_view)



    def run_training_wizard(self, selected_network):
        dataset_view = Dataset_View()
        dataset_model = Dataset_Menu(selected_network)
        dataset_dialog = Dataset_Controller(dataset_model, dataset_view)

        dataset_result = dataset_dialog.exec()

        if dataset_result != QDialog.DialogCode.Accepted:
            print("Dataset step cancelled.")
            return

        self.dataset_config = dataset_dialog.get_config_dict()
        print("DATASET CONFIG:")
        print(self.dataset_config)
        print("open dataset menu_controller")

        print("open training menu_controller")

        training_model = Training_Menu(selected_network)
        training_view = Training_View()
        training_controller = Training_Controller(training_model, training_view)
        training_view.set_controller(training_controller)

        # inject dataset config into training controller
        training_controller.set_dataset_config(self.dataset_config)

        self.open_secondary_window(training_view)







    def open_testing_menu(self,selected_network):
        print("open testing menu_controller")
        self.testing_model = Testing_Menu(selected_network)
        self.testing_view = Testing_View()
        self.testing_controller = Testing_Controller(self.testing_model, self.testing_view)
        self.testing_view.set_controller(self.testing_controller)

        self.open_secondary_window(self.testing_view)



    def update_network_list(self):
        self.view.list_widget.clear()
        self.model.generate_networks()
        for network in self.model.network_list:
            item = QListWidgetItem(network)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.list_widget.addItem(item)









