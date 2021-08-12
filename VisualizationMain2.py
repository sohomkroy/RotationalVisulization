from tkinter import *


coordinates = {"x":0,"y":0,"x2":0,"y2":0}
# keep a reference to all lines by keeping them in a list
lines = []
line_coordinate_list = []

startX = None
startY = None
endX = None
endY = None

class Draw(Frame):
    canvas = None
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

    def click(self, e):
        self.canvas.delete("all")
        #lines = []

        # define start point for line
        coordinates["x"] = e.x
        coordinates["y"] = e.y

        startX = coordinates["x"]
        startY = coordinates["y"]

        # create a line on this point and store it in the list
        lines.append(self.canvas.create_line(coordinates["x"], coordinates["y"], coordinates["x"], coordinates["y"], width = 1, fill = "yellow"))

    def drag(self, e):
        # update the coordinates from the event
        coordinates["x2"] = e.x
        coordinates["y2"] = e.y

        line_coordinate_list.append([startX, startY, endX, endY])

        endX = coordinates["x2"]
        endY = coordinates["y2"]

        if (abs(coordinates["x"]-coordinates["x2"]) > 100):
            self.canvas.coords(lines[-1], coordinates["x"], coordinates["y"], coordinates["x2"], coordinates["y2"])



            coordinates["x"] = e.x
            coordinates["y"] = e.y
            startX = coordinates["x"]
            startY = coordinates["y"]
            lines.append(self.canvas.create_line(coordinates["x"], coordinates["y"], coordinates["x"], coordinates["y"], width = 1, fill = "yellow"))

def main():
    window = Tk()
    draw = Draw()
    draw.initialize_canvas()
    draw.line_drag()
    window.geometry("1600x1000")
    window.mainloop()

if __name__ == "__main__":
    main()