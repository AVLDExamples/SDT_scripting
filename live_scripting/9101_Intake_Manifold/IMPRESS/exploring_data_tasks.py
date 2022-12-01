import os
import sdt.results
dirname = os.path.dirname(project.filename)
result_projects = sdt.results.get_projects(dirname) # lists all projects within dirname
result_proj = result_projects[0]


#task 1
import numpy as np
inflow = casenode["/DOM_1/2D_Results/Total Inlet Massflow"]
outflow = casenode["/DOM_1/2D_Results/Total Outlet Massflow"]
outflow = casenode["/DOM_1/2D_Results/Total Outlet Massflow"]
inflow = np.asarray(inflow.values[1])
outflow = np.asarray(outflow.values[1])
balance = inflow - outflow
np.max(balance)
np.min(balance)

#task2
sumfol = casenode.insert_summary_folder("Summary")
sumfol.insert_single_value(name="Max Imbalance", value=repr(max_value), title="Max Imbalance ", data_type="DOUBLE", unit_str="massflow~kg_h")
sumfol.insert_single_value(name="Min Imbalance", value=repr(min_value), title="Min Imbalance ", data_type="DOUBLE", unit_str="massflow~kg_h")

root_folder = casenode.insert_root_folder("Additional Data")
x_vec = sdt.results.create_vector(name="Iterations", unit_str="time_iteration~iterations", title="Iterations")
y_vec = sdt.results.create_vector(name="Massflow Imbalance", title="Massflow Imbalance", unit_str="massflow~kg_s")
x_vec.values = x_values
y_vec.values = balance
root_folder.insert_curve(x=x_vec, y=y_vec, name="Imbalance")

casenode.write_tree()
casenode.release()
