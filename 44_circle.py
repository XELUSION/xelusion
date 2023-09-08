import turtle
def tangentCircles (ttl):
    """Print 10 tangent circle . """
    r = 10
    n = 10
    for i in range (1 , n + 1, 1):
         ttl.circle ( r *i)

def concentricCircles (ttl):
    """ print 10 concentric circles"""
    r = 10 
    for i in range (10):
        ttl.circle ( r * i)
        ttl.up()
        ttl.sety (( r * i) * (-1))
        ttl.down()

Ben = turtle . Turtle ()
Ben.up() ; Ben.goto(0, 150)
Ben.down() ; Ben.pencolor("Blue")
tangentCircles(Ben)
Ben.up() ; Ben.goto(0, -150)
Ben.down() ; Ben.pencolor("Red")
concentricCircles(Ben)