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
