import tkinter as tk
import pyautogui


def on_mouse_down(event):
    global x1, y1
    x1, y1 = event.x, event.y

def on_mouse_up(event):
    global x2, y2
    x2, y2 = event.x, event.y
    root.destroy()

def take_screenshot(left, top, width, height):
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.crop((left, top, left+width, top+height))
    screenshot.save('screenshot.png')

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='#808080')

canvas = tk.Canvas(root, bg='', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind('<Button-1>', on_mouse_down)
canvas.bind('<ButtonRelease-1>', on_mouse_up)

root.mainloop()

if x1 < x2:
    left, width = x1, x2 - x1
else:
    left, width = x2, x1 - x2

if y1 < y2:
    top, height = y1, y2 - y1
else:
    top, height = y2, y1 - y2

screenshot = pyautogui.screenshot()
screenshot = screenshot.crop((left, top, left+width, top+height))

mask = tk.Toplevel()
mask.attributes('-fullscreen', True)
mask.overrideredirect(True)
mask.configure(bg='#808080')
mask.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0')

canvas = tk.Canvas(mask, bg='', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

canvas.create_rectangle(0, 0, root.winfo_screenwidth(), root.winfo_screenheight(), fill='#808080')

canvas.create_rectangle(left, top, left+width, top+height, outline='white', width=2)

screenshot_image = tk.PhotoImage(data=screenshot.tobytes())
canvas.create_image(left, top, anchor='nw', image=screenshot_image)

take_screenshot(left, top, width, height)

mask.destroy()
