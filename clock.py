import sys
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont, QColor, QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QWidget

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 500, 250)  # Adjusted size for AM/PM
        
        # Timer to update the time every second
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        
        self.show()
    
    def paintEvent(self, event):
        current_time = QTime.currentTime()
        display_text = current_time.toString('hh:mm:ss AP')  # 12-hour format with AM/PM
        
        # Customize font
        font = QFont('Helvetica', 72, QFont.Bold)
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(font)
        
        # Customize background
        painter.setBrush(QBrush(QColor(30, 30, 30)))
        painter.drawRect(self.rect())
        
        # Customize text color
        painter.setPen(QColor(255, 255, 255))
        
        # Draw time
        rect = self.rect()
        painter.drawText(rect, Qt.AlignCenter, display_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    sys.exit(app.exec_())

