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
    
    centers = [[1000,1000],[1500,1500],[1500,500],[500,500],[500,1500]]
    
    for i in range(0,5):
        draw_shape(int(random(10,30)),int(random(3,20)),int(random(20,100)), centers[i][0], centers[i][1])
    
    save('Examples/out.png')

def draw_shape(line_thickness,num_vertices,base_radius,xpos,ypos):
    
    count = num_vertices
    slice = radians(360/count)
    
    radius = base_radius
    
    #create the base shape
    #choose color
    color = colors[int(random(0,len(colors)))]
    stroke(color[0],color[1],color[2])
    strokeWeight(line_thickness)
    
    pushMatrix()
    translate(xpos, ypos)
    
    offset = 10
    
    #draw a shape
    base_vertices = []
    
    #need to put last vertex at beginning
    #need to put first two vertices at end
    beginShape()
    
    #last point
    rl = random(radius-offset,radius+offset)
    vertex(cos(slice*(count-1)) * rl, sin(slice * (count-1)) * rl)
    base_vertices.append([cos(slice*(count-1)) * rl, sin(slice * (count-1)) * rl])
    
    #first point
    r = random(radius-offset,radius+offset)
    vertex(cos(slice*count) * r, sin(slice * count) * r)
    base_vertices.append([cos(slice*count) * r, sin(slice * count) * r])
    # print("first point:")
    # print(
    #second point
    r2 = random(radius-offset,radius+offset)
    vertex(cos(slice) * r2, sin(slice) * r2)
    base_vertices.append([cos(slice) * r2, sin(slice) * r2])
    #from third pt to third last pt
    for i in range(2,count-1):
        angle = i*slice
        rand_radius = random(radius-offset,radius+offset)
        x = cos(angle)*rand_radius
        y = sin(angle)*rand_radius
        vertex(x,y)
        base_vertices.append([x,y])
        
    #last point
    vertex(cos(slice*(count-1)) * rl, sin(slice * (count-1)) * rl)
    base_vertices.append([cos(slice*(count-1)) * rl, sin(slice * (count-1)) * rl])
    #first point
    vertex(cos(0) * r, sin(0) * r)
    base_vertices.append([cos(0) * r, sin(0) * r])
    #second point
    vertex(cos(slice) * r2, sin(slice) * r2)
    base_vertices.append([cos(slice) * r2, sin(slice) * r2])
    endShape()
        
    #outline the base shape (just scale each vertex, assuming origin is at center of current shape

    for i in range(0,int(random(5,20))):
        #use same vertices, change scale every time w/ radius
        radius = radius + line_thickness*2
        
        shape_scale = radius/base_radius
        
        beginShape()
        
        #just use the saved vertices and multiply each by shape_scale
        for j in range(0,len(base_vertices)):
            vertex(shape_scale*base_vertices[j][0],shape_scale*base_vertices[j][1])
        
        endShape()
        
    popMatrix()
