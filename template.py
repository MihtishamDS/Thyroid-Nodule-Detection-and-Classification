import os

folders = [
    "notebooks",
    "templates",
    "static",
    "model"
]

files = [
    "app.py",
    "requirements.txt",
    "README.md",
    ".gitignore"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "a").close()

print("Project structure created successfully!")