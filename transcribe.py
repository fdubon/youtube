import azure.cognitiveservices.speech as speechsdk
import time

# Set up the Azure Speech configuration
speech_key = "YOURKEY"
service_region = "YOUR REGION"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Set the audio file path
audio_file = "FreddyDubon.wav"

# Set up the audio configuration
audio_config = speechsdk.audio.AudioConfig(filename=audio_file)

# Create a speech recognizer object
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# Create an empty list to store the transcription results
transcriptions = []

# Define an event handler for continuous recognition
def continuous_recognition_handler(evt):
    if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
        transcriptions.append(evt.result.text)

# Start continuous recognition
speech_recognizer.recognized.connect(continuous_recognition_handler)
speech_recognizer.start_continuous_recognition()

# Wait for the recognition to complete
timeout_seconds = 600  # Set a timeout value (in seconds) based on your audio file length
timeout_expiration = time.time() + timeout_seconds

while time.time() < timeout_expiration:
    time.sleep(1)  # Adjust the sleep duration as needed

# Stop continuous recognition
speech_recognizer.stop_continuous_recognition()

# Combine transcriptions into a single string
transcription = ' '.join(transcriptions)

# Write the transcription to a file
output_file = "transcription.txt"
with open(output_file, "w") as file:
    file.write(transcription)

print("Transcription saved to: " + output_file)

