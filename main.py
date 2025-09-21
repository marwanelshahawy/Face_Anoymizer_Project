import cv2
import argparse
import os
import mediapipe as mp

def process_img(img,face_detection):
    H, W, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box
            x1, y1, w, h, = bbox.xmin, bbox.ymin, bbox.width, bbox.height
            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)
            # blur faces
            img[y1:y1 + h, x1:x1 + w:] = cv2.blur(img[y1:y1 + h, x1:x1 + w:], (30, 30))
            img =cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (255, 0, 0), 2)
    else:
        print("No face detected")
    return img
args = argparse.ArgumentParser()
args.add_argument("--mode",default='image')
args.add_argument("--filePath",default=os.path.join(os.getcwd(),'testImg.png'))
args = args.parse_args()

mp_face_detection = mp.solutions.face_detection
with mp_face_detection.FaceDetection(model_selection=0,min_detection_confidence=0.5) as face_detection:
    if args.mode in ['webcam']:
        webcam = cv2.VideoCapture(args.filePath)
        while True:

            ret ,frame = webcam.read()

            frame =process_img(frame,face_detection)
            cv2.imshow('WebCam', frame)
            if cv2.waitKey(25) & 0Xff == ord("q"):
                break
    elif args.mode in ['image']:
        img = cv2.imread(args.filePath)
        img = process_img(img,face_detection)
        cv2.imshow('Image', img)
        cv2.waitKey(0)
    # save image
webcam.release()
cv2.destroyAllWindows()