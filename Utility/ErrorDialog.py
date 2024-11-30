import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton


class ErrorDialog(QDialog):
    def __init__(self, error_message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Error")

        # Set up the layout
        layout = QVBoxLayout()

        # Error message label
        self.error_label = QLabel(error_message)
        layout.addWidget(self.error_label)

        # Close button
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)


# Example usage

