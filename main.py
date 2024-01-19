from canvas import Canvas
from shapes import Rectangle, Square
from random import randint

# Get canvas width and height from the user
canvas_w = int(input("Enter canvas width: "))
canvas_h = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color(black or white): ")

# Create canvas with the user data
canvas = Canvas(height=canvas_h, width=canvas_w, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw? Enter quit to quit. ")

    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_w = int(input("Enter width of the rectangle: "))
        rec_h = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should the rectangle have(0 to 255)? "))
        green = int(input("How much green should the rectangle have(0 to 255)? "))
        blue = int(input("How much blue should the rectangle have(0 to 255)? "))

        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_h, height=rec_h, width=rec_w, color=(red, green, blue))
        r1.draw(canvas)

    # Asl for square data and create square if user entered 'square'
    if shape_type.lower() == 'square':
        rec_x = int(input("Enter x of the square: "))
        rec_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter side lenght of the square: "))
        red = int(input("How much red should the rectangle have(0 to 255)? "))
        green = int(input("How much green should the rectangle have(0 to 255)? "))
        blue = int(input("How much blue should the rectangle have(0 to 255)? "))

        # Create the square
        s1 = Square(x=rec_x, y=rec_y, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)

    # Quit for exiting the loop
    if shape_type == 'quit':
        break

# It will generate a random number and it will attach to the name of the canvas
random_number = randint(1, 100)
canvas.make(f'design/canvas{random_number}.png')