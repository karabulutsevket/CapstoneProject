import psycopg2
from arayuz import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        conn = psycopg2.connect(
            host="localhost",
            database="sendpython",
            user="postgres",
            password="1973852"
        )
        self.cur = conn.cursor()
        self.aramaYapButton.clicked.connect(self.listele)
    
    def listele(self):
        square_meters_min = self.metreKareAraligi1.text() 
        square_meters_max = self.metreKareAraligi2.text()
        rooms = self.odaSayisi.currentText()
        district = self.ilce.currentText()
        
        select_query = """
            SELECT title, link, square_meters, rooms, price, date, district, AVG(price) OVER () as avg_price
            FROM tablo 
            WHERE square_meters > %s AND square_meters < %s AND rooms = %s AND district LIKE %s
        """
        self.cur.execute(select_query, (square_meters_min, square_meters_max, rooms, district + "%"))
        result = self.cur.fetchall()
        
        self.tabloWidget.setColumnCount(8)
        self.tabloWidget.setHorizontalHeaderLabels(["Title", "Link", "Square Meters", "Rooms", "Price", "Date", "District", "Avg Price"])
        
        self.tabloWidget.setRowCount(len(result))
        for row_index, row in enumerate(result):
            for col_index, col_value in enumerate(row):
                item = QTableWidgetItem(str(col_value))
                self.tabloWidget.setItem(row_index, col_index, item)
        
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())