from sys import getsizeof
from time import time

def space(s1, c1,
          s2, c2,
          s3, c3,
          par, ch1):

    if par == "a":
        p1 = Node(s1, c1)
        if ch1 == "b":
            p2 = Node(s2, c2)
            p3 = Node(s3, c3)
        else:
            p2 = Node(s3, c3)
            p3 = Node(s2, c2)
    elif par == "b":
        p1 = Node(s2, c2)
        if ch1 == "a":
            p2 = Node(s1, c1)
            p3 = Node(s3, c3)
        else:
            p2 = Node(s3, c3)
            p3 = Node(s1, c1)
    else:
        p1 = Node(s3, c3)
        if ch1 == "a":
            p2 = Node(s1, c1)
            p3 = Node(s2, c2)
        else:
            p2 = Node(s2, c2)
            p3 = Node(s1, c1)
            
    return p1, p2, p3

def comp_child(a1,a2,a3):
      vol_a1 = a1[0]* a1[1]* a1[2]
      vol_a2 = a2[0]* a2[1]* a2[2]
      vol_a3 = a3[0]* a3[1]* a3[2]
      
      # 1>2>3, 1>3>2, 3>1>2, 2>1>3, 2>3>1, 3>2>1
      if vol_a1 >= vol_a2:
          if vol_a1 >= vol_a3: #  1>2, 1>3
              par = "a"
              vol = vol_a1

              if vol_a2 >= vol_a3: # 1>2>3
                  child1 = "b"
                  
                  child2 = "c"
              else:                 # 1>3>2
                  child1 = "c"
                  
                  child2 = "b"
                  
          else: #a3 is the biggest  #1>2, 3>1  ,3>1>2
              par = "c"
              
              vol = vol_a3
              
              child1 = "a"
              
              child2 = "b"
 
      elif vol_a2 >= vol_a3:     # 2>1, 2>3 
          par = "b"
          
          vol = vol_a2

          if vol_a1 >= vol_a3:  # 2>1>3
              child1 = "a"
              
              child2 = "c"
          else:                 # 2>3>1
              child1 = "c"
              
              child2 = "a"

      else:                     #1<2, 2<3 , 3>2>1
          par = "c"
          
          vol = vol_a3

          child1 = "b"
          
          child2 = "a"
      
      vol_arr = [vol_a1,vol_a2,vol_a3]
      check(vol_arr,
            [r(par),r(child1),r(child2)])
      #print(vol_a1,vol_a2,vol_a3)
      #print(par,child1,child2)
      return vol, par, child1, child2

def r(x):
    if x == "a":
        return 0
    if x == "b":
        return 1
    if x == "c":
        return 2
    
def check(a,b):
    if( (a[b[0]] < a[b[1]]) or (a[b[1]] < a[b[2]]) ):
        print("error")
        
 
def split(box, cont):
      # yellow
      s_a1= [cont.s[0],
             (cont.s[1] - box.s[1]),
             cont.s[2]]
      
      c_a1= [cont.c[0],
             cont.c[1] + box.s[1],
             cont.c[2]]
      # red
      s_a2= [(cont.s[0] - box.s[0]),
             box.s[1],
             box.s[2]]
      
      c_a2= [cont.c[0] + box.s[0],
             cont.c[1],
             cont.c[2]]
      # white
      s_a3= [cont.s[0],
             box.s[1],
             (cont.s[2] - box.s[2])]
      
      c_a3= [cont.c[0],
             cont.c[1],
             cont.c[2] + box.s[2]]
      
      vol_par_a, par_a, ch1_a, ch2_a = comp_child(s_a1, s_a2, s_a3)
      par_a, ch1_a, ch2_a = space(s_a1, c_a1, s_a2, c_a2, s_a3, c_a3, par_a, ch1_a)
      
      # white
      s_b1 = [cont.s[0],
              cont.s[1],
              (cont.s[2] - box.s[2])]
      
      c_b1 = [cont.c[0],
              cont.c[1],
              cont.c[2] + box.s[2]]
      # red
      s_b2 = [(cont.s[0] - box.s[0]),
              box.s[1],
              box.s[2]]

      c_b2 = [cont.c[0] + box.s[0],
              cont.c[1],
              cont.c[2]]
      # yellow
      s_b3 = [cont.s[0],
              (cont.s[1] - box.s[1]),
              box.s[2]]

      c_b3 = [cont.c[0],
              cont.c[1] + box.s[1],
              cont.c[2]]
      
      vol_par_b, par_b, ch1_b, ch2_b = comp_child(s_b1, s_b2, s_b3)
      par_b, ch1_b, ch2_b = space(s_b1, c_b1, s_b2, c_b2, s_b3, c_b3, par_b, ch1_b)
      
      # red
      s_c1 = [(cont.s[0] - box.s[0]),
              cont.s[1],
              cont.s[2]]

      c_c1 = [cont.c[0] + box.s[0],
              cont.c[1],
              cont.c[2]]
      # white
      s_c2 = [box.s[0],
              cont.s[1],
              cont.s[2] - box.s[2]]

      c_c2 = [cont.c[0],
              cont.c[1],
              cont.c[2] + box.s[2]]
      # yellow
      s_c3 = [box.s[0],
              (cont.s[1] - box.s[1]),
               box.s[2]]

      c_c3 = [cont.c[0],
              cont.c[1] + box.s[1],
              cont.c[2]]
      
      vol_par_c, par_c, ch1_c, ch2_c = comp_child(s_c1, s_c2, s_c3)
      par_c, ch1_c, ch2_c = space(s_c1, c_c1, s_c2, c_c2, s_c3, c_c3, par_c, ch1_c)
      
      #  acb, abc, cab, bac, bca, cba
      if(vol_par_a <= vol_par_b):                   
          if(vol_par_a <= vol_par_c):               # a<b , a<c
              parent = par_a
              parent.occupied = True
              #--------put children-----------
              parent.right = ch1_a
              parent.right.right = ch2_a

              #---------put alternative configs-----------
              #  vol_par_c is in the middle
              if( vol_par_c <= vol_par_b ):                 # a<c<b
                    parent.left = par_c
                    #--------put children-----------
                    parent.left.right = ch1_c
                    parent.left.right.right = ch2_c
                    
                    parent.left.left = par_b   # vol_par_b is the biggest
                    #--------put children-----------
                    parent.left.left.right = ch1_b
                    parent.left.left.right.right = ch2_b

              #  vol_par_b is the middle      
              else:                                         # a<b<c
                    parent.left = par_b
                    #--------put children-----------
                    parent.left.right = ch1_b
                    parent.left.right.right = ch2_b
                    
                    parent.left.left = par_c     #  vol_par_c is the biggest
                    #--------put children-----------
                    parent.left.left.right = ch1_c
                    parent.left.left.right.right = ch2_c

              return parent
                
          else: # vol_par_c is the smallest                 # a>c, c<a<b
                parent= par_c
                parent.occupied = True
                #--------- put children----------
                parent.right = ch1_c       
                parent.right.right = ch2_c

                #---------put alternative configs-----------
                #  vol_par_a is the middle
                parent.left = par_a
                #--------put children-----------
                parent.left.right = ch1_a
                parent.left.right.right = ch2_a

                parent.left.left = par_b
                #--------put children-----------
                parent.left.left.right = ch1_b
                parent.left.left.right.right = ch2_b
                return parent
            
      # vol_par_b is the smallest                 
      elif(vol_par_b <= vol_par_c):                        #b<c
          parent = par_b
          parent.occupied = True
          #------------- put children-----------
          parent.right = ch1_b
          parent.right.right = ch2_b

          #---------------put alternative config------
          #  vol_par_a is the middle
          if( vol_par_a <= vol_par_c ):                     # b<a<c
                parent.left = par_a
                #------------- put children-----------
                parent.left.right = ch1_a
                parent.left.right.right = ch2_a

                parent.left.left = par_c
                #------------- put children-----------
                parent.left.left.right = ch1_c
                parent.left.left.right.right = ch2_c

          #   vol_par_c is the middle
          else:                                            # b<c<a
                parent.left = par_c
                #------------- put children-----------
                parent.left.right = ch1_c
                parent.left.right.right = ch2_c
                
                parent.left.left = par_a
                #------------- put children-----------
                parent.left.left.right = ch1_a
                parent.left.left.right.right = ch2_a

          return parent
              
      else: #c is the smallest                            # b<a, c<b,  c<b<a
                parent = par_c
                parent.occupied = True
                #---------- put children--------
                parent.right = ch1_c
                parent.right.right = ch2_c

                #------------- put alt configs ----------
                #  vol_par_a is the middle
                parent.left = par_a
                #------------- put children-----------
                parent.left.right = ch1_a
                parent.left.right.right = ch2_a
                
                parent.left.left = par_b
                #------------- put children-----------
                parent.left.left.right = ch1_b
                parent.left.left.right.right = ch2_b
                
                return parent
            
