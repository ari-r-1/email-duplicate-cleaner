### ✨ Email Duplicate Cleaner – Smart Web App with Flask

Upload ➜ Extract ➜ Filter ➜ Download — All in Seconds 🚀

Email Duplicate Cleaner is a lightweight, intelligent web app that helps you clean up messy email lists with zero coding required. Whether you’re a marketer, developer, or data wrangler, this tool lets you:

A sleek and powerful web application built using **Flask** that empowers users to:

    - 📤 Upload raw .txt, .csv, .json files containing email lists

    - 🧠 Intelligently extract valid email addresses using advanced regular expressions

    - ♻️ Instantly separate **unique** & **duplicate** entries 

    - 🎯 Filter by domain like `@gmail.com`, `@yahoo.com`, etc.

    - 📥 Download cleaned results as .txt files

    - 💡 Enjoy a smooth, interactive UI with helpful notifications and visual effects

---

## 🚀 Features

| Feature                 | Description                                           |
| ----------------------- | ---------------------------------------------         |
| 📤 **File Upload**      | Drag-and-drop or select `.txt`, `.cvs`, `.json` files|
| 🧮 **Smart Extraction** | Uses regex to extract all valid emails               |
| 🧹 **Auto Filtering**   | Sorts unique and duplicate emails                    |
| 🎯 **Domain Filter**    | Focus on specific domains like Gmail or Yahoo        |
| 📄 **Download Options** | Export filtered emails as plain text                 |
| ✨ **Modern UI**         | Clean interface with helpful flash messages         |


---

## 📁 Project Structure

email-duplicate-cleaner/
│           
├── templates/        → HTML (Jinja2), CSS, JS, animations (Vanta.js, CountUp.js, AOS)
├── uploads/          → Temporary file uploads
├── app.py            → Main Flask application
├── requirements.txt  → Dependency list
├── LICENCE.txt       → Linence File
├── render.yaml       → Configuration File
└── README.md         → This file

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/your-username/email-duplicate-cleaner.git
cd email-duplicate-cleaner
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App
```bash
python email_duplicate_cleaner_flask.py
```

### 4️⃣ Open in Browser  
Visit 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 How It Works (Step-by-Step)

1. Upload a .txt file with email content.

2.  app uses regex to scan for valid emails.

3. Emails are grouped into:

    - ✅ Unique emails

    - ❗ Duplicate emails

4. You can filter by domain using the input box.

5. Click to download the results instantly.

---

## 🛠️ Tech Stack

- 🐍 Python + Flask

- 📜 Regex (for email parsing)

- 🎨 HTML/CSS + JavaScript (AOS, CountUp.js, Vanta.js)

- ☁️ Download-ready .txt exports

---

## 📄 License

This project is licensed under the MIT License. 
Created and maintained by **Ari R**.
Feel free to use, modify, and distribute.

---
