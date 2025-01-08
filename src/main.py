import tkinter as tk
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk
import copy


#initialise window
window = tk.Tk()
window.geometry("810x600")
window.title("Rubics Cube")


#initialise cube with sides
def assemble():
    cube = np.zeros((11,15))
    cube[4:7,0:3]=back
    cube[4:7,4:7]=left
    cube[4:7,8:11]=front
    cube[4:7,12:15]=right
    cube[0:3,8:11]=top
    cube[8:11,8:11]=bottom

    image = np.kron(cube, np.ones((50,50)))
    image_rgb = np.zeros((550,750,3))
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            match image[x,y]:
                case 1:image_rgb[x,y] = [255,255,255]
                case 2:image_rgb[x,y] = [255,0,0]
                case 3:image_rgb[x,y] = [0,255,0]
                case 4:image_rgb[x,y] = [0,0,255]
                case 5:image_rgb[x,y] = [255,255,0]
                case 6:image_rgb[x,y] = [255,122,0]

    image = Image.fromarray(image_rgb.astype(np.uint8), mode='RGB')
    image = ImageTk.PhotoImage(image=image)
    return image

front = np.zeros((3,3))+1
top = np.zeros((3,3))+2
bottom = np.zeros((3,3))+3
right = np.zeros((3,3))+4
left = np.zeros((3,3))+5
back = np.zeros((3,3))+6

image = assemble()


#button logic
def handle_back_left():
    temp = copy.copy(top[0])
    top[0] = left[:,0][::-1]
    left[:,0] = bottom[2]
    bottom[2] = right[:,2][::-1]
    right[:,2] = temp

    temp = copy.copy(back[2,1:])
    back[2,1:] = back[1:,0]
    back[1:,0] = back[0,:2][::-1]
    back[0,:2] = back[:2,2]
    back[:2,2] = temp[::-1]

    image = assemble()
    panel.configure(image=image)
    panel.image = image

def handle_back_right():
    temp = copy.copy(top[0])
    top[0] = right[:,2]
    right[:,2] = bottom[2][::-1]
    bottom[2] = left[:,0]
    left[:,0] = temp[::-1]

    temp = copy.copy(back[2,1:])
    back[2,1:] = back[:2,2][::-1]
    back[:2,2] = back[0,:2]
    back[0,:2] = back[1:,0][::-1]
    back[1:,0] = temp

    image = assemble()
    panel.configure(image=image)
    panel.image = image

def handle_top_left():
    temp = copy.copy(front[0])
    front[0] = left[0]
    left[0] = back[0]
    back[0] = right[0]
    right[0] = temp

    temp = copy.copy(top[2,1:])
    top[2,1:] = top[1:,0]
    top[1:,0] = top[0,:2][::-1]
    top[0,:2] = top[:2,2]
    top[:2,2] = temp[::-1]

    image = assemble()
    panel.configure(image=image)
    panel.image = image

def handle_top_right():
    temp = copy.copy(front[0])
    front[0] = right[0]
    right[0] = back[0]
    back[0] = left[0]
    left[0] = temp

    temp = copy.copy(top[2,1:])
    top[2,1:] = top[:2,2][::-1]
    top[:2,2] = top[0,:2]
    top[0,:2] = top[1:,0][::-1]
    top[1:,0] = temp

    image = assemble()
    panel.configure(image=image)
    panel.image = image

def handle_left_up():
    temp = copy.copy(top[:,0])
    top[:,0] = front[:,0]
    front[:,0] = bottom[:,0]
    bottom[:,0] = back[:,2][::-1]
    back[:,2] = temp[::-1]

    temp = copy.copy(left[2,1:])
    left[2,1:] = left[1:,0]
    left[1:,0] = left[0,:2][::-1]
    left[0,:2] = left[:2,2]
    left[:2,2] = temp[::-1]

    image = assemble()
    panel.configure(image=image)
    panel.image = image

def handle_left_down():
    temp = copy.copy(top[:,0])
    top[:,0] = back[:,2][::-1]
    back[:,2] = bottom[:,0][::-1]
    bottom[:,0] = front[:,0]
    front[:,0] = temp

    temp = copy.copy(left[2,1:])
    left[2,1:] = left[:2,2][::-1]
    left[:2,2] = left[0,:2]
    left[0,:2] = left[1:,0][::-1]
    left[1:,0] = temp

    image = assemble()
    panel.configure(image=image)
    panel.image = image

def handle_bottom_left():
    temp = copy.copy(front[2])
    front[2] = right[2]
    right[2] = back[2]
    back[2] = left[2]
    left[2] = temp

    temp = copy.copy(bottom[2,1:])
    bottom[2,1:] = bottom[1:,0]
    bottom[1:,0] = bottom[0,:2][::-1]
    bottom[0,:2] = bottom[:2,2]
    bottom[:2,2] = temp[::-1]

    image = assemble()
    panel.configure(image=image)
    panel.image = image

