import numpy as np
import matplotlib.pyplot as plt

pts = np.array([
    [-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],
    [-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]
])
edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]

ang1 = 0.0
ang2 = 0.0

fig, ax = plt.subplots()

def draw():
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    
    cx = np.cos(ang1)
    sx = np.sin(ang1)
    cy = np.cos(ang2)
    sy = np.sin(ang2)
    
    mat1 = np.array([[1,0,0],[0,cx,-sx],[0,sx,cx]])
    mat2 = np.array([[cy,0,sy],[0,1,0],[-sy,0,cy]])
    
    for e in edges:
        p1 = pts[e[0]]
        p2 = pts[e[1]]
        
        r1 = p1 @ mat1.T @ mat2.T
        r2 = p2 @ mat1.T @ mat2.T
        
        z1 = 1 / (r1[2] + 4)
        xx1 = r1[0] * z1
        yy1 = r1[1] * z1
        
        z2 = 1 / (r2[2] + 4)
        xx2 = r2[0] * z2
        yy2 = r2[1] * z2
        
        ax.plot([xx1,xx2],[yy1,yy2],'b-')
    fig.canvas.draw()

def press(event):
    global ang1, ang2
    if event.key == 'w':
        ang1 += 0.2
    if event.key == 's':
        ang1 -= 0.2
    if event.key == 'a':
        ang2 -= 0.2
    if event.key == 'd':
        ang2 += 0.2
    draw()

fig.canvas.mpl_connect('key_press_event', press)
draw()
plt.show()