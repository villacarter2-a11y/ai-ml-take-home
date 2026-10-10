import argparse
import os
from ultralytics import YOLO

#Initialize argument parser for inpiut and output folders
parser = argparse.ArgumentParser(
    description = "Run YOLOv8 inference and export normalized text files"
)

parser.add_argument(
    "input_dir", type= str, help = "Path to the folder containign input images"
)

parser.add_argument(
    "output_dir",
    type = str,
    help = "Path to the folder where txt files will be saved"
)

args = parser.parse_args()

#Load model and set confiddece threshold
model = YOLO("best.pt")
CONF_THRESH = .47 # this number comes from the peak f-1 scores which maximizes accuracy and recall


os.makedirs(args.output_dir, exist_ok=True)

#loop through images and run iterference script
for img_name in os.listdir(args.input_dir):
    if img_name.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(args.input_dir, img_name)
        results = model.predict(img_path, conf = CONF_THRESH, verbose = False)[0]

        txt_name = f"{os.path.splitext(img_name)[0]}.txt"
        txt_path = os.path.join(args.output_dir, txt_name)
        with open(txt_path, "w") as f:
            if results.boxes is not None:
                for box, cls, conf in zip(
                    results.boxes.xywhn, results.boxes.cls, results.boxes.conf

                ):
                    f.write(
                        f"{int(cls)} {box[0]:.6f} {box[1]:.6f} {box[2]:.6f}"
                        f" {box[3]:.6f} {conf:.6f}\n"
                        
                    )

print(f"Inference complete using confidence threshold: {CONF_THRESH}. Results "
      f" saved to {args.output_dir}.")