def insert(box, ptr):
        prev_parent = Node([0,0,0],[0,0,0])
        parent = Node([0,0,0],[0,0,0])
        child = ptr
        s = child
        done = False
        
        #  if box fits try smaller container of the same config
        while fits(box, child):
              prev_parent= parent
              #  eliminate the alternate configs
              if prev_parent.left is not False:
                  prev_parent.left = False
                  #prev_parent.left.left = False
              parent = child
              child = child.right
              # box fits but no children yet 
              if child is False:
                  visited = [parent.c[0],parent.c[1],parent.c[2]]
                  parent = split(box, parent)
                  #parent.visited = visited
                  #parent.right.visited = visited
                  #parent.right.right.visited = visited
                  parent.right.right.right = child
                  prev_parent.right = parent
                  print("done")
                  return prev_parent
              
        # item didn't even go into the while loop and it doesn't fit from the beginning
        if parent.s == [0,0,0]:
            print("box is too big")
            print("stop eating thyroid")
            return False
                
        if not fits(box, child ) and rotatefit(box, child):
                print("rotating")
                tmp = child.right
                visited = [parent.c[0],parent.c[1],parent.c[2]]
                child = split(box, child)
                #child.visited = visited
                #child.right.visited = visited
                #child.right.right.visited = visited
                child.right.right.right = tmp
                parent.right = child
                print("done")
                return parent
            
        if not fits(box, child ):
            if prev_parent.s == [0,0,0]:
                visited = [parent.c[0],parent.c[1],parent.c[2]]
                parent = split(box, parent)
                #parent.visited = visited
                #parent.right.visited = visited
                #parent.right.right.visited = visited
                parent.right.right.right = child
                #parent.visited= visited
                print("jj")
                return parent
            # try combining
            #Fit(remainder(box,child),adj(child, big_cont),child,box,big_cont)
            x = Fit(remainder(box,child),adj(child, s),child,box,s)
            if x is not False:
                print("**************************************")
                pr(x)
                print("**************************************")
                return x
            print("ss")
            visited = [parent.c[0],parent.c[1],parent.c[2]]
            parent = split(box, parent)
            #parent.visited = visited
            #parent.right.visited = visited
            #parent.right.right.visited = visited
            prev_parent.right = parent
            prev_parent.right.right.right.right = child
            return prev_parent
        print("kofta")

def insert_left(box,ptr):
     # try another config first when box doesn't fit       
        if( child.left is not False and
           child is not False):
            if fits(box, child.left):
                done = insert(box, child.left)

                # box fits in one the current config's children
                if done is not False:
                    # config's last child right points to the last config's next right neighbour
                    # get the last pointer in the current config after it split
                    tmp_ptr = done
                    while tmp_ptr.right is not False:
                        tmp_ptr = tmp_ptr.right
                        
                    tmp_ptr.right = child.right.right.right
                    parent.right = done 
                    return done
                
                # box only fits in the config's parent
                elif done is False:
                    parent.right = split(box, child.left)
                    parent.right.right.right.right= child
                    return parent
                
            if fits(box, child.left.left):
                done = insert(box, child.left.left)

                # box fits in one the current config's children
                if done is not False:
                    # config's last child right points to the last config's next right neighbour
                    # get the last pointer in the current config after it split
                    tmp_ptr = done
                    while tmp_ptr.right is not False:
                        tmp_ptr = tmp_ptr.right
                        
                    tmp_ptr.right = child.right.right.right
                    parent.right = done 
                    return done
                
                # box only fits in the config's parent
                elif done is False:
                    parent.right = split(box, child.left.left)
                    parent.right.right.right.right= child
                    return parent
        
def fits(box, ptr):
    if( (box.s[0] < ptr.s[0]) and
        (box.s[1] < ptr.s[1]) and
        (box.s[2] < ptr.s[2]) ):

       return True
    else:
        return False
                  
