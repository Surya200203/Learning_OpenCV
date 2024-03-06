import cv2
import numpy as np

def detect_green_balls(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the green color
    lower_green = np.array([100, 50, 50])
    upper_green = np.array([130, 255, 255])

    # Threshold the frame to get only green pixels
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area to avoid small noise
    min_area = 100
    green_balls = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

    return green_balls

def draw_rectangles(frame, contours):
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Detect green balls
        green_balls = detect_green_balls(frame)

        # Draw rectangles around green balls
        draw_rectangles(frame, green_balls)

        # Display the resulting frame
        cv2.imshow('Green Ball Detection', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    # Release the webcam and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
