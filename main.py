import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import psycopg2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt with PostgreSQL")
        self.setGeometry(100, 100, 600, 400)

        label = QLabel("Connected to PostgreSQL", self)
        label.setGeometry(50, 50, 500, 50)

        self.connect_to_db()

    def connect_to_db(self):
        try:
            connection = psycopg2.connect(
                user="myuser",
                password="mypassword",
                host="localhost",
                port="5432",
                database="mydatabase"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            print(f"Connected to - {db_version}")

            cursor.close()
            connection.close()
        except (Exception, psycopg2.Error) as error:
            print(f"Error while connecting to PostgreSQL: {error}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
