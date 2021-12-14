import bpy
from math import radians

# clear scene - start from scratch
bpy.ops.object.select_all()
bpy.ops.object.delete()

bpy.ops.mesh.primitive_cube_add()
so = bpy.context.active_object

# move object
so.location[0] = 5
#so.location[1] = 3
#so.location[2] = -3

# rotate object 
so.rotation_euler[0] += radians(45)

# create modifyer
#so.modifiers.new("My Modifier",'SUBSURF')
#so.modifiers["My Modifier"].levels =3

# create modifyer 2 - easier and more intuitive
mod_subsurf=so.modifiers.new("My Modifier",'SUBSURF')
mod_subsurf.levels=3

# smooth the object
bpy.ops.object.shade_smooth()

# smooth by polygons - same results
#mesh = so.data
#for face in mesh.polygons:
#    face.use_smooth = True

# create displacement modifier
mod_displace=so.modifiers.new("My Displacement",'DISPLACE')
mod_displace=2

# create the texture
new_tex = bpy.data.textures.new("My Texture",'DISTORTED_NOISE')
new_tex.noise_scale = 2.0

mod_displace.texture = new_tex

bpy.ops.object.select_all(action='TOGGLE')