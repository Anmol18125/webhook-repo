

```markdown
# 📡 GitHub Webhook Listener & Live Event Feed

This project receives GitHub webhook events (Push, Pull Request, Merge), stores them in MongoDB Atlas, and displays them in a live-updating frontend using Flask.

---

## 🚀 Features

- ✅ Listens to webhooks from `action-repo`
- ✅ Supports Push, Pull Request, and Merge events
- ✅ Parses and stores data in MongoDB Atlas
- ✅ Frontend polls `/events` every 15 seconds
- ✅ Clean card-based UI with emojis and colored tags
- ✅ 🌙 Dark mode toggle

---

## 🛠️ Tech Stack

- Python (Flask)
- MongoDB Atlas
- HTML, CSS, JavaScript
- ngrok (for webhook testing)
- GitHub Webhooks

---

## 📂 Folder Structure

```

webhook-repo/
├── app.py                # Flask app
├── db.py                 # MongoDB connection
├── models.py             # Webhook event parser
├── templates/
│   └── index.html        # Frontend UI
├── static/
│   └── style.css         # Optional styling
├── .env                  # MongoDB URI (ignored)
├── .gitignore
├── requirements.txt
├── README.md

````

---

## 🔧 Setup Instructions

### 1. Clone and install dependencies

```bash
git clone https://github.com/Anmol18125/webhook-repo.git
cd webhook-repo
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
````

### 2. Add `.env` file

```
MONGO_URI=mongodb+srv://<your-atlas-uri>
```

> Do **NOT** commit `.env` (it's ignored by `.gitignore`)

---

## 🚦 Run the App

### 1. Start Flask

```bash
python app.py
```

### 2. Start ngrok in another terminal

```bash
ngrok http 5000
```

Copy the HTTPS URL from ngrok (e.g., `https://abcd1234.ngrok-free.app`)

---

## 🔗 Add Webhook to GitHub (`action-repo`)

* Payload URL: `https://<your-ngrok>.ngrok-free.app/webhook`
* Content type: `application/json`
* Events: `Push` and `Pull Request`

---

## 💻 Live Frontend

Visit: [http://localhost:5000](http://localhost:5000)

### Shows:

* ⬆️ Pushes
* 📥 Pull Requests
* 🔀 Merges

With auto-refresh every 15 seconds and dark mode toggle 🌙

---

## 📦 Dependencies

```txt
Flask
pymongo
flask-cors
python-dotenv
gunicorn
```

---

## 📎 Related Repo

* [`action-repo`](https://github.com/Anmol18125/action-repo) – Source of GitHub webhook events

---

## 👤 Author

**Anmol Rai**
Built as part of a Developer Assessment Task 💼

````

---

### ✅ Next Step:
1. Save this as `README.md`
2. Run:
```bash
git add README.md
git commit -m "📘 Added README with setup, UI, and features"
git push origin main
````

And you're done, boss. 💪

