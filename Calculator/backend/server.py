from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/add', methods=['POST'])
def add():
    num1 = request.form.get("num1", "0").strip()
    num2 = request.form.get("num2", "0").strip()

    if num1 == "":
        num1 = "0"
    if num2 == "":
        num2 = "0"

    try:
        result = float(num1) + float(num2)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    


@app.route('/subtract', methods=['POST'])
def subtract():
    num1 = request.form.get("num1", "0").strip()
    num2 = request.form.get("num2", "0").strip()
    
    if num1 == "":
        num1 = "0"
    if num2 == "":
        num2 = "0"
    
    try:
        result = float(num1) - float(num2)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400
    

if __name__ == '__main__':
    app.run(debug=True)
