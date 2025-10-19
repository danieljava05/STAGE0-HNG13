# 🧠 Fact API — FastAPI Project

This is a simple **FastAPI** project that fetches random facts from an external API using `httpx` with timeout handling.  
It’s built with clean architecture — separating routes, schemas, and repository logic — and includes basic logging for debugging.

---

## 🚀 Features

- ✅ Fetch random fact from an external API  
- ⚡ Timeout handling to avoid hanging requests  
- 🧭 Clean project structure (routes, schemas, repository)  
- 🪵 Basic logging added for debugging  
- 🧰 Ready to deploy or run locally

---

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)  
- [Uvicorn](https://www.uvicorn.org/)  
- [HTTPX](https://www.python-httpx.org/)  
- Python 3.10+  
- dotenv (for environment variables)

---

## 📥 Installation & Setup Instructions

### 1️⃣ Clone the Repository

git clone https://github.com/danieljava05/STAGE0-HNG13.git

cd STAGE0-HNG13

---

##Create and Activate a Virtual Environment

python -m venv venv

# On Windows
venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate

---
## move inside the src directory
cd src
## 3️⃣ Install Dependencies
pip install -r requirements.txt

## ⚙️ Environment Variables
###EMAIL=umuafemonidanie@gmail.com
###NAME=OLUWATOSIN DANIEL
###STACK=PYTHON/FASTAPI
###FACT_URL=https://catfact.ninja/fact

##🧾 Requirements File (requirements.txt)
pydantic
httpx
fastapi 
uvicorn
pydantic_settings
slowapi

##🧪 How to Run the Project Locally
### 1️⃣ Start the FastAPI server
uvicorn main:app --reload
### 2️⃣ Open in your browser or Postman
http://127.0.0.1:8000/fact
### ✅ Expected Response:
{
  "fact": "Bananas are berries, but strawberries aren't."
}
##🧭 Project Structure
📂 fact-api
 ┣ 📂 routes
 ┃ ┗ fact_route.py
 ┣ 📂 schemas
 ┃ ┗ fact_schema.py
 ┣ 📂 repository
 ┃ ┗ fact_repository.py
 ┣ 📜 main.py
 ┣ 📜 requirements.txt
 ┣ 📜 README.md
 ┣ 📜 .env 
 ┗ 📜 .gitignore
## 🌍 API Endpoint
| Method | Endpoint | Description           |
| ------ | -------- | --------------------- |
| GET    | `/fact`  | Returns a random fact |
##🪵 Logging
Basic logging is included to help with debugging.
##🧱 Deployment
You can deploy this project to:
### railway
##🧪 Testing the API with Curl
curl http://127.0.0.1:8000/fact
##🛡️ .gitignore Example
venv/
__pycache__/
.env
##🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you would like to change.
##🪪 License
This project is licensed under the MIT License — you are free to use, modify, and distribute.


