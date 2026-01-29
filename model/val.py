import os
from pathlib import Path
from ultralytics.models.yolo import YOLO

model = YOLO(f"runs/detect/train/weights/best.pt")

metrics = model.val(data="data.yaml", split="test")

with open(f"runs/detect/test.txt", "w") as f:
    print(metrics, file=f)
