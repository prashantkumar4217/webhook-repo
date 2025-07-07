# GitHub Webhook Listener - webhook-repo

A Flask-based web service that receives GitHub webhook events and stores merged pull request events in MongoDB Atlas. Provides an API and a simple frontend UI to view stored events.

---

## Features

- Receive GitHub webhook POST requests at `/webhook/receiver`
- Filter and store only **merged pull request** events
- Store events in MongoDB Atlas database
- REST API to retrieve all stored events (`GET /events`)
- Minimal frontend UI to display merged PR events (`GET /`)

---

## Tech Stack

- Python 3.x
- Flask
- MongoDB Atlas
- HTML/JS for frontend UI

---

## Setup & Run

1. Clone this repo and navigate to it:

   ```bash
   git clone https://github.com/prashantkumar4217/webhook-repo.git
   cd webhook-repo
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   
3. Configure your MongoDB Atlas connection string in app.py:
   ```bash
   MONGO_URI = "your_mongodb_atlas_connection_string"
4. Run the app:
      ```bash
         python app.py

5. Access the frontend UI at: http://127.0.0.1:5000/
6. API to get stored events:
 ```bash
GET /events


               


   
