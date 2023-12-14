import subprocess

from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_folder='static')


class config:
    def __init__(self):
        self.pid = False
        self.pid_value = 0
        self.cpu = False
        self.gpu = False
        self.memory = False
        self.power = False
        self.all_components = False
        self.plot = False
        self.frequency_enabled = False
        self.frequency_value = 0
        self.interval_enabled = False
        self.interval_value = 0
        self.smoothing_enabled = False
        self.smoothing_value = 0
        self.save_enabled = False
        self.save_value = 0

    def __str__(self):
        return f"PID: {self.pid}\n" \
               f"PID Value: {self.pid_value}\n" \
               f"CPU: {self.cpu}\n" \
               f"GPU: {self.gpu}\n" \
               f"Memory: {self.memory}\n" \
               f"Power: {self.power}\n" \
               f"All Components: {self.all_components}\n" \
               f"Plot: {self.plot}\n" \
               f"Frequency Enabled: {self.frequency_enabled}\n" \
               f"Frequency Value: {self.frequency_value}\n" \
               f"Interval Enabled: {self.interval_enabled}\n" \
               f"Interval Value: {self.interval_value}\n" \
               f"Smoothing Enabled: {self.smoothing_enabled}\n" \
               f"Smoothing Value: {self.smoothing_value}\n" \
               f"Save Enabled: {self.save_enabled}\n" \
               f"Save Value: {self.save_value}\n"

config = config()


@app.route('/')
def index():
    return render_template('MainPage.html')


@app.route('/configuration')
def configuration():
    return render_template('Config.html')


@app.route('/save_configuration', methods=['POST'])
def save_configuration():
    # Récupérer les valeurs du formulaire
    config.pid = request.form.get('pidCheckbox') == 'on'
    config.pid_value = request.form.get('PIDInput')

    config.cpu = request.form.get('cpuCheckbox') == 'on'
    config.gpu = request.form.get('gpuCheckbox') == 'on'
    config.memory = request.form.get('memoryCheckbox') == 'on'
    config.power = request.form.get('powerCheckbox') == 'on'
    config.all_components = request.form.get('allCheckbox') == 'on'
    config.plot = request.form.get('plotCheckbox') == 'on'

    config.frequency_enabled = request.form.get('frequencyCheckbox') == 'on'
    config.frequency_value = request.form.get('frequencyInput')

    config.interval_enabled = request.form.get('intervalCheckbox') == 'on'
    config.interval_value = request.form.get('intervalInput')

    config.smoothing_enabled = request.form.get('smoothingCheckbox') == 'on'
    config.smoothing_value = request.form.get('smoothingInput')

    config.save_enabled = request.form.get('saveCheckbox') == 'on'
    config.save_value = request.form.get('saveInput')

    print(config)

    return redirect('/')
    # return render_template('Config.html')


@app.route('/start_program', methods=['POST'])
def start():
    command = "python3 ../main.py -i 10 -cpu"
    subprocess.Popen(command, shell=True)
    print(config)
    return render_template('Start.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)
