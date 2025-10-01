# video_processor.py
import cv2
from src.utils import draw_boxes

class VideoProcessor:
    def __init__(self, detector, input_path, output_path):
        self.detector = detector
        self.input_path = input_path
        self.output_path = output_path

    def process_video(self):
        cap = cv2.VideoCapture(self.input_path)

        if not cap.isOpened():
            print("❌ Error: Could not open video.")
            return

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(
            self.output_path, fourcc, int(cap.get(cv2.CAP_PROP_FPS)),
            (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
             int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        )

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            detections = self.detector.detect_objects(frame)
            frame = draw_boxes(frame, detections)

            out.write(frame)
            cv2.imshow("Object Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        print(f"✅ Processed video saved at {self.output_path}")
