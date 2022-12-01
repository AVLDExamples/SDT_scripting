#getting dataref

import os
import sdt
import sdt.report
import sdt.results

project = sdt.project.load_project("9101_Intake_Manifold.proj")
dirname = os.path.dirname(project.filename)
projectname = os.path.splitext(os.path.basename(project.filename))[0]
modelname = "9101_Intake_Manifold"

result_key = {
        'project_directory': dirname,
        'project': projectname,
        'model': modelname,
        'case_set': 'Case set 1',
        'case': 'Case 1',
        'channel_path': '/3D Result Data/3D Result Data',
        'sub_key':None
}


#adding page and view
mdl = project.models["9101_Intake_Manifold"]
rep = mdl.report
neuS = rep.create_page("neue Seite")
view = neuS.create_view("Neuer View", viewtype="View3d")
d3d = view.add_entity(type="ColoredSurface", data=result_key.values())
d3d.data_mapping.data_channel = "Flow:AbsolutePressure[Pa]"
d3d.color_mapping.scheme = "Magma"
d3d.vectors.enabled=True
d3d.vectors.data_mapping.data_channel="Flow:Velocity[m/s]"
d3d.vectors.distribution.maximum_number_of_vectors=10000

project.save()
