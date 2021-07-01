##-----------------------------------------------------------
'''范例题目：
https://nbviewer.jupyter.org/github/Pyomo/PyomoGallery/blob/master/diet/DietProblem.ipynb
Sets
F = set of foods
N = set of nutrients
Parameters
ci = cost per serving of food i, ∀i∈F
aij = amount of nutrient j in food i, ∀i∈F,∀j∈N
Nminj = minimum level of nutrient j, ∀j∈N
Nmaxj = maximum level of nutrient j, ∀j∈N
Vi = the volume per serving of food i, ∀i∈F
Vmax = maximum volume of food consumed
Variables
xi = number of servings of food i to consume

'''
from pyomo.environ import *
infinity = float('inf')

model = AbstractModel() #抽象建模

# Foods 食物
model.F = Set() #set
# Nutrients 营养
model.N = Set()

# Cost of each food 花费
model.c    = Param(model.F, within=PositiveReals)
# Amount of nutrient in each food 每个食物的营养
model.a    = Param(model.F, model.N, within=NonNegativeReals)
# Lower and upper bound on each nutrient 营养上下界
model.Nmin = Param(model.N, within=NonNegativeReals, default=0.0)
model.Nmax = Param(model.N, within=NonNegativeReals, default=infinity)
# Volume per serving of food 食物包的质量
model.V    = Param(model.F, within=PositiveReals)
# Maximum volume of food consumed 食物包的最大质量
model.Vmax = Param(within=PositiveReals)





# Number of servings consumed of each food
model.x = Var(model.F, within=NonNegativeIntegers)

# Minimize the cost of food that is consumed
def cost_rule(model):
    return sum(model.c[i]*model.x[i] for i in model.F)
model.cost = Objective(rule=cost_rule)

# Limit nutrient consumption for each nutrient
def nutrient_rule(model, j):
    value = sum(model.a[i,j]*model.x[i] for i in model.F)
    return model.Nmin[j] <= value <= model.Nmax[j]
model.nutrient_limit = Constraint(model.N, rule=nutrient_rule)

# Limit the volume of food consumed
def volume_rule(model):
    return sum(model.V[i]*model.x[i] for i in model.F) <= model.Vmax

model.volume = Constraint(rule=volume_rule)



