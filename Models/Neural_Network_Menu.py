from keras import Sequential
from keras.layers import Conv1D, BatchNormalization, MaxPooling1D, Activation, Flatten, Dense
from keras.optimizers import Adam
from keras.regularizers import l1_l2
from tensorflow.python.keras import regularizers


class Neural_Network_Menu:
    def __init__(self):
        self.layer_types = {'layer1Type': 'Conv', 'layer2Type': 'Conv', 'layer3Type': 'Dense'}
        self.number_of_layers = 3








    def create_model(self):


        try :
            print("setting first layer")

            self.model = Sequential()

            self.set_first_layer()

            num_of_layers = len(self.layers)
            for layer_index in range(1, num_of_layers - 1):
                print("Adding layer " + str(layer_index))
                self.add_layer(layer_index)

            self.model.add(Dense(self.categories_size))

            print("Saving model")

            self.save_model(self.name)
        except Exception as e:
            print(e)






    def add_layer(self,index):

        print(f"add_layer : index {index}")


        activation = self.layers[index]["activation"]
        type = self.layers[index]["type"]
        batch_norm = self.layers[index]["batch_normalization"]
        dropout_rate = self.layers[index]["dropout_rate"]
        l1 = self.layers[index]["l1_reg"]
        l2 = self.layers[index]["l2_reg"]
        reg = regularizers.l1_l2(l1=0.01, l2=0.01)


        if type == 'Conv':
            pooling = self.layers[index]["pooling"]
            filters = int(self.layers[index]["filters"])
            kernel = int(self.layers[index]["kernel"])
            flatten = self.layers[index]["flatten"]
            self.model.add(Conv1D(filters=filters, kernel_size=kernel,kernel_regularizer=reg))

            if (batch_norm):
                self.model.add(BatchNormalization())

            self.addActivation(activation)

            if pooling != "None" :
                self.model.add(MaxPooling1D(pool_size=int(pooling)))

            if flatten == True:
                self.model.add(Flatten())


        if type == 'Dense':
            dense_units = self.layers[index]["dense_units"]

            self.model.add(Dense(dense_units),kernel_regularizer=reg)

            if (batch_norm):
                self.model.add(BatchNormalization())

            self.addActivation(activation)


    def set_first_layer(self):


        print("set_first_layer")






        activation = self.first_layer["activation"]
        type = self.first_layer["type"]
        l1 = self.first_layer["l1_reg"]
        l2 = self.first_layer["l2_reg"]
        batch_norm = self.first_layer["batch_normalization"]
        dropout_rate = self.first_layer["dropout_rate"]

        print(self.first_layer)

        print("first layer architecture")

        if type == 'Conv':
            filters = self.first_layer["filters"]
            pooling = self.first_layer["pooling"]
            kernel = int(self.first_layer["kernel"])
            flatten = int(self.first_layer["flatten"])

            print("creating first layer conv")
            self.model.add(Conv1D(filters=filters, kernel_size=kernel, input_shape=(self.time_steps, self.categories_size),
                                  kernel_regularizer=l1_l2(l1=l1, l2=l2)))

            print("aids")
            if (batch_norm):
                self.model.add(BatchNormalization())

            self.addActivation(activation)

            if pooling != "None":
                self.model.add(MaxPooling1D(pool_size=int(pooling)))

            if flatten == True:
                self.model.add(Flatten())

            print("frist layer conv set")

        if type == 'Dense':
            dense_units = self.first_layer["dense_units"]

            self.model.add(Dense(dense_units, kernel_regularizer=l1_l2(l1=l1, l2=l2)))

            if (batch_norm):
                self.model.add(BatchNormalization())

            self.addActivation(activation)

            print("frist layer dense set")

        print("wtf")

    def addActivation(self, activationType):
        activationType = activationType.lower()
        self.model.add(Activation(activationType))  # Corrected line

    def set_data(self,data):

        print("set_data")
        print(data)


        self.name = data["general"]["name"]
        print(self.name)

        self.time_steps = data["general"]["time_steps"]
        print(self.time_steps)

        self.number_of_layers = data["general"]["layers"]
        print(self.number_of_layers)

        self.compiler = data["compile"]["compiler"]
        print(self.compiler)


        self.categories_size = data["general"]["categories"]
        print(self.compiler)




        self.layers = data["layers"]
        print(self.layers)

        self.first_layer = self.layers[0]
        print(self.first_layer)










    def handle_create_btn(self):
        self.create_model()

    def new_model(self):
        print("Creating Neural Network Model")

        self.model = Sequential()
        # First Conv1D layer - split into convolution and activation






    def compile(self,learning_rate,optimizer):

        if optimizer == "Adam":
            optimizer = Adam()
        self.model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    def save_model(self,name):
        self.model.save(f"Saved Models\\{name}")
        print(f"model saved a Saved Models\\{name}")
