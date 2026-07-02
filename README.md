---
title: Thyroid Nodule Detection and Classification
emoji: 🩺
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# 🩺 Thyroid Nodule Detection and Classification using YOLOv8

## 📖 Overview

This project presents an AI-powered web application for detecting and classifying thyroid nodules in ultrasound images using the YOLOv8 object detection model.

The system automatically detects thyroid nodules and classifies them into:

- 🟢 Benign
- 🔴 Malignant

The application is built using Flask and provides a simple, responsive web interface where users can upload thyroid ultrasound images and receive prediction results with confidence scores and detected bounding boxes.

---

# ✨ Features

- Detect thyroid nodules from ultrasound images
- Classify nodules as Benign or Malignant
- Display bounding boxes around detected nodules
- Show prediction confidence score
- Modern and responsive web interface
- Fast inference using YOLOv8
- Easy image upload and prediction

---

# 🧠 Model

**Model:** YOLOv8 Nano (YOLOv8n)

**Framework:**
- Ultralytics YOLOv8

**Training Parameters**

- Epochs: 100
- Image Size: 640 × 640
- Batch Size: 16
- Optimizer: Default YOLO Optimizer
- Early Stopping: Patience = 20

---

# 📂 Dataset

**Dataset:** TN5000 Thyroid Ultrasound Dataset

**Classes**

- Benign
- Malignant

**Dataset Structure**

```
Annotations/
JPEGImages/
ImageSets/
```

The XML annotations were converted into YOLO format before training.

---

# 📊 Model Performance

| Metric | Value |
|---------|---------|
| Accuracy | 90.86% |
| Precision | 90.71% |
| Recall | 90.86% |
| F1 Score | 90.73% |

---

# 💻 Technologies Used

- Python
- Flask
- Ultralytics YOLOv8
- OpenCV
- NumPy
- HTML5
- CSS3
- JavaScript
- Bootstrap
- Scikit-learn

---

# 📁 Project Structure

```
Thyroid-Nodule-Detection-and-Classification/

│── app.py
│── README.md
│── requirements.txt
│── Dockerfile
│── LICENSE
│
├── model/
│   └── best.pt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── index.css
│   ├── js/
│   │   └── index.js
│   ├── uploads/
│   └── predictions/
│
├── notebooks/
├── screenshots/
└── .gitignore
```

---

# 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/MihtishamDS/Thyroid-Nodule-Detection-and-Classification.git
```

### Go to the project folder

```bash
cd Thyroid-Nodule-Detection-and-Classification
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

### Open your browser

```
http://127.0.0.1:5000
```

---

# 📷 Screenshots

## 🏠 Home Page

![Home Page](screenshots/homepage.png)

## 📤 Upload Image

![Upload Image](screenshots/upload.png)

## 🟢 Benign Prediction

![Benign Result](screenshots/benign_result.png)

## 🔴 Malignant Prediction

![Malignant Result](screenshots/malignant_result.png)

---

# 🔮 Future Improvements

- Improve detection accuracy using larger YOLO models
- Train with additional thyroid ultrasound datasets
- Add Grad-CAM visualization for explainable AI
- Develop a mobile-friendly version
- Support real-time ultrasound image analysis
- Deploy on cloud platforms

---

# 👨‍💻 Author

**Muhammad Ihtisham**

BS Computer Science

Government Degree College Lal Qilla Maidan

GitHub:

https://github.com/MihtishamDS

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.