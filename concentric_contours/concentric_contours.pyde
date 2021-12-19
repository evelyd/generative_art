count = 20
spacing = 20
slice = radians(360/count)

colors =  [[255,204,204],[255,229,204],[255,255,204],
                    [229,255,204],[204,255,204],[204,255,229],
                    [204,255,255],[204,229,255],[204,204,255],
                    [229,204,255],[255,204,255],[255,204,229]]

def setup():
    size(2000,2000)
    background(0)
    #transformations
    # translate(width/2,height/2)
    noFill()
    draw_stuff()
    
    save('Examples/out.png')

def draw_stuff():
    
    radius = 50
    
    for i in range(0,20):
        #choose color
        color = colors[int(random(0,len(colors)))]
        stroke(color[0],color[1],color[2])
        
        pushMatrix()
        translate(width/2, height/2)
        
        radius = radius + 50
        offset = 30
        
        #draw a shape
        #need to put last vertex at beginning
        #need to put first two vertices at end
        beginShape()
        
        #last point
        rl = random(radius-offset,radius+offset)
        curveVertex(cos(slice*(count-1)) * rl, sin(slice * (count-1)) * rl)
        #first point
        r = random(radius-offset,radius+offset)
        curveVertex(cos(slice*count) * r, sin(slice * count) * r)
        # print("first point:")
        # print(
        #second point
        r2 = random(radius-offset,radius+offset)
        curveVertex(cos(slice) * r2, sin(slice) * r2);
        #from third pt to third last pt
        for i in range(2,count-1):
            angle = i*slice
            rand_radius = random(radius-offset,radius+offset)
            x = cos(angle)*rand_radius
            y = sin(angle)*rand_radius
            curveVertex(x,y)
            
        #last point
        curveVertex(cos(slice*(count-1)) * rl, sin(slice * (count-1)) * rl)
        #first point
        curveVertex(cos(0) * r, sin(0) * r)
        #second point
        curveVertex(cos(slice) * r2, sin(slice) * r2)
        endShape()
        
        popMatrix()
    
    # beginShape()
    # theta = 0

    # x = 0+300
    # y = 0
    # step_size = 10
    # curveVertex(x,y)
    # for i in range(0,100):
    #     x = x + step_size*round(random(1,2))*cos(theta)
    #     y = y + step_size*round(random(1,2))*sin(theta)
    #     curveVertex(x,y)
    #     theta = theta + random(radians(-30),radians(30))
    # endShape()
