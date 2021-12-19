def draw_lines():
    colors =  [[255,204,204],[255,229,204],[255,255,204],
                        [229,255,204],[204,255,204],[204,255,229],
                        [204,255,255],[204,229,255],[204,204,255],
                        [229,204,255],[255,204,255],[255,204,229]]
    noFill()
    color = colors[int(random(0,len(colors)))]
    stroke(color[0],color[1],color[2])
    beginShape()
    theta = 0

    x = 0+300
    y = 0
    step_size = 10
    curveVertex(x,y)
    for i in range(0,100):
        x = x + step_size*round(random(1,2))*cos(theta)
        y = y + step_size*round(random(1,2))*sin(theta)
        curveVertex(x,y)
        theta = theta + random(radians(-30),radians(30))
    endShape()

def setup():
    size(2000,2000)
    background(0)
    #transformations
    translate(width/2,height/2)
    
    for i in range(0,100*360/15):
        rotate(radians(15))
        draw_lines()
    
    save('Examples/out.png')
