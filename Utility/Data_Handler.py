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

import math
import os
import random
from typing import List, Optional

import numpy as np
import pandas as pd
from keras.utils import to_categorical


class Data_Handler:
    def __init__(self, bin_num, data_length, dataset_options=None, include_subfolders=False):
        self.bin_num = bin_num
        self.data_length = data_length
        self.include_subfolders = include_subfolders
        self.dataset_options = dataset_options or {}

        self._load_dataset_config()

    # -------------------------------------------------
    # Config
    # -------------------------------------------------
    def _load_dataset_config(self):
        self.task = self.dataset_options.get("task", "Classification")
        self.label_mode = self.dataset_options.get("label_mode", "Percent Change Bins")

        self.target_col = self.dataset_options.get("target_col", 3)
        self.label_col = self.dataset_options.get("label_col", 0)
        self.horizon = self.dataset_options.get("horizon", 1)

        self.feature_mode = self.dataset_options.get("feature_mode", "Use first N columns")
        self.feature_count = self.dataset_options.get("feature_count", 7)
        self.feature_columns = self.dataset_options.get("feature_columns", [])

        self.stride = self.dataset_options.get("stride", 25)
        self.sampling_mode = self.dataset_options.get("sampling_mode", "Random")
        self.max_windows_per_file = self.dataset_options.get("max_windows_per_file", 100)
        self.seed = self.dataset_options.get("seed", 42)
        self.skip_first_row = self.dataset_options.get("skip_first_row", True)

        self.num_classes = self.dataset_options.get("num_classes", self.bin_num)
        self.bin_min = self.dataset_options.get("bin_min", -5.0)
        self.bin_max = self.dataset_options.get("bin_max", 5.0)

    # -------------------------------------------------
    # Formatting
    # -------------------------------------------------
    def format_data(self, X_data, Y_data):
        X_data = np.array(X_data)
        Y_data = np.array(Y_data)

        task = self.task.lower()
        label_mode = self.label_mode.lower()

        if task == "classification":
            if label_mode == "percent change bins":
                vectorized_function = np.vectorize(self.bin_change)
                Y_data = vectorized_function(Y_data)
                Y_data = to_categorical(Y_data.astype(int), num_classes=self.num_classes)

            elif label_mode == "existing label column":
                Y_data = to_categorical(Y_data.astype(int), num_classes=self.num_classes)

            else:
                raise ValueError(f"Unsupported classification label mode: {self.label_mode}")

        elif task == "regression":
            Y_data = Y_data.astype(float)

        else:
            raise ValueError(f"Unsupported task type: {self.task}")

        print("Y Contains NaN:", np.any(np.isnan(Y_data)))
        print("Y Contains Inf:", np.any(np.isinf(Y_data)))
        print("X Contains NaN:", np.any(np.isnan(X_data)))
        print("X Contains Inf:", np.any(np.isinf(X_data)))

        return X_data, Y_data

    # -------------------------------------------------
    # Main fetch
    # -------------------------------------------------
    def fetch_data(self, size, data_type, directory):
        random.seed(self.seed)

        X_data = []
        Y_data = []

        if self.include_subfolders:
            directories = self.get_directories(directory)
            number_of_folders = len(directories)

            print(f"Number of folders: {number_of_folders}")

            if number_of_folders == 0:
                raise ValueError(f"No subfolders found in {directory}")

            size_from_each_folder = max(1, size // number_of_folders)
            print(f"Size of data to extract from each folder: {size_from_each_folder}")

            for folder in directories:
                dir_list = [f for f in os.listdir(folder) if f.lower().endswith(".csv")]
                random.shuffle(dir_list)

                print(f"Fetching {size_from_each_folder} {data_type} Data from : {folder}")
                print(f"Directory list: {dir_list}")

                for file_count, filename in enumerate(dir_list[:size_from_each_folder]):
                    filepath = os.path.join(folder, filename)
                    x_file, y_file = self._process_file(
                        filepath=filepath,
                        file_count=file_count,
                        total_files=size_from_each_folder,
                        data_type=data_type
                    )
                    X_data.extend(x_file)
                    Y_data.extend(y_file)

        else:
            dir_list = [f for f in os.listdir(directory) if f.lower().endswith(".csv")]
            random.shuffle(dir_list)

            print(f"Fetching {size} {data_type} Data from : {directory}")
            print(f"Directory list: {dir_list}")

            for file_count, filename in enumerate(dir_list[:size]):
                filepath = os.path.join(directory, filename)
                x_file, y_file = self._process_file(
                    filepath=filepath,
                    file_count=file_count,
                    total_files=size,
                    data_type=data_type
                )
                X_data.extend(x_file)
                Y_data.extend(y_file)

        X_data, Y_data = self.format_data(X_data, Y_data)
        self.check_data(X_data, Y_data, data_type)

        print("saving Debug data slices")
        self.save_data_slices(X_data, "X_data", 10)
        self.save_data_slices(Y_data, "Y_data", 10)

        return X_data, Y_data

    # -------------------------------------------------
    # File processing helpers
    # -------------------------------------------------
    def _process_file(self, filepath, file_count, total_files, data_type):
        try:
            data = pd.read_csv(filepath)
            percent = math.floor((file_count + 1) / max(total_files, 1) * 100)
            print(f"Reading file {filepath} ({percent}%)")
        except ValueError as e:
            raise ValueError(f"Error processing file {filepath} : {str(e)}")

        data = self._prepare_dataframe(data)

        X_data = []
        Y_data = []

        starts = self._get_window_starts(len(data))

        for start in starts:
            if start >= len(data):
                continue

            x_window = self._get_feature_data(data, start)
            y_label = self._get_label(data, start)

            if y_label is None:
                continue

            X_data.append(x_window)
            Y_data.append(y_label)

        return X_data, Y_data

    def _prepare_dataframe(self, data):
        if self.skip_first_row:
            data = data[1:]
        return data.reset_index(drop=True)

    def _get_window_starts(self, total_rows):
        min_start = max(self.data_length, self.horizon)
        max_start = total_rows - 1

        if max_start <= min_start:
            return []

        possible_starts = list(range(min_start, max_start + 1, self.stride))

        sampling = self.sampling_mode.lower()

        if sampling == "all":
            return possible_starts

        if sampling == "sequential":
            return possible_starts[:self.max_windows_per_file]

        if sampling == "random":
            sample_size = min(len(possible_starts), self.max_windows_per_file)
            return random.sample(possible_starts, sample_size)

        raise ValueError(f"Unsupported sampling mode: {self.sampling_mode}")

    # -------------------------------------------------
    # Feature + label helpers
    # -------------------------------------------------
    def _get_feature_data(self, data, start):
        feature_mode = self.feature_mode.lower()

        if feature_mode == "use first n columns":
            return data.iloc[start - self.data_length:start, :self.feature_count].values

        if feature_mode == "select columns manually":
            if not self.feature_columns:
                raise ValueError("Feature mode is manual, but no feature_columns were provided.")
            return data.iloc[start - self.data_length:start, self.feature_columns].values

        raise ValueError(f"Unsupported feature mode: {self.feature_mode}")

    def _get_label(self, data, start):
        label_mode = self.label_mode.lower()

        if label_mode in ("percent change bins", "percent change numeric"):
            previous_index = start - self.horizon
            if previous_index < 0:
                return None

            current_value = data.iloc[start, self.target_col]
            previous_value = data.iloc[previous_index, self.target_col]

            return ((current_value - previous_value) / (previous_value + 1e-7)) * 100

        if label_mode == "existing label column":
            return data.iloc[start, self.label_col]

        raise ValueError(f"Unsupported label mode: {self.label_mode}")

    # -------------------------------------------------
    # Utility
    # -------------------------------------------------
    def get_directories(self, main_dir):
        directories = []
        for folder in os.listdir(main_dir):
            path = os.path.join(main_dir, folder)
            if os.path.isdir(path):
                directories.append(path)
        return directories

    def bin_change(self, change):
        bin_edges = np.linspace(self.bin_min, self.bin_max, self.num_classes + 1)

        for i in range(len(bin_edges) - 1):
            if bin_edges[i] <= change < bin_edges[i + 1]:
                return i

        return len(bin_edges) - 2

    def save_data_slices(self, X, prefix, num_slices_to_save=10):
        os.makedirs("Data Samples (Debuging)", exist_ok=True)

        dimensions = X.ndim
        if dimensions == 3:
            a, b, c = X.shape
            reshaped_data = X.reshape(a, b * c)
            for i, data_slice in enumerate(reshaped_data):
                if i >= num_slices_to_save:
                    break
                np.savetxt(
                    f"Data Samples (Debuging)\\{prefix}_{i}.csv",
                    data_slice.reshape(b, c),
                    delimiter=","
                )

        elif dimensions == 2:
            for i, data_slice in enumerate(X):
                if i >= num_slices_to_save:
                    break
                np.savetxt(
                    f"Data Samples (Debuging)\\{prefix}_{i}.csv",
                    np.atleast_1d(data_slice),
                    delimiter=","
                )

        elif dimensions == 1:
            for i, data_slice in enumerate(X):
                if i >= num_slices_to_save:
                    break
                np.savetxt(
                    f"Data Samples (Debuging)\\{prefix}_{i}.csv",
                    np.array([data_slice]),
                    delimiter=","
                )

        else:
            raise ValueError(
                f"Unexpected number of dimensions in {prefix}. Expected 1, 2 or 3, got {dimensions}"
            )

    def check_data(self, X, Y, data_type):
        print(f"{data_type} Data Y : {Y.__sizeof__()}")
        print(f"{data_type} Data X : {X.__sizeof__()}")