##-----------------------------------------------------------
'''范例题目：啤酒混合策略(Jenchura, 2017)
  找到最低成本组合
    酿酒厂收到了100加仑4% ABV(酒精含量)啤酒的订单。
    啤酒A为4.5% ABV，每加仑成本为0.32美元，
    啤酒B为3.7% ABV，每加仑成本为0.25美元。
    水也可用作混合剂，每加仑成本为0.05美元。

  Cost:
    0.32*a + 0.25*b+0.05*w
  subject:
    a + b + w == 100
    0.045*a + 0.037*b == 0.04*100
'''

from pyomo.environ import *

##-----------------------------------------------------------
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

# 打印模型细节
#model.pprint()



##-----------------------------------------------------------
'''optimizate 优化求解'''

#setting SolverFactory 设置求解器（glpk）
SolverFactory('glpk', executable='C:/Windows/System32/glpk-4.65/w64/glpsol').solve(model).write()

# display solution
print('\ncost = ', model.cost())


print('\nDecision Variables')
print('a = ', model.a())
print('b = ', model.b())
print('w = ', model.w())



##-----------------------------------------------------------
##输出内容
'''
# ==========================================================
# = Solver Results                                         =
# ==========================================================
# ----------------------------------------------------------
#   Problem Information
# ----------------------------------------------------------
Problem:
- Name: unknown
  Lower bound: 27.625
  Upper bound: 27.625
  Number of objectives: 1
  Number of constraints: 3
  Number of variables: 4
  Number of nonzeros: 6
  Sense: minimize
# ----------------------------------------------------------
#   Solver Information
# ----------------------------------------------------------
Solver:
- Status: ok
  Termination condition: optimal
  Statistics:
    Branch and bound:
      Number of bounded subproblems: 0
      Number of created subproblems: 0
  Error rc: 0
  Time: 0.011999845504760742
# ----------------------------------------------------------
#   Solution Information
# ----------------------------------------------------------
Solution:
- number of solutions: 0
  number of solutions displayed: 0


  '''