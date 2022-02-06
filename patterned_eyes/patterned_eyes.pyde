def setup():
    size(2000, 2000)
    background(0)
    
    #define eye colors
    c_blue = [153, 204, 255]
    c_dark_blue = [0, 102, 204]
    c_green = [76, 153, 0]
    c_hazel = [153, 153, 0]
    c_brown = [205, 133, 63]
    c_dark_brown = [102, 51, 0]
    
    #create arrays of possibilities
    colors = [c_blue, c_dark_blue, c_green, c_hazel, c_brown, c_dark_brown]
    animals = ['human', 'sheep', 'cat', 'lizard', 'cuttlefish']
    
    #define randomization
    spacing = 10*int(random(1,20))
    eyes_per_row = int(random(2,10))
    eye_size = width/(eyes_per_row + 2*spacing)
    
    print(str(eyes_per_row) + " eyes per row with spacing of " + str(spacing) + " pts")
    
    vertical = False
    #loop through grid locations
    for i in range(width*1/(eyes_per_row + 1), width*eyes_per_row/(eyes_per_row + 1), width*1/(eyes_per_row + 1)):
        for j in range(height*1/(eyes_per_row + 1), height*eyes_per_row/(eyes_per_row + 1), height*1/(eyes_per_row + 1)):
            if (not vertical):
                draw_eye(colors[int(random(0, len(colors)))], animals[int(random(0, len(animals)))], [i,j], 100, 0)
            else:
                draw_eye(colors[int(random(0, len(colors)))], animals[int(random(0, len(animals)))], [i,j], 100, HALF_PI)
            vertical = not vertical
        vertical = not vertical
        
    save('Examples/out.png')
            
def draw_eye(c, animal, loc, sz, ang):
    pushMatrix()
    translate(loc[0], loc[1])
    rotate(ang)
    
    #draw eye outline
    fill(255)
    stroke(0)
    beginShape()
    vertex(0 - sz, 0)
    quadraticVertex(0, 0 + sz, 0 + sz, 0)
    quadraticVertex(0, 0 - sz, 0 - sz, 0)
    endShape()
    
    #draw iris
    stroke(0) #black outline
    fill(c[0], c[1], c[2])
    circle(0, 0, sz)
    
    #check and draw pupil shape
    fill(0)
    noStroke()
    
    if animal == 'human':
        circle(0, 0, 0.5*sz)
        
    elif animal == 'sheep':
        rectMode(CENTER)
        rect(0, 0, sz*2/3, 0.25*sz, 0.125*sz)
        
    elif animal == 'cat':
        beginShape()
        vertex(0, 0 - sz/3)
        quadraticVertex(0 - 0.1*sz, 0, 0, 0 + sz/3)
        quadraticVertex(0 + 0.1*sz, 0, 0, 0 - sz/3)
        endShape()
   
    elif animal == 'lizard':
        l = sz/3 #half height of pupil
        beginShape()
        vertex(0, 0 - l)
        quadraticVertex(0 - 0.05*sz, 0 - l*2/3, 0 - 0.2*sz, 0 - l/3)
        quadraticVertex(0 - 0.05*sz, 0, 0 - 0.2*sz, 0 + l/3)
        quadraticVertex(0 - 0.05*sz, 0 + l*2/3, 0, 0 + l)
        quadraticVertex(0 + 0.05*sz, 0 + l*2/3, 0 + 0.2*sz, 0 + l/3)
        quadraticVertex(0 + 0.05*sz, 0, 0 + 0.2*sz, 0 - l/3)
        quadraticVertex(0 + 0.05*sz, 0 - l*2/3, 0, 0 - l)
        endShape()
        
    elif animal == 'cuttlefish':
        l = 2*sz/3 #width of pupil
        beginShape()
        vertex(0 - l/2, 0 - l/3)
        quadraticVertex(0 - l/4, 0 + l/8, 0 - l/8, 0)
        quadraticVertex(0, 0 - l/4, 0 + l/8, 0)
        quadraticVertex(0 + l/4, 0 + l/8, 0 + l/2, 0 - l/3)
        quadraticVertex(0 + l/4, 0 + 3*l/8, 0 + l/8, 0 + 2*l/8)
        quadraticVertex(0, 0, 0 - l/8, 0 + 2*l/8)
        quadraticVertex(0 - l/4, 0 + 3*l/8, 0 - l/2, 0 - l/3)
        endShape()
    
    popMatrix()
