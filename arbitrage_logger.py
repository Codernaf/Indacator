import csv
import os
from datetime import datetime

class ArbitrageLogger:
    def __init__(self, log_file='arbitrage_log.csv'):
        self.log_file = log_file
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Timestamp', 'From Exchange', 'To Exchange', 'Symbol', 'Profit %'])

    def log(self, from_ex, to_ex, symbol, profit):
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.utcnow(), from_ex, to_ex, symbol, f"{profit*100:.2f}"])