def rotatefit(box, ptr):   
   if( (box.s[0] < ptr.s[0]) and
       (box.s[2] < ptr.s[1]) and
       (box.s[1] < ptr.s[2]) ):
         print("x rotation")

         ptr.Rotate = 'x'
         tmp = box.s[2]
         box.s[2] = box.s[1]
         box.s[1] = tmp
         return True
     
   elif( (box.s[2] < ptr.s[0]) and
         (box.s[1] < ptr.s[1]) and
         (box.s[0] < ptr.s[2]) ):
        print("y rotation")

        ptr.Rotate = 'y'
        tmp = box.s[2]
        box.s[2] = box.s[0]
        box.s[0] = tmp
        return True
    
   elif( (box.s[1] < ptr.s[0]) and
         (box.s[0] < ptr.s[1]) and
         (box.s[2] < ptr.s[2]) ):
        print("z rotation")

        ptr.Rotate = 'z'
        tmp = box.s[1]
        box.s[1] = box.s[0]
        box.s[0] = tmp
        return True
   else:
        return False
    
class Node:
     def __init__(self,a=[0]*3,b=[0]*3,c=False):
          self.s = a
          self.c = b
          self.left = False
          self.right = False
          self.Rotate = False
          #self.occupied = False
          self.visited = c

class c:
     def __init__(self,x,y,z):
          self.x = x
          self.y = y
          self.z = z
          self.cx = self.cy = self.cz = 0

def vol(p):
    #print(p.s[0]* p.s[1]* p.s[2])
    return(p.s[0]* p.s[1]* p.s[2])

def remainder(box, cont):
    return [box.s[0] - cont.s[0],
            box.s[1] - cont.s[1],
            box.s[2] - cont.s[2]]

def adj(cont, big_cont):

    arr = []
    ptr = big_cont
    while ptr.right is not False:

             if( (cont.c[1] + cont.s[1] == ptr.c[1]) and
                 (ptr.c[0] <= cont.c[0] <=  ptr.c[0] + ptr.s[0]) and
                 (ptr.c[2] <= cont.c[2] <=  ptr.c[2] + ptr.s[2]) ):

                       arr.append([ptr,"py"])

             if( (cont.c[1] == ptr.c[1] + ptr.s[1] ) and
                 (ptr.c[0] <= cont.c[0] <=  ptr.c[0] + ptr.s[0]) and
                 (ptr.c[2] <= cont.c[2] <=  ptr.c[2] + ptr.s[2]) ):

                       arr.append([ptr,"ny"])

             if( (cont.c[0] + cont.s[0] == ptr.c[0]) and
                 (ptr.c[1] <= cont.c[1] <=  ptr.c[1] + ptr.s[1]) and
                 (ptr.c[2] <= cont.c[2] <=  ptr.c[2] + ptr.s[2]) ):

                       arr.append([ptr,"px"])

             if( (cont.c[0] == ptr.c[0] + ptr.s[0] ) and
                 (ptr.c[1] <= cont.c[1] <=  ptr.c[1] + ptr.s[1]) and
                 (ptr.c[2] <= cont.c[2] <=  ptr.c[2] + ptr.s[2]) ):

                       arr.append([ptr,"nx"])

             if( (cont.c[2] + cont.s[2] == ptr.c[2]) and
                 (ptr.c[0] <= cont.c[0] <=  ptr.c[0] + ptr.s[0]) and
                 (ptr.c[1] <= cont.c[1] <=  ptr.c[1] + ptr.s[1]) ):

                       arr.append([ptr,"pz"])

             if( (cont.c[2] == ptr.c[2] + ptr.s[2]) and
                 (ptr.c[0] <= cont.c[0] <=  ptr.c[0] + ptr.s[0]) and
                 (ptr.c[1] <= cont.c[1] <=  ptr.c[1] + ptr.s[1]) ):

                       arr.append([ptr,"nz"])

             ptr = ptr.right
    print('sdasd')         
    return arr

def arr_fits(a,ptr):
    if( (a[0] < ptr.s[0]) and
        (a[1] < ptr.s[1]) and
        (a[2] < ptr.s[2]) ):

       return True
    else:
        return False

def assemble(new,
             cont,
             big_cont,
             ptr):
    
    tmp_ptr= big_cont

    while tmp_ptr.right != False:
        if tmp_ptr == cont:
            print("B")
            #print(ptr.c[0],ptr.c[1],ptr.c[2],"ptr")
            #print(cont.c[0],cont.c[1],cont.c[2],"cont")
            tmp_ptr.s[0] = 0
            tmp_ptr.s[1] = 0
            tmp_ptr.s[2] = 0
        if tmp_ptr == ptr:
            print("C")
            #print(ptr.c[0],ptr.c[1],ptr.c[2],"ptr")
            #print(cont.c[0],cont.c[1],cont.c[2],"cont")
            tmp_ptr.s[0] = 0
            tmp_ptr.s[1] = 0
            tmp_ptr.s[2] = 0
        tmp_ptr = tmp_ptr.right     

    tnmp = new
    new.right.right.right.right.right.right.right.right = big_cont

    return SorT(tnmp)
        
def Fit(rem_arr,
        adj_arr,
        ptr,
        box,
        big_cont):
    print("as")
    for i in adj_arr:
        if( i[1] == "py" and arr_fits([rem_arr[0],rem_arr[1],rem_arr[2]],
                                      i[0])):
            
            return assemble(fit_py(i[0],ptr,box), i[0], big_cont, ptr)
            
        elif( i[1] == "ny" and arr_fits([rem_arr[0],rem_arr[1],rem_arr[2]],
                                        i[0])):
            
            return assemble(fit_ny(i[0],ptr,box), i[0],big_cont, ptr)
            
        elif( i[1] == "px" and arr_fits([rem_arr[0],rem_arr[1],rem_arr[2]],
                                        i[0])):
            
            return assemble(fit_px(i[0],ptr,box), i[0],big_cont, ptr)
            
        elif( i[1] == "nx" and arr_fits([rem_arr[0],rem_arr[1],rem_arr[2]],
                                        i[0])):
            
            return assemble(fit_nx(i[0],ptr,box), i[0],big_cont, ptr)
            
        elif( i[1] == "pz" and arr_fits([rem_arr[0],rem_arr[1],rem_arr[2]],
                                        i[0])):
            
            return assemble(fit_pz(i[0],ptr,box), i[0],big_cont, ptr)
            
        elif( i[1] == "nz" and arr_fits([rem_arr[0],rem_arr[1],rem_arr[2]],
                                        i[0])):
            
            return assemble(fit_nz(i[0],ptr,box), i[0],big_cont, ptr)
        else:
            print("no fit")
            return False

