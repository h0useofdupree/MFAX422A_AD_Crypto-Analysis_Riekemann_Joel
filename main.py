import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class DataAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Data Visualization App')
        self.setWindowIcon(QIcon('app_icon.png'))  # Optionally set an icon
        self.setGeometry(100, 100, 360, 200)  # Adjust window size and position

        outer_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        widget = QWidget()
        widget.setLayout(outer_layout)
        self.setCentralWidget(widget)

        # Define button styles
        button_style = "QPushButton { font-size: 16px; margin: 5px; padding: 10px; }"

        # Line Graph Button
        btn_line = QPushButton('Line Graph', self)
        btn_line.setStyleSheet(button_style)
        btn_line.clicked.connect(lambda: self.open_file('line'))
        button_layout.addWidget(btn_line)

        # Bar Chart Button
        btn_bar = QPushButton('Bar Chart', self)
        btn_bar.setStyleSheet(button_style)
        btn_bar.clicked.connect(lambda: self.open_file('bar'))
        button_layout.addWidget(btn_bar)

        # Scatter Plot Button
        btn_scatter = QPushButton('Scatter Plot', self)
        btn_scatter.setStyleSheet(button_style)
        btn_scatter.clicked.connect(lambda: self.open_file('scatter'))
        button_layout.addWidget(btn_scatter)

        outer_layout.addLayout(button_layout)

    def open_file(self, graph_type):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)", options=options)
        if file_name:
            self.plot_data(file_name, graph_type)

    def plot_data(self, file_path, graph_type):
        data = pd.read_csv(file_path, parse_dates=['snapped_at'], index_col='snapped_at')
        plt.figure(figsize=(10, 5))

        if graph_type == 'line':
            sns.lineplot(x=data.index, y=data['price'], marker='o', linestyle='-')
        elif graph_type == 'bar':
            plt.bar(data.index, data['price'], color='blue')
        elif graph_type == 'scatter':
            plt.scatter(data.index, data['price'], color='red')

        plt.title(f'{graph_type.capitalize()} of Price Data Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.grid(True)
        plt.show()

def main():
    app = QApplication(sys.argv)
    ex = DataAnalyzer()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
