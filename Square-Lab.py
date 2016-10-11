from Myro import *
init ("sim")

#square

penDown()
forward (1,2)
turnBy (-90)
forward (1,2)
turnBy (-90)
forward (1,2)
turnBy (-90)
forward (1,2)
penUp()
stop()

#triangle
forward (1,2)
penDown()
forward (1,2)
turnBy (120)
forward (1,2)
turnBy (120)
forward (1,2)
penUp()

# letter "N"
forward (1,3)
penDown()
forward (1,2)
backward (1,2)
turnBy (30)
forward (1,2)
turnBy (150)
forward (1,2)
stop()

