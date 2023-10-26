```python
import cv2
from backend.ai_engine import analyze_video

class VideoIntegration:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def sync_video_with_data(self, data):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Analyze the video frame using AI engine
            analysis = analyze_video(frame)

            # Sync the analysis with the provided data
            for key in data.keys():
                if key in analysis:
                    data[key].append(analysis[key])

            # Display the resulting frame
            cv2.imshow('Video Analysis', frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def display_video(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Display the resulting frame
            cv2.imshow('Video Analysis', frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
```