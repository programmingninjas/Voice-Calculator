from flask import Flask,render_template,jsonify,request
from calculator import calculate


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('voice.html')

@app.route('/backend',methods=['GET','POST'])
def backend():

    dataGet = request.get_json(force=True)

    output = calculate(dataGet)

    return jsonify(output)

if __name__ == '__main__':

    app.run()

