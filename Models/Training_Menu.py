import os
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import os
import time
import tensorflow as tf
from sklearn.model_selection import KFold
from tensorflow.keras.optimizers import Adam
from Utility import Tf_Network
from keras.models import load_model
from Utility.Data_Handler import Data_Handler
from Utility.Tf_Network import Tf_Network
from Utility.Test_Log import Test_Log
from Utility.Training_Log import Training_Log
import tensorflow as tf
from Utility.ModelData import get_model_info
from tensorflow.keras.callbacks import LearningRateScheduler
class Training_Menu:
    def __init__(self, model_name):
        self.model_name = model_name


    def train(self, trainOptions):





        self.load_model(self.model_name)

        self.setTrainingOptions(trainOptions)


        model_info = get_model_info("Saved Models//" + self.model_name)

        try:
            input_shape = model_info["inputs"][0]["shape"]
            print(f"Input shape of selected model: {input_shape}")
        except (IndexError, KeyError) as e:
            print(f"Error accessing input shape: {e}")



        category_depth = model_info["inputs"][0]["shape"][2]
        length = model_info["inputs"][0]["shape"][1]

        print(f"Category depth of selected model: {category_depth}")
        print(f"Length of selected model: {length}")




        self.data_handler = Data_Handler(category_depth,length)


        if self.data_source == 0:
            X_Train, Y_Train, X_Test, Y_Test = self.load_split_data()
        else:
            X_Train, Y_Train, X_Test, Y_Test = self.load_seperate_data()


        start = time.time()
        self.train_model(X_Train, Y_Train, X_Test, Y_Test, self.epochs,self.model,self.folds)
        end = time.time()

        self.model.save(f"Saved Models\\{self.model_name}")

        log = Training_Log(self.model_name, self.epochs)
        log.add_log()

        print(f"Time taken to train total : {(end - start) / 60} min")
        print(f"Time per Epoch : {((end - start) / self.epochs) / 60} min")




    def load_split_data(self):
        X_Data, Y_Data = self.load_training_data(self.training_dir)
        X_Train, X_Test, Y_Train, Y_Test = train_test_split(X_Data, Y_Data, test_size=float(self.split),
                                                                            random_state=42)
        return X_Train, Y_Train, X_Test, Y_Test





    def load_seperate_data(self):

        X_Train, Y_Train = self.load_training_data(self.training_dir)
        X_Test, Y_Test = self.load_testing_data(self.training_dir)
        return X_Train, Y_Train, X_Test, Y_Test






 
    def load_model(self, file_name):
        self.model = load_model(f"Saved Models\\{file_name}")




    def load_training_data(self, dir):
        dataset_size = len(os.listdir(dir))
        print(f" Number of training files found : {dataset_size}")
        X_train,Y_train = self.data_handler.fetch_data(self.batch_size,"Training",dir)
        return X_train, Y_train


    def load_testing_data(self, dir):
        dataset_size = len(os.listdir(dir))
        print(f" Number of testing files found : {dataset_size}")
        X_test, Y_test = self.data_handler.fetch_data(self.batch_size,"Testing",dir)
        return X_test, Y_test



    def train_model(self, X_train, y_train, x_test, y_test, epochs, model, n_splits):
        print(f"Training Neural Network with {n_splits}-fold Cross-Validation for {epochs} epochs each.")

        kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
        fold = 1

        call_backs = []
        if self.scheduler_enabled:
            print("setting scheduler")
            call_backs.append(LearningRateScheduler(self.scheduler))

        if self.enable_stopping:
            print("setting early stopping")
            call_backs.append(self.getEarlyStopping())


        for train_index, val_index in kf.split(X_train):
            print(f"Training fold {fold}...")
            X_train_fold, X_val_fold = X_train[train_index], X_train[val_index]
            y_train_fold, y_val_fold = y_train[train_index], y_train[val_index]




            if (fold == 1):
                # Preview and debug information
                print("Previewing training data:")
                print(f"X_train_fold shape: {X_train_fold.shape}")
                print(f"y_train_fold shape: {y_train_fold.shape}")
                print(f"X_val_fold shape: {X_val_fold.shape}")
                print(f"y_val_fold shape: {y_val_fold.shape}")

                # Print some samples of the data
                print("Sample training data:")
                print(X_train_fold[:2])  # Print the first 2 samples of the training data
                print("Sample training labels:")
                print(y_train_fold[:2])  # Print the first 2 labels of the training data
                print("Sample validation data:")
                print(X_val_fold[:2])  # Print the first 2 samples of the validation data
                print("Sample validation labels:")
                print(y_val_fold[:2])  # Print the first 2 labels of the validation data





            optimizer = Adam(learning_rate=self.initial_learning_rate)



            print("compiling")
            model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

            log = model.fit(X_train_fold, y_train_fold, epochs=epochs, batch_size=self.batch_size, verbose=self.verbiose_mode,
                            validation_data=(X_val_fold, y_val_fold), callbacks=call_backs)

            print(f"Fold {fold} training finished.")
            print(log.history)
            fold += 1

        print(f"Cross-Validation Training Finished.")

        kf = KFold(n_splits=n_splits, shuffle=True, random_state=32)

        fold = 1

        test_losses = []
        test_accuracies = []

        for iteration in kf.split(x_test):

            test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=self.verbiose_mode)
            print(f"Test set evaluation {fold} : Loss = {test_loss}, Accuracy = {test_accuracy}")
            test_losses.append(test_loss)
            test_accuracies.append(test_accuracy)
            fold += 1


        # Calculate and print the average metrics across all folds
        avg_test_loss = np.mean(test_losses)
        avg_test_accuracy = np.mean(test_accuracies)
        print(f"Average Test set evaluation across all {self.folds} folds: Loss = {avg_test_loss}, Accuracy = {avg_test_accuracy}")

        # Evaluate on the provided test set




    def getEarlyStopping(self):

        if (self.monitored_variable == "Loss"):
            monitor = "val_loss"

        if (self.monitored_variable == "Accuracy"):
            monitor = "val_accuracy"

        if (self.stop_trigger == 0):
            mode = "min"

        if (self.stop_trigger == 1):
            mode = "max"

        # Print debug information
        print(f"Monitored Variable: {self.monitored_variable}")
        print(f"Monitor: {monitor}")
        print(f"Stop Trigger: {self.stop_trigger}")
        print(f"Mode: {mode}")
        print(f"Patience: {self.epochs_till_stop}")
        print(f"Verbose Mode: {self.verbiose_mode}")

        early_stopping = tf.keras.callbacks.EarlyStopping(
             monitor=monitor,  # Monitor the validation loss
             patience=self.epochs_till_stop,  # Number of epochs with no improvement after which training will be stopped
             verbose=self.verbiose_mode,  # Log when training is stopped
             mode=mode,  # The training will stop when the quantity monitored has stopped decreasing
             restore_best_weights=self.restore_weights
                        # Restore model weights from the epoch with the best value of the monitored quantity
          )
        return early_stopping







    def scheduler(self, epoch, lr):
        min_lr = 1e-7
        if epoch < 2:
            return max(lr, min_lr)
        else:
            decay_rate = self.decay_rate
            new_lr = lr * decay_rate ** (epoch - 1)
            return max(new_lr, min_lr)





    def setTrainingOptions(self, data):
        # Extract general variables
        self.epochs = data['general']['epochs']
        self.verbiose_mode = data['general']['verbiose']
        self.initial_learning_rate = data['general']['initial_learning_rate']
        self.batch_size = data['general']['batch_size']
        self.data_source = data['general']['data_source']
        self.split = float(data['general']['split'])/100
        self.training_dir = data['general']['training_dir']
        self.testing_dir = data['general']['testing_dir']
        self.folds = data['general']['folds']
        self.subfolders = data['general']['subfolders']

        # Extract early stopping variables
        self.enable_stopping = data['early_stopping']['enable_stopping']
        self.monitored_variable = data['early_stopping']['monitored_variable']
        self.epochs_till_stop = data['early_stopping']['epochs_till_stop']
        self.stop_trigger = data['early_stopping']['stop_trigger']
        self.restore_weights = data['early_stopping']['restore_weights']

        # Extract learning rate scheduler variables
        self.scheduler_enabled = 'params' in data['learning_rate_scheduler'] and bool(
            data['learning_rate_scheduler']['params'])
        self.decay_type = data['learning_rate_scheduler']['type'] if self.scheduler_enabled else None
        self.decay_rate = data['learning_rate_scheduler']['params'].get(
            'decay_rate') if self.scheduler_enabled else None
        self.decay_steps = data['learning_rate_scheduler']['params'].get(
            'decay_steps') if self.scheduler_enabled else None

        # Print or use the variables as needed
        print(
            f"epochs: {self.epochs}, verbiose_mode: {self.verbiose_mode}, initial_learning_rate: {self.initial_learning_rate}, batch_size: {self.batch_size}")
        print(f"data_source: {self.data_source}, split: {self.split}, enable_stopping: {self.enable_stopping}")
        print(
            f"monitored_variable: {self.monitored_variable}, epochs_till_stop: {self.epochs_till_stop}, stop_trigger: {self.stop_trigger}, restore_weights: {self.restore_weights}")
        print(
            f"scheduler_enabled: {self.scheduler_enabled}, decay_type: {self.decay_type}, decay_rate: {self.decay_rate}, decay_steps: {self.decay_steps}")
