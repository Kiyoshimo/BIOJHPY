from pyomo.environ import *



## read 
##默认使用20*20标准
## var_read(cc,lus,lue):
## cc:[Climate change]:h,m,l
## lus:植物的三个来源:1(Arable),2(Grass),3(Forest)
## lue:物种：- Wheat (LUe1.csv) - Sugar beet (LUe2.csv) - OSR (LUe3.csv) - SRC (LUe4.csv) - SRF (LUe5.csv) - Miscanthus (LUe6.csv)
## var:1-CO2，2-CH4, 3-N2O, 4-固体C,5-GHG

def var_read(cc,lus,lue,var):

    wenjianming=".\\data\\Results\\Average\\20\\0\\" #文件名
    if cc=="h":
        wenjianming=wenjianming+"high\\"
    elif cc=="m":
        wenjianming=wenjianming+"med\\"
    elif cc=="l":
        wenjianming=wenjianming+"low\\"
    else:
        print("error:Climate change ")
        return 0
    
    if lus==1:
        wenjianming=wenjianming+"LUs1\\"
    elif lus==2:
        wenjianming=wenjianming+"LUs2\\"
    elif lus==3:
        wenjianming=wenjianming+"LUs3\\"
    else:
        print("error:lus ")
        return 0

    if lue==1:
        wenjianming=wenjianming+"LUe1\\"
    elif lue==2:
        wenjianming=wenjianming+"LUe2\\"
    elif lue==3:
        wenjianming=wenjianming+"LUe3\\"
    elif lue==4:
        wenjianming=wenjianming+"LUe4\\"
    elif lue==5:
        wenjianming=wenjianming+"LUe5\\"
    elif lue==6:
        wenjianming=wenjianming+"LUe6\\"
    else:
        print("error:lue ")
        return 0   

    if var==1:
        wenjianming=wenjianming+"var1"
    elif var==2:
        wenjianming=wenjianming+"var2"
    elif var==3:
        wenjianming=wenjianming+"var3"
    elif var==4:
        wenjianming=wenjianming+"var4"
    elif var==5:
        wenjianming=wenjianming+"var5"

    else:
        print("error:var ")
        return 0   

    wenjianming=wenjianming+".csv"

    #print(wenjianming) #test文件路径


    model = AbstractModel()

    model.C = Set(dimen=9) 
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
##zzz=var_read("h",1,6,1)

