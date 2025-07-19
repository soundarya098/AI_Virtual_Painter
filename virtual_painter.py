import cv2
import mediapipe as mp
import numpy as np
import datetime
import pyttsx3

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Drawing canvas
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# Brush color options + eraser + rainbow
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)]  # Last one is Eraser (white)
color_names = ['Blue', 'Green', 'Red', 'Eraser']
selected_color_index = 0
color = colors[selected_color_index]
rainbow_mode = False
speak_color = True
last_spoken_color = ""

# For brush tracking
prev_x, prev_y = 0, 0
frame_count = 0

# Get pixel coordinates from landmarks
def get_position(hand_landmarks, index):
    h, w = 480, 640
    return int(hand_landmarks.landmark[index].x * w), int(hand_landmarks.landmark[index].y * h)

# Speak function
def speak(text):
    global last_spoken_color
    if text != last_spoken_color:
        engine.say(text)
        engine.runAndWait()
        last_spoken_color = text

# Rainbow brush generator
def get_rainbow_color(step):
    step = step % 180
    hsv = np.uint8([[[step, 255, 255]]])
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return tuple(int(x) for x in bgr[0][0])

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    frame_count += 1

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            index_finger = get_position(handLms, 8)
            thumb = get_position(handLms, 4)
            x, y = index_finger

            # Color selection buttons
            if y < 100:
                selected_color_index = x // 100
                selected_color_index = min(selected_color_index, len(colors) - 1)
                color = colors[selected_color_index]
                rainbow_mode = False
                speak(color_names[selected_color_index])
                prev_x, prev_y = 0, 0
                continue

            # Activate rainbow mode if pinky finger and index finger far apart (just for fun)
            pinky = get_position(handLms, 20)
            if abs(index_finger[0] - pinky[0]) > 150:
                rainbow_mode = True
                speak("Rainbow Brush")

            # Dynamic brush size
            distance = ((index_finger[0] - thumb[0]) ** 2 + (index_finger[1] - thumb[1]) ** 2) ** 0.5
            brush_size = int(np.clip(distance / 2, 5, 40))

            # Clear screen with pinch gesture
            if abs(index_finger[0] - thumb[0]) < 30 and abs(index_finger[1] - thumb[1]) < 30:
                canvas = np.zeros((480, 640, 3), dtype=np.uint8)
                speak("Canvas cleared")
            else:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = index_finger

                # Rainbow brush color update
                if rainbow_mode:
                    color = get_rainbow_color(frame_count)

                # Draw on canvas
                cv2.line(canvas, (prev_x, prev_y), index_finger, color, brush_size)
                prev_x, prev_y = index_finger

            draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    # Blend canvas with video feed
    frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    # Draw color buttons
    for i, col in enumerate(colors):
        cv2.rectangle(frame, (i * 100, 0), ((i + 1) * 100, 100), col, -1)
        if i == selected_color_index and not rainbow_mode:
            cv2.rectangle(frame, (i * 100, 0), ((i + 1) * 100, 100), (0, 0, 0), 3)
        cv2.putText(frame, color_names[i], (i * 100 + 10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    if rainbow_mode:
        cv2.putText(frame, "🌈 Rainbow Mode", (380, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (150, 0, 255), 2)

    # Show brush size
    cv2.putText(frame, f'Brush: {brush_size}', (450, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    cv2.imshow("AI Virtual Painter - Enhanced", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        filename = f"painting_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(filename, canvas)
        speak("Saved")
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()
input("Press Enter to exit...")
