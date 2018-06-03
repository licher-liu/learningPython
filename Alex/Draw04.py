import turtle as tt
def main():

#    Square(20,0,0)
#    Square(10*2+20,0-10,0+10).
    Swidth=20
    Sx=0
    Sy=0
    gap=20
    number=5
    tt.speed(5000)
    for i in range(number):
        Square(Swidth,Sx,Sy)
        Swidth = Swidth+gap*2
        Sx=Sx-gap
        Sy=Sy+gap

    tt.done()

def Square(width,x,y):

    tt.penup()
    tt.goto(x,y)
    tt.pendown()
    tt.fd(width)
    tt.right(90)
    tt.fd(width)
    tt.right(90)
    tt.fd(width)
    tt.right(90)
    tt.fd(width)
    tt.right(90)

main()
