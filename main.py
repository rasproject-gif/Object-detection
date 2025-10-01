# main.py
from src.config import MODEL_PATH, VIDEO_PATH, OUTPUT_PATH, TARGET_CLASS, CONF_THRESHOLD
from src.detector import ObjectDetector
from src.video_processor import VideoProcessor

def main():
    detector = ObjectDetector(MODEL_PATH, TARGET_CLASS, CONF_THRESHOLD)
    processor = VideoProcessor(detector, VIDEO_PATH, OUTPUT_PATH)
    processor.process_video()

if __name__ == "__main__":
    main()
