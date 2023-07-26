import tkinter as tk

class LineAnimationApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.line = self.canvas.create_line(50, 200, 350, 200, fill='blue', width=3)
        self.points = [(50, 200), (350, 200)]  # 初期座標と終点の座標
        self.animating = False
        self.step_count = 0

    def animate_line(self):
        if self.step_count < 5:
            x1, y1 = self.points[-2]
            x2, y2 = self.points[-1]
            dx = (350 - 50) / 5  # 変化させるxの量
            dy = (350 - 200) / 5  # 変化させるyの量
            x1 += dx
            x2 += dx
            y1 += dy
            y2 += dy
            self.points.append((x1, y1))
            self.points.append((x2, y2))
            self.canvas.coords(self.line, x1, y1, x2, y2)
            self.step_count += 1
            self.root.after(1000, self.animate_line)  # 1000ミリ秒（1秒）後に次のアニメーションステップを呼び出す
        else:
            self.animating = False

    def start_animation(self):
        if not self.animating:
            self.animating = True
            self.animate_line()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Line Animation")
    app = LineAnimationApp(root)
    tk.Button(root, text="Start Animation", command=app.start_animation).pack()
    root.mainloop()