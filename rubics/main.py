import tkinter as tk
from tkinter import ttk
import sys
import rubics


def main(args):
    #initialise window
    root = tk.Tk()
    root.geometry("810x600")
    root.title("Rubics Cube")
    cube = rubics.rc()

    #window layout
    style = ttk.Style()
    style.theme_use('winnative')
    style.layout('Left.TButton', [ ('Button.focus', {'children': [ ('Button.leftarrow', None) ] } ) ] )
    style.layout('Right.TButton', [ ('Button.focus', {'children': [ ('Button.rightarrow', None) ] } ) ] )
    style.layout('Up.TButton', [ ('Button.focus', {'children': [ ('Button.uparrow', None) ] } ) ] )
    style.layout('Down.TButton', [ ('Button.focus', {'children': [ ('Button.downarrow', None) ] } ) ] )

    ttk.Button(root, style='Left.TButton', command=cube.handle_back_left).grid(row=0,column=1)
    tk.Label(root, text="Back").grid(row=0,column=2)
    ttk.Button(root, style='Right.TButton', command=cube.handle_back_right).grid(row=0,column=3)

    ttk.Button(root, style='Left.TButton', command=cube.handle_top_left).grid(row=0,column=7)
    tk.Label(root, text="Top").grid(row=0,column=8)
    ttk.Button(root, style='Right.TButton', command=cube.handle_top_right).grid(row=0,column=9)

    ttk.Button(root, style='Up.TButton', command=cube.handle_left_up).grid(row=5,column=0)
    tk.Label(root, text="Left").grid(row=6,column=0)
    ttk.Button(root, style='Down.TButton', command=cube.handle_left_down).grid(row=7,column=0)

    ttk.Button(root, style='Left.TButton', command=cube.handle_bottom_left).grid(row=12,column=7)
    tk.Label(root, text="Bottom").grid(row=12,column=8)
    ttk.Button(root, style='Right.TButton', command=cube.handle_bottom_right).grid(row=12,column=9)

    ttk.Button(root, style='Up.TButton', command=cube.handle_right_up).grid(row=5,column=16)
    tk.Label(root, text="Right").grid(row=6,column=16)
    ttk.Button(root, style='Down.TButton', command=cube.handle_right_down).grid(row=7,column=16)

    ttk.Button(root, style='Left.TButton', command=cube.handle_front_left).grid(row=12,column=13)
    tk.Label(root, text="Front").grid(row=12,column=14)
    ttk.Button(root, style='Right.TButton', command=cube.handle_front_right).grid(row=12,column=15)

    panel = tk.Label(root, image=cube.assemble())
    panel.grid(row=1,column=1, rowspan=11, columnspan = 15)

    #update logic
    def update(root):
        image = cube.assemble()
        panel.configure(image=image)
        panel.image = image

        root.after(10,update,root)

    update(root)
    root.mainloop()


if __name__ == '__main__':
    main(sys.argv)