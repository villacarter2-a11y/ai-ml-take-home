from ultralytics import YOLO

# creatting and testing a model from a real video feed
model  = YOLO("best.pt")

model.predict(source = "detectionvideo.mp4", save = True, save_txt = True, conf=.2) #use low confidence level to increase detection
