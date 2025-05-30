# train_yolov8.py

from ultralytics import YOLO

# Path to your dataset YAML file
dataset_yaml = "data.yaml"  # 👈 update this path if needed

# Choose a model variant: yolov8n.pt, yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt
model = YOLO("yolov8n.pt")  # Using YOLOv8 Nano for speed

# Train the model
model.train(
    data=dataset_yaml,
    epochs=50,
    imgsz=1080,
    batch=4,
    project="yolov8_custom_train",
    name="exp",
    device=""  # set to "cpu" if you don't have GPU
)
