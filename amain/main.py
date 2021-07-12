import sys
from pyomo.environ import *
import pyomo.environ as pyo
import math  



from read_grid import *
from read_var import *
from read_yield import *
from read_bplant import * #发电厂

##---------------------------------------------------------------------------------
## 【说明】
##---------------------------------------------------------------------------------
## main
##默认使用20*20标准
## 副程序：read_grid,read_var,read_yield,read_bplant




##---------------------------------------------------------------------------------
## 【主程序】
##---------------------------------------------------------------------------------

'''setting model 模型设置'''

# create a model 创建模型
#model = ConcreteModel()
model = AbstractModel() # 这是一个抽象的Pyomo模型


# declare Param 设置参数
model.GR = (read_grid())

model.I = pyo.RangeSet(1, 6)
model.YI = pyo.Param(model.I, read_yield("h",1)) #some BUG!
model.BP = (read_bplant())




# declare decision variables 设置变量
model.npn=Var(domain=NonNegativeReals)  #Negotiation power indicator of the node n节点n的协商能力指标
model.TI=Var(domain=NonNegativeReals) #Total impacts caused by node n expressed as economic performance indicator (NPV), consisting of the impacts at biomass growth, biomass conversion and bio-product distribution stages.节点n引起的总影响表示为经济绩效指标(NPV)，包括生物量增长、生物量转换和生物产品分配阶段的影响
model.TI_=Var(domain=NonNegativeReals)
model.n=set()

# declare objective 设置目标
#model.profit = Objective(expr = 40*model.x + 30*model.y, sense=maximize) # maximize最大化 minimize最小化
#fct-1
model.obj1 = Objective(expr = sum((model.TI[i]-model.TI_[i])^model.npn[i] for i in model.n), sense=maximize) # maximize最大化 minimize最小化





# declare constraints 设置约束条件
#model.demand = Constraint(expr = model.x <= 40) #需求

#fct-2
model.TI=Constraint(expr = sum(SALEI + SUBSIDY - TAX -sum(Yield[r,c,t]*A[r,sn,c,t]*EIf[r,kpt,t]* landarea[c,sn]) +TRI+sum(STOR*SIF)-Cap_B)) 




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



##-----------------------------------------------------------
##SolverFactory的输出内容


