import os
import json

from datetime import datetime
class Training_Log():

    def __init__(self,model_name,epochs):
        self.model_name = model_name
        self.epochs = epochs


    def add_log(self):
        log_path = "Log Files\\Training Log\\" + self.model_name + ".txt"
        with (open(log_path, 'a') as file):
            if not os.path.exists(log_path) or os.path.getsize(log_path) == 0 :
                self.create_new_log_file(log_path)

            self.update_log_file(log_path)


    def create_new_log_file(self,log_path):
        log_format = {'model_name': f'{self.model_name}', 'epochs': f'{self.epochs}'}
        with (open(log_path, 'w') as file):
            json.dump(log_format, file, indent=4)

    def update_log_file(self, log_path):
        try:
            with open(log_path, 'r') as file:
                data = json.load(file)

            # Correctly assign new values to 'epochs' and 'model_name'
            data['epochs'] = str(int(self.epochs) + int(data['epochs']))
            data['model_name'] = self.model_name

            with open(log_path, 'w') as file:
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            print("File not found.")


