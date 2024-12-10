from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

# Load the model
try:
    model = pickle.load(open('random_regressor.pkl', 'rb'))
except Exception as e:
    print(f"Error loading model: {e}")
# model = pickle.load(open('xgb_regressor.pkl', 'rb'))

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    if model is None:
        return "Error: Model not loaded properly", 500
    
    try:
        # Retrieve form data
        Brand = request.form['Brand']  # Updated to match dropdown name
        Battery = request.form['Battery']
        RAM = request.form['RAM']
        DisplaySize = request.form['DisplaySize']
        InternalMemory = request.form['InternalMemory']
    except KeyError as e:
        return f"Missing form data: {e}", 400

    # Mapping for Brand (dropdown values)
    # Brand_mapping = {
    #     'infinix': 0, 'samsung': 1, 'tecno': 2, 'nokia': 3, 'xiaomi': 4, 'oppo': 5,
    #     'realme': 6, 'honor': 7, 'motorola': 8, 'poco': 9, 'vgotel': 10, 'itel': 11,
    #     'zte': 12, 'calme': 13, 'sparx': 14, 'vivo': 15, 'villaon': 16, 'dcode': 17,
    #     'umidigi': 18, 'gfive': 19, 'q': 20, 'digit': 21, 'oneplus': 22, 'x': 23,
    #     'g': 24, 'huawei': 25, 'apple': 26, 'xsmart': 27, 'kxd': 28, 'gionee': 29,
    #     'oukitel': 30, 'vnus': 31, 'xmobile': 32, 'me-mobile': 33, 'club-mobile': 34
    # }

    # # Convert Brand using mapping
    # Brand = Brand_mapping.get(Brand, -1)

    # Convert other fields to numeric (if possible, otherwise set to -1)
    # try:
    #     Battery = float(Battery) if Battery else -1
    # except ValueError:
    #     Battery = -1

    # try:
    #     RAM = float(RAM) if RAM else -1
    # except ValueError:
    #     RAM = -1

    # try:
    #     DisplaySize = float(DisplaySize) if DisplaySize else -1
    # except ValueError:
    #     DisplaySize = -1

    # try:
    #     InternalMemory = float(InternalMemory) if InternalMemory else -1
    # except ValueError:
    #     InternalMemory = -1

    # Prepare the input for the model
    input_data = np.array([[Brand, Battery, RAM, DisplaySize, InternalMemory]])
    input_df = pd.DataFrame(input_data, columns=['Brand', 'Battery', 'RAM', 'Display Size', 'Internal Memory'])

    # Make the prediction
    pred = model.predict(input_df)

    # Render the result back to the user
    return render_template('home.html', data=pred[0], prediction_made=True)

if __name__ == "__main__":
    app.run(debug=True)
