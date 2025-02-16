# Calculator
Web Application Calculator

Project Folder Hierarchy <br>
calculator/ <br>
│── backend/ <br>
│   ├── server.py  # Flask backend <br>
│   ├── requirements.txt  # Dependencies <br>
│   ├── test.py # For unit testing <br>
│ <br>
│── frontend/ <br>
│   ├── index.html  # Main frontend <br>
│   ├── app.js  # JavaScript logic <br>
│

This calculator contains 2 main functionality, Addition and Subtraction. The backend uses Flask and REST API to accept requests from frontend and the frontend uses HTML form and Javascript to interact with the backend. <br>

To run the web app, activate the virtual environment and run server.py <br>
> Windows: venv\Scripts\activate <br>
> Mac: source venv/bin/activate <br>
> pip install -r requirements.txt <br>
> python server.py <br>

For testing, I used the flask-testing package. <br>
> pip install requests flask-testing

Testing done:
- Addition
- Subtraction
- Missing one input
- Invalid input
