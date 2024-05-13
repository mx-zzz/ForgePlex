import sys
from PySide6.QtWidgets import QApplication
from Models.Menu import Menu
from Views.Menu_View import Menu_View
from Controllers.Menu_Controller import Menu_Controller
import tensorflow as tf

class Application:
    def __init__(self):

        gpus = tf.config.experimental.list_physical_devices('GPU')
        if gpus:
            try:
                # Assuming you want to use the first GPU (RTX 4060)
                tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
            except RuntimeError as e:
                # Visible devices must be set before GPUs have been initialized
                print(e)


        self.app = QApplication(sys.argv)
        print("app")
        self.model = Menu()
        print("model")
        self.view = Menu_View()
        print("view")
        # At this point, both model and view are initialized but not connected.
        self.controller = Menu_Controller(self.model, self.view)
        print("controller")
        print("setting controller in view")
        # Now that the controller is created, you can set it in the view.
        self.view.set_controller(self.controller)
        print("set controller in view")
        self.view.show()
        print("show")

    def run(self):
        return self.app.exec()

if __name__ == "__main__":
    try:
        app = Application()
        sys.exit(app.run())
    except Exception as e:
        print(f"Unhandled exception: {e}")
        raise

