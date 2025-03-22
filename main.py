from datetime import datetime
from app.audio_capture import capture_audio
from app.noise_reduction import reduce_noise
from app.detection.keyword_detection import keyword_detection
from app.alerts.alert_system import send_alert
from app.alerts.logger import log_event

def main():
    audio_file = 'assets/samples/audio_sample.wav'
    cleaned_file = 'assets/samples/cleaned_audio.wav'

    try:
        while True:
            # Step 1: Capture Audio
            capture_audio(audio_file, duration=None)  # Set duration to None for continuous recording

            # Step 2: Reduce Noise
            reduce_noise(audio_file, cleaned_file)

            # Step 3: Keyword Detection
            keywords = ['help', 'answer', 'cheat', 'copy', 'whisper', 'phone', 'google', 'search', 'browser', 'text', 'message', 'call', 'assist', 'solution', 'hint']
            if keyword_detection(cleaned_file, keywords):
                event = "Suspicious Keyword Detected"
                timestamp = datetime.now()
                
                # Step 4: Send Alert
                send_alert(event, timestamp)

                # Step 5: Log Event
                log_event(event, timestamp)

            # Check for user input to stop recording
            stop = input("Press 'q' to stop recording or any other key to continue: ")
            if stop.lower() == 'q':
                break

    except KeyboardInterrupt:
        print("Recording stopped by user.")

if __name__ == "__main__":
    main()