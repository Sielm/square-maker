from Myro import *
init ("sim")

#square
penDown()
forward (1,1)
turnBy (-90)
forward (1,1)
turnBy (-90)
forward (1,1)
turnBy (-90)
forward (1,1)
penUp()
stop()

#triangle
forward (1,3)
penDown()
foward (1,1)
turnBy (120)
forward (1,1)
turnBy (60)
forward (1,1)
penUp()

# letter "N"
forward (1,3)
penDown()
forward (1,2)
turnBy (120)
forward (1,2)
turnBy (-120)
forward (1,2)
penUp()
stop()
