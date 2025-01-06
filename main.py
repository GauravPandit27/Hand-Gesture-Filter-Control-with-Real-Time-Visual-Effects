import cv2
import mediapipe as mp
import numpy as np
import time  # For adding delay

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# List of filters with their names (removed the DFT filter)
filters = [
    ("Grayscale", lambda frame: cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)),  # Grayscale
    ("Edge Detection", lambda frame: cv2.Canny(frame, 100, 200)),  # Edge Detection
    ("Gaussian Blur", lambda frame: cv2.GaussianBlur(frame, (15, 15), 0)),  # Gaussian Blur
    ("Jet Colormap", lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_JET)),  # Colormap
    ("Ocean Colormap", lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_OCEAN)),  # Ocean Colormap
    ("Pink Colormap", lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_PINK)),  # Pink Colormap
    ("Bilateral Filter", lambda frame: cv2.bilateralFilter(frame, 9, 75, 75)),  # Bilateral Filter
    ("Median Blur", lambda frame: cv2.medianBlur(frame, 15)),  # Median Blur
    ("Laplacian Edge Detection", lambda frame: cv2.Laplacian(frame, cv2.CV_64F).astype(np.uint8)),  # Laplacian Edge Detection
    ("Invert Colors", lambda frame: cv2.bitwise_not(frame)),  # Invert Colors
    ("Sobel Edge Detection", lambda frame: cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=3)),  # Sobel Edge Detection
    ("Scharr Filter", lambda frame: cv2.Scharr(frame, cv2.CV_64F, 1, 0)),  # Scharr Filter (Edge Detection)
    ("Resize Half", lambda frame: cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2))),  # Resize to half
    ("Affine Transformation", lambda frame: cv2.warpAffine(frame, np.float32([[1, 0, 100], [0, 1, 50]]), (frame.shape[1], frame.shape[0]))),  # Affine transformation (translation)
    ("Erosion", lambda frame: cv2.erode(frame, None, iterations=1)),  # Erosion
    ("Dilation", lambda frame: cv2.dilate(frame, None, iterations=1)),  # Dilation
    ("Winter Colormap", lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_WINTER)),  # Winter Colormap
    ("Cool Colormap", lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_COOL)),  # Cool Colormap
    ("Black-and-White Silhouette", lambda frame: cv2.inRange(frame, (0, 0, 0), (100, 100, 100))),  # Black-and-white Silhouette effect
    ("Contrast Enhancement", lambda frame: cv2.convertScaleAbs(frame, alpha=1.5, beta=0)),  # Contrast enhancement
    ("CLAHE", lambda frame: cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))),  # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    #("Noise Reduction", lambda frame: cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)),  # Non-Local Means Denoising
]

# Helper function to calculate Euclidean distance
def euclidean_distance(pt1, pt2):
    return np.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Video capture
cap = cv2.VideoCapture(0)
current_filter_idx = 0
applied_filters = set()
last_pinch_time = 0  # Track the last pinch time
filter_change_delay = 1  # Delay of 1 second for changing filters after pinch

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame with Mediapipe
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            #mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get index, thumb, and middle finger tip coordinates
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            middle_x, middle_y = int(middle_tip.x * w), int(middle_tip.y * h)

            # Detect pinch gesture (index finger and thumb)
            pinch_distance = euclidean_distance((index_x, index_y), (thumb_x, thumb_y))
            if pinch_distance < 30:  # Pinch detected
                current_time = time.time()
                if current_time - last_pinch_time >= filter_change_delay:  # Only change filter after delay
                    # Ensure that the filter doesn't repeat until all filters are applied
                    while current_filter_idx in applied_filters:
                        current_filter_idx = (current_filter_idx + 1) % len(filters)
                    applied_filters.add(current_filter_idx)
                    last_pinch_time = current_time  # Update last pinch time

            # Detect index-middle finger touch gesture
            middle_distance = euclidean_distance((index_x, index_y), (middle_x, middle_y))
            if middle_distance < 30:  # Reset filter set if all are applied
                if len(applied_filters) == len(filters):
                    applied_filters.clear()

            # Apply the filter
            filter_name, filter_func = filters[current_filter_idx]
            frame = filter_func(frame)

            # Ensure the image has 3 channels before showing it
            if len(frame.shape) == 2:  # If grayscale
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
            elif len(frame.shape) == 3 and frame.shape[2] == 4:  # If there are 4 channels (e.g., BGRA)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  # Convert to 3 channels

            # Show the name of the filter on the image
            cv2.putText(frame, filter_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the frame
    cv2.imshow("Hand Gesture Filters", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

