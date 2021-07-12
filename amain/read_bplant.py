from pyomo.environ import *

##---------------------------------------------------------------------------------
## 【说明】
## read 
##默认使用20*20标准
## grid_read(cc,lus,lue):
## cc:[Climate change]:h,m,l
## lus:植物的三个来源:1(Arable),2(Grass),3(Forest)
## lue:物种：- Wheat (LUe1.csv) - Sugar beet (LUe2.csv) - OSR (LUe3.csv) - SRC (LUe4.csv) - SRF (LUe5.csv) - Miscanthus (LUe6.csv)
## var:1-CO2，2-CH4, 3-N2O, 4-固体C,5-GHG
##---------------------------------------------------------------------------------



##---------------------------------------------------------------------------------
## 【主程序】
##---------------------------------------------------------------------------------
def read_bplant():

    wenjianming=".\\data\\" #文件名
    wenjianming=wenjianming+"BiomassPlant.csv"

    #print(wenjianming) #test文件路径


    model = AbstractModel()

    model.C = Set(dimen=6) 
    data = DataPortal()
    #data.load(filename='A.csv', set=model.C)  #py ide 的文件路径
    #data.load(filename='.\\test\\read\\A.csv', set=model.C)  #vscode的文件路径
    data.load(filename=wenjianming, set=model.C)  #vscode的文件路径


    instance = model.create_instance(data)
    #instance.pprint()
    a=(instance.C.ordered_data())



    #print(a[3])  # 測試輸出用
    return(a)




##---------------------------------------------------------------------------------
## 【測試function】
##---------------------------------------------------------------------------------
#zzz=read_bplant()
#print(zzz)
'''((1, 'Avonmouth', 11, 75000, 51.529869, -2.678875), (2, 'Barrow in Furness', 10, 86000, 54.100578, -3.21929), (3, '\tBarry', 10, 72000, 51.401297, '-3.259063\t'), (4, '\tBoston Lincolnshire', 10, 86400, 52.963398, -0.015868), (5, 'Clay Cross Derbyshire', 10.5, 80000, 53.171309, -1.409836), (6, 'Greenham Thatcham', 6.3, 7000, 51.37725, -1.286567), (7, '\tGreenwich', 0, 0, 51.493562, 0.002983), (8, '\tHolyhead', 299, 1500000, 53.298876, '-4.603443\t'), (9, 'Hull', 10, 86400, 53.744253, '-0.326282\t'), (10, '\tHuntingdon', 4.5, 49000, 52.333905, -0.29943), (11, ' Little Houghton (near Barnsley)', 20, 150000, 53.546959, -1.363592), (12, 'Sittingbourne Kent', 8.4, 48000, 51.367612, '0.746333\t'), (13, '\tSunderland', 9, 72000, 54.907209, -1.356691), (14, '\tSwindon', 4.5, 49000, 51.595885, -1.739657), (15, 'Wellingborough Northamptonshire', 4.8, 0, 52.321028, -0.684561), (16, ' West Thurrock', 15, 0, 51.47618, '\t0.30677\t'))'''