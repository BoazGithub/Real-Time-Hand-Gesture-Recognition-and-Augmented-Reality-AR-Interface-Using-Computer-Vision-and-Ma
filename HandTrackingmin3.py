import cv2
import mediapipe as mp

# Initialize video capture (use the correct camera index for your system)
cap = cv2.VideoCapture(1)  # Try 0 or 1 depending on your camera

# Set frame size
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Initialize MediaPipe Hands with confidence thresholds
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()

    if not success:
        print("Error: Failed to capture image")
        break

    # Convert the BGR image to RGB for MediaPipe processing
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # Check if hand landmarks are detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Draw landmarks and hand connections on the image
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            # Optional: Print landmark coordinates to debug
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(f'ID: {id}, X: {cx}, Y: {cy}')

    # Display the image with hand landmarks
    cv2.imshow('Image', img)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
