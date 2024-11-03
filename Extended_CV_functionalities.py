import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
import speech_recognition as sr

# Initialize MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

# Initialize video capture
cap = cv2.VideoCapture(0)  # Change the index if needed

# For real-time data visualization
plt.ion()  # Interactive mode
data_points = []

def process_frame(img):
    """Process each frame for hand detection and recognition."""
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            landmark_positions = [(lm.x, lm.y) for lm in handLms.landmark]
            gesture = gesture_recognition(landmark_positions)
            control_ui(gesture)
            augmented_reality(img, landmark_positions)

    return img

def gesture_recognition(landmarks):
    """Recognize gestures based on landmark positions."""
    # Simple example: Recognize a "swipe" gesture based on wrist movement
    wrist = landmarks[mpHands.HandLandmark.WRIST]
    if wrist.y < 0.2:  # Example threshold for a swipe gesture
        return "swipe_up"
    elif wrist.y > 0.8:
        return "swipe_down"
    return "none"

def augmented_reality(img, landmarks):
    """Overlay AR content based on hand positions."""
    if landmarks:
        h, w, _ = img.shape
        wrist_x, wrist_y = int(landmarks[mpHands.HandLandmark.WRIST].x * w), int(landmarks[mpHands.HandLandmark.WRIST].y * h)
        cv2.circle(img, (wrist_x, wrist_y), 10, (0, 255, 0), -1)  # Draw a green circle at the wrist

def control_ui(gesture):
    """Control UI elements based on recognized gestures."""
    if gesture == "swipe_up":
        print("Perform swipe up action")
    elif gesture == "swipe_down":
        print("Perform swipe down action")

def voice_command_recognition():
    """Recognize voice commands."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for voice command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("Voice command:", command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

def update_visualization(data):
    """Update real-time data visualization."""
    data_points.append(data)
    plt.clf()  # Clear the current figure
    plt.plot(data_points)
    plt.title("Gesture Recognition Data")
    plt.xlabel("Time")
    plt.ylabel("Gesture Value")
    plt.pause(0.01)  # Pause to allow plot to update

def main():
    while True:
        success, img = cap.read()
        if not success:
            print("Error: Failed to capture image")
            break
        
        img = process_frame(img)

        # Simulate data for visualization 
        gesture_value = len(data_points) % 10  # Example: Simulated gesture value
        update_visualization(gesture_value)

        cv2.imshow('Hand Tracking', img)
        
        # Listen for voice commands in the background
        voice_command_recognition()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    plt.close()  # Close the plot

if __name__ == "__main__":
    main()
