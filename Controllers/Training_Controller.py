import os as os

from Utility.ErrorDialog import ErrorDialog


class Training_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view



    def handle_train_btn(self, training_params):

        print("handle_train_btn")


        if (not self.checkPaths(training_params)):
            error_dialog = ErrorDialog("Path/s is empty or invalid")
            error_dialog.exec()
            return

        if  (str(training_params['general']['split']) == "0" and training_params['general']['data_source'] == 0):
            error_dialog = ErrorDialog("Split cant be 0")
            error_dialog.exec()
            return


        self.model.train(training_params)



    def checkPaths(self, training_params):

        source = training_params['general']['data_source']
        training_dir = training_params['general']['training_dir']
        testing_dir = training_params['general']['testing_dir']

        if training_params['general']['data_source'] == 0:
            return(self.checkPath(training_dir))
        else:
            return(self.checkPath(training_dir) and self.checkPath(testing_dir))




    def checkPath(self, dir):
        try:
            if not os.path.exists(dir):
                return False

            if not os.path.isdir(dir):
                return False

            if len(os.listdir(dir)) == 0:
                return False

            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False





