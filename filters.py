import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np

# Initialize filter categories with descriptions
filters = {
    "Grayscale": (
        lambda frame: cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),
        "Converts the image to grayscale. This is the most basic image processing technique and is used for simplifying an image into shades of gray.\n"
        "Code: `cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)`"
    ),
    "Edge Detection": (
        lambda frame: cv2.Canny(frame, 100, 200),
        "Highlights edges in the image. It uses the Canny algorithm, which detects sharp intensity contrasts in images.\n"
        "Code: `cv2.Canny(frame, 100, 200)`"
    ),
    "Gaussian Blur": (
        lambda frame: cv2.GaussianBlur(frame, (15, 15), 0),
        "Applies a smoothing effect to reduce noise. Gaussian blur is commonly used for noise reduction and image smoothing.\n"
        "Code: `cv2.GaussianBlur(frame, (15, 15), 0)`"
    ),
    "Median Blur": (
        lambda frame: cv2.medianBlur(frame, 15),
        "Reduces noise using a median filter. The median filter is useful in removing salt-and-pepper noise from an image.\n"
        "Code: `cv2.medianBlur(frame, 15)`"
    ),
    "Bilateral Filter": (
        lambda frame: cv2.bilateralFilter(frame, 9, 75, 75),
        "Preserves edges while reducing noise. Bilateral filter is ideal for noise reduction without blurring edges.\n"
        "Code: `cv2.bilateralFilter(frame, 9, 75, 75)`"
    ),
    "Invert Colors": (
        lambda frame: cv2.bitwise_not(frame),
        "Inverts the colors of the image. This can be used for creating a negative effect or for artistic transformations.\n"
        "Code: `cv2.bitwise_not(frame)`"
    ),
    "Contrast Enhancement": (
        lambda frame: cv2.convertScaleAbs(frame, alpha=1.5, beta=0),
        "Enhances the contrast of the image. This is used to improve visibility in images with low contrast.\n"
        "Code: `cv2.convertScaleAbs(frame, alpha=1.5, beta=0)`"
    ),
    "CLAHE": (
        lambda frame: cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)),
        "Enhances contrast using adaptive histogram equalization. It is useful for improving local contrast in images with varying brightness.\n"
        "Code: `cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))`"
    ),
    "Jet Colormap": (
        lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_JET),
        "Applies a colorful heatmap (Jet colormap) to the image. This is commonly used for visualizing data or highlighting certain regions in the image.\n"
        "Code: `cv2.applyColorMap(frame, cv2.COLORMAP_JET)`"
    ),
    "Ocean Colormap": (
        lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_OCEAN),
        "Applies an ocean-themed heatmap to the image. Ocean colormap is generally used to display images with cooler tones.\n"
        "Code: `cv2.applyColorMap(frame, cv2.COLORMAP_OCEAN)`"
    ),
    "Pink Colormap": (
        lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_PINK),
        "Applies a pink-themed heatmap to the image. This filter gives the image a vibrant, pink color palette.\n"
        "Code: `cv2.applyColorMap(frame, cv2.COLORMAP_PINK)`"
    ),
    "Winter Colormap": (
        lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_WINTER),
        "Applies a winter-themed heatmap. Winter colormap uses cooler shades to enhance images.\n"
        "Code: `cv2.applyColorMap(frame, cv2.COLORMAP_WINTER)`"
    ),
    "Cool Colormap": (
        lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_COOL),
        "Applies a cool-toned heatmap. This filter is perfect for creating visually cool or icy effects.\n"
        "Code: `cv2.applyColorMap(frame, cv2.COLORMAP_COOL)`"
    ),
    "Resize Half": (
        lambda frame: cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2)),
        "Resizes the image to half its size. Useful for reducing the image size for processing or display purposes.\n"
        "Code: `cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2))`"
    ),
    "Affine Transformation": (
        lambda frame: cv2.warpAffine(frame, np.float32([[1, 0, 100], [0, 1, 50]]), (frame.shape[1], frame.shape[0])),
        "Shifts the image position by applying an affine transformation. This transformation involves translation, rotation, and scaling.\n"
        "Code: `cv2.warpAffine(frame, np.float32([[1, 0, 100], [0, 1, 50]]), (frame.shape[1], frame.shape[0]))`"
    ),
    "Erosion": (
        lambda frame: cv2.erode(frame, None, iterations=1),
        "Reduces noise by eroding boundaries. Erosion shrinks bright areas and enlarges dark areas in an image.\n"
        "Code: `cv2.erode(frame, None, iterations=1)`"
    ),
    "Dilation": (
        lambda frame: cv2.dilate(frame, None, iterations=1),
        "Expands boundaries in the image. Dilation is often used to connect broken parts of an object.\n"
        "Code: `cv2.dilate(frame, None, iterations=1)`"
    ),
    "Laplacian Edge Detection": (
        lambda frame: cv2.Laplacian(frame, cv2.CV_64F).astype(np.uint8),
        "Detects edges using the Laplacian method. It computes the second-order derivative of the image to highlight rapid intensity changes.\n"
        "Code: `cv2.Laplacian(frame, cv2.CV_64F).astype(np.uint8)`"
    ),
    "Sobel Edge Detection": (
        lambda frame: cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=3),
        "Detects edges using the Sobel method. Sobel edge detection calculates the first-order derivative along the x or y axis.\n"
        "Code: `cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=3)`"
    ),
    "Scharr Filter": (
        lambda frame: cv2.Scharr(frame, cv2.CV_64F, 1, 0),
        "Detects edges using the Scharr method. Scharr is similar to Sobel but with a more advanced kernel for better edge detection.\n"
        "Code: `cv2.Scharr(frame, cv2.CV_64F, 1, 0)`"
    ),
    "Black-and-White Silhouette": (
        lambda frame: cv2.inRange(frame, (0, 0, 0), (100, 100, 100)),
        "Creates a black-and-white silhouette. This filter isolates dark areas and removes light regions of the image.\n"
        "Code: `cv2.inRange(frame, (0, 0, 0), (100, 100, 100))`"
    ),
    "Noise Reduction": (
        lambda frame: cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21),
        "Reduces noise while preserving details. Non-local means denoising algorithm reduces noise by averaging pixels with similar values.\n"
        "Code: `cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)`"
    ),
    "Sepia Tone": (
        lambda frame: cv2.transform(frame, np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])),
        "Gives the image a sepia tone effect, creating a warm, brownish color. This effect is often used to make images appear older or vintage.\n"
        "Code: `cv2.transform(frame, np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]))`"
    ),
    "Emboss": (
        lambda frame: cv2.filter2D(frame, -1, np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])),
        "Gives the image an embossed effect by using a convolution kernel. The effect highlights edges and gives the image a 3D-like appearance.\n"
        "Code: `cv2.filter2D(frame, -1, np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]))`"
    ),
    "Adaptive Threshold": (
        lambda frame: cv2.adaptiveThreshold(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2),
        "Applies adaptive thresholding to the image, making it effective for images with varying lighting.\n"
        "Code: `cv2.adaptiveThreshold(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)`"
    ),
    "Otsu Threshold": (
        lambda frame: cv2.threshold(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        "Applies Otsu's method to determine an optimal threshold for separating foreground and background in images.\n"
        "Code: `cv2.threshold(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]`"
    ),

}
class FilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Filter App")
        self.root.geometry("1000x800")  # Increased window size
        
        # Webcam Feed
        self.cap = None
        self.running = False
        
        # UI Elements
        self.filter_var = tk.StringVar()
        self.filter_info = tk.StringVar()
        
        ttk.Label(root, text="Select Filter", font=("Arial", 14)).pack(pady=10)
        self.filter_menu = ttk.Combobox(root, textvariable=self.filter_var, font=("Arial", 12))
        self.filter_menu["values"] = list(filters.keys())  # Now this works because filters is a dictionary
        self.filter_menu.bind("<<ComboboxSelected>>", self.update_info)
        self.filter_menu.pack(pady=10)
        
        self.canvas = tk.Canvas(root, width=640, height=480)
        self.canvas.pack(pady=20)
        
        ttk.Label(root, textvariable=self.filter_info, wraplength=800, font=("Arial", 12), justify="left").pack(pady=10)
        
        # Create buttons with horizontal layout (Start, Stop, Next, Back)
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        self.start_button = tk.Button(button_frame, text="Start", command=self.apply_filter, width=20, height=2, font=("Arial", 12))
        self.start_button.grid(row=0, column=0, padx=10)
        
        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_feed, width=20, height=2, font=("Arial", 12))
        self.stop_button.grid(row=0, column=1, padx=10)
        
        self.next_button = tk.Button(button_frame, text="Next", command=self.next_filter, width=20, height=2, font=("Arial", 12))
        self.next_button.grid(row=0, column=2, padx=10)
        
        self.back_button = tk.Button(button_frame, text="Back", command=self.previous_filter, width=20, height=2, font=("Arial", 12))
        self.back_button.grid(row=0, column=3, padx=10)
        
    def update_info(self, event):
        filter_name = self.filter_var.get()
        if filter_name:
            _, info = filters[filter_name]  # Access the filter description and function
            self.filter_info.set(f"{filter_name}: {info}")

    def next_filter(self):
        filters_list = list(filters.keys())
        current_filter = self.filter_var.get()
        if current_filter:
            current_index = filters_list.index(current_filter)
            next_index = (current_index + 1) % len(filters_list)
            self.filter_var.set(filters_list[next_index])
            self.update_info(None)

    def previous_filter(self):
        filters_list = list(filters.keys())
        current_filter = self.filter_var.get()
        if current_filter:
            current_index = filters_list.index(current_filter)
            prev_index = (current_index - 1) % len(filters_list)
            self.filter_var.set(filters_list[prev_index])
            self.update_info(None)

    def apply_filter(self):
        if not self.running:
            self.running = True
            self.cap = cv2.VideoCapture(0)
            self.process_feed()

    def process_feed(self):
        if self.running:
            ret, frame = self.cap.read()
            if not ret:
                return
            frame = cv2.flip(frame, 1)
            
            filter_name = self.filter_var.get()
            if filter_name:
                filter_func, _ = filters[filter_name]
                frame = filter_func(frame)
                
                # Convert float32 or float64 to uint8
                if frame.dtype != np.uint8:
                    frame = cv2.convertScaleAbs(frame)

                # If the frame is grayscale, convert it to BGR for display
                if len(frame.shape) == 2:  # If grayscale, convert to BGR for display
                    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
                
            # Convert frame to ImageTk format
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            self.img_tk = ImageTk.PhotoImage(img)  # Store reference to avoid garbage collection
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)
            
            # Continue processing
            self.root.after(10, self.process_feed)

    def stop_feed(self):
        if self.running:
            self.running = False
            self.cap.release()
            self.canvas.delete("all")
            self.cap = None

# Start Tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    app = FilterApp(root)
    root.mainloop()

