import os
import time

from keras.saving.save import load_model

from Utility.Data_Handler import Data_Handler
from Utility.ModelData import get_model_info
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve
import seaborn as sns


class Testing_Menu:
    def __init__(self,model_name):
        self.model_name = model_name
        self.dataset_size = 0


    def test(self,dataset_size, dir, options):



        print("Testing_Menu - Test()")


        self.load_model(self.model_name)
        self.dataset_size = dataset_size
        self.dir = dir
        self.options = options or {'conmat_box': False, 'auc_box': False}





        model_info = get_model_info("Saved Models//" + self.model_name)

        try:
            input_shape = model_info["inputs"][0]["shape"]
            print(f"Input shape of selected model: {input_shape}")
        except (IndexError, KeyError) as e:
            print(f"Error accessing input shape: {e}")



        input_shape = None
        if model_info.get("inputs"):
            input_shape = model_info["inputs"][0].get("shape")

        if not isinstance(input_shape, list) or len(input_shape) < 3:
            raise ValueError(
                f"Unable to infer model input shape from saved model metadata: {input_shape}. "
                "Expected rank-3 shape like [None, time_steps, features]."
            )

        category_depth = input_shape[2]
        length = input_shape[1]

        if category_depth is None or length is None:
            raise ValueError(
                f"Model input shape contains undefined dimensions: {input_shape}. "
                "Please use a saved model with fixed time_steps and feature depth."
            )

        print(f"Category depth of selected model: {category_depth}")
        print(f"Length of selected model: {length}")




        self.data_handler = Data_Handler(category_depth,length)



        X_Test, Y_Test = self.load_testing_data(dir)


        start = time.time()
        self.test_model(X_Test, Y_Test)
        end = time.time()



        #log = Training_Log(self.model_name, self.epochs)
        #log.add_log()

        print(f"Time taken to test total : {(end - start) / 60} min")







    def load_model(self, file_name):
        self.model = load_model(f"Saved Models\\{file_name}")




    def load_testing_data(self, dir):
        files_found = len(os.listdir(dir))
        print(f" Number of testing files found : {files_found}")
        X_test, Y_test = self.data_handler.fetch_data(self.dataset_size,"Testing",dir)
        return X_test, Y_test

    def test_model(self, X_Test, Y_Test):
        # Evaluate the model
        test_loss, test_accuracy = self.model.evaluate(X_Test, Y_Test, verbose=2)
        print(f"Test Loss: {test_loss}")
        print(f"Test Accuracy: {test_accuracy}")

        # Make predictions
        Y_Pred_Prob = self.model.predict(X_Test)
        Y_Pred = np.argmax(Y_Pred_Prob, axis=1)
        Y_Test_Classes = np.argmax(Y_Test, axis=1)

        # Calculate metrics
        self.calculate_metrics(Y_Test_Classes, Y_Pred, Y_Pred_Prob, Y_Test)

    def calculate_metrics(self, Y_Test_Classes, Y_Pred, Y_Pred_Prob, Y_Test):
        # Confusion Matrix
        cm = confusion_matrix(Y_Test_Classes, Y_Pred)

        if self.options.get('conmat_box', False) is True:
            self.plot_confusion_matrix(cm)


        # Classification Report (Precision, Recall, F1-score)
        report = classification_report(Y_Test_Classes, Y_Pred)
        print("\nClassification Report:\n", report)


        if self.options.get('auc_box', False) is True:
            # AUC and ROC for each class
            self.plot_roc_curve(Y_Test, Y_Pred_Prob)


    def plot_roc_curve(self, Y_Test, Y_Pred_Prob):
        n_classes = Y_Test.shape[1]
        fpr = dict()
        tpr = dict()
        roc_auc = dict()



        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(Y_Test[:, i], Y_Pred_Prob[:, i])
            roc_auc[i] = roc_auc_score(Y_Test[:, i], Y_Pred_Prob[:, i])

        # Plot ROC curve for each class
        plt.figure()
        for i in range(n_classes):
            plt.plot(fpr[i], tpr[i], label=f'Class {i} (area = {roc_auc[i]:0.2f})')

        plt.plot([0, 1], [0, 1], 'k--')  # Random chance line
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic (ROC) Curve')
        plt.legend(loc="lower right")
        plt.show()

    def plot_confusion_matrix(self, cm):
        plt.figure(figsize=(10, 7))
        sns.heatmap(cm, annot=True, fmt='g', cmap='Blues')
        plt.title('Confusion Matrix')
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.show()





