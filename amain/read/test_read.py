from pyomo.environ import *




model = AbstractModel()

model.C = Set(dimen=9) 
data = DataPortal()
#data.load(filename='A.csv', set=model.C)  #py ide 的文件路径
#data.load(filename='.\\test\\read\\A.csv', set=model.C)  #vscode的文件路径
data.load(filename='.\\data\\Results\\Average\\5\\0\\high\\LUs1\\LUe6\\var1.csv', set=model.C)  #vscode的文件路径

instance = model.create_instance(data)

#instance.pprint()
a=(instance.C.ordered_data())
print(a[3])