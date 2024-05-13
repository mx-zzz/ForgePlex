class Training_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view



    def handle_train_btn(self, epochs,training_data_size,testing_data_size):

        selected_network = self.view.get_selected_network()
        if selected_network is not None:
            self.model.train_existing_model(epochs,selected_network, training_data_size, testing_data_size)