import pySTL
from numpy import array
import subprocess

print("counting meshes")
#induce a bash task , count number of meshes inside
task = subprocess.Popen("ls -1 ../Mesh/| wc -l",shell=True,stdout=subprocess.PIPE)
Mesh_No = task.stdout.read()
Mesh_No = int(Mesh_No)

mesh_arr = []

print("started moving all data to blender space coords representation")

for i in range(1, Mesh_No):
             #Load a model from a file.
             model = pySTL.STLmodel('../Mesh/%d.stl'%i)

             #print model properties
             print("Volume  " + str(model.get_volume()))
             c = model.get_centroid()
             print("Centroid " +  "X: " + str(c[0]) + " Y:" + str(c[1]) + "  Z:" + str(c[2]))


             #Translate the model so that the centroid is at the origin.
             model.translate(-c)

             model.write_text_stl('../Mesh/centered/%d.stl'%i)
                                    
print("finished successfully")
