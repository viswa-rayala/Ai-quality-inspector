# VisionGuard AI

VisionGuard AI is an AI-powered product quality inspection dashboard designed for defect detection and automated pass/fail assessment of manufactured products. The project uses a YOLO-based model and a Streamlit interface to display inspection results, confidence levels, and historical data.

## Project Overview

This prototype is built for quality monitoring in manufacturing and MSME-level production lines. It helps identify visual defects, categorize product condition, and present results through a clean dashboard.

## Key Features

- AI-powered defect detection using YOLO
- PASS / FAIL classification
- Real-time dashboard with inspection metrics
- Confidence score display
- Product inspection history in CSV format
- Visual output for prediction and result images
- Simple web UI built with Streamlit

## Project Structure

```text
Ai-quality-inspector/
├── app.py                 # Basic Streamlit inspection screen
├── dashboard.py           # Main AI dashboard with analytics and status cards
├── detect.py              # YOLO model inference script
├── inspection.csv         # Inspection history data
├── result.json            # Latest inspection result
├── result.jpg             # Latest processed image result
├── prediction.jpg         # Prediction preview image
├── test_images/           # Sample images used for detection
├── visionguard_model.pt   # Trained YOLO model
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

## Tech Stack

- Python
- Streamlit
- OpenCV
- Ultralytics YOLO
- Pandas
- Matplotlib
- Pillow

## Setup

1. Clone the repository
2. Open the project folder
3. Create a virtual environment and install dependencies:

```bash
cd Ai-quality-inspector
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install streamlit pandas matplotlib pillow ultralytics
```

## Run the Application

Start the dashboard with:

```bash
cd Ai-quality-inspector
. .venv/bin/activate
python -m streamlit run dashboard.py
```

Then open the local URL shown by Streamlit, typically:

```text
http://localhost:8501
```

## Verified Status

The project was run successfully in a virtual environment and the Streamlit app launched successfully on:

```text
http://localhost:8501
```

This confirms the dashboard is operational in the current environment.

## Notes

- The app reads data from `result.json`, `inspection.csv`, and `result.jpg` when available.
- `detect.py` loads the YOLO model and runs inference on the `test_images` folder.
- The model file `visionguard_model.pt` is required for prediction-based workflows.
- The project is a working prototype and suitable for demo or hackathon deployment.

## Example Use Case

The system can be used to inspect products visually, detect defects, and provide a quick summary for operators or quality assurance personnel.