# splitting the box's parent cont is not done yet
def fit_py(cont,ptr,b):
     c1 = Node([0,0,0],[0,0,0])
     c2 = Node([0,0,0],[0,0,0])
     c3 = Node([0,0,0],[0,0,0])
     c4 = Node([0,0,0],[0,0,0])
     c5 = Node([0,0,0],[0,0,0])
     print(ptr.c[0],ptr.c[1],ptr.c[2],"py ptr")
     print(cont.c[0],cont.c[1],cont.c[2],"py cont")
     #print("py")
     #print(hex(id(c1.c)),hex(id(c5.c)))

     c1.c[0] = cont.c[0]
     c1.c[1] = cont.c[1]
     c1.c[2] = cont.c[2]

     c1.s[0] = ptr.c[0] - cont.c[0]
     c1.s[1] = cont.s[1]
     c1.s[2] = cont.s[2]
     
     #print(cont.c[2],c1.c[2])
     
     c2.c[0] = ptr.c[0] 
     c2.c[1] = cont.c[1]
     c2.c[2] = cont.c[2]

     c2.s[0] = cont.s[0] - (ptr.c[0] - cont.c[0])
     c2.s[1] = b.s[1] - ptr.s[1]
     c2.s[2] = ptr.c[2] - cont.c[2] 
     #print(cont.c[2],c1.c[2])
     c3.c[0] = ptr.c[0]
     c3.c[1] = cont.c[1] + (b.s[1] - ptr.s[1])
     c3.c[2] = cont.c[2]
     
     c3.s[0] = cont.s[0] - (ptr.c[0] - cont.c[0])
     #print(cont.c[2],c1.c[2])

     c3.s[1] = cont.s[1] - (b.s[1] - ptr.s[1])
     c3.s[2] = cont.s[2]
     
     c4.c[0] = ptr.c[0] + b.s[0]
     c4.c[1] = cont.c[1]
     
     c4.c[2] = ptr.c[2]
     #print(ptr.c[2])
     #print(cont.c[2],c1.c[2])
     #print(cont.c[2],c1.c[2])

     c4.s[0] = cont.s[0] - ((ptr.c[0] - cont.c[0]) + b.s[0])
     c4.s[1] = (b.s[1] - ptr.s[1])
     c4.s[2] = cont.s[2] - (ptr.c[2] - cont.c[2])
     
     #print(cont.c[2],c1.c[2])
     
     c5.c[0] = ptr.c[0]
     c5.c[1] = cont.c[1]
     c5.c[2] = ptr.c[2] + b.s[2]
     #print(hex(id(c5.c[2])))

     c5.s[0] = b.s[0]
     c5.s[1] = b.s[1] - ptr.s[1]
     c5.s[2] = cont.s[2] - (b.s[2] +(ptr.c[2] - cont.c[2]))

     #print(cont.c[2],hex(id(c1.c)),hex(id(c5.c)))

     c1.right = c2
     c2.right = c3
     c3.right = c4
     c4.right = c5
     b.s[1] = ptr.s[1]
     c5.right = split(b,ptr)
     print("py")
     print(ptr.c[0],ptr.c[1],ptr.c[2],"py ptr")
     print(cont.c[0],cont.c[1],cont.c[2],"py cont")
     return c1

def fit_ny(cont,ptr,b):
      c1 = Node([0,0,0],[0,0,0])
      c2 = Node([0,0,0],[0,0,0])
      c3 = Node([0,0,0],[0,0,0])
      c4 = Node([0,0,0],[0,0,0])
      c5 = Node([0,0,0],[0,0,0])

      print("ny")
      
      c1.c[0] = cont.c[0]
      c1.c[1] = cont.c[1]
      c1.c[2] = cont.c[2]

      c1.s[0] = ptr.c[0] - cont.c[0]
      c1.s[1] = cont.s[1]
      c1.s[2] = cont.s[2]

      c2.c[0] = ptr.c[0]
      c2.c[1] = cont.c[1]
      c2.c[2] = cont.c[2]

      c2.s[0] = cont.s[0] - (ptr.c[0] - cont.c[0])
      c2.s[1] = cont.s[1] - (b.s[1] - ptr.s[1])
      c2.s[2] = cont.s[2]

      c3.c[0] = ptr.c[0]
      c3.c[1] = cont.c[1] + (cont.s[1] - (b.s[1] - ptr.s[1]))
      c3.c[2] = cont.c[2]

      c3.s[0] = cont.s[0] - (ptr.c[0] - cont.c[0])
      c3.s[1] = b.s[1] - ptr.s[1]
      c3.s[2] = ptr.c[2] - cont.c[2]

      c4.c[0] = ptr.c[0] + b.s[0]
      c4.c[1] = cont.c[1] + (cont.s[1] - (b.s[1] - ptr.s[1]))
      c4.c[2] = ptr.c[2]

      c4.s[0] = cont.s[0] - ((ptr.c[0] - cont.c[0]) + b.s[0])
      c4.s[1] = b.s[1] - ptr.s[1]
      c4.s[2] = cont.s[2] - (ptr.c[2] - cont.c[2]) 

      c5.c[0] = ptr.c[0]
      c5.c[1] = cont.c[1] + (cont.s[1] - (b.s[1] - ptr.s[1]))
      c5.c[2] = ptr.c[2] + b.s[2]

      c5.s[0] = b.s[0]
      c5.s[1] = b.s[1] - ptr.s[1]
      c5.s[2] = cont.s[2] - (b.s[2] + (ptr.c[2] - cont.c[2]))

      c1.right = c2
      c2.right = c3
      c3.right = c4
      c4.right = c5
      b.s[1] = ptr.s[1]
      c5.right = split(b,ptr)
      print(ptr.c[0],ptr.c[1],ptr.c[2],"ny ptr")
      print(cont.c[0],cont.c[1],cont.c[2],"ny cont")
      return c1

