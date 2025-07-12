# for the future me, if you are wondering why is this code commented cause usually I do not comment my code.
# and that's because you have a nut brain, after sleepign you won't remember how your code works, that's why I wanted to help your dunmb ass
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,  QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QColor, QFont, QFontDatabase

class Clock(QWidget):
    def __init__(self, military_time=False):
        super().__init__()
        self.military_time = military_time
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.time_label.setFont(QFont("Consolas", 60, QFont.Bold))
        self.SetUI()
        
    def SetUI(self): # All of things related to UI willl be taken care of here
        #first windows's UI
        self.setWindowTitle("My Digital clock")
        self.setGeometry(130, 130, 900, 110)
        #creation of a layout manager
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        #clock's UI
        self.setStyleSheet("background-color: black;")
        self.time_label.setStyleSheet("""
            font-size: 170px;
            color: #39FF14;
        """)
        #loading a custoom cool font
        font_id = QFontDatabase.addApplicationFont("digital.ttf")  
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(family, 60, QFont.Bold)
        #using the font
        self.time_label.setFont(my_font)
        # making a glow visual , so that it ressemble those cool movies hacking green shades
        glow = QGraphicsDropShadowEffect(self)
        glow.setBlurRadius(999)
        glow.setColor(QColor("#39FF14"))
        glow.setOffset(0, 0)
        self.time_label.setGraphicsEffect(glow)
        

        self.time_update()
    #Making the clock functional In the line above this one, I Just called the function that made the clock functional)
        self.timer.timeout.connect(self.time_update)  # call time_update every "timeout"
        self.timer.start(1000)                        # then setting that "timeout" to one second, because a clock updaate evry second lmao
    def time_update(self):
        if self.military_time:
            current_time = QTime.currentTime().toString("HH:mm:ss")
        else:
            current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

def show_clock():
    app = QApplication(sys.argv)
    user_choice =  input("Choose time format: 12h or 24h? ").strip()
    if user_choice == "24h":
        clock_windows = Clock(military_time=True)
    else:
        clock_windows = Clock(military_time=False)
    clock_windows.show()    
    sys.exit(app.exec_())
show_clock()