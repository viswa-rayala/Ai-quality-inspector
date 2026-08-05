from ultralytics import YOLO

# Load the trained model
model = YOLO("visionguard_model.pt")

# Run prediction
results = model.predict(
    source="test_images",
    save=True,
    show=True,
    conf=0.5
)

print("Prediction completed!")
