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

#####################################
#####################################
solcon = model.root["Model"]["DOM 1"]["Solver Control"]["Continuity Equation"]
eqnsetting = solcon.equation_settings

numcon = model.root["Model"]["DOM 1"]["Numerics Control"]
numcon.numerics_control.cell_face_adjustment_geometry=True
#####################################
#####################################

solcon = model.root["Model"]["DOM 1"]["Solver Control"]["Continuity Equation"]
eqnsetting = solcon.equation_settings

eqnsetting.convergence_criteria.input_type='const'
# ‘table’, ‘const’ of ‘none’
eqnsetting.convergence_criteria.const = 1e-4
#####################################
#####################################
boco_in = model.root["Model"]["DOM 1"]["Boundary Conditions"]["BND_Inlet"]
mom_con = boco_in.momentum_and_continuity
#####################################
#####################################
mom_con.mass_flow.input_type='table'
mom_con.mass_flow.table = np.asarray( [ [0,0.01], [50,0.1]])
mom_con.mass_flow.table = (np.asarray([[0.e+00, 1.e-02],[5.e+01, 1.e-01]]), ("iterations", "g_s"))


