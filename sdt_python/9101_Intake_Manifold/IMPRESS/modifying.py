#getting dataref
#############################################################
#############################################################
#############################################################
import os
dirname = os.path.dirname(project.filename)
projectname = os.path.splitext(os.path.basename(project.filename))[0]
modelname = mdl.name
dataref = ( dirname, projectname, modelname, "Case set 1", "Case 1", "/3D Result Data/3D Result Data", None)
#############################################################
#############################################################
#############################################################
import sdt
import sdt.project
project = sdt.project.load_project("9101_Intake_Manifold.proj")
mdl = project.models[1]
rep = mdl.report
neuS = rep.create_page("neue Seite")
view = neuS.create_view("Neuer View", viewtype="View3d")
d3d = view.add_entity(type="ColoredSurface", data=dataref)
d3d.data_mapping.data_channel = "Flow:Velocity[m/s]"
d3d.color_mapping.scheme = "Magma"
#############################################################
#############################################################
#############################################################
d3d.vectors.enabled=True
d3d.vectors.data_mapping.data_channel = "Flow:Velocity[m/s]"
d3d.vectors.distribution.maximum_number_of_points=10000
d3d.vectors.transformation.scaling_mode ="ALL"
project.save()
#############################################################
#############################################################
#############################################################
view2d = neuS.create_view("Chart", "Linechart")
dataref2d = ( dirname, projectname, modelname, "Case set 1", "Case 1", "/DOM_1/2D_Results/BND_Outlet_1/Mass Flow", None)
enti2d = view2d.add_entity(name="My Curve",y_data=dataref2d)
enti2d.markers.show=True
project.save()
