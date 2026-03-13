
import json
import os
class Dataset_Menu:
    def __init__(self, selected_network: str):
        self.selected_network = selected_network


    def get_task_type(self):
        try:
            with open("Saved Models//" + self.selected_network + "//metadata.json", "r") as file:
                data = json.load(file)
                return data['general']['task_type']

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading model info: {e}")
            return None
