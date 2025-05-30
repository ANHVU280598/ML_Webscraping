from ultralytics import YOLO


# Load the trained model
model = YOLO("best.pt")

# Predict on a test image
results = model("scroll_006.png")
results[0].show()  # Show results
