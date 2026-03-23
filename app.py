from flask import Flask, request
import pickle

app = Flask(__name__)

model = pickle.load(open("Task3\data\model.pkl", "rb"))

@app.route("/")
def home():
    return '''
    <h2>Salary Prediction</h2>
    <form action="/predict" method="post">
    Experience: <input type="text" name="exp">
    <input type="submit">
    </form>
    '''

@app.route("/predict", methods=["POST"])
def predict():
    exp = float(request.form["exp"])
    prediction = model.predict([[exp]])
    return f"Predicted Salary: {prediction[0]}"

app.run(debug=True)
