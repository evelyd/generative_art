
size(2000, 2000)
background(0)

#save unrotated frame
pushMatrix()
#set origin to center of grid
translate(width/2,height/2)

offset = 50
#diagonals
current1 = [offset*sin(radians(45)), offset*sin(radians(45))]
current2 = [-offset*sin(radians(45)), offset*sin(radians(45))]
current3 = [offset*sin(radians(45)), -offset*sin(radians(45))]
current4 = [-offset*sin(radians(45)), -offset*sin(radians(45))]

#horizontal/vertical
current5 = [offset, 0]
current6 = [0, offset]
current7 = [-offset, 0]
current8 = [0, -offset]

# color_specs1 = [[255,204,204],[255,229,204],[255,255,204]]
# color_specs2 = [[229,255,204],[204,255,204],[204,255,229]]
# color_specs3 = [[204,255,255],[204,229,255],[204,204,255]]
# color_specs4 = [[229,204,255],[255,204,255],[255,204,229]]

color_specs = [[255,204,204],[255,229,204],[255,255,204],
               [229,255,204],[204,255,204],[204,255,229],
               [204,255,255],[204,229,255],[204,204,255],
               [229,204,255],[255,204,255],[255,204,229]]

iterations = 3000
rand_range = 40
ell_size = 100
step_size = 10

#choose a color scheme
# color_pick = int(random(1,4))
# if color_pick == 1:
#     # background(255,128,0)
#     color_specs = color_specs1
# elif color_pick == 2:
#     # background(0,255,0)
#     color_specs = color_specs2
# elif color_pick == 3:
#     # background(0,128,255)
#     color_specs = color_specs3
# else:
#     # background(255,0,255)
#     color_specs = color_specs4

for i in range(0,iterations):   
    
    #ellipses get gradually smaller
    ell_size = ell_size*random(0.5,1.5)
    # ell_size = ell_size*0.95
    #rotate the grid around the center by a random amount
    rotate(radians(random(-5,5)))
    
    # current1 = [current1[0]+random(rand_range), current1[1]+random(rand_range)]
    current1 = [current1[0]+step_size*sin(radians(45)), current1[1]+step_size*sin(radians(45))]
    noStroke()
    fill(color_specs[i%len(color_specs)][0],color_specs[i%len(color_specs)][1],color_specs[i%len(color_specs)][2])
    ellipse(current1[0],current1[1],ell_size,ell_size)
    
    current2 = [current2[0]-step_size*sin(radians(45)), current2[1]+step_size*sin(radians(45))]
    noStroke()
    fill(color_specs[i%len(color_specs)][0],color_specs[i%len(color_specs)][1],color_specs[i%len(color_specs)][2])
    ellipse(current2[0],current2[1],ell_size,ell_size)
    
    current3 = [current3[0]+step_size*sin(radians(45)), current3[1]-step_size*sin(radians(45))]
    noStroke()
    fill(color_specs[i%len(color_specs)][0],color_specs[i%len(color_specs)][1],color_specs[i%len(color_specs)][2])
    ellipse(current3[0],current3[1],ell_size,ell_size)
    
    current4 = [current4[0]-step_size*sin(radians(45)), current4[1]-step_size*sin(radians(45))]
    noStroke()
    fill(color_specs[i%len(color_specs)][0],color_specs[i%len(color_specs)][1],color_specs[i%len(color_specs)][2])
    ellipse(current4[0],current4[1],ell_size,ell_size)
    
    current5 = [current5[0]+step_size, current5[1]]
    noStroke()
    fill(color_specs[i%len(color_specs)][0],color_specs[i%len(color_specs)][1],color_specs[i%len(color_specs)][2])
    ellipse(current5[0],current5[1],ell_size,ell_size)
    
    current6 = [current6[0], current6[1]+step_size]
    noStroke()
    fill(color_specs[i%len(color_specs)][0],color_specs[i%len(color_specs)][1],color_specs[i%len(color_specs)][2])
    ellipse(current6[0],current6[1],ell_size,ell_size)
    
    current7 = [current7[0]-step_size, current7[1]]
    noStroke()
    fill(color_specs[i%len(color_specs)][0],color_specs[i%len(color_specs)][1],color_specs[i%len(color_specs)][2])
    ellipse(current7[0],current7[1],ell_size,ell_size)
    
    current8 = [current8[0], current8[1]-step_size]
    noStroke()
    fill(color_specs[i%len(color_specs)][0],color_specs[i%len(color_specs)][1],color_specs[i%len(color_specs)][2])
    ellipse(current8[0],current8[1],ell_size,ell_size)
    
save('Examples/out.png')
