import os

from Utility.ErrorDialog import ErrorDialog


class Testing_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_test_btn(self,options):

        print("Testing_Controller - Handle_Test_Btn()")
        # Get the testing data size from the view
        testing_data_size = self.view.get_testing_data_size()

        # Check if the data size is valid
        if testing_data_size is None or testing_data_size <= 0:
            self.show_error(f"Invalid dataset size. Please select a valid dataset. \n Test Data value : {testing_data_size}")
            return


        test_path = self.get_test_path()

        if not self.checkPath(test_path):
            return


        # If all checks are valid, proceed with testing
        try:
            self.model.test(testing_data_size,test_path,options)
            print("Testing completed successfully!")
        except Exception as e:
            self.show_error(f"An error occurred during testing: {str(e)}")

    def get_testing_data_size(self):
        return self.view.get_testing_data_size()

    def get_test_path(self):
        return self.view.get_test_path()



    def show_error(self, message):
        error_dialog = ErrorDialog(message)
        error_dialog.exec()






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

