'''范例:数据格式与def用法'''
from pyomo.environ import *

##-----------------------------------------------------------

vol=100
abv=0.04
data = {
 'A': {'abv': 0.045, 'cost': 0.32},
 'B': {'abv': 0.037, 'cost': 0.25},
 'W': {'abv': 0.000, 'cost': 0.05},
}


##-----------------------------------------------------------
def beer(vol, abv, data): 

  '''setting model 模型设置'''
  # create a model 创建模型
  model = ConcreteModel()
  # declare decision variables 设置变量
  model.a = Var(domain=NonNegativeReals) 
  model.b = Var(domain=NonNegativeReals) 
  model.w = Var(domain=NonNegativeReals) 
  # declare objective 设置目标
  model.cost = Objective(expr = 0.32*model.a + 0.25*model.b+0.05*model.w, sense=minimize) # maximize最大化 minimize最小化
  # declare constraints 设置约束条件
  model.v = Constraint(expr = model.a + model.b + model.w == 100)
  model.alc = Constraint(expr = 0.045*model.a + 0.037*model.b == 0.04*100)


  '''optimizate 优化求解'''
  #setting SolverFactory 设置求解器（glpk）
  SolverFactory('glpk', executable='C:/Windows/System32/glpk-4.65/w64/glpsol').solve(model)
  # display solution
  print('\ncost = ', model.cost())
  print('\nDecision Variables')
  print('a = ', model.a())
  print('b = ', model.b())
  print('w = ', model.w())



##-----------------------------------------------------------
#运行beer函数
beer(vol, abv, data)