from flask import Flask, render_template, request,  jsonify
import pickle;
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Create the application instance
application = Flask(__name__)
app=application

# initialise models
ridge_model = pickle.load(open('models/ridge.pickle','rb'))
standard_scaler = pickle.load(open('models/scaler.pickle','rb'))

# Define the route for the home page ('/')
@app.route('/')
def index():
    # Flask looks for 'index.html' inside the 'templates' folder
    return render_template('index.html', title='Forest Fire Prediction', heading='Welcome to FF prediction!')

# define prediction route
@app.route('/predictdata', methods=['GET','POST'])
def predict_dataPoint():
    if request.method == 'POST':
        temperature = float(request.form.get('Temperature'))
        rh = float(request.form.get('RH'))
        ws = float(request.form.get('Ws'))
        rain = float(request.form.get('Rain'))
        ffmc = float(request.form.get('FFMC'))
        dmc = float(request.form.get('DMC'))
        isi = float(request.form.get('ISI'))
        classes = float(request.form.get('Classes'))
        region = float(request.form.get('Region'))

        input_data = np.array([[temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]])
        input_scaled = standard_scaler.transform(input_data)
        result = ridge_model.predict(input_scaled)
        return render_template('home.html', result=result[0])
    else:
        return render_template('home.html')

if __name__ == '__main__':
    # Run the app in debug mode so it reloads automatically on changes
    app.run(debug=True)