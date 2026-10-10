from ultralytics import YOLO


model  = YOLO("runs/detect/train-14/weights/best.pt")

model.predict(source = "detectionvideo.mp4", save = True, save_txt = True, conf=.2)
