import os
import time

from Utility import Tf_Network
from keras.models import load_model
from Utility.Data_Handler import Data_Handler
from Utility.Tf_Network import Tf_Network
from Utility.Test_Log import Test_Log
from Utility.Training_Log import Training_Log


class Network_Handler:


    def __init__(self):
        self.data_length = 100
        self.category_depth = 3
        self.learning_rate = 0.001
        self.nn = Tf_Network(self.data_length, self.learning_rate)
        self.testing_data_loaded = False
        self.training_data_loaded = False
        self.training_data_path = "Training Data\\"
        self.data_handler = Data_Handler(self.category_depth,self.data_length)
        self.Y_train = []
        self.X_train = []
        self.Y_test = []
        self.X_test = []


    def new_model(self,name):
        print("Creating new model")
        self.model_name = name
        self.nn.new_model()
        self.save_model()
        print("New Model created")


    def load_model(self, file_name):
        self.nn.set_model(load_model(f"Saved Models\\{file_name}"))
        self.model = load_model(f"Saved Models\\{file_name}")
        self.model_name = file_name

    def train_existing_model(self, epochs, file_name, training_data_size, testing_data_size):

        self.load_model(file_name)

        self.load_training_data(training_data_size)
        self.load_testing_data(testing_data_size)

        start = time.time()
        self.nn.train_model(self.X_train,self.Y_train,self.X_test,self.Y_test,epochs)
        end = time.time()

        self.save_model()

        log = Training_Log(self.model_name,epochs)
        log.add_log()

        print(f"Time taken to train total : {(end - start)/60} min")
        print(f"Time per Epoch : {((end - start)/epochs)/60} min")

        #print(f"Time per Dataset : {((end - start) / dataset_size) / 60} min")

    def train_new_model(self, epochs,file_name,training_datasize,testing_datasize):

        self.new_model(file_name)

        self.load_training_data(training_datasize)
        self.load_testing_data(testing_datasize)

        start = time.time()
        self.nn.train_model(self.X_train,self.Y_train,self.X_test,self.Y_test,epochs)
        end = time.time()

        log = Training_Log(self.model_name,epochs)
        log.add_log()

        self.nn.save_model(self.model_name)

        print(f"Time taken to train total : {(end - start) / 60} min")
        print(f"Time per Epoch : {((end - start) / epochs) / 60} min")

    def evaluate_model(self,testing_datasize):

        self.load_model()
        self.load_testing_data(testing_datasize)
        nn_sucsess, control_sucsess,mse,mse_zero = self.nn.evaluate_model(self.X_test, self.Y_test)
        log = Test_Log(self.model_name,nn_sucsess,control_sucsess,mse,mse_zero,self.lstm_units,self.learning_rate,self.data_length,self.category_depth)
        log.add_log()

    def save_model(self):
        self.nn.save_model(self.model_name)

    def load_training_data(self,selected_data_set_size):
        self.X_train, self.Y_train = self.data_handler.fetch_data(selected_data_set_size,"Training")

    def load_testing_data(self,selected_data_set_size):
        self.X_test, self.Y_test = self.data_handler.fetch_data(selected_data_set_size,"Testing")

    def get_testing_data_size(self):
        dataset_size = len(os.listdir("../TrainingData/Testing"))
        print(f" Number of testing files : {dataset_size}")

    def get_training_data_size(self):
        dataset_size = len(os.listdir("../TrainingData/Training"))
        print(f" Number of Training files : {dataset_size}")











