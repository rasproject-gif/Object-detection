🎥 Object Detection in Video (YOLOv8 + OpenCV)
📌 Overview

This project is all about making machines see things in videos 👀.
We use YOLOv8 (a state-of-the-art deep learning model) + OpenCV (for handling video frames) to detect a specific object (like person, car, dog, etc.) in a video.

The program goes through each frame of the video, runs object detection, draws bounding boxes around the chosen object, and finally saves the processed video with annotations. You can also view the detections in real-time while the video plays.

Think of it like:

🎯 Want to find all the people in a CCTV feed?

🚗 Want to count only cars in a traffic video?

🐕 Or just detect your dog running around in a garden clip?

This project is a great starting point!

✨ Features

✅ Detect only the object you care about (configurable).

✅ Works on video files (MP4, AVI, etc.) and easily extendable to webcam live-stream.

✅ Saves the output video with bounding boxes + labels.

✅ Modular & clean code structure (easy to customize).

✅ Based on YOLOv8, one of the fastest & most accurate object detection models.


🚀 Project Structure

object-detection-video/
│
├── data/                     # Store input/output data
│   ├── videos/               # Input videos
│   │   └── sample.mp4
│   └── images/               # For optional single image tests
│
├── outputs/                  # Output files (processed videos, logs, etc.)
│   ├── processed_videos/
│   └── logs/
│
├── models/                   # YOLO model weights
│   └── yolov8n.pt
│
├── src/                      # Core project source code
│   ├── config.py             # Configuration (paths, thresholds, target object)
│   ├── detector.py           # Handles YOLO inference
│   ├── utils.py              # Helper functions (drawing boxes, FPS, etc.)
│   └── video_processor.py    # Frame-by-frame video processing
│
├── notebooks/                # Jupyter notebooks for experiments
│   └── object_detection_demo.ipynb
│
├── requirements.txt          # Python dependencies
├── README.md                 # Project guide (you’re here!)
└── main.py                   # Entry point to run detection
