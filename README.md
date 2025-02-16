# calculator
Web Application Calculator

Project Folder Hierarchy
calculator/
│── backend/
│   ├── server.py  # Flask backend
│   ├── requirements.txt  # Dependencies
│   ├── test.py # For unit testing
│
│── frontend/
│   ├── index.html  # Main frontend
│   ├── app.js  # JavaScript logic
│

This calculator contains 2 main functionality, Addition and Subtraction. The backend uses Flask and REST API to accept requests from frontend and the frontend uses HTML form and Javascript to interact with the backend.

To run the web app, activate the virtual environment and run server.py
Windows: venv\Scripts\activate
Mac: source venv/bin/activate
pip install -r requirements.txt
python server.py

For testing, I used the flask-testing package.
pip install requests flask-testing

Testing done:
- Addition
- Subtraction
- Missing one input
- Invalid input
