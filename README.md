
---

# Hand Gesture Filter Control with Real-Time Visual Effects & Image Filter Application

This repository contains two interactive applications that apply real-time visual effects using **OpenCV** and **Mediapipe** for hand gesture recognition. Users can control the application either by using hand gestures (for the Hand Gesture Filter Control) or by selecting filters from a dropdown menu (for the Image Filter Application). Both projects provide a dynamic user experience where filters are applied in real-time on webcam video feeds.

## 1. Hand Gesture Filter Control with Real-Time Visual Effects

This application uses **Mediapipe** to track hand gestures, enabling control over real-time video filters with gestures like pinches or finger touches. **OpenCV** is used for applying various visual effects to the webcam feed, and users can cycle through different filters using simple hand movements.

### Features:
- **Hand Gesture Recognition:** Detects gestures like pinches and finger touches to trigger real-time filter changes.
- **Multiple Filters:** Includes a collection of filters (e.g., Grayscale, Edge Detection, Colormap Effects, Blur, and more).
- **Gesture-Controlled Filter Cycling:** Filter changes occur on detecting a pinch gesture, with a delay to avoid rapid switching.
- **Interactive Feedback:** The active filter is displayed on the live video feed.
- **Real-Time Video Processing:** Webcam input is processed in real-time using **OpenCV**.

### Supported Filters:
- Grayscale
- Canny Edge Detection
- Gaussian Blur
- Colormap Effects (Jet, Ocean, Pink, Winter, Cool)
- Bilateral Filter
- Median Blur
- Laplacian Edge Detection
- Sobel Edge Detection
- Noise Reduction (Optional)
- And more...

### Use Cases:
- **Interactive Art Creation:** Create dynamic art with hand gestures.
- **Live Streaming:** Apply filters to a live video stream for an engaging viewer experience.
- **Gesture-Controlled Interfaces:** Use hand gestures to control applications or games.
- **Fitness or Wellness Apps:** Track movements during workouts with customized filters.

---

## 2. Image Filter Application with Real-Time Webcam Feed

This application provides a GUI for applying various image filters to a live webcam feed. It uses **OpenCV** to process video frames and **Tkinter** to display the webcam feed and filter options. Users can select filters from a dropdown and control the webcam feed using buttons for real-time effects.

### Features:
- **Webcam Feed with Filters:** Real-time video processing using **OpenCV** to apply filters to a webcam feed.
- **Multiple Filters:** A variety of filters, including edge detection, sepia tone, emboss, noise reduction, and thresholding.
- **Filter Selection:** Users can choose a filter from a dropdown menu and view its description.
- **Filter Navigation:** Users can cycle through filters using **Next** and **Back** buttons.
- **Interactive GUI:** Built with **Tkinter**, featuring buttons to start/stop the webcam and display filter information.

### Supported Filters:
- Laplacian Edge Detection
- Sobel Edge Detection
- Scharr Filter
- Black-and-White Silhouette
- Noise Reduction
- Sepia Tone
- Emboss Effect
- Adaptive Threshold
- Otsu Threshold
- And more...

### Use Cases:
- **Webcam Effects:** Apply filters to a live webcam feed for entertainment, streaming, or tutorials.
- **Image Processing Education:** Demonstrates various computer vision techniques like edge detection and noise reduction.
- **Creative Art Effects:** Apply artistic effects for a unique visual experience.

---

## Requirements:
For both applications, you need the following dependencies:

- **Python 3.x**
- **OpenCV**
- **Mediapipe** (for Hand Gesture Filter Control)
- **Tkinter** (pre-installed with Python)
- **Pillow (PIL)**
- **NumPy**

You can install the required dependencies using the following command:

```bash
pip install opencv-python mediapipe numpy pillow
```

---

## Installation Instructions:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/hand-gesture-filters.git
   ```

2. **Install dependencies:**

   Install all dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   - For **Hand Gesture Filter Control**, run the following command:
   
     ```bash
     python main.py
     ```

   - For **Image Filter Application**, run this command:
   
     ```bash
     python filter.py
     ```

---

## Contributions:
Feel free to contribute to this project! You can:
- Create pull requests to add more filters or features.
- Report bugs or issues.
- Suggest new features to improve the application.

---

## Acknowledgments:
- **OpenCV**: For providing powerful computer vision tools.
- **Mediapipe**: For efficient hand gesture recognition.
- **Tkinter**: For building the graphical user interface.

---

This repository aims to demonstrate the power of computer vision and interactive user interfaces in creating engaging and dynamic applications. Enjoy experimenting with the filters and hand gestures!

---

This **README** provides an overview of both applications, installation instructions, and features for the users to easily navigate and use the respective projects.
