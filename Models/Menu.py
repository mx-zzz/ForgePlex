from Utility.Network_Handler import Network_Handler
import os

class Menu:
    def __init__(self):
        self.nn = Network_Handler()
        self.network_list = []
        self.generate_networks()
        print("init model")






    def generate_networks(self):
        self.network_list = os.listdir("Saved Models")

    def get_networks(self):
        return self.network_list
