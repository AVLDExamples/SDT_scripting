
# Task 1
########
model = project.models[1]
out2 = model.root["Model"]["DOM 1"]["Boundary Conditions"]["BND_Outlet_2"]
out3 = model.root["Model"]["DOM 1"]["Boundary Conditions"]["BND_Outlet_3"]
out2.definition.type="WALL"
out3.definition.type="WALL"

# Task 2
########
eq_con = model.root["Model"]["DOM 1"]["Equation Control"]
eq_con.energy.use="USAGE_CALCULATED"
