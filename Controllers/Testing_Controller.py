class Testing_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_test_btn(self):
        testing_data_size = self.view.get_testing_data_size()
        if testing_data_size > 0 and not None:
            selected_network = self.view.get_selected_network()
            if selected_network is not None:
                self.model.test_model(selected_network, testing_data_size)






