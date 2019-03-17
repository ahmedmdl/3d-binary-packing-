from stl import mesh
import math
import numpy
import stl
from matplotlib import pyplot
from mpl_toolkits import mplot3d


def F(obj):
    minx = maxx = miny = maxy = minz = maxz = None
    for p in obj.points:
        # p contains (x, y, z)
        if minx is None:
            minx = p[stl.Dimension.X]
            maxx = p[stl.Dimension.X]
            miny = p[stl.Dimension.Y]
            maxy = p[stl.Dimension.Y]
            minz = p[stl.Dimension.Z]
            maxz = p[stl.Dimension.Z]
        else:
            maxx = max(p[stl.Dimension.X], maxx)
            minx = min(p[stl.Dimension.X], minx)
            maxy = max(p[stl.Dimension.Y], maxy)
            miny = min(p[stl.Dimension.Y], miny)
            maxz = max(p[stl.Dimension.Z], maxz)
            minz = min(p[stl.Dimension.Z], minz)
    return minx, maxx, miny, maxy, minz, maxz

def f(obj):
   minx = maxx = miny = maxy = minz = maxz = None
   for p in obj.points:
   # p contains (x, y, z)
      if minx is None:
         minx = p[stl.Dimension.X]
         maxx = p[stl.Dimension.X]
         miny = p[stl.Dimension.Y]
         maxy = p[stl.Dimension.Y]
         minz = p[stl.Dimension.Z]
         maxz = p[stl.Dimension.Z]
         if minx == 0:
             minx = 1000000
         if miny == 0:
             miny = 1000000
         if minz == 0:
             minz = 1000000
      else:
         mix = minx
         miy = miny
         miz = minz
         maxx = max(p[stl.Dimension.X], maxx)
         minx = min(p[stl.Dimension.X], minx)
         maxy = max(p[stl.Dimension.Y], maxy)
         miny = min(p[stl.Dimension.Y], miny)
         maxz = max(p[stl.Dimension.Z], maxz)
         minz = min(p[stl.Dimension.Z], minz)
         if minx == 0:
             minx = mix
         if miny == 0:
             miny = miy
         if minz == 0:
             minz = miz
   return [maxx-minx, maxy-miny, maxz-minz,
           minx, miny, minz]

def split(s,x):
    step = int(len(s) /x)
    print(len(s),step)
    l = []
    i = 0
    h = mesh.Mesh(s.data.copy())
    h.points[step:] =0
    l.append(h)
    i = step
    for a in range(0,x-1):
         h = mesh.Mesh(s.data.copy())
         h.points[:i] = 0
         h.points[i+step:] = 0
         l.append(h)
         i += step
         
    return l
"""
class Node:
     def __init__(self,a=[0]*3,b=[0]*3):
          self.s = a
          self.c = b
          self.left = False
          self.right = False
          self.Rotate = False
          self.occupied = False
          self.visited = False
"""
"""
from slicer import split,f,F
from stl import mesh
from a import insert_consec,Node
import math
import numpy
import stl
from matplotlib import pyplot
from mpl_toolkits import mplot3d

N = 1 # no of boxes to split
M = mesh.Mesh.from_file('centered/6.stl')
_,CC,_ = M.get_mass_properties()
M.translate(-CC)
minx, maxx, miny, maxy, minz, maxz = F(M)
M.translate([-1*minx,-1*miny,-1*minz])
M.points = M.points[M.points[:,2].argsort(axis=0)]
s = split(M,N)

boxes = []
for i in range(0,len(s)):
    boxes.append(f(s[i]))

big_cont = Node([500,500,500],[0,0,0])
h=insert_consec(boxes,big_cont)

N = 1   # no of boxes to split
L = mesh.Mesh.from_file('centered/7.stl')
_,CC,_ = M.get_mass_properties()
L.translate(-CC)
minx, maxx, miny, maxy, minz, maxz = F(L)
L.translate([-1*minx,-1*miny,-1*minz])
L.points = L.points[L.points[:,2].argsort(axis=0)]
s = split(L,N)

h=insert_consec(boxes,h)

N = 1   # no of boxes to split
H = mesh.Mesh.from_file('centered/11.stl')
_,CC,_ = H.get_mass_properties()
H.translate(-CC)
minx, maxx, miny, maxy, minz, maxz = F(H)
H.translate([-1*minx,-1*miny,-1*minz])
H.points = H.points[H.points[:,2].argsort(axis=0)]
s = split(H,N)

boxes = []
for i in range(0,len(s)):
    boxes.append(f(s[i]))

h=insert_consec(boxes,h)

N = 1   # no of boxes to split
A = mesh.Mesh.from_file('centered/8.stl')
_,CC,_ = A.get_mass_properties()
A.translate(-CC)
minx, maxx, miny, maxy, minz, maxz = F(A)
A.translate([-1*minx,-1*miny,-1*minz])
A.points = A.points[A.points[:,2].argsort(axis=0)]
s = split(A,N)

boxes = []
for i in range(0,len(s)):
    boxes.append(f(s[i]))

h=insert_consec(boxes,h)

N = 1   # no of boxes to split
B = mesh.Mesh.from_file('centered/3.stl')
_,CC,_ = B.get_mass_properties()
B.translate(-CC)
minx, maxx, miny, maxy, minz, maxz = F(B)
B.translate([-1*minx,-1*miny,-1*minz])
B.points = B.points[B.points[:,2].argsort(axis=0)]
s = split(B,N)

boxes = []
for i in range(0,len(s)):
    boxes.append(f(s[i]))

h=insert_consec(boxes,h)

N = 1   # no of boxes to split
C = mesh.Mesh.from_file('centered/10.stl')
_,CC,_ = C.get_mass_properties()
C.translate(-CC)
minx, maxx, miny, maxy, minz, maxz = F(C)
C.translate([-1*minx,-1*miny,-1*minz])
C.points = C.points[C.points[:,2].argsort(axis=0)]
s = split(C,N)

boxes = []
for i in range(0,len(s)):
    boxes.append(f(s[i]))

h=insert_consec(boxes,h)

N = 1   # no of boxes to split
D = mesh.Mesh.from_file('centered/12.stl')
_,CC,_ = D.get_mass_properties()
D.translate(-CC)
minx, maxx, miny, maxy, minz, maxz = F(D)
D.translate([-1*minx,-1*miny,-1*minz])
D.points = D.points[D.points[:,2].argsort(axis=0)]
s = split(D,N)

boxes = []
for i in range(0,len(s)):
    boxes.append(f(s[i]))

h=insert_consec(boxes,h)

N = 1   # no of boxes to split
E = mesh.Mesh.from_file('centered/13.stl')
_,CC,_ = E.get_mass_properties()
E.translate(-CC)
minx, maxx, miny, maxy, minz, maxz = F(E)
E.translate([-1*minx,-1*miny,-1*minz])
E.points = E.points[E.points[:,2].argsort(axis=0)]
s = split(E,N)

boxes = []
for i in range(0,len(s)):
    boxes.append(f(s[i]))

h=insert_consec(boxes,h)

M.translate([0,0,0])
H.translate([0,0,45])
L.translate([0,0,95])
A.translate([0,0,150])
B.translate([0,31,152])
C.translate([0,66,152])
D.translate([0,66,152])
E.translate([0,14,0])

#meshes = [M,L,H]
combined = mesh.Mesh(numpy.concatenate([H.data]+[L.data]+[A.data]+[B.data]+[C.data]+[D.data]+[E.data]))
combined.save('combined_lastt.stl')
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)
for m in meshes:
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(m.vectors))

scale = numpy.concatenate([m.points for m in meshes]).flatten(-1)
axes.auto_scale_xyz(scale,scale,scale)
pyplot.show()

combined = mesh.Mesh(numpy.concatenate([L.data]+[M.data]+[H.data])










positions = []
size = []
for i in boxes:
     size.append([i[0],i[1],i[2]])
     positions.append([i[3],i[4],i[5]])



orig = boxes[0]
orig = Node([orig[1] - orig[0],
             orig[3] - orig[2],
             orig[5] - orig[4]],
            [0,0,0])

orig_c = insert_orig(orig)

Node_boxes = []
for box in boxes[1:]:
    Node_boxes.append([box[1] - box[0],
                       box[3] - box[2],
                       box[5] - box[4],
                       orig_c[0] + box[0],
                       orig_c[1] + box[2],
                       orig_c[2] + box[4]])
    
"""