def handle_bottom_right():
    temp = copy.copy(front[2])
    front[2] = left[2]
    left[2] = back[2]
    back[2] = right[2]
    right[2] = temp

    temp = copy.copy(bottom[2,1:])
    bottom[2,1:] = bottom[:2,2][::-1]
    bottom[:2,2] = bottom[0,:2]
    bottom[0,:2] = bottom[1:,0][::-1]
    bottom[1:,0] = temp

    image = assemble()
    panel.configure(image=image)
    panel.image = image

def handle_right_up():
    temp = copy.copy(top[:,2])
    top[:,2] = front[:,2]
    front[:,2] = bottom[:,2]
    bottom[:,2] = back[:,0][::-1]
    back[:,0] = temp[::-1]

    temp = copy.copy(right[2,1:])
    right[2,1:] = right[:2,2][::-1]
    right[:2,2] = right[0,:2]
    right[0,:2] = right[1:,0][::-1]
    right[1:,0] = temp

    image = assemble()
    panel.configure(image=image)
    panel.image = image

def handle_right_down():
    temp = copy.copy(top[:,2])
    top[:,2] = back[:,0][::-1]
    back[:,0] = bottom[:,2][::-1]
    bottom[:,2] = front[:,2]
    front[:,2] = temp

    temp = copy.copy(right[2,1:])
    right[2,1:] = right[1:,0]
    right[1:,0] = right[0,:2][::-1]
    right[0,:2] = right[:2,2]
    right[:2,2] = temp[::-1]

    image = assemble()
    panel.configure(image=image)
    panel.image = image

def handle_front_left():
    temp = copy.copy(top[2])
    top[2] = right[:,0]
    right[:,0] = bottom[0][::-1]
    bottom[0] = left[:,2]
    left[:,2] = temp[::-1]

    temp = copy.copy(front[2,1:])
    front[2,1:] = front[1:,0]
    front[1:,0] = front[0,:2][::-1]
    front[0,:2] = front[:2,2]
    front[:2,2] = temp[::-1]

    image = assemble()
    panel.configure(image=image)
    panel.image = image

def handle_front_right():
    temp = copy.copy(top[2])
    top[2] = left[:,2][::-1]
    left[:,2] = bottom[0]
    bottom[0] = right[:,0][::-1]
    right[:,0] = temp

    temp = copy.copy(front[2,1:])
    front[2,1:] = front[:2,2][::-1]
    front[:2,2] = front[0,:2]
    front[0,:2] = front[1:,0][::-1]
    front[1:,0] = temp

    image = assemble()
    panel.configure(image=image)
    panel.image = image


#window layout
style = ttk.Style()
style.theme_use('winnative')
style.layout('Left.TButton', [ ('Button.focus', {'children': [ ('Button.leftarrow', None) ] } ) ] )
style.layout('Right.TButton', [ ('Button.focus', {'children': [ ('Button.rightarrow', None) ] } ) ] )
style.layout('Up.TButton', [ ('Button.focus', {'children': [ ('Button.uparrow', None) ] } ) ] )
style.layout('Down.TButton', [ ('Button.focus', {'children': [ ('Button.downarrow', None) ] } ) ] )

button = ttk.Button(window, style='Left.TButton', command=handle_back_left).grid(row=0,column=1)
label = tk.Label(window, text="Back").grid(row=0,column=2)
button = ttk.Button(window, style='Right.TButton', command=handle_back_right).grid(row=0,column=3)

button = ttk.Button(window, style='Left.TButton', command=handle_top_left).grid(row=0,column=7)
label = tk.Label(window, text="Top").grid(row=0,column=8)
button = ttk.Button(window, style='Right.TButton', command=handle_top_right).grid(row=0,column=9)

button = ttk.Button(window, style='Up.TButton', command=handle_left_up).grid(row=5,column=0)
label = tk.Label(window, text="Left").grid(row=6,column=0)
button = ttk.Button(window, style='Down.TButton', command=handle_left_down).grid(row=7,column=0)

button = ttk.Button(window, style='Left.TButton', command=handle_bottom_left).grid(row=12,column=7)
label = tk.Label(window, text="Bottom").grid(row=12,column=8)
button = ttk.Button(window, style='Right.TButton', command=handle_bottom_right).grid(row=12,column=9)

button = ttk.Button(window, style='Up.TButton', command=handle_right_up).grid(row=5,column=16)
label = tk.Label(window, text="Right").grid(row=6,column=16)
button = ttk.Button(window, style='Down.TButton', command=handle_right_down).grid(row=7,column=16)

button = ttk.Button(window, style='Left.TButton', command=handle_front_left).grid(row=12,column=13)
label = tk.Label(window, text="Front").grid(row=12,column=14)
button = ttk.Button(window, style='Right.TButton', command=handle_front_right).grid(row=12,column=15)


panel = tk.Label(window, image=image)
panel.grid(row=1,column=1, rowspan=11, columnspan = 15)



# Start the event loop.
window.mainloop()