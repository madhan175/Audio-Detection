from datetime import datetime
from app.audio_capture import capture_audio
from app.noise_reduction import reduce_noise
from app.detection.keyword_detection import keyword_detection
from app.alerts.alert_system import send_alert
from app.alerts.logger import log_event

def main():
    audio_file = 'assets/samples/audio_sample.wav'
    cleaned_file = 'assets/samples/cleaned_audio.wav'

    capture_audio(audio_file, duration=10)

    reduce_noise(audio_file, cleaned_file)

    keywords = ['help', 'answer', 'cheat']
    if keyword_detection(cleaned_file, keywords):
        event = "Suspicious Keyword Detected"
        timestamp = datetime.now()
        
        send_alert(event, timestamp)

        log_event(event, timestamp)

if __name__ == "__main__":
    main()
