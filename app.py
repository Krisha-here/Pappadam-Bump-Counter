from flask import Flask, request, jsonify, send_file, render_template
import cv2
import numpy as np
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/papadam.html')
def papadam_page():
    return open("papadam.html").read()

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    image_path = 'static/uploaded.jpg'
    file.save(image_path)

    # Read image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 3)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_img = img.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 1)

    # Save all images
    cv2.imwrite("static/original.jpg", img)
    cv2.imwrite("static/threshold.jpg", thresh)
    cv2.imwrite("static/contours.jpg", contour_img)

    return jsonify({
        "count": len(contours),
        "original": "/static/original.jpg",
        "threshold": "/static/threshold.jpg",
        "contours": "/static/contours.jpg"
    })

if __name__ == '__main__':
    app.run(debug=True)