from flask import Flask, render_template, request
from os import system
import pandas as pd
# import pandas as pd
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET','POST'])
def data():
    if request.method == 'POST':
        f = request.form['csvfile']
        data =[]
        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        return render_template('data.html', data=data)

@app.route('/sale/<transaction_id>')
def get_sale(transaction_id=0):
    data =[]
    with open(csvfile) as file:
        csvfile = csv.reader(file)
        for row in csvfile:
            data.append(row)

    return render_template('data.html', data=data)


@app.route('/candidate/<transaction_row>/<transaction_col>', methods=['GET', 'POST'])
def data_number(transaction_row, transaction_col):
    with open('main2.csv') as fd:
        # os.system('data.html.{}'.format(PlayfileDir))
        data = []
        reader=csv.reader(fd)
        rows = list(fd)
        data.append(rows[int(transaction_row)][int(transaction_col)])
    return render_template('candidate.html', data=data)

# @app.route('/csvup', methods=['GET'])
# def upload():
#     data = pd.read_csv (r'main2.csv')   
#     df = pd.DataFrame(data)
#     return render_template('csvup.html', aa=df)


if __name__ == "__main__":
    app.run(debug=True)