# Controller
from PyQt6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem

from Controllers.Testing_Controller import Testing_Controller
from Controllers.Training_Controller import Training_Controller
from Models.Neural_Network_Menu import Neural_Network_Menu
from Models.Testing_Menu import Testing_Menu
from Models.Training_Menu import Training_Menu
from Views.Neural_Network_View import Neural_Network_View
from Views.Testing_View import Testing_View

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


    def open_training_menu(self, selected_network):
        print("open training menu_controller")
        self.training_model = Training_Menu(selected_network)
        self.training_view = Training_View()
        self.training_controller = Training_Controller(self.training_model,self.training_view)
        self.training_view.set_controller(self.training_controller)

        self.open_secondary_window(self.training_view)




    def open_testing_menu(self):
        print("open testing menu_controller")
        self.testing_model = Testing_Menu(self.view.get_selected_network())
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









