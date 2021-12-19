def draw_wave(start_y,Ac,theta,colors):
    #define values
    Tc = 30
    start_x = 0
    end_x = 2000
    end_y = start_y
    mu = 0.8
    Tm = Tc*20
    var_range = Tc*0.8
    
    noFill()
    color = colors[int(random(0,len(colors)))]
    stroke(color[0],color[1],color[2])
    beginShape()
    curveVertex(start_x,start_y)       
    
    for t in range(0,end_x,10):
        y = start_y+Ac*cos((2*PI*t/Tc)+random(-var_range,var_range))*(1+mu*sin((2*PI*t/Tm)+theta))+random(-var_range,var_range)
        curveVertex(t,y)
    
    curveVertex(end_x,end_y)
    endShape()

def setup():
    size(2000,2000)
    background(255)
    neon_colors = [[0,0,102],[51,0,102],[0,0,204],[102,0,204],[51,51,255],
                   [0,0,102],[51,0,102],[0,0,204],[102,0,204],[51,51,255],
                   [0,0,102],[51,0,102],[0,0,204],[102,0,204],[51,51,255],
                   [0,0,102],[51,0,102],[0,0,204],[102,0,204],[51,51,255],
                   [153,51,255],[255,0,255],[153,255,255]]
    pastel_colors =  [[255,204,204],[255,229,204],[255,255,204],
                      [229,255,204],[204,255,204],[204,255,229],
                      [204,255,255],[204,229,255],[204,204,255],
                      [229,204,255],[255,204,255],[255,204,229]]

    
    theta = PI/2
    Ac = 100
    for j in range(0,2000+Ac*3,Ac*3):
        for i in range(0,50):
            draw_wave(j,Ac,theta,pastel_colors)
        theta = -theta
        
    save('Examples/out.png')
