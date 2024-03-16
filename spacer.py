import cadquery as cq
from cadquery import exporters

# Parameters
length = 19
width = 15
height = 11
groove_depth = 1
groove_width = 13
fillet_radius = 0.5

# Create box
box = cq.Workplane("XY").box(length, width, height)

# Cut a groove on the top face
groove = (cq.Workplane("XY")
          .workplane(offset=height/2 - groove_depth)
          .rect(length, groove_width)
          .extrude(groove_depth))

box = box.cut(groove)
del(groove)
#for e in box.edges('|Y').all():
    #if e.vals()[0].Length()==13 and e.vals()[0].startPoint().z>0:
        #print(e)
    #box = e.fillet(fillet_radius)
edge_list = [e for e in box.edges('|Y').all() if e.vals()[0].Length()==13 and e.vals()[0].startPoint().z>0]
box = box.edges('|Y').fillet(fillet_radius)
#box = box.newObject(edge_list)
#box = box.fillet(fillet_radius)

exporters.export(
    box, 
    "box.json",
    tolerance=0.01,
    angularTolerance=0.1,
    exportType=exporters.ExportTypes.TJS
)