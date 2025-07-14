# webhook-repo

This project demonstrates GitHub webhook handling using:
- A GitHub repo (`action-repo`) that triggers events
- A Flask backend (`webhook-repo`) that receives those events
- MongoDB for storage
- A frontend that polls for new data

# 📦 Repo 1: `webhook-repo` (Backend + Frontend)

## 🔧 Tech Stack
- Python + Flask
- MongoDB
- HTML + JavaScript (Jinja2 + polling)

## 📁 Folder Structure

webhook-repo/ <br>
├── templates/ <br>
│ └── index.html <br>
├── .env <br>
├── app.py <br>
├── requirements.txt <br>

## 🚀 Setup Instructions

1. Clone the repo
   git clone https://github.com/YOUR_USERNAME/webhook-repo.git
   cd webhook-repo
2. Create a virtual environment
   python -m venv venv
   venv\Scripts\activate
3. Install required packages
   pip install -r requirements.txt
4. Create a .env file
   MONGO_URI=mongodb://localhost:27017
5. Start the server
   python app.py
6. Explore flask with ngrok
   ngrok http 5000
7. Add webhook to GitHub (action-repo)
   Payload URL: https://your-ngrok-url/webhook
   Content type: application/json
   Events: push, pull_request
   

   
