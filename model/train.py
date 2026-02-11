import os
import sys

ultralytics_path = os.path.abspath(os.path.join(os.getcwd(), "ultralytics"))
sys.path.insert(0, ultralytics_path)

from ultralytics.models.yolo import YOLO

epochs = 200

model = YOLO("yolov8s.pt")

model.train(data="data.yaml", epochs=epochs, imgsz=640, mosaic=0.0, patience=0, workers=8, project="runs", name="train")
