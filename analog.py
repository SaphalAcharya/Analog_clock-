import tkinter as tk
import time
import math

class Clock:
    def __init__(self):
        self.root = tk.Tk()
        self .root.title("Analog Clock")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='brown')
        self.canvas.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.localtime()
        self.canvas.delete("all")
        origin_x = 200
        origin_y = 200
        self.canvas.create_oval(50, 50, 350, 350)
        for i in range(1, 13):
            x = origin_x + 150 * math.sin(math.radians(i * 30))
            y = origin_y - 150 * math.cos(math.radians(i * 30))
            self.canvas.create_text(x, y, text=str(i), font=('Arial', 12))
        self.draw_hand(now.tm_hour, now.tm_min, now.tm_sec)
        self.root.after(1000, self.update_clock)

    def draw_hand(self, hour, minute, second):
        origin_x = 200
        origin_y = 200
        hour_x = origin_x + 50 * math.sin(math.radians((hour % 12) * 30 + minute * 0.5))
        hour_y = origin_y - 50 * math.cos(math.radians((hour % 12) * 30 + minute * 0.5))
        self.canvas.create_line(origin_x, origin_y, hour_x, hour_y, width=3)
        minute_x = origin_x + 70 * math.sin(math.radians(minute * 6))
        minute_y = origin_y - 70 * math.cos(math.radians(minute * 6))
        self.canvas.create_line(origin_x, origin_y, minute_x, minute_y, width=2)
        second_x = origin_x + 80 * math.sin(math.radians(second * 6))
        second_y = origin_y - 80 * math.cos(math.radians(second * 6))
        self.canvas.create_line(origin_x, origin_y, second_x, second_y, width=1, fill='red')

if __name__ == "__main__":
    clock = Clock()