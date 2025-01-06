
---

# Hand Gesture Filter Control with Real-Time Visual Effects

This project enables interactive control of real-time video filters using hand gestures. Using **Mediapipe** for hand tracking and **OpenCV** for applying a variety of visual filters, users can trigger filter changes with simple gestures like pinches or finger touches. It creates a dynamic and interactive user experience, where gestures are used to cycle through different visual effects on a live video stream.

## Features:
- **Hand Gesture Recognition:** Detects gestures such as pinches and finger touches using **Mediapipe** to apply real-time filters.
- **Multiple Filters:** A collection of filters (e.g., Grayscale, Edge Detection, Colormap Effects, Blur, and more) that can be applied to live video streams.
- **Filter Cycling:** Filter changes occur on detecting a pinch gesture, with a delay to prevent rapid switching.
- **Interactive Feedback:** Display the name of the active filter on the live video feed.
- **Real-Time Video Processing:** Works with webcam input, processing frames in real-time using **OpenCV**.

## Supported Filters:
- Grayscale
- Edge Detection (Canny)
- Gaussian Blur
- Colormap Effects (Jet, Ocean, Pink, Winter, Cool)
- Bilateral Filter
- Median Blur
- Laplacian Edge Detection
- Sobel Edge Detection
- Noise Reduction (Optional)
- And more...

## Use Cases:
- **Interactive Art Creation:** Create dynamic art with hand gestures.
- **Live Streaming:** Apply different filters on a live video stream in real-time for an engaging viewer experience.
- **Gesture-Controlled Interfaces:** Control applications or games using hand gestures.
- **Fitness or Wellness Apps:** Track movements or gestures during workouts while applying filters for a personalized experience.

## Requirements:
- Python 3.x
- OpenCV
- Mediapipe
- Numpy

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hand-gesture-filters.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Contributions:
Feel free to contribute to this project by creating pull requests, reporting issues, or suggesting new features. Your contributions will help improve the project and add more filters or functionalities.



---
