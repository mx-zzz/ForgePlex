import math
import os
import random

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from keras.optimizers import Adam
from keras.utils import to_categorical
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
class Data_Handler:

    def format_data(self, X_data, Y_data):

        X_data = np.array(X_data)
        Y_data = np.array(Y_data)

        vectorized_function = np.vectorize(self.bin_change)
        Y_data = vectorized_function(Y_data)
        Y_data = to_categorical(Y_data.astype(int), num_classes=self.bin_num)

        # Check for NaN and infinity
        print("Y Contains NaN:", np.any(np.isnan(Y_data)))
        print("Y Contains Inf:", np.any(np.isinf(Y_data)))
        print("X Contains NaN:", np.any(np.isnan(X_data)))
        print("X Contains Inf:", np.any(np.isinf(X_data)))

        return X_data, Y_data

    def fetch_data(self, size, type, dir):

        stride = 25  # Assuming you might still want to keep this for something else
        Y_data = []
        X_data = []

        if self.include_subfolders:
            directories = self.get_directories(type, dir)
            number_of_folders = len(directories)
            print(f"Number of folders: {number_of_folders}")

            size_from_each_folder = size // number_of_folders
            print(f"Size of data to extract from each folder: {size_from_each_folder}")

            for folder in directories:
                dir_list = os.listdir(folder)
                random.shuffle(dir_list)
                file_count = 0

                print(f"Fetching {size_from_each_folder} {type} Data from : {folder} ")
                print(f"Directory list: {dir_list}")

                for filename in dir_list[:size_from_each_folder]:
                    try:
                        data = pd.read_csv(folder + "/" + filename)
                        percent = math.floor(file_count / size_from_each_folder * 100)
                        print(f"Reading file {folder}/{filename} ({percent}%)")
                    except ValueError as e:
                        raise ValueError(f"Error processing file {folder}/{filename} : {str(e)}")
                    data = data[1:]  # Skips the first row assuming it's a header or irrelevant

                    num_windows = (len(data) - self.data_length) // stride  # Calculate the number of possible windows
                    random_starts = random.sample(range(self.data_length, len(data) - self.data_length),
                                                  k=min(num_windows, 100))  # Randomly choose start points

                    for start in random_starts:
                        if start + self.data_length > len(data):
                            continue  # Skip if the window exceeds the bounds of the file
                        X_data.append(data.iloc[start - self.data_length:start, :self.bin_num].values)
                        # Assuming you're calculating a target based on the closing price change
                        Y_data.append(((data.iloc[start, 3] - data.iloc[start - 1, 3]) /
                                       (data.iloc[start - 1, 3] + 0.0000001)) * 100)

                    file_count += 1
        else:
            # Include only files from the provided directory without considering subfolders
            dir_list = os.listdir(dir)
            random.shuffle(dir_list)
            print(f"Fetching {size} {type} Data from : {dir} ")
            print(f"Directory list: {dir_list}")

            for filename in dir_list[:size]:
                try:
                    data = pd.read_csv(dir + "/" + filename)
                    percent = math.floor((dir_list.index(filename) + 1) / size * 100)
                    print(f"Reading file {dir}/{filename} ({percent}%)")
                except ValueError as e:
                    raise ValueError(f"Error processing file {dir}/{filename} : {str(e)}")
                data = data[1:]  # Skips the first row assuming it's a header or irrelevant

                num_windows = (len(data) - self.data_length) // stride  # Calculate the number of possible windows
                random_starts = random.sample(range(self.data_length, len(data) - self.data_length),
                                              k=min(num_windows, 100))  # Randomly choose start points

                for start in random_starts:
                    if start + self.data_length > len(data):
                        continue  # Skip if the window exceeds the bounds of the file
                    X_data.append(data.iloc[start - self.data_length:start, :7].values)
                    # Assuming you're calculating a target based on the closing price change
                    Y_data.append(((data.iloc[start, 3] - data.iloc[start - 1, 3]) /
                                   (data.iloc[start - 1, 3] + 0.0000001)) * 100)

        X_data, Y_data = self.format_data(X_data, Y_data)
        self.check_data(X_data, Y_data, type)

        print("saving Debug data slices")
        self.save_data_slices(X_data, "X_data", 10)
        self.save_data_slices(Y_data, "Y_data", 10)

        return X_data, Y_data

    def get_directories(self, type, mainDir):
        directories = []
        for folder in os.listdir(mainDir):
            path = mainDir + "/" + folder
            if os.path.isdir(path):  # Ensure it's a directory
                directories.append(path)
        return directories

    def bin_change(self, change):
        bin_edges = np.linspace(-5, 5, self.bin_num + 1)  # Create bin edges based on the number of bins
        for i in range(len(bin_edges) - 1):
            if bin_edges[i] <= change < bin_edges[i + 1]:
                return i
        return len(bin_edges) - 2  # Return the last bin if change equals the last edge

    def __init__(self, bin_num, data_length, include_subfolders=False):
        self.bin_num = bin_num
        self.data_length = data_length
        self.include_subfolders = include_subfolders
        self.bin_num = bin_num

    def save_data_slices(self, X, prefix, num_slices_to_save=10):
        dimensions = X.ndim
        if dimensions == 3:
            a, b, c = X.shape
            reshaped_data = X.reshape(a, b * c)
            for i, data_slice in enumerate(reshaped_data):
                if i >= num_slices_to_save: break
                np.savetxt(f"Data Samples (Debuging)\{prefix}_{i}.csv", data_slice.reshape(b, c), delimiter=",")
        elif dimensions == 2:
            for i, data_slice in enumerate(X):
                if i >= num_slices_to_save: break
                np.savetxt(f"Data Samples (Debuging)\{prefix}_{i}.csv", data_slice, delimiter=",")
        else:
            raise ValueError(f"Unexpected number of dimensions in {prefix}. Expected 2 or 3, got {dimensions}")

    def check_data(self, X, Y, type):
        print(f"{type} Data Y : {Y.__sizeof__()}")
        print(f"{type} Data X : {X.__sizeof__()}")
