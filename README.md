# Face Blur with MediaPipe & OpenCV

This project uses **MediaPipe** and **OpenCV** to detect faces in images, videos, or webcam streams and blur them for privacy purposes. It also draws a bounding box around each detected face.

---

## Features
- Detects faces using **MediaPipe Face Detection**.
- Blurs detected faces for anonymization.
- Supports three modes:
  - **image** → process a single image.
  - **video** → process a video file.
  - **webcam** → process live webcam feed.

---

## Requirements
Make sure you have Python 3.x installed, then install dependencies:

```bash
pip install opencv-python mediapipe
