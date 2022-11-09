project
dir(project)
project.models["9101_Intake_Manifold"]
mdl = _
dir(mdl)
mdl.domains[0]
mdl.run_mode
mdl.run_mode.definition.maximum_iterations_steady
mdl.run_mode.definition.maximum_iterations_steady = 1500
mdl.run_mode.definition.maximum_iterations_steady = 1000
mdl.run_mode.definition.minimum_iterations_steady = 100
mdl.run_mode.definition.maximum_iterations_steady = 1500
mdl.run_mode.definition.type = "TRANSIENT_TIME"
mdl.run_mode.definition.type = "STEADY"
mdl.root['Model']['DOM 1']['Boundary Conditions']
dom = mdl.domains[0]
dom.boundary_conditions.create_boundary_condition("BND_Stuff")
boco = _
boco.definition.type="WALL"
boco.definition.type="WALL"
boco.definition.selection="BND_Stuff"
boco.momentum_and_continuity.movement_type = "WALL_VELOCITY"
boco.momentum_and_continuity.movement_type = "MESH_MOVEMENT"
boco.momentum_and_continuity.movement_type = "MESH_MOVEME"
boco.momentum_and_continuity.movement_type = "FREE_SLIP_WALL"
