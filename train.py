from ultralytics import YOLO
from multiprocessing import freeze_support

# create model and train using base settings for initialization
def train_model():
    model = YOLO("yolov8n.pt")

    model.train(
        data = "Sampled-YD-Object-Detection-2/data.yaml",
        epochs = 40,
        imgsz = 640,
        hsv_h = .020
     
        
)
    
if __name__ == "__main__":
    freeze_support()
    train_model()




