import turtle

tu = turtle. Turtle()
tu.screen.bgcolor('#EBF1F5')
tu.pensize(2)
tu.color('#2A1503')
tu.left(90)
tu.backward(100)
tu.speed(50)
tu.shape('turtle')

def tree(i):
    if i<10:
        return
    else:
        tu.forward(i)
        tu.color('#DE3161')
        tu.circle(2)
        tu.color('#7B481C')
        tu.left(30)
        tree(3*i/4)
        tu.right(60)
        tree(3*i/4)
        tu.left(30)
        tu.backward(i)

tree(100)
turtle.done()