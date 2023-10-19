import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image,ImageTk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
import random
import string
from main import ListeningLoop

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def update_image():
    assigned_name = get_random_string(5)
    ListeningLoop(assigned_name)
    img_path = ""
    img = Image.open(r"D:\Scripts\ToastmastersProject\Images\fnftt.png")
    for i in ["jpg", "png", 'jpeg']:
        try:
            img_path = f"D:\Scripts\ToastmastersProject\Images\{assigned_name}.{i}"
            img = Image.open(img_path)
            img = mpimg.imread(img_path)
        except:
            print("Not succsesful!")
        img = img.resize((1920, 1080))
        imgplot.set_data(img)
        canvas.draw()

# Create the main window
root = tk.Tk()
root.title("Image Viewer")
root.geometry("1920x1080")

# Create a Matplotlib figure
fig, ax = plt.subplots()
img = mpimg.imread(r"D:\Scripts\ToastmastersProject\Images\fnftt.png")


imgplot = ax.imshow(img)
ax.axis('off')  # Remove axis labels and ticks

# Create a Tkinter canvas to display the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Create a button to trigger image updates
update_button = tk.Button(root, text="Update Image", command=update_image)
update_button.pack()

# Start a periodic image update

root.mainloop()

while True:
    update_image()
    time.sleep(10)  # Update every 10 seconds


# Start the main loop

