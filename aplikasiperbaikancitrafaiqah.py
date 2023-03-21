import tkinter as tk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

class LabelCreator:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.creator_label = tk.Label(self.frame, text="Dibuat oleh Faiqah Ferarista Hamu-F55121112-TI C")
        self.creator_label.pack(side=tk.BOTTOM, padx=20, pady=20 )

    def create_label(self):
        new_label = tk.Label(self.master, text=self.label_text.get())
        new_label.pack()

class ImageEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Perbaikan Citra Faiqah")
        self.frame1 = tk.Frame(self.master)
        self.frame1.pack(side=tk.LEFT)
        self.frame2 = tk.Frame(self.master)
        self.frame2.pack(side=tk.LEFT)

        self.original_image = Image.open("fotofaiqah.jpg")
        self.edited_image = self.original_image.copy()
        self.display_image = ImageTk.PhotoImage(self.original_image)

        self.image_label = tk.Label(self.frame1, image=self.display_image)
        self.image_label.pack()

        self.control_frame = tk.LabelFrame(self.frame2, text="Kontrol Pengeditan")
        self.control_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.contrast_label = tk.Label(self.control_frame, text="Kontras")
        self.contrast_label.pack()
        self.contrast_slider = tk.Scale(self.control_frame, from_=0.0, to=2.0, resolution=0.1, orient=tk.HORIZONTAL,
                                        command=self.update_contrast)
        self.contrast_slider.set(1.0)
        self.contrast_slider.pack()

        self.blur_label = tk.Label(self.control_frame, text="Blur")
        self.blur_label.pack()
        self.blur_slider = tk.Scale(self.control_frame, from_=0, to=20, resolution=1, orient=tk.HORIZONTAL,
                                    command=self.update_blur)
        self.blur_slider.set(0)
        self.blur_slider.pack()

        self.reset_button = tk.Button(self.control_frame, text="Reset", command=self.reset_image)
        self.reset_button.pack()

    def update_contrast(self, value):
        contrast_value = float(value)
        contrast = ImageEnhance.Contrast(self.original_image)
        self.edited_image = contrast.enhance(contrast_value)
        self.update_image()

    def update_blur(self, value):
        blur_value = int(value)
        if blur_value > 0:
            self.edited_image = self.original_image.filter(ImageFilter.GaussianBlur(blur_value))
        else:
            self.edited_image = self.original_image.copy()
        self.update_image()

    def update_image(self):
        self.display_image = ImageTk.PhotoImage(self.edited_image)
        self.image_label.configure(image=self.display_image)

    def reset_image(self):
        self.edited_image = self.original_image.copy()
        self.update_image()


root = tk.Tk()
app = ImageEditor(root)
app = LabelCreator(root)
root.mainloop()
