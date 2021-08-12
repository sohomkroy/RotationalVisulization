from tkinter import *
import math

coordinates = {"x":0,"y":0,"x2":0,"y2":0}

lines = []
line_coordinate_list = []

class Draw(Frame):
    canvas = None
    startX = None
    startY = None
    endX = None
    endY = None
    vert_lines = []
    def __init__(self):
        super().__init__()
        self.master.title("RotationDraw")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.pack()

    def initialize_canvas(self):
        self.canvas.configure(bg='black')
        self.canvas.pack(fill=BOTH, expand=1)

    def line_drag(self):
        self.canvas.bind("<ButtonPress-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.drag)
        self.canvas.bind('<ButtonRelease-1>', self.release)

    def click(self, e):
        self.canvas.delete("all")

        global line_coordinate_list
        line_coordinate_list = []
        self.vert_lines = []

        # define start point for line
        coordinates["x"] = e.x
        coordinates["y"] = e.y

        self.startX = coordinates["x"]
        self.startY = coordinates["y"]

        lines.append(self.canvas.create_line(coordinates["x"], coordinates["y"], coordinates["x"], coordinates["y"], width = 1, fill = "yellow"))

    def drag(self, e):
        global line_coordinate_list
        coordinates["x2"] = e.x
        coordinates["y2"] = e.y
        self.endX = coordinates["x2"]
        self.endY = coordinates["y2"]

        if (abs(coordinates["x"]-coordinates["x2"]) > 20):

            line_coordinate_list.append([self.startX, self.startY])
            self.canvas.coords(lines[-1], coordinates["x"], coordinates["y"], coordinates["x2"], coordinates["y2"])
            coordinates["x"] = e.x
            coordinates["y"] = e.y
            self.startX = coordinates["x"]
            self.startY = coordinates["y"]
            lines.append(self.canvas.create_line(coordinates["x"], coordinates["y"], coordinates["x"], coordinates["y"], width = 1, fill = "yellow"))


    def release(self, e):
        global line_coordinate_list
        line_coordinate_list.append([coordinates["x"], coordinates["y"]])
        self.draw_vertical_lines()
        self.draw_horizontal_lines()

    def draw_vertical_lines(self):
        global line_coordinate_list
        midline = int(self.canvas.winfo_height()/2)
        for x in range(0, len(line_coordinate_list)):
            height = midline - line_coordinate_list[x][1]
            self.canvas.create_line(line_coordinate_list[x][0], line_coordinate_list[x][1], line_coordinate_list[x][0],
                                    midline+height, width = 1, fill = "yellow")

    def draw_horizontal_lines(self):
        vals = []
        num = 10
        for x in range(0, num):
            vals.append(180 / num * (x + 1))


        global line_coordinate_list
        midline = int(self.canvas.winfo_height() / 2)

        for angle in vals:
            for x in range(0, len(line_coordinate_list)-1):
                height1 = midline - line_coordinate_list[x][1]
                height2 = midline - line_coordinate_list[x+1][1]

                x_1 = line_coordinate_list[x][0]
                y_1 = midline-height1*math.cos(math.radians(angle))
                x_2 = line_coordinate_list[x+1][0]
                y_2 = midline-height2*math.cos(math.radians(angle))

                print(y_1)

                self.canvas.create_line(x_1, y_1, x_2, y_2, width=1, fill="yellow")
                
def main():
    window = Tk()
    draw = Draw()
    draw.initialize_canvas()
    draw.line_drag()
    window.geometry("1600x1000")
    window.mainloop()

if __name__ == "__main__":
    main()