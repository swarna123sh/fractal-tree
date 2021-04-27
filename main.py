import turtle
turtle.pensize(5)
turtle.bgcolor("pink")
def tree(branchLen):
    if branchLen > 5:
        turtle.forward(branchLen)
        turtle.right(20)
        tree(branchLen-15)
        turtle.left(40)
        tree(branchLen-15)
        turtle.right(20)
        turtle.backward(branchLen)
turtle.left(90)
turtle.penup()
turtle.backward(100)
turtle.pendown()
turtle.color("purple")
tree(75)