def fit_pz(cont,ptr,b):
      c1 = Node([0,0,0],[0,0,0])
      c2 = Node([0,0,0],[0,0,0])
      c3 = Node([0,0,0],[0,0,0])
      c4 = Node([0,0,0],[0,0,0])
      c5 = Node([0,0,0],[0,0,0])

      print("pz")
      
      c1.c[0] = cont.c[0]
      c1.c[1] = cont.c[1]
      c1.c[2] = cont.c[2]

      c1.s[0] = ptr.c[0] - cont.c[0]
      c1.s[1] = cont.s[1]
      c1.s[2] = cont.s[2]

      c2.c[0] = ptr.c[0]
      c2.c[1] = cont.c[1]
      c2.c[2] = cont.c[2]

      c2.s[0] = cont.s[0] - (ptr.c[0] - cont.c[0])
      c2.s[1] = ptr.c[1] - cont.c[1]
      c2.s[2] = cont.s[2]

      c3.c[0] = ptr.c[0]
      c3.c[1] = b.s[1] + ptr.c[1]
      c3.c[2] = cont.c[2]

      c3.s[0] = cont.s[0] - (ptr.c[0] - cont.c[0])
      c3.s[1] = cont.s[1] - (b.s[1] + (ptr.c[1] - cont.c[1]))
      c3.s[2] = cont.s[2]

      c4.c[0] = ptr.c[0] + b.s[0]
      c4.c[1] = ptr.c[1]
      c4.c[2] = cont.c[2]

      c4.s[0] = cont.s[0] - (b.s[0] + (ptr.c[0] - cont.c[0]))
      c4.s[1] = b.s[1]
      c4.s[2] = cont.s[2]

      c5.c[0] = ptr.c[0]
      c5.c[1] = ptr.c[1]
      c5.c[2] = cont.c[2] + (b.s[2] - ptr.s[2])

      c5.s[0] = b.s[0]
      c5.s[1] = b.s[1]
      c5.s[2] = cont.s[2] - (b.s[2] - ptr.s[2])
      
      c1.right = c2
      c2.right = c3
      c3.right = c4
      c4.right = c5
      b.s[2] = ptr.s[2]
      c5.right = split(b,ptr)
      print(ptr.c[0],ptr.c[1],ptr.c[2],"pz ptr")
      print(cont.c[0],cont.c[1],cont.c[2],"pz cont")
      return c1

def fit_nz(cont,ptr,b):
      c1 = Node([0,0,0],[0,0,0])
      c2 = Node([0,0,0],[0,0,0])
      c3 = Node([0,0,0],[0,0,0])
      c4 = Node([0,0,0],[0,0,0])
      c5 = Node([0,0,0],[0,0,0])

      print("nz")
      
      c1.c[0] = cont.c[0]
      c1.c[1] = cont.c[1]
      c1.c[2] = cont.c[2]

      c1.s[0] = ptr.c[0] - cont.c[0]
      c1.s[1] = cont.s[1]
      c1.s[2] = cont.s[2]

      c2.c[0] = ptr.c[0]
      c2.c[1] = cont.c[1]
      c2.c[2] = cont.c[2]

      c2.s[0] = cont.s[0] - (ptr.c[0] - cont.c[0])
      c2.s[1] = ptr.c[1] - cont.c[1]
      c2.s[2] = cont.s[2]

      c3.c[0] = ptr.c[0]
      c3.c[1] = ptr.c[1]
      c3.c[2] = cont.c[2]

      c3.s[0] = b.s[0]
      c3.s[1] = b.s[1]
      c3.s[2] = cont.s[2] - (b.s[2] - ptr.s[2])

      c4.c[0] = ptr.c[0]
      c4.c[1] = ptr.c[1] + b.s[1]
      c4.c[2] = cont.c[2]

      c4.s[0] = cont.s[0] - (ptr.c[0] - cont.c[0])
      c4.s[1] = cont.s[1] - (b.s[1] + (ptr.c[1] - cont.c[1]))
      c4.s[2] = cont.s[2]

      c5.c[0] = ptr.c[0] + b.s[0]
      c5.c[1] = ptr.c[1]
      c5.c[2] = cont.c[2]

      c5.s[0] = cont.s[0] - (b.s[0] + (ptr.c[0] - cont.c[0]))
      c5.s[1] = b.s[1]
      c5.s[2] = cont.s[2]

      c1.right = c2
      c2.right = c3
      c3.right = c4
      c4.right = c5
      b.s[2] = ptr.s[2]
      c5.right = split(b,ptr)
      print(ptr.c[0],ptr.c[1],ptr.c[2],"nz ptr")
      print(cont.c[0],cont.c[1],cont.c[2],"nz cont")
      return c1

def fit_nx(cont,ptr,b):
      c1 = Node([0,0,0],[0,0,0])
      c2 = Node([0,0,0],[0,0,0])
      c3 = Node([0,0,0],[0,0,0])
      c4 = Node([0,0,0],[0,0,0])
      c5 = Node([0,0,0],[0,0,0])

      print("nx")
      
      c1.c[0] = cont.c[0]
      c1.c[1] = cont.c[1]
      c1.c[2] = cont.c[2]

      c1.s[0] = cont.s[0] - (b.s[0] - ptr.s[0])
      c1.s[1] = cont.s[1]
      c1.s[2] = cont.s[2]

      c2.c[0] = cont.c[0] + (cont.s[0] - (b.s[0] - ptr.s[0])) 
      c2.c[1] = cont.c[1]
      c2.c[2] = cont.c[2]

      c2.s[0] = b.s[0] - ptr.s[0]
      c2.s[1] = ptr.c[1] - cont.c[1]
      c2.s[2] = cont.s[2]

      c3.c[0] = cont.c[0] + (cont.s[0] - (b.s[0] - ptr.s[0]))
      c3.c[1] = ptr.c[1]
      c3.c[2] = cont.c[2]

      c3.s[0] = b.s[0] - ptr.s[0]
      c3.s[1] = b.s[1]
      c3.s[2] = ptr.c[2] - cont.c[2]

      c4.c[0] = cont.c[0] + (cont.s[0] - (b.s[0] - ptr.s[0]))
      c4.c[1] = ptr.c[1] + b.s[1]
      c4.c[2] = cont.c[2]

      c4.s[0] = b.s[0] - ptr.s[0]
      c4.s[1] = cont.s[1] - (b.s[1] + (ptr.c[1] - cont.c[1]))
      c4.s[2] = cont.s[2]

      c5.c[0] = cont.c[0] + (cont.s[0] - (b.s[0] - ptr.s[0]))
      c5.c[1] = ptr.c[1]
      c5.c[2] = ptr.c[2] + b.s[2]

      c5.s[0] = b.s[0] - ptr.s[0]
      c5.s[1] = b.s[1]
      c5.s[2] = cont.s[2] - (b.s[2] + (ptr.c[2] - cont.c[2]))

      c1.right = c2
      c2.right = c3
      c3.right = c4
      c4.right = c5
      b.s[0] = ptr.s[0]
      c5.right = split(b,ptr)
      print(ptr.c[0],ptr.c[1],ptr.c[2],"nx ptr")
      print(cont.c[0],cont.c[1],cont.c[2],"nx cont")

      return c1

