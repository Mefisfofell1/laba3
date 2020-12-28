import math
import struct

t = 0
y_offset = -3
is_pixel = []
list1 = []

while t <= 5 * math.pi:
    x = round(t*math.sin(t), 2)
    y = round(t*math.cos(t), 2)
    list1.append(x)
    list1.append(y)
    is_pixel.append(list(list1))
    list1.clear()
    t += 0.01
color_1 = (255, 255, 255, 0)
color_2 = (0, 0, 0, 0)

with open("smth.bmp", "w+b") as f:
    f.write(struct.pack("<HL2HL", 19778, 62+1000*1000, 0, 0, 62))
    f.write(struct.pack("<3L2H6L", 40, 1000, 1000, 1, 8, 0, 0, 0, 0, 2, 0))
    f.write(struct.pack("<8B", *(255, 255, 255, 0), *(0, 0, 0, 0)))

    for y_counter in range(1000):
        x_offset = -3
        for x_counter in range(1000):
            if [x_offset, y_offset] in is_pixel:
                f.write(struct.pack("<B", 1))
            else:
                f.write(struct.pack("<B", 0))
            x_offset = round(x_offset + 0.01, 2)
        y_offset = round(y_offset + 0.01, 2)
