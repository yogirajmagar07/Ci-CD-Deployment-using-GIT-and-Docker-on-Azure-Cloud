from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return "<h2> This Simple Flask application </h2>"

@app.route('/predict',methods=['POST'])
def predict_result():
    return "Predict"




if __name__=="__main__":
    app.run(debug=True)