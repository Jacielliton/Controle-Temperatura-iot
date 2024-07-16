import serial
import time
import threading
import pandas as pd

class ArduinoReader:
    def __init__(self, port, baudrate=9600, interval=10):
        self.port = port
        self.baudrate = baudrate
        self.interval = interval
        self.serial_connection = serial.Serial(port, baudrate)
        self.data = pd.DataFrame(columns=['timestamp', 'sensor1', 'sensor2'])
        self.running = False

    def read_data(self):
        while self.running:
            try:
                line = self.serial_connection.readline().decode('utf-8').strip()
                timestamp = pd.to_datetime('now')
                sensor1, sensor2 = map(float, line.split(','))
                new_data = pd.DataFrame({
                    'timestamp': [timestamp],
                    'sensor1': [sensor1],
                    'sensor2': [sensor2]
                })
                self.data = pd.concat([self.data, new_data], ignore_index=True)
                time.sleep(self.interval)
            except Exception as e:
                print(f"Error reading data: {e}")

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.read_data)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()