def fit_px(cont,ptr,b):
      c1 = Node([0,0,0],[0,0,0])
      c2 = Node([0,0,0],[0,0,0])
      c3 = Node([0,0,0],[0,0,0])
      c4 = Node([0,0,0],[0,0,0])
      c5 = Node([0,0,0],[0,0,0])

      #print("px")
      
      c1.c[0] = cont.c[0]
      c1.c[1] = cont.c[1]
      c1.c[2] = cont.c[2]

      c1.s[0] = cont.s[0] 
      c1.s[1] = ptr.c[1] - cont.c[1]
      c1.s[2] = cont.s[2]

      c2.c[0] = cont.c[0] + (b.s[0] - ptr.s[0])
      c2.c[1] = ptr.c[1]
      c2.c[2] = cont.c[2]

      c2.s[0] = cont.s[0] - (b.s[0] - ptr.s[0])
      c2.s[1] = b.s[1]
      c2.s[2] = cont.s[2]

      c3.c[0] = cont.c[0]
      c3.c[1] = cont.c[1] + (b.s[1] +(ptr.c[1] - cont.c[1]))
      c3.c[2] = cont.c[2]

      c3.s[0] = cont.s[0]
      c3.s[1] = cont.s[1] - (b.s[1] +(ptr.c[1] - cont.c[1]))
      c3.s[2] = cont.s[2]

      c4.c[0] = cont.c[0]
      c4.c[1] = ptr.c[1] 
      c4.c[2] = b.s[2] + ptr.c[2]

      c4.s[0] = b.s[0] - ptr.s[0]
      c4.s[1] = b.s[1]
      c4.s[2] = cont.s[2] - (b.s[2] +(ptr.c[2] - cont.c[2]))

      c5.c[0] = cont.c[0]
      c5.c[1] = ptr.c[1]
      c5.c[2] = cont.s[2]

      c5.s[0] = b.s[0] - ptr.s[0]
      c5.s[1] = b.s[1]
      c5.s[2] = ptr.c[2] - cont.c[2]

      c1.right = c2
      c2.right = c3
      c3.right = c4
      c4.right = c5
      b.s[0] = ptr.s[0]
      c5.right = split(b,ptr)
      print("px")
      print(ptr.c[0],ptr.c[1],ptr.c[2],"px ptr")
      print(cont.c[0],cont.c[1],cont.c[2],"px cont")

      return c1
              
def pr(ptr):
    a=ptr
    size = []
    positions = []
    while a is not False:
      size.append(a.s)
      positions.append(a.c)
      a=a.right
    print(positions)
    print(size)

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if vol(L[i]) > vol(R[j]): 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
def SorT(p):
    tmp = p
    arr = []
    while tmp != False:
        if( tmp.s[0] == 0 or
            tmp.s[1] == 0 or
            tmp.s[2] == 0):
              tmp = tmp.right
              continue
        """  
        if( tmp.s[0] == 300 and
            tmp.s[1] == 300 and
            tmp.s[2] == 300):
               tmp = tmp.right
               continue
        """   
        arr.append(tmp)
        tmp = tmp.right
    mergeSort(arr)
    return convarr(arr)

def convarr(a):
    p = a[0]
    tmp = p
    for i in a[1:]:
        i.right=False
        i.left = False
        tmp.right = i
        tmp = tmp.right
    return p

# look for rectangles, if one of its sides is beyond a certain length,check adj and treat it as a box 
# def combine(a):
# traverse tree, if origin fits , mark this as origin visited

# convert mesh into [[size][position related to origin]]
# traverse tree, if origin fits, 
# put each mesh in respective place:
#   add origin coordinate to each mesh
#   check if place is visited:
#         check if mesh (origin plus size) added to all visited (origin plus size) is bigger than the cont:
#               if bigger check adj fits:
#                           if not return False,shortage array
# if all fits              
# mark place as visited and put our size and coords inside but no split
# insert consecutive points in pointer into container
def deep_copy(big_cont):
    tmp_ptr = big_cont
    copy_cont = Node([tmp_ptr.s[0],tmp_ptr.s[1],tmp_ptr.s[2]],
                     [tmp_ptr.c[0],tmp_ptr.c[1],tmp_ptr.c[2]])
    copy_cont.visited = True
    tmp_ptr_cont = copy_cont
    tmp_ptr = tmp_ptr.right
    while tmp_ptr is not False:
        tmp_ptr_cont.right = Node([tmp_ptr.s[0],tmp_ptr.s[1],tmp_ptr.s[2]],
                                  [tmp_ptr.c[0],tmp_ptr.c[1],tmp_ptr.c[2]])
        
        tmp_ptr_cont = tmp_ptr_cont.right
        tmp_ptr = tmp_ptr.right
        
    return copy_cont
    
