import os
from datetime import datetime
class Test_Log():

    def __init__(self,model_name,nn_sucsess,control_sucsess,mse,mse_zero,lstm_units,learning_rate,data_length,category_depth):
        self.model_name = model_name
        self.nn_sucsess = nn_sucsess
        self.control_sucsess = control_sucsess
        self.mse = mse
        self.mse_zero = mse_zero


    def add_log(self):
        with (open("Log Files\\Testing_Menu Log\\" + self.model_name + ".txt", 'a') as file):
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            entry = f"model name: {self.model_name} \n" + "nn_sucsess: " + str(self.nn_sucsess) + "\n" + "control_sucsess: " + str(self.control_sucsess) + "\n" + "mse: " + str(self.mse) + "\n" + "mse_zero: " + str(self.mse_zero) + "\n" + f"time : {formatted_datetime}\n"
            file.write(entry + '\n\n\n\n')
