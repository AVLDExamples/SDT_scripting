#adding page and view
mdl = sdt.live.active_model()
rep = mdl.report
neuS = rep.create_page(“neue Seite”)
view = neuS.create_view(‘Neuer View’, viewtype=“View3d”)
d3d = view.add_entity(type=“ColoredSurface”, data=dataref)
d3d.color_mapping.scheme = “Magma”
#getting dataref
projectname = os.path.splitext(os.path.basename(project.filename))[0]
modelname = mdl.name
datataref = ( dirname, projectname, modelname, “Case Set 1”, “Case 1”, “/DomainName/3D Result Data/NameInTree[UnitInTree]”, None)

