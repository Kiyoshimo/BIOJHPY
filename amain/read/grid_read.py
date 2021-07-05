from pyomo.environ import *



## read 
##默认使用20*20标准
## grid_read(cc,lus,lue):
## cc:[Climate change]:h,m,l
## lus:植物的三个来源:1(Arable),2(Grass),3(Forest)
## lue:物种：- Wheat (LUe1.csv) - Sugar beet (LUe2.csv) - OSR (LUe3.csv) - SRC (LUe4.csv) - SRF (LUe5.csv) - Miscanthus (LUe6.csv)
## var:1-CO2，2-CH4, 3-N2O, 4-固体C,5-GHG

def var_read(cc,lus,lue,var):

    wenjianming=".\\data\\Results\\Average\\20\\0\\" #文件名
    wenjianming=wenjianming+"grid.csv"

    #print(wenjianming) #test文件路径


    model = AbstractModel()

    model.C = Set(dimen=3) 
    data = DataPortal()
    #data.load(filename='A.csv', set=model.C)  #py ide 的文件路径
    #data.load(filename='.\\test\\read\\A.csv', set=model.C)  #vscode的文件路径
    data.load(filename=wenjianming, set=model.C)  #vscode的文件路径


    instance = model.create_instance(data)
    #instance.pprint()
    a=(instance.C.ordered_data())



    ## 測試輸出用
    #print(a[3])
    return(a)




## 測試function
zzz=var_read("h",1,6,1)
print(zzz)

