import turtle

def draw_triangle(vertices):
    """Draw a triangle using turtle given its vertices."""
    turtle.penup()
    turtle.goto(vertices[0])
    turtle.pendown()
    turtle.goto(vertices[1])
    turtle.goto(vertices[2])
    turtle.goto(vertices[0])

def sierpinski(vertices, depth):
    """Recursively draw the Sierpiński triangle."""
    if depth == 0:
        draw_triangle(vertices)
    else:
        # Calculate midpoints of each side
        midpoints = [
            ((vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2),
            ((vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2),
            ((vertices[0][0] + vertices[2][0]) / 2, (vertices[0][1] + vertices[2][1]) / 2)
        ]
        # Recursively draw smaller triangles
        sierpinski([vertices[0], midpoints[0], midpoints[2]], depth - 1)
        sierpinski([vertices[1], midpoints[0], midpoints[1]], depth - 1)
        sierpinski([vertices[2], midpoints[1], midpoints[2]], depth - 1)

def main():
    turtle.speed(0)  # Fastest drawing speed
    turtle.hideturtle()  # Hide the turtle pointer
    turtle.bgcolor("white")  # Background color

    # Define the vertices of the main triangle
    vertices = [(-200, -150), (200, -150), (0, 200)]
    
    # Set the depth of recursion
    depth = 7  # You can adjust this value for more or fewer iterations
    sierpinski(vertices, depth)

    turtle.done()  # Finish drawing

if __name__ == "__main__":
    main()