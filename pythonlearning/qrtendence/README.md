# QRtendence Web App

This project is a web application for managing student attendance using QR codes. It consists of a React frontend and a FastAPI backend.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

*   Node.js and npm (for the frontend)
*   Python 3.8+ and pip (for the backend)

### Backend Setup

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Create and activate a Python virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```
    The backend will be running at `http://127.0.0.1:8000`.

### Frontend Setup

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install the Node.js dependencies:
    ```bash
    npm install
    ```
3.  Start the React development server:
    ```bash
    npm start
    ```
    The frontend will typically open in your browser at `http://localhost:3000`.

## Project Structure

*   `backend/`: Contains the FastAPI backend application.
*   `frontend/`: Contains the React frontend application.
*   `README.md`: This file.

## Google Sheets API Setup

To enable Google Sheets integration, you need to obtain a `credentials.json` file:

1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Create a new project or select an existing one.
3.  Enable the "Google Sheets API" for your project.
4.  Go to "Credentials" and click "Create Credentials" -> "OAuth client ID".
5.  Select "Desktop app" as the application type and create it.
6.  Download the `credentials.json` file.
7.  Place the downloaded `credentials.json` file in the `backend/` directory of this project.

The first time you run the backend with Google Sheets integration, a browser window will open asking you to authorize the application. After authorization, a `token.json` file will be created in the `backend/` directory, which will be used for subsequent authentications.

### Google Sheet for Student Data

For student registration, you'll need a Google Sheet to store the student information. Create a new Google Sheet and note its ID from the URL (e.g., `https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_ID_HERE/edit`).

Update the `STUDENT_SPREADSHEET_ID` variable in `backend/main.py` with your sheet's ID.

## Next Steps

*   Develop student registration and attendance marking features.
*   Build admin functionalities (attendance verification, QR code generation, schedule management).
*   Enhance UI/UX and add styling.
