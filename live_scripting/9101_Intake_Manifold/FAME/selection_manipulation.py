fame = project.models["FAME M 1"]
mesh = fame.root['meshes']['all_meshes']['IM_polymesh']
import numpy as np
from numpy.linalg import norm
centre = np.asarray([0,0,-0.005])

selection = list()
with mesh.get_data_interface() as x:
    if "Sphere" in x.get_cell_selection_names():
        x.remove_cell_selection("Sphere")
    for i in range(mesh.mesh.num_cells):
        p = x.get_cell_center(i)
        if np.linalg.norm(p-centre)<0.01:
            selection.append(i)
    x.add_cell_selection("Sphere")
    x.cell_selection_append("Sphere", selection)

