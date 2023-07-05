import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

canvas = tk.Canvas(root, bg = "white")

canvas.pack(fill = tk.BOTH, expand = True)

canvas.create_oval(40, 10, 80, 50, width=2, tag="h")#頭
canvas.create_line(60, 50, 60, 100, width=2, tag="h")#胴体
canvas.create_line(20, 50, 60, 65, width=2, tag="h")#左腕
canvas.create_line(60, 65, 100, 50, width=2, tag="h")#右腕
canvas.create_line(20, 120, 60, 100, width=2, tag="h")#左足
canvas.create_line(60, 100, 100, 120, width=2, tag="h")#右足

def move():
    canvas.move("h", 50, 0)
    canvas.after(100, move)
    
move()
    
root.mainloop()