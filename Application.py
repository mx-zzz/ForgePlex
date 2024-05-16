import sys
from PySide6.QtWidgets import QApplication
from Models.Menu import Menu
from Views.Menu_View import Menu_View
from Controllers.Menu_Controller import Menu_Controller
import tensorflow as tf

class Application:
    def __init__(self):



        # Debug info for tensor flow gpu detection

        gpus = tf.config.experimental.list_physical_devices('GPU')
        if gpus:
            try:
                tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
            except RuntimeError as e:
                print(e)

        print("Initializing App")
        self.app = QApplication(sys.argv)
        print("Initializing Menu")
        self.model = Menu()
        print("Initializing View")
        self.view = Menu_View()
        print("Initializing controller")
        self.controller = Menu_Controller(self.model, self.view)

        print("Parsing controller to view")
        self.view.set_controller(self.controller)
        print("Showing Menu View")
        self.view.show()


    def run(self):
        return self.app.exec()

if __name__ == "__main__":
    try:
        app = Application()
        sys.exit(app.run())
    except Exception as e:
        print(f"Unhandled exception: {e}")
        raise

