from pyomo.environ import *




model = AbstractModel()
model.C = Set(dimen=2)
data = DataPortal()
#data.load(filename='A.csv', set=model.C)  #py ide 的文件路径
data.load(filename='.\\amain\\read\\A.csv', set=model.C)  #vscode的文件路径
instance = model.create_instance(data)

data.pprint()
