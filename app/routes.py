from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd
import plotly.express as px
from .arduino import ArduinoReader

main = Blueprint('main', __name__)

# Inicializa um DataFrame vazio
columns = ['timestamp', 'sensor1', 'sensor2']
df = pd.DataFrame(columns=columns)
arduino_reader = None

@main.route('/')
def index():
    fig = px.line(df, x='timestamp', y=['sensor1', 'sensor2'], title='Leituras de Temperatura e Umidade ao Longo do Tempo')
    fig.update_layout(
        xaxis_title='Data e Hora',
        yaxis_title='Valores',
        legend_title='Sensores'
    )
    graph = fig.to_html(full_html=False)
    return render_template('index.html', graph=graph)

@main.route('/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        timestamp = request.form['timestamp']
        sensor1 = float(request.form['sensor1'])
        sensor2 = float(request.form['sensor2'])
        
        global df
        new_data = pd.DataFrame({
            'timestamp': [pd.to_datetime(timestamp)],
            'sensor1': [sensor1],
            'sensor2': [sensor2]
        })
        df = pd.concat([df, new_data], ignore_index=True)
        df.sort_values(by='timestamp', inplace=True)
        
        return redirect(url_for('main.index'))
    return render_template('add_data.html')

@main.route('/connect_arduino', methods=['GET', 'POST'])
def connect_arduino():
    global arduino_reader, df
    if request.method == 'POST':
        port = request.form['port']
        baudrate = int(request.form['baudrate'])
        interval = int(request.form['interval'])
        
        arduino_reader = ArduinoReader(port, baudrate, interval)
        arduino_reader.start()
        
        # Atualizar o DataFrame a cada 10 segundos
        def update_dataframe():
            global df
            while arduino_reader.running:
                df = arduino_reader.data
                time.sleep(interval)
        
        threading.Thread(target=update_dataframe).start()
        
        return redirect(url_for('main.index'))
    return render_template('connect_arduino.html')
