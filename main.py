import sys
from backend import ChatBot
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import threading

class ChatbotWIndow(QMainWindow):
    def __init__(self):
        self.chatbot = ChatBot()
        super().__init__()

        self.setMinimumSize(700, 500)

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message())

        self.button = QPushButton("send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):

            user_input = self.input_field.text().strip()
            self.chat_area.append(f"<p style= 'color:#333333'>user:{user_input}</p>")

            thread = threading.Thread(target=self.get_bot_responce, args=(user_input, ))
            thread.start()

    def get_bot_responce(self, user_input):

        responce = self.chatbot.get_respoce(user_input)
        self.chat_area.append(f"<p style= 'color:#333333'>user:{responce}</p>")


app = QApplication(sys.argv)
main_window = ChatbotWIndow()
sys.exit(app.exec())


