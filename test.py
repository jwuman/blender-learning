import bpy
import random

bpy.ops.object.select_all()
bpy.ops.object.delete()

spacing = 2.2
for x in range(10):
    for y in range(10):
        location=(x*spacing,y*spacing,random.random()*2)
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=location, scale=(1,1,1))
        
        item=bpy.context.object
        if random.random() < 0.1:
            item.data.materials.append(bpy.data.materials["Material"])
        else:
            item.data.materials.append(bpy.data.materials["Material"])
            
bpy.ops.object.select_all(action='TOGGLE')