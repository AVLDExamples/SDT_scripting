#get the FAME model
fame = project.models["FAME M 1"]
#Type can be 'axis', 'box', 'cone', 'cylinder', 'line', 'plane', 'point', 'sphere' or 'truncated_cone'
cone = fame.new_datum_object("cone")
cone.height = (10, "cm")
cone.radius= (5, "cm")
# coordinate are represented by tuples of 3 doubles, unit is SI unit
cone.origin = (0,0,0.1)
#coordinates can be given with units:
cone.origin = ((0,0,0.1), "in")
fame.datum_objects[0]
fame.datum_objects['point']
