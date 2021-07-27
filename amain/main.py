import sys
from pyomo.environ import *
import pyomo.environ as pyo
import pyomo.kernel as pmo
import math  
import numpy
import pandas



from read_grid import *
from read_var import *
from read_yield import *
from read_bplant import * #发电厂


'''
#-------------------------------------------------------------------------------
## 【说明】
## main
##默认地图使用20*20标准格子
## 引用副程序：read_grid,read_var,read_yield,read_bplant
#-------------------------------------------------------------------------------
'''


#-------------------------------------------------------------------------------
#setting model 模型设置
#-------------------------------------------------------------------------------

# create a model 创建模型
model = AbstractModel() # 这是一个抽象的Pyomo模型



#-------------------------------------------------------------------------------
# declare Param 设置参数
#-------------------------------------------------------------------------------

P_GR = (read_grid())
P_I = pyo.RangeSet(1, 6)
P_YI = pyo.Param(model.I, read_yield("h",1)) #some BUG!
P_BP = (read_bplant())

## 公式相关
model.TI_=Var(domain=NonNegativeReals) # Status quo point (minimum NPV threshold) for node n 节点n的现状点（最低NPV阈值）



#-------------------------------------------------------------------------------
# declare decision variables 设置变量
#-------------------------------------------------------------------------------

## Indices and sets 
model.r=set() #resources资源 (biomass, non-energy resources and energy carriers ) 
model.c=set() #Regions {1, 2…….48…} 区域
model.n=set() # Value chain nodes, including biorefinery, biomass plantations, current industrial sector nodes, distribution centres  价值链节点，包括生物精炼厂、生物质种植园、当前工业部门节点、配送中心
model.t=set() # Time in years {1, 2…} 时间年
model.m=set() # Production mode considering centralised and decentralised modes (CM/DM) at different capacity (large, medium) {CM-L, CM-M… DM-L, DM-M…}考虑不同容量（大容量、中容量）的集中模式和分散模式（CM/DM）（CM-M）
model.p=set() # Production technologies (e.g. bioethanol, biobutanol, lactic acid, biomethanol…) {1, 2, 3…}生产技术（例如。生物乙醇、生物丁醇、乳酸、biomethanol...){1、2、3……}


## Continuous variables 连续变量
model.epsilon=Var(domain=NonNegativeReals)  #Negotiation power indicator of the node n节点n的协商能力指标
model.TI=Var(domain=NonNegativeReals) # Total impacts caused by node n expressed as economic performance indicator (NPV), consisting of the impacts at biomass growth, biomass conversion and bio-product distribution stages.节点n引起的总影响表示为经济绩效指标(NPV)，包括生物量增长、生物量转换和生物产品分配阶段的影响
model.TF=Var(domain=NonNegativeReals)#Transported resource from note n to n’ via mode l  通过模式l将资源从注释n传输到n‘
model.CF=Var(domain=NonNegativeReals)#Transport resource by node n from cell c to c’ via mode l按节点n通过模式l将资源从单元格c传输到c‘

## Binary variables  二元变量
model.Pro=Var(domain=pmo.Binary)
model.ProC=Var(domain=pmo.Binary)






#-------------------------------------------------------------------------------
# declare objective 设置目标
#-------------------------------------------------------------------------------

#fct-1
model.obj1 = Objective(\
    expr = numpy.prod((model.TI[n]-model.TI_[n])^model.epsilon[n] for n in model.N), sense=maximize) # maximize最大化 minimize最小化


#-------------------------------------------------------------------------------
# declare constraints 设置约束条件
#-------------------------------------------------------------------------------

#fct-2 #不会写待修改
model.TI=Constraint(\
    expr = sum(SALEI[n,t] + SUBSIDY - TAX -sum(Yield[r,c,t]*A[r,sn,c,t]*EIf[r,kpt,t]* landarea[c,sn]) +TRI+sum(STOR*SIF)-Cap_B)) 

#fct-3


#fct-4


#fct-5
for r,c,c_,n,l,t in [model.r,model.c,model.c_,model.n,model.l,model.t]:
    model.CF[r,c,c_,n,l,t]= Constraint(\
        expr=sum(model.TF[r,n,n_,l,t]*model.ProC[c,n,t]*model.ProC[c_,n_,t] for n_ in n_从何而来) ) #n_从何而来?我猜是发电厂的列表是n

#fct-6
for c,n,t in [model.c,model.n,model.t]:
    model.ProC[n,c,t]= Constraint(\
        expr=sum(model.Pro[p,m,c,n,t]  for m in model.m for p in model.p))



# 打印模型细节
#model.pprint()




#-------------------------------------------------------------------------------
# optimizate 优化求解
#-------------------------------------------------------------------------------


#setting SolverFactory 设置求解器（glpk）
SolverFactory('glpk', executable='C:/Windows/System32/glpk-4.65/w64/glpsol').solve(model).write()

# display solution
print('\nProfit = ', model.profit())


print('\nDecision Variables')
print('x = ', model.x())
print('y = ', model.y())


print('\nConstraints')
print('Demand  = ', model.demand())





#-------------------------------------------------------------------------------
# ##SolverFactory的输出内容
#-------------------------------------------------------------------------------

