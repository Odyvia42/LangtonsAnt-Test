from tkinter import *

start_coords = (512, 512)
coords_colors = dict()
black_squares_counter = 0
initial_direction = 0
steps_counter = 0
x = start_coords[0]
y = start_coords[1]
coords_to_check = (x, y)

root = Tk()
c = Canvas(width=1024, height=1024, bg='white')
c.pack()


def check_coords(coords):
    if coords not in coords_colors.keys():
        coords_colors[coords] = 1


def check_color(coords):
    if coords_colors[coords] == 1:
        return True
    else:
        return False


def check_direction(direction, coords):
    if check_color(coords):
        direction += 90
        if direction == 360:
            direction = 0
        elif direction > 360:
            direction -= 360
    else:
        if direction >= 90:
            direction -= 90
        else:
            direction += 360
            direction -= 90
    return direction


while x > 0 and x < 1024 and y > 0 and y < 1024:
    check_coords(coords_to_check)
    direction = check_direction(initial_direction, coords_to_check)
    if check_color(coords_to_check):
        coords_colors[coords_to_check] = 0
        black_squares_counter += 1
        c.create_rectangle(coords_to_check[0], coords_to_check[1], coords_to_check[0], coords_to_check[1])
    else:
        coords_colors[coords_to_check] = 1
        black_squares_counter -= 1
        c.create_rectangle(coords_to_check[0], coords_to_check[1], coords_to_check[0], coords_to_check[1],
                           outline='white')
    if direction == 0:
        y -= 1
    elif direction == 90:
        x += 1
    elif direction == 180:
        y += 1
    elif direction == 270:
        x -= 1
    coords_to_check = (x, y)
    steps_counter += 1
    initial_direction = direction
print('total black squares:', black_squares_counter)

root.mainloop()


