from flask import Flask, render_template, request, send_file, redirect, flash
import re
from io import BytesIO
import webbrowser
import threading
import os
from pathlib import Path
import sys

app = Flask(__name__)
app.secret_key = "secret"

def resource_path(relative_path):
    """ Get absolute path to resource (works for dev and for PyInstaller) """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def create_app():
    # Set template and static folder paths properly
    template_folder = resource_path("app/templates")

    app = Flask(__name__, template_folder=template_folder)
    app.secret_key = "secret"

    from .routes import main
    app.register_blueprint(main)

    return app

# Extract emails using regex
def extract_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

# Separate emails into unique and duplicates
def separate_emails(email_list):
    seen = set()
    duplicates = set()
    for email in email_list:
        if email in seen:
            duplicates.add(email)
        else:
            seen.add(email)
    return sorted(seen), sorted(duplicates)

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('email_file')
        if not file:
            flash("Please upload a file", "warning")
            return redirect('/')

        content = file.read().decode('utf-8', errors='ignore')
        emails = extract_emails(content)

        if not emails:
            flash("No emails found in the file.", "info")
            return redirect('/')

        selected_domains = request.form.getlist('domains')
        if selected_domains:
            filtered = [e for e in emails if any(e.lower().endswith("@" + d.lower()) for d in selected_domains)]
        else:
            filtered = emails

        unique, duplicate = separate_emails(filtered)

        return render_template('index.html',
                               unique_emails=unique,
                               duplicate_emails=duplicate,
                               total=len(filtered),
                               selected_domains=selected_domains)

    return render_template('index.html')

# Download route
@app.route('/download/<which>', methods=['POST'])
def download_emails(which):
    data = request.form.get('emails', '').strip()

    # Prevent downloading if data is empty or contains placeholder
    if not data or data.startswith("✅ No duplicates found!"):
        flash(f"No {which} emails to download.", "warning")
        return redirect('/')

    buffer = BytesIO()
    buffer.write(data.encode('utf-8'))
    buffer.seek(0)

    filename = f"{which}_emails.txt"
    return send_file(buffer, as_attachment=True, download_name=filename, mimetype='text/plain')

# Auto open browser
# def open_browser():
    # webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    # threading.Timer(1, open_browser).start()
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=10000)

# MIT License
# Copyright (c) 2025 Ari R

"""
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction..."""
