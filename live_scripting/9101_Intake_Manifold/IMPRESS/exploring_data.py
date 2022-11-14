#first page
import os
import sdt.results
dirname = os.path.dirname(project.filename)
result_projects = sdt.results.get_projects(dirname) # lists all projects within dirname
result_proj = result_projects[0]
result_proj.models[0]


#2nd page
casenode = result_proj["9101_Intake_Manifold"]["Case set 1"]["Case 1"]
twoD = casenode["/DOM_1/2D_Results"]
outflow_node = casenode["/DOM_1/2D_Results/Total Outlet Massflow"]
outflow_node.values

#3rd page: Task
inflow = casenode["/DOM_1/2D_Results/Total Inlet Massflow"]
outflow = casenode["/DOM_1/2D_Results/Total Outlet Massflow"]
outflow = casenode["/DOM_1/2D_Results/Total Outlet Massflow"]
inflow = np.asarray(inflow.values[1])
outflow = np.asarray(outflow.values[1])
balance = inflow - outflow
np.max(balance)
np.min(balance)



#4th page
import os
projectname = os.path.splitext(os.path.basename(project.filename))[0]
modelname = sdt.live.active_model().name
#all address parts have to be given --> single or no channel will be returned
#channel = sdt.results.get_channel(project_directory=dirname, project=projectname, model=modelname, case_set="", case="", channel_path="")
#some address parts may be left out --> all matching channels will be returned
channels = sdt.results.get_channel(project_directory=dirname, project=projectname, model=modelname )#, case_set="", case="", channel_path="")

#5th page
sumfol = casenode.insert_summary_folder("Summary")
sumfol.insert_single_value(name="MyName", value=repr(100), title="MyName" ,data_type="DOUBLE", unit_str="length~mm")
casenode.write_tree()
casenode.release()

#6th page
import numpy as np
root_folder=casenode.insert_root_folder("Additional Curves")
curve_folder = root_folder.insert_folder(name="curves", title="Several Curves")
x_vec = sdt.results.create_vector(name="ordinate", unit_str="length~mm", title="Ordinate")
x_vec.values = np.linspace(-np.pi, np.pi,360)
y_vec = sdt.results.create_vector(name="coordinate", unit_str="power~kW", title="Coordinate")
y_vec.values = np.sin(x_vec.values)
curve_folder.insert_curve(x=x_vec, y=y_vec,name="New Curve")
casenode.write_tree()
casenode.release()

