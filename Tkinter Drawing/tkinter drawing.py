import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")
        
        self.canvas = tk.Canvas(root, bg="white", width=400, height=400)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.color = "black"
        self.line_width = 2
        self.eraser_size = 10
        self.is_drawing = False
        
        # Create buttons and eraser size slider
        self.color_button = tk.Button(root, text="Choose Color", command=self.choose_color)
        self.color_button.pack(fill=tk.X, padx=10, pady=10)
        
        self.erase_button = tk.Button(root, text="Eraser", command=self.use_eraser)
        self.erase_button.pack(fill=tk.X, padx=10, pady=10)
        
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(fill=tk.X, padx=10, pady=10)
        
        self.color_size_label = tk.Label(root, text="Color Size:")
        self.color_size_label.pack(fill=tk.X, padx=10, pady=10)
        
        self.color_size_slider = tk.Scale(root, from_=2, to=20, orient=tk.HORIZONTAL)
        self.color_size_slider.pack(fill=tk.X, padx=10, pady=10)
        self.color_size_slider.set(self.line_width)  # Default color size
        
        self.eraser_size_label = tk.Label(root, text="Eraser Size:")
        self.eraser_size_label.pack(fill=tk.X, padx=10, pady=10)
        
        self.eraser_size_slider = tk.Scale(root, from_=2, to=20, orient=tk.HORIZONTAL)
        self.eraser_size_slider.pack(fill=tk.X, padx=10, pady=10)
        self.eraser_size_slider.set(self.eraser_size)  # Default eraser size
        
        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color
            self.line_width = self.color_size_slider.get()

    def use_eraser(self):
        self.color = "white"  # Use white color for erasing
        self.eraser_size = self.eraser_size_slider.get()
        self.line_width = self.eraser_size

    def clear_canvas(self):
        self.canvas.delete("all")

    def start_drawing(self, event):
        self.is_drawing = True
        self.prev_x = event.x
        self.prev_y = event.y

    def draw(self, event):
        if self.is_drawing:
            x, y = event.x, event.y
            self.canvas.create_line(self.prev_x, self.prev_y, x, y, fill=self.color, width=self.line_width)
            self.prev_x, self.prev_y = x, y

    def stop_drawing(self, event):
        self.is_drawing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
