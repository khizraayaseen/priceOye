from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('best_xgb_regressor.pkl', 'rb'))

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    brand = request.form['brand']
    Battery = request.form['Battery']
    RAM = request.form['RAM']
    DisplaySize = request.form['DisplaySize']
    InternalMemory = request.form['InternalMemory']

    if brand=='New Balance':
        brand=0
    elif brand=='Under Armour':
        brand=1
    elif brand=='Nike':
        brand=2
    elif brand=='Adidas':
        brand=3
    elif brand=='Reebok':
        brand=4
    elif brand=='Puma':
        brand=5
    
    if Battery=='Dress':
        Battery=0
    elif Battery=='Jeans':
        Battery=1
    elif Battery=='Shoes':
        Battery=2
    elif Battery=='Sweater':
        Battery=3
    elif Battery=='Jacket':
        Battery=4
    elif Battery=='T-shirt':
        Battery=5

    if RAM=='White':
        RAM=0
    elif RAM=='Black':
        RAM=1
    elif RAM=='Red':
        RAM=2
    elif RAM=='Green':
        RAM=3
    elif RAM=='Yellow':
        RAM=4
    elif RAM=='Blue':
        RAM=5

    if DisplaySize=='XS':
        DisplaySize=0
    elif DisplaySize=='S':
        DisplaySize=1
    elif DisplaySize=='M':
        DisplaySize=2
    elif DisplaySize=='L':
        DisplaySize=3
    elif DisplaySize=='XL':
        DisplaySize=4
    elif DisplaySize=='XXL':
        DisplaySize=5

    if InternalMemory=='Nylon':
        InternalMemory=0
    elif InternalMemory=='Silk':
        InternalMemory=1
    elif InternalMemory=='Wool':
        InternalMemory=2
    elif InternalMemory=='Cotton':
        InternalMemory=3
    elif InternalMemory=='Polyester':
        InternalMemory=4
    elif InternalMemory=='Denim':
        InternalMemory=5

        
    arr = np.array([[brand, Battery, RAM, DisplaySize, InternalMemory]])
    new_data_df = pd.DataFrame(arr, columns=['Brand', 'Battery', 'RAM', 'DisplaySize', 'InternalMemory'])
    # pred = lin_reg_model.predict(new_data_df)
    pred = model.predict(new_data_df)
    print(pred)
    return render_template('home.html', data=pred[0], prediction_made=True)

if __name__ == "__main__":
    app.run(debug=True)