def insert_origin(ptr, big_cont,var):
    big_cont_ptr = big_cont
    pr(big_cont)
    #print(big_cont_ptr.visited)
    tmp_cont = deep_copy(big_cont)
    #print(big_cont_ptr.visited)
    tmp_ptr = tmp_cont
    pr(tmp_ptr)  
    # check if max,min x,y,z can be placed if coord is in that place
    # (max x, min y, min z),(max x,max y , min z) ...................... 
    # check_bounds(tmp_ptr, big_cont)
    """
    while tmp_ptr is not False:
        print(big_cont_ptr.visited)
        if big_cont_ptr.visited is False:
              print("aaaaaaaaaaaaaaa")
              big_cont_ptr.visited = True
              if within(Node([ptr[0], ptr[1], ptr[2]],
                             [tmp_ptr.c[0]+ptr[3], tmp_ptr.c[1]+ptr[4], tmp_ptr.c[2]+ptr[5]]), tmp_ptr, tmp_cont):
                
                  return [tmp_ptr.c[0]+ptr[3], tmp_ptr.c[1]+ptr[4], tmp_ptr.c[2]+ptr[5]], tmp_cont
        print("aaaaaaaaaaaaaaa")      
        big_cont_ptr = big_cont_ptr.right
        tmp_ptr = tmp_ptr.right
    """
    while tmp_ptr is not False:
        """
        varr = var
        x= tmp_ptr.c[0]+ptr[3] +varr
        y= tmp_ptr.c[1]+ptr[4] +varr
        z= tmp_ptr.c[2]+ptr[5] +varr
        while( x < tmp_ptr.c[0]+tmp_ptr.s[0] and
               y < tmp_ptr.c[1]+tmp_ptr.s[1] and
               z < tmp_ptr.c[2]+tmp_ptr.s[2] ):
        
                  x += varr
                  y += varr
                  z += varr
                  print("**********************")
                  print(varr)
                  print("**********************")
                  if within(Node([ptr[0], ptr[1], ptr[2]],[x, y, z]),
                            tmp_ptr,
                            tmp_cont):
                      return [x,y,z], tmp_cont,varr
                  
                  varr += 1 
        """
        varr = var
        x= tmp_ptr.c[0]+ptr[3] +varr
        y= tmp_ptr.c[1]+ptr[4] +varr
        z= tmp_ptr.c[2]+ptr[5] +varr

        if within(Node([ptr[0], ptr[1], ptr[2]],[x, y, z]),
                        tmp_ptr,
                        tmp_cont):
            return [x,y,z], tmp_cont
        
        tmp_ptr = tmp_ptr.right
    return False,False

def insert_consec(boxes, big_cont):
    var = 0
    origin_c ,orig_cont = insert_origin(boxes[0], big_cont,var)
    if origin_c is False:
        print("box too big..... stop eating thyroid")
        return False
    print("*********************************************************")
    print("first origin done")
    print(origin_c)
    while insert_rest(origin_c, boxes[1:], orig_cont) is False :
         print(origin_c)
         #print(hex(id(orig_cont)),hex(id(big_cont)))
         #print(boxes[0])
         origin_c, orig_cont = insert_origin(boxes[0], big_cont,var)
         var += 1
         print("************************origin_C*************")
         print(origin_c)
         #checkbounds()
         if origin_c is False:
             print("box couldn't fit after all retries")
             return False
    big_cont = orig_cont
    #cleanup(big_cont)
    print("done inserting")
    print("final origin")
    print(origin_c)
    return orig_cont, origin_c

# box_arr = [box.s0,box.s1,box.s2,box.c0,box.c1,box.c2]
def insert_rest(orig_c, box_arr,big_cont):    
    for box_ptr in box_arr:
       box = Node([box_ptr[0],
                   box_ptr[1],
                   box_ptr[2]],
                   [orig_c[0] + box_ptr[3],
                    orig_c[1] + box_ptr[4],
                    orig_c[2] + box_ptr[5]])
       if fits_consec(box ,big_cont):
            #clean(big_cont)
            continue
       else:
           return False
       
    return True
           
# iterates over the whole big_cont to find the cont with the
# right coords and dimensions to contain the box
def fits_consec(box, big_cont):
    tmp_ptr = big_cont
    while tmp_ptr is not False:
        if within(box, tmp_ptr, big_cont):
            return True
        else:
            tmp_ptr = tmp_ptr.right
        
    return False

"""
def splitter(big_cont):
    tmp = big_cont
    while tmp is not False:
        if len(tmp.child) > 0:
            tmp_ptr = Node(tmp.s,tmp.c)
            for child in tmp.child:
                tmp_ptr = split(tmp_ptr,child)
                
           
def insert_child(cont,child):
    ptr = cont
    while ptr is not False:
        if fits(ptr,child):
            tmp = ptr.right
            ptr.right = split(box,ptr)
            ptr.right.right.right.right = tmp
            # make its size zero and cleaner will remove it
            # instead of dealing with the whole parent,child issue
            ptr.s = [0,0,0]
            return True
        if fits(ptr.left,child):
            tmp = ptr.right
            ptr.right = split(box,ptr.left)
            ptr.right.right.right.right = tmp
            # make its size zero and cleaner will remove it
            # instead of dealing with the whole parent,child issue
            ptr.s = [0,0,0]
            return True            
        ptr = ptr.right
    return False
"""                            
def within(box, cont,big_cont):
    print("box.c", box.c[0],box.c[1],box.c[2])
    print("box.s", box.s[0],box.s[1],box.s[2])
    print("cont.c", cont.c[0],cont.c[1],cont.c[2])
    print("cont.s", cont.s[0],cont.s[1],cont.s[2])
    
    if( cont.c[0] <= box.c[0] <= cont.c[0] + cont.s[0] and
        cont.c[1] <= box.c[1] <= cont.c[1] + cont.s[1] and
        cont.c[2] <= box.c[2] <= cont.c[2] + cont.s[2] ):

        if( cont.c[0] <= box.c[0]+ box.s[0] <= cont.c[0] + cont.s[0] and
            cont.c[1] <= box.c[1]+ box.s[1] <= cont.c[1] + cont.s[1] and
            cont.c[2] <= box.c[2]+ box.s[2] <= cont.c[2] + cont.s[2] ):

                   #cont.child.append([box.s[0],box.s[1],box.s[2],box.c[0],box.c[1],box.c[2]])

                   tmp = cont.right
                   cont.right = split(box,cont)
                   cont.right.right.right.right = tmp
                   # make its size zero and cleaner will remove it
                   # instead of dealing with the whole parent,child issue
                   cont.s = [0,0,0]
                   print("within")
                   return True
        else:
            # we make a box out of the remains  
            x_diff = box.c[0] + box.s[0] - (cont.c[0] + cont.s[0])
            y_diff = box.c[1] + box.s[1] - (cont.c[1] + cont.s[1])
            z_diff = box.c[2] + box.s[2] - (cont.c[2] + cont.s[2])
            
            #probably box is not bigger than cont in all directions
            if x_diff <= 0:
                x_coor = box.c[0]
                x_diff = box.s[0]
                px_done = True
            else:
                x_coor = cont.c[0] + cont.s[0]
                px_done = False

            if y_diff <= 0:
                y_coor = box.c[1]
                y_diff = box.s[1]
                py_done = True
            else:
                y_coor = cont.c[1] + cont.s[1]
                py_done = False
                
            if z_diff <= 0:
                z_coor = box.c[2]
                z_diff = box.s[2]
                pz_done = True
            else:
                z_coor = cont.c[2] + cont.s[2]
                pz_done = False
            
            diff_box = Node([x_diff, y_diff ,z_diff],
                            [x_coor, y_coor, z_coor])
            
            adj_arr = adj_consec(cont,big_cont)
        
            if adj_arr is not False:
                   for i in adj_arr:
                       if i[1] == "px" :
                                 if px_done is False:
                                     if within(diff_box, i[0],big_cont):
                                          #cont.child.append([box.c[0],box.c[1],box.c[2], box.s[0],box.s[1],box.s[2]])
                                          px_done = True

                       if i[1] == "py" :
                                 if py_done is False:
                                     if within(diff_box, i[0],big_cont):
                                          #cont.child.append([box.c[0],box.c[1],box.c[2], box.s[0],box.s[1],box.s[2]])
                                          py_done = True

                       if i[1] == "pz" :
                                 if pz_done is False:
                                     if within(diff_box, i[0],big_cont):
                                          #cont.child.append([box.c[0],box.c[1],box.c[2], box.s[0],box.s[1],box.s[2]])
                                          pz_done = True

                   if px_done is True and py_done is True and pz_done is True:
                       return True
                   else:
                       return False
        
            else:
                return False
    else:
        return False
               
                   

