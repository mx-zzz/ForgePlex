import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QSlider, QVBoxLayout, QLabel, QStyle
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QPalette, QColor


class CustomSlider(QSlider):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)



        self.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.setTickInterval(10)  # Adjust to your desired interval
        self.setMaximum(100)
        self.setMinimum(0)

        # Set up the label for displaying the value
        self.value_label = QLabel(self)
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.value_label.setStyleSheet("color: blue;")  # Styling the label, you can customize it as you wish

        # Connect the valueChanged signal to update the label text
        self.valueChanged.connect(self.updateValueLabel)


    def updateValueLabel(self, value):
        self.value_label.setText(str(value))
        self.updateLabelPosition()



    def updateLabelPosition(self):
        # Update the label position to be above the slider handle
        handle_rect = self.handleRect()
        self.value_label.move(handle_rect.x() + (handle_rect.width() - self.value_label.width()) // 2,
                              handle_rect.y() - self.value_label.height())

    def handleRect(self):
        # Calculate the handle rectangle (you might need to adjust this based on your styling)
        slider_length = self.width() if self.orientation() == Qt.Orientation.Horizontal else self.height()
        available_length = slider_length - self.style().pixelMetric(QStyle.PixelMetric.PM_SliderLength)
        proportion = (self.value() - self.minimum()) / (self.maximum() - self.minimum())
        offset = round(proportion * available_length)
        handle_side = self.style().pixelMetric(QStyle.PixelMetric.PM_SliderThickness)
        if self.orientation() == Qt.Orientation.Horizontal:
            return QRect(offset, 0, handle_side, handle_side)
        else:
            return QRect(0, offset, handle_side, handle_side)



    def paintEvent(self, event):
        # Custom paint event to draw the slider, you can do further customization here
        super().paintEvent(event)
        painter = QPainter(self)
        pen = painter.pen()
        pen.setColor(QColor('blue'))
        painter.setPen(pen)

        # Draw the tick marks, adjust the positions as necessary
        tick_size = 10  # The size of the ticks
        for i in range(self.minimum(), self.maximum() + 1, self.tickInterval()):
            if self.orientation() == Qt.Orientation.Horizontal:
                x = self.width() * (i - self.minimum()) / (self.maximum() - self.minimum())
                painter.drawLine(x, 0, x, tick_size)
            else:
                y = self.height() * (i - self.minimum()) / (self.maximum() - self.minimum())
                painter.drawLine(0, y, tick_size, y)

        self.updateLabelPosition()  # Make sure to update the label position
        
