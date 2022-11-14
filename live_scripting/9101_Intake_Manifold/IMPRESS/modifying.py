#getting dataref
projectname = os.path.splitext(os.path.basename(project.filename))[0]
modelname = mdl.name
dataref = ( dirname, projectname, modelname, "Case set 1", "Case 1", "/DOM 1/3D Result Data/Flow:Velocity", None)
#adding page and view
mdl = sdt.live.active_model()
rep = mdl.report
neuS = rep.create_page("neue Seite")
view = neuS.create_view("Neuer View", viewtype="View3d")
d3d = view.add_entity(type="ColoredSurface", data=dataref)
d3d.color_mapping.scheme = "Magma"


