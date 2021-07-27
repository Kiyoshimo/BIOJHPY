##-----------------------------------------------------------
'''范例题目：
  求最大利润
    X、Y两种产品
    A、B两个工人
    X产品:净利润40，需要A工人干1hr，B工人干2hr,需求最多40个
    Y产品:净利润30，需要A工人干1hr，B工人干1hr，需求无限个
    A工人一周最多工时80hr，B工人一周最多工时100hr
s
    profit:
        max(40x+30y)
    subject:
        x<=40 #产品A的需求
        x+y<=80 #A工时
        2x+y<=100   #B工时
'''

from pyomo.environ import *

##-----------------------------------------------------------
'''setting model 模型设置'''

# create a model 创建模型
model = ConcreteModel()

# declare decision variables 设置变量





# declare objective 设置目标
model.profit = Objective(expr = 40*model.x + 30*model.y, sense=maximize) # maximize最大化 minimize最小化

# declare constraints 设置约束条件
model.demand = Constraint(expr = model.x <= 40) #需求
model.laborA = Constraint(expr = model.x + model.y <= 80) #A工人工时
model.laborB = Constraint(expr = 2*model.x + model.y <= 100) #B工人工时

# 打印模型细节
#model.pprint()



##-----------------------------------------------------------
'''optimizate 优化求解'''

#setting SolverFactory 设置求解器（glpk）
SolverFactory('glpk', executable='C:/Windows/System32/glpk-4.65/w64/glpsol').solve(model).write()

# display solution
print('\nProfit = ', model.profit())


print('\nDecision Variables')
print('x = ', model.x())
print('y = ', model.y())


print('\nConstraints')
print('Demand  = ', model.demand())
print('Labor A = ', model.laborA())
print('Labor B = ', model.laborB())



##-----------------------------------------------------------
##SolverFactory的输出内容
'''
# ==========================================================
# = Solver Results                                         =
# ==========================================================
# ----------------------------------------------------------
#   Problem Information
# ----------------------------------------------------------
Problem:
- Name: unknown
  Lower bound: 2600.0
  Upper bound: 2600.0
  Number of objectives: 1
  Number of constraints: 4
  Number of variables: 3
  Number of nonzeros: 6
  Sense: maximize
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
  Time: 0.014000177383422852
# ----------------------------------------------------------
#   Solution Information
# ----------------------------------------------------------
Solution:
- number of solutions: 0
  number of solutions displayed: 0
  '''