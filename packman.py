from stl import mesh
from slicer import f,F
from a import insert,Node,split,pr,SorT   
import math
import numpy
import stl
from matplotlib import pyplot
from mpl_toolkits import mplot3d

import subprocess
import math
from random import shuffle

N = 1

Tol_x = 1
Tol_y = 1
Tol_z = 1

big_cont = Node([1000,1000,1000],[0,0,0])

print("Hi Coralie")
print("Do you want the output combination to be random each time?")
xx= input()
if xx == "y":
        Randomize = 1
elif xx == "n":
        Randomize = 0

print("counting meshes")
#induce a bash task , count number of meshes inside
task = subprocess.Popen("ls -1 ../Mesh/centered| wc -l",shell=True,stdout=subprocess.PIPE)
Mesh_No = task.stdout.read()
Mesh_No = int(Mesh_No)+1
Mesh_No = list(range(1,Mesh_No))

if Randomize == 1:
     shuffle(Mesh_No)
     
print("translating first mesh into mathematical representations")
M = mesh.Mesh.from_file('../Mesh/centered/%d.stl'%Mesh_No[0])
_,CC,_ = M.get_mass_properties()
M.translate(-CC)
minx, maxx, miny, maxy, minz, maxz = F(M)
M.translate([-1*minx,-1*miny,-1*minz])
M.points = M.points[M.points[:,2].argsort(axis=0)]
box = Node([maxx-minx, maxy-miny, maxz-minz],
           [minx, miny, minz])

print("done translating, now inserting")
cont = split(box, big_cont)
print("done inserting first mesh")
#print([maxx-minx, maxy-miny, maxz-minz],"first")

mesh_arr = [M]
SorT(cont)
for _,i in enumerate(Mesh_No[1:]):
          print("translating mesh %d.stl into mathematical representation"%i)
          M = mesh.Mesh.from_file('../Mesh/centered/%d.stl'%i)
          _,CC,_ = M.get_mass_properties()
          M.translate(-CC)
          minx, maxx, miny, maxy, minz, maxz = F(M)
          M.translate([-1*minx,-1*miny,-1*minz])
          M.points = M.points[M.points[:,2].argsort(axis=0)]
          box_dims = f(M)
          box = Node(box_dims[0:3],
                     box_dims[3:])
          print("inserting mesh %d.stl"%i)
          #print(box_dims)
          coor, rot = insert(box, cont)
          #print(coor,rot)
          SorT(cont)
          if rot is not False:
                  if rot is 'z':
                          M.rotate([0.0, 0.0, box_dims[2]/2], math.radians(90))
                  elif rot is 'y':
                          M.rotate([0.0, box_dims[1]/2, 0.0], math.radians(90))
                  elif rot is 'x':
                          M.rotate([box_dims[0]/2, 0.0, 0.0], math.radians(90))

                  _,CC,_ = M.get_mass_properties()
                  M.translate(-CC)
                  minx, maxx, miny, maxy, minz, maxz = F(M)
                  M.translate([-1*minx,-1*miny,-1*minz])
                  M.points = M.points[M.points[:,2].argsort(axis=0)]

          if coor is False:
                  print("can't insert mesh %d.stl"%i)
                  print("probably a size issue")
                  break
          M.translate([coor[0]*Tol_x/2,coor[1]*Tol_y/2,coor[2]*Tol_z/2])
        
          mesh_arr.append(M)
          print("done inserting mesh %d.stl"%i)
          
print("inserted %d meshes"%len(mesh_arr),"out of a total of %d meshes"%len(Mesh_No))
combined = mesh.Mesh(numpy.concatenate([mesh.data for mesh in mesh_arr]))
task = subprocess.Popen("ls -1v ../Finale",shell=True,stdout=subprocess.PIPE)
last_mesh = task.stdout.read()

if len(last_mesh) == 0:
        combined.save('../Finale/combined_001.stl')
        print("saved file combined_001.stl into Finale folder")
else:
    last_mesh = int(last_mesh[-8:-5])
    combined.save('../Finale/combined_%03d.stl'%(last_mesh+1))
    print("saved file combined_%03d.stl into Finale folder"%(last_mesh+1))

