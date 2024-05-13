
import os
import numpy as np
import pandas as pd
from keras.layers import Activation
from tensorflow.keras.initializers import HeNormal
from keras.models import Sequential
from keras.optimizers import Adam
from keras.regularizers import l1_l2
from tensorflow.keras.layers import Input, Conv1D, MaxPooling1D, LSTM, Dense, Dropout, Flatten, concatenate, \
    BatchNormalization
import tensorflow as tf
class Tf_Network:

    def __init__(self, data_length, learning_rate):
        self.data_length = data_length
        self.category_depth = 3
        self.learning_rate = learning_rate
        self.nn_model = None

    def new_model(self):
        print("Creating Neural Network Model")

        model = Sequential()
        # First Conv1D layer - split into convolution and activation
        model.add(Conv1D(filters=32, kernel_size=3, input_shape=(100, 7),kernel_regularizer=l1_l2(l1=0.01, l2=0.01))) # Remove activation and bias
        model.add(BatchNormalization())  # Add BatchNormalization layer after convolution
        model.add(Activation('relu'))  # Add Activation layer after BatchNormalization

        # Second Conv1D layer - split into convolution and activation
        model.add(Conv1D(filters=64, kernel_size=3, use_bias=False))  # Remove activation and bias
        model.add(BatchNormalization())  # Add BatchNormalization layer after convolution
        model.add(Activation('relu'))  # Add Activation layer after BatchNormalization

        model.add(MaxPooling1D(pool_size=2))
        model.add(Flatten())
        model.add(Dense(500, activation='relu'))  # First dense layer with 250 neurons
        model.add(Dropout(0.2))  # Dropout for regularization
        model.add(Dense(7, activation='softmax'))  # Output layer for multi-class classification

        optimizer = Adam(learning_rate=self.learning_rate)

        model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
        self.nn_model = model

        return model

    def set_model (self,model):
        print(f"loading Neural Network Model")
        self.nn_model = model

    def get_model(self):
        return self.nn_model

    def save_model(self,name):
        self.nn_model.save(f"Saved Models\\{name}")

    def train_model(self,X_train, y_train,epochs):
        print(f"Training Neural Network for {epochs}.")

        scheduler_callback = tf.keras.callbacks.LearningRateScheduler(self.scheduler)

        # Define the EarlyStopping callback
        early_stopping = tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',  # Monitor the validation loss
            patience=3,  # Number of epochs with no improvement after which training will be stopped
            verbose=1,  # Log when training is stopped
            mode='min',  # The training will stop when the quantity monitored has stopped decreasing
            restore_best_weights=True
            # Restore model weights from the epoch with the best value of the monitored quantity
        )

        initial_learning_rate = self.learning_rate
        optimizer = Adam(learning_rate=initial_learning_rate)
        self.nn_model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

        log = self.nn_model.fit(X_train, y_train, epochs=epochs, batch_size=10, verbose=1, validation_split=0.02,callbacks=[scheduler_callback, early_stopping])

        print(f"Training Finished.")
        print(log)

    def scheduler(self,epoch, lr):
        min_lr = 1e-6
        if epoch < 2:
            return max(lr, min_lr)
        else:
            decay_rate = 0.85
            new_lr = lr * decay_rate ** (epoch - 1)
            return max(new_lr, min_lr)

    def evaluate_model(self, x_test, y_test):

        if (x_test is None):
            print("fuck x")

        if (y_test is None):
            print("fuck y")

        num_samples = 10000
        shuffled_indices = np.random.permutation(len(x_test))
        selected_indices = shuffled_indices[:num_samples]
        predictions = self.nn_model.predict(x_test[selected_indices])
        predicted_percentage_change = (np.argmax(predictions, axis=1))
        actual_percentage_change = (np.argmax(y_test[selected_indices], axis=1))

        predicted_percentage_change = predicted_percentage_change-3

        actual_percentage_change = actual_percentage_change-3

        nn_sucsess, control_sucsess = self.print_prediction_details(actual_percentage_change, predicted_percentage_change, predictions)
        mse = self.calculate_mean_squared_error(actual_percentage_change, predicted_percentage_change)
        mse_zero = self.calculate_mean_squared_error_compared_to_0(actual_percentage_change)

        return nn_sucsess, control_sucsess,mse,mse_zero


    def print_prediction_details(self,actual, predicted, predictions):
        print("    Predicted    Result       Error   ")
        print("---------------------------------------------------")

        nn_sucsess_count = 0
        control_sucsess_count = 0
        for i in range(len(predicted)):
            # print(predictions[i])
            error = np.abs(predicted[i] - actual[i])
            print(f"{i + 1}\t{predicted[i]:.2f}\t\t{actual[i]:.2f}\t\t{error:.2f}\t\t")
            if (predicted[i] == actual[i]):
                nn_sucsess_count += 1

            if (actual[i] == 0):
                control_sucsess_count += 1

        nn_sucsess = nn_sucsess_count/len(predicted) * 100
        control_sucsess = control_sucsess_count / len(predicted) * 100

        print(f"NN Success rate : {nn_sucsess}%")
        print(f"Control Success rate : {control_sucsess}%")

        return nn_sucsess, control_sucsess


    def calculate_mean_squared_error(self,actual, predicted):
        error = np.abs(predicted - actual)
        mse = np.square(error).mean()
        print(f"\nMean Squared Error for the test set: {mse:.3f}")
        return mse

    def calculate_mean_squared_error_compared_to_0(self,actual):
        error = np.abs(0 - actual)
        mse = np.square(error).mean()
        print(f"\nMean Squared Error for 0 is : {mse:.3f}")
        return mse