def adj_consec(cont, big_cont):

    arr = []
    ptr = big_cont
    while ptr.right is not False:

             if( (cont.c[1] + cont.s[1] == ptr.c[1]) and
                 (ptr.c[0] <= cont.c[0] <=  ptr.c[0] + ptr.s[0]) and
                 (ptr.c[2] <= cont.c[2] <=  ptr.c[2] + ptr.s[2]) ):

                       arr.append([ptr,"py"])


             if( (cont.c[0] + cont.s[0] == ptr.c[0]) and
                 (ptr.c[1] <= cont.c[1] <=  ptr.c[1] + ptr.s[1]) and
                 (ptr.c[2] <= cont.c[2] <=  ptr.c[2] + ptr.s[2]) ):

                       arr.append([ptr,"px"])


             if( (cont.c[2] + cont.s[2] == ptr.c[2]) and
                 (ptr.c[0] <= cont.c[0] <=  ptr.c[0] + ptr.s[0]) and
                 (ptr.c[1] <= cont.c[1] <=  ptr.c[1] + ptr.s[1]) ):

                       arr.append([ptr,"pz"])

             ptr = ptr.right
    print('adj_consec Done')         
    return arr

def cleanup(big_cont):
        tmp_ptr = big_cont
        print("cleaninng")
        while tmp_ptr is not False:
            #tmp_ptr.child = []
            if( tmp_ptr.s[0] == 0 or
                tmp_ptr.s[1] == 0 or
                tmp_ptr.s[2] == 0):

                tmp_ptr = tmp_ptr.right
                continue
            tmp_ptr.visited = False
            tmp_ptr = tmp_ptr.right

def clean(big_cont):
        tmp_ptr = big_cont
        print("cleaning")
        while tmp_ptr is not False:
            #tmp_ptr.child = []
            if( tmp_ptr.s[0] == 0 or
                tmp_ptr.s[1] == 0 or
                tmp_ptr.s[2] == 0):
                  tmp_ptr = tmp_ptr.right
                  continue
            if( tmp_ptr.s[0] == 300 and
                tmp_ptr.s[1] == 300 and
                tmp_ptr.s[2] == 300):
                  tmp_ptr = tmp_ptr.right
                  continue
        return big_cont
"""
from a import insert,Node,split,pr,SorT,insert_consec
s = Node([20,20,20],[0,0,0])
b1 = Node([5,5,5],[0,0,0])
b3 = Node([2,2,2],[0,0,0])
b4 = Node([1,1,1],[0,0,0])
b2 = Node([19,14,4],[0,0,0])
b5 = Node([2,2,2],[0,0,0])
#from a import fit_py
#b1 = split(b3,b1)
#b4 = Node([3,4,3],[0,0,0])
#s= fit_py(b1,b1.right,b4)
s = split(b1,s)
s= SorT(s)
m = insert(b2,s)
m = SorT(m)
h = insert(b3,m)
#pr(h)
h = SorT(h)
f = insert(b4,h)
#pr(f)
f = SorT(f)
n = insert(b5,f)
#pr(n)
#s.right.right= split(b2,s.right.right)
size = []
positions = []
a=f
while a is not False:
     size.append(a.s)
     positions.append(a.c)
     a=a.right

positions
size

"""
"""
assuming b1 < b2

if (b1.x + b1.xs < b2.x > b1.x or b2.x + b2.xs < b1.x > b2.x) and  
   (b1.y + b1.ys < b2.y > b1.y or b2.y + b2.ys < b1.y > b2.y):
   
if (b1.x + b1.xs < b2.x > b1.x and b1.y + b1.ys < b2.y > b1.y):
     if b1.z > b2.z:
         b2_cz = b1.z
     else:
         b1_cz = b2.z

if (i[0].x + i[0].xs < i[1].x > i[0].x and i[0].y + i[0].ys < i[1].y > i[0].y):
    
    if i[0].z > i[1].z:
        i[1].czs = i[0].z - c.z
        i[1].cz = c.z
        i[0].czs = c.zs - (i[0].z - c.z + i[0].zs)
        i[0].cz = i[0].z
        
    else:
        i[0].czs = i[1].z - c.z
        i[0].cz = c.z
        i[1].czs = c.zs - (i[1].z - c.z + i[1].zs)
        i[1].cz = i[1].z

    


if (b1.x + b1.xs < b2.x or b2.x + b2.xs < b1.x) and 
   (b1.y + b1.ys < b2.y or b2.y + b2.ys < b1.y):

   y is free
   x is free
   z is free
   
if b1.x + b1.xs < b2.x and
   b1.y + b1.ys < b2.y:

   x is free
   y is free
   z is free

if b1.x + b1.xs < b2.x and
   b1.y + b1.ys > b2.y:

from a import insert,Node,split,pr,SorT   
s = Node([200,200,300],[0,0,0])
b1 = Node([70,45,90],[0,0,0])
s = split(b1,s)
s= SorT(s)
b1 = Node([70,45,130],[0,0,0])
h = insert(b1,s)
a=h
positions = []
size = []
visit = []
while a is not False:
     size.append(a.s)
     positions.append(a.c)
     visit.append(a.visited)
     a=a.right
   

"""    
    

