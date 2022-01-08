shift = 0
l = random(0,0.1)
A = random(20,50)
omega = random(0.1,2)

def setup():
    size(2000,2000,P3D)

    noFill()
    
    # draw()
    
    save('Examples/out.png')

def draw():  
    global shift
    global l
    global A
    global omega
    
    background(0)

    translate(width/2,height/2)
    
    rotateX(PI/4)
    rotateZ(PI/4)

    translate(-width/4,-height/4)
    
    spacing = 50
    loops = (width/2)/spacing

    # shift = shift + 1
    
    #use vaporwave colors, starting at teal
    c = [0,255,255]
    
    #draw vertical lines
    for i in range(0,width/2+1,spacing):
        stroke(c[0],c[1],c[2])
        beginShape()
        # curveVertex(i,0,0)
        for j in range(0,height/2+1,spacing):
            z = exp(l*sqrt(i^2+j^2))*A*sin(omega*sqrt(i^2+j^2)+shift)
            curveVertex(i,j,z)
            # if j == 0:
            #     curveVertex(i,j,z)
        # curveVertex(i,height/2,0)
        endShape()
        #change to next color
        c[0] = int(c[0]+150/loops)
        c[1] = int(c[1]-255/loops)
    
    delay(50)
