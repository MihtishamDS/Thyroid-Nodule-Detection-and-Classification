from flask import Flask, render_template, request
from ultralytics import YOLO
from werkzeug.utils import secure_filename
import os
import cv2

# ======================
# APP INITIALIZATION
# ======================
app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
PREDICTION_FOLDER = "static/predictions"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PREDICTION_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ======================
# LOAD MODEL
# ======================
model = YOLO("model/best.pt")


# ======================
# CHECK FILE TYPE
# ======================
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ======================
# HOME
# ======================
@app.route("/")
def home():
    return render_template("index.html")


# ======================
# PREDICT
# ======================
@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return "No file part found."

    file = request.files["file"]

    if file.filename == "":
        return "Please select an image."

    if not allowed_file(file.filename):
        return "Only JPG, JPEG and PNG images are allowed."

    filename = secure_filename(file.filename)

    image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    try:
        file.save(image_path)
    except Exception as e:
        return f"Error saving image: {e}"

    # ======================
    # RUN MODEL
    # ======================
    results = model(image_path)
    result = results[0]

    # ======================
    # DEBUG OUTPUT
    # ======================
    print("\n" + "=" * 60)
    print("MODEL NAMES:", model.names)

    if result.boxes is not None and len(result.boxes) > 0:

        for i, box in enumerate(result.boxes):

            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            print(f"Detection {i+1}")
            print("Class ID:", cls_id)
            print("Class Name:", model.names[cls_id])
            print("Confidence:", conf)

    else:
        print("No Detection Found")

    print("=" * 60 + "\n")

    # ======================
    # PREDICTION
    # ======================
    prediction = "Unknown"
    confidence = 0
    description = "No thyroid nodule detected."

    if result.boxes is not None and len(result.boxes) > 0:

        best_box = max(result.boxes, key=lambda b: float(b.conf[0]))

        cls_id = int(best_box.cls[0])
        confidence = float(best_box.conf[0]) * 100

        predicted_class = model.names[cls_id].lower().strip()

        print("Best Prediction:", predicted_class)

        if predicted_class == "benign":
            prediction = "Benign Thyroid Nodule"
            description = (
                "Benign thyroid nodule detected. "
                "This is usually non-cancerous and may only require monitoring."
            )

        elif predicted_class == "malignant":
            prediction = "Malignant Thyroid Nodule"
            description = (
                "Malignant thyroid nodule detected. "
                "Medical consultation is strongly recommended."
            )

        else:
            prediction = predicted_class.capitalize()
            description = "Unknown thyroid nodule class."

    # ======================
    # SAVE RESULT IMAGE
    # ======================
    annotated_image = result.plot()

    prediction_filename = "pred_" + filename

    prediction_path = os.path.join(PREDICTION_FOLDER, prediction_filename)

    cv2.imwrite(prediction_path, annotated_image)

    # ======================
    # SHOW RESULT
    # ======================
    return render_template(
        "index.html",
        uploaded_image=filename,
        prediction_image=prediction_filename,
        prediction=prediction,
        confidence=round(confidence, 2),
        description=description,
    )


# ======================
# RUN
# ======================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)