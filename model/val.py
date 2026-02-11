import os
import sys

ultralytics_path = os.path.abspath(os.path.join(os.getcwd(), "ultralytics"))
sys.path.insert(0, ultralytics_path)

from ultralytics.models.yolo import YOLO

model_dir = "train"

model = YOLO(f"runs/{model_dir}/weights/best.pt")

metrics = model.val(data="data.yaml", split="test", project="runs", name=f"val_{model_dir}")

with open(f"runs/val_{model_dir}/val.txt", "w") as f:
    print(metrics, file=f)
