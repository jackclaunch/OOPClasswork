import tkinter, random
root = tkinter.Tk()
root.resizable(False, False)
s1xranpos = random.randint(0, 720)
s2xranpos = random.randint(0, 720)
s1yranpos = random.randint(0, 520)
s2yranpos = random.randint(0, 520)
myCanvas = tkinter.Canvas(root, bg="white", height=600, width=800)
shape1 = myCanvas.create_rectangle(s1xranpos, s1yranpos, s1xranpos+80, s1yranpos+80, fill="blue")
shape2 = myCanvas.create_rectangle(s2xranpos, s2yranpos, s2xranpos+80, s2yranpos+80, fill="red")

#initialize the constants xx, yy
s1xx = s1yy = 3
s2xx = s2yy = 3
def move_shape():
    global s1xx, s1yy, s2xx, s2yy
    #move the shape with the constanct xx, yy
    myCanvas.move(shape1, s1xx, s1yy)
    myCanvas.move(shape2, s2xx, s2yy)
    #get the current coordinates of the shape
    (s2x1, s2y1, s2x2, s2y2) = myCanvas.coords(shape2)
    (s1x1, s1y1, s1x2, s1y2) = myCanvas.coords(shape1)
    #check the boundaries of the coordinates and change the constants xx, yy
    if s1x1 <= 0 or s1x2 >= 800:
        s1xx = -s1xx
    if s1y1 <= 0 or s1y2 >= 600:
        s1yy = -s1yy
    if s2x1 <= 0 or s2x2 >= 800:
        s2xx = -s2xx
    if s2y1 <= 0 or s2y2 >= 600:
        s2yy = -s2yy
    #collision
    if s1x1 < s2x2 and s1x2 > s2x1 and s1y1 < s2y2 and s1y2 > s2y1:
        s1xx = -s1xx
        s2xx = -s2xx
    #call the function recursively
    myCanvas.after(30, move_shape)


#in the main program call the function move_shape()
myCanvas.after(10,move_shape())
myCanvas.pack()
root.mainloop()