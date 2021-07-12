from pyomo.environ import *


##---------------------------------------------------------------------------------
## 【说明】
## read 
##默认使用20*20标准
## grid_read(cc,lue):
## cc:[Climate change]:1-h,2-m,3-l
## lue:物种：1- Wheat (LUe1.csv) 2- Sugar beet (LUe2.csv) 3- OSR (LUe3.csv) 4- SRC (LUe4.csv) 5- SRF (LUe5.csv) 6- Miscanthus (LUe6.csv)
##---------------------------------------------------------------------------------




##---------------------------------------------------------------------------------
## 【主程序】
##---------------------------------------------------------------------------------

def read_yield(cc,lue):

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
    
    
    wenjianming=wenjianming+"yield\\"

    if lue==1:
        wenjianming=wenjianming+"LUe1"
    elif lue==2:
        wenjianming=wenjianming+"LUe2"
    elif lue==3:
        wenjianming=wenjianming+"LUe3"
    elif lue==4:
        wenjianming=wenjianming+"LUe4"
    elif lue==5:
        wenjianming=wenjianming+"LUe5"
    elif lue==6:
        wenjianming=wenjianming+"LUe6"
    else:
        print("error:lue ")
        return 0   
 

    wenjianming=wenjianming+".csv"

    print(wenjianming) #test文件路径


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







##---------------------------------------------------------------------------------
## 【測試function】
##---------------------------------------------------------------------------------
#zzz=read_yield("h",1)
#print(zzz)


"""((1, 2.584, 5.16325, 7.74725, 10.393, 13.04825, 15.656, 18.2685, 20.91425), (2, 4.488, 8.96775, 13.45575, 18.05075, 22.66125, 27.18975, 31.7265, 36.32075), (3, 3.944, 7.88075, 11.82475, 
15.863, 19.91575, 23.896, 27.8835, 31.92175), (4, 19.448, 38.86025, 58.30825, 78.221, 98.20525, 117.832, 137.4945, 157.40725), (5, 29.648, 59.2415, 88.8895, 119.23975, 149.674, 179.57575, 209.532, 239.8635), (6, 2.856, 5.70675, 8.56275, 11.48175, 14.39025, 17.25675, 20.1285, 23.03175), (7, 1.088, 2.174, 3.262, 4.376, 5.494, 6.6395, 7.78425, 8.95625), (9, 1.088, 2.174, 3.262, 4.376, 5.494, 6.592, 7.692, 8.806), (10, 15.776, 31.523, 47.299, 63.44025, 79.5925, 95.47825, 111.393, 127.499), (11, 35.224, 70.38325, 105.60725, 141.61125, 177.49775, 212.92825, 
248.421, 284.32625), (12, 10.608, 21.1965, 31.8045, 42.666, 53.5665, 64.683, 75.81825, 87.0405), (13, 3.264, 6.522, 9.786, 13.128, 16.482, 19.872, 23.268, 26.703), (14, 9.656, 19.29425, 
28.95025, 38.837, 48.75925, 58.92025, 69.069, 79.507), (15, 18.496, 36.958, 55.454, 74.392, 93.398, 112.885, 132.3525, 152.3305), (16, 3.808, 7.609, 11.417, 15.316, 19.229, 23.233, 27.237, 31.318), (17, 0.272, 0.5435, 0.8155, 1.0935, 1.3705, 1.6435, 1.917, 2.1935), (18, 26.928, 53.8065, 80.7345, 108.288, 135.8685, 163.7145, 191.5785, 220.0545), (19, 28.152, 56.25225, 84.40425, 113.229, 142.15725, 171.74825, 201.34425, 231.65125), (20, 22.168, 44.29525, 66.46325, 89.161, 111.94025, 135.19125, 158.43, 182.191), (21, 18.768, 37.5015, 56.2695, 75.517, 94.787, 114.5325, 134.2705, 154.53375), (22, 8.84, 17.66375, 26.50375, 35.5585, 44.6405, 53.9105, 63.179, 72.64025), (23, 9.52, 19.0225, 28.5425, 38.2855, 48.0625, 58.056, 68.0495, 78.235), 
(24, 0.816, 1.6305, 2.4465, 3.271, 4.093, 4.91025, 5.72725, 6.56175), (25, 1.088, 2.174, 3.262, 4.356, 5.448, 6.53, 7.61, 8.708), (26, 0.136, 0.27175, 0.40775, 0.5445, 0.681, 0.81625, 0.95125, 1.0885), (27, 0.87, 1.74, 2.6085, 3.4875, 4.368, 5.2365, 6.1035, 6.9885), (28, 1.088, 2.174, 3.262, 4.376, 5.494, 6.638, 7.782, 8.958), (29, 20.4, 40.7625, 61.1625, 82.05, 103.0125, 124.4675, 145.92, 167.9725), (30, 39.032, 77.99225, 117.02425, 156.989, 197.09725, 238.23725, 279.32775, 321.5715), (31, 28.016, 55.9805, 83.9965, 112.7665, 141.51275, 171.05675, 200.6, 230.97575), (32, 17.816, 35.59925, 53.41525, 71.7215, 89.9965, 108.21525, 126.46275, 144.94475), (33, 17.816, 35.59925, 53.41525, 71.43525, 89.45425, 107.2475, 125.04575, 143.1535), (34, 20.264, 40.49075, 60.75475, 81.17625, 101.602, 121.70525, 141.8085, 162.2885), (35, 8.16, 16.305, 24.465, 32.715, 40.97925, 49.15425, 57.32925, 65.664), (36, 14.008, 27.99025, 41.99825, 56.16075, 70.28525, 84.319, 98.35275, 112.682), (37, 33.32, 66.57875, 99.89875, 133.49675, 167.06175, 200.39825, 233.69, 267.62725), (38, 25.024, 50.002, 75.026, 100.2125, 125.3775, 
150.337, 175.2505, 200.6025), (39, 5.847, 11.68725, 17.5305, 23.41675, 29.2965, 35.1, 40.89725, 46.78875), (40, 13.05, 26.1, 39.1275, 52.295, 65.4675, 78.40375, 91.335, 104.48), (41, 24.94, 49.88, 74.777, 99.975, 125.216, 150.11, 174.961, 200.325), (42, 2.32, 4.64, 6.956, 9.2985, 11.6435, 13.9505, 16.2535, 18.6045), (43, 4.785, 9.57, 14.34675, 19.173, 23.99925, 28.7265, 33.4455, 38.2635), (44, 1.305, 2.61, 3.91275, 5.2245, 6.53175, 7.821, 9.108, 10.41975), (45, 0.145, 0.29, 0.43475, 0.5805, 0.72575, 0.869, 1.012, 1.15775), (46, 0.816, 1.6305, 2.4465, 3.282, 4.1205, 4.9785, 5.8365, 6.7185), (47, 45.696, 91.308, 137.004, 183.792, 230.748, 278.796, 326.844, 376.26425), (48, 42.296, 84.51425, 126.81025, 170.1295, 213.5855, 257.9265, 302.276, 347.8475), (49, 39.304, 78.53575, 117.83975, 158.118, 198.48825, 238.5895, 278.762, 319.378), (50, 28.016, 55.9805, 83.9965, 112.58925, 141.15675, 169.902, 198.658, 228.027), (51, 40.12, 80.16625, 120.28625, 160.88425, 201.48525, 241.631, 281.77675, 322.6785), (52, 38.216, 76.36175, 114.57775, 153.22075, 191.9325, 230.222, 268.5095, 307.529), (53, 36.856, 73.64425, 
110.50025, 147.76275, 185.05925, 221.97325, 258.88725, 296.435), (54, 38.352, 76.6335, 114.9855, 153.7355, 192.3695, 230.607, 268.832, 307.7055), (55, 39.168, 78.264, 117.432, 156.9205, 
196.3235, 235.353, 274.34, 313.9175), (56, 30.121, 60.21675, 90.3095, 120.678, 151.0015, 180.934, 210.8255, 241.19175), (57, 10.295, 20.59, 30.86725, 41.25775, 51.655, 61.857, 72.05225, 
82.40725), (58, 20.445, 40.89, 61.29975, 81.95625, 102.648, 122.96175, 143.24025, 163.84575), (59, 27.695, 55.39, 83.03725, 111.07225, 139.0755, 166.511, 193.932, 221.892), (60, 31.32, 62.64, 93.906, 125.465, 157.022, 187.983, 218.899, 250.469), (61, 25.955, 51.91, 77.82025, 103.917, 130.01075, 155.69025, 181.3285, 207.51675), (62, 19.285, 38.57, 57.82175, 77.2065, 96.57975, 115.6595, 134.706, 154.14575), (63, 34.365, 68.73, 103.03575, 137.5785, 172.00275, 205.953, 239.844, 274.38675), (64, 20.3, 40.6, 60.865, 81.2395, 101.5745, 121.5685, 141.5275, 161.8105), (65, 6.96, 13.92, 20.868, 27.83625, 34.79775, 41.634, 48.4635, 55.38525), (66, 0.145, 0.29, 0.43475, 0.5795, 0.72425, 0.86625, 1.00825, 1.15175), (67, 10.744, 21.46825, 32.21225, 43.213, 54.25325, 65.55025, 76.84725, 88.467), (68, 25.704, 51.36075, 77.06475, 103.383, 129.79575, 156.78875, 183.78375, 211.56), (69, 22.168, 44.29525, 66.46325, 89.163, 111.94125, 134.7995, 157.6815, 180.964), (70, 18.36, 36.68625, 55.04625, 73.9095, 92.7435, 112.095, 131.43675, 151.31475), (71, 31.144, 62.23075, 93.37475, 125.23425, 157.0365, 188.752, 220.4675, 252.717), (72, 31.552, 63.046, 94.598, 126.758, 158.898, 190.69, 222.43, 254.6505), (73, 35.088, 70.1115, 105.1995, 140.80425, 176.40825, 211.62825, 246.81375, 282.4815), (74, 44.064, 88.047, 132.111, 176.7465, 221.2485, 265.293, 309.3375, 353.997), (75, 36.176, 72.2855, 108.4615, 145.071, 181.559, 217.6595, 253.76, 290.263), (76, 40.392, 80.70975, 121.10175, 161.94375, 202.6915, 242.88975, 282.9825, 323.62775), (77, 41.818, 83.6215, 125.381, 167.7555, 210.03675, 251.5695, 293.0615, 335.196), (78, 45.24, 90.48, 135.642, 181.48825, 227.30175, 272.2415, 317.13625, 362.737), (79, 40.745, 81.49, 122.16475, 163.49375, 204.7745, 245.21075, 285.625, 326.767), (80, 25.23, 50.46, 75.6465, 101.16, 126.66825, 151.574, 176.47575, 201.80575), (81, 46.4, 92.8, 139.12, 185.94075, 232.70975, 278.47475, 324.23725, 370.7035), (82, 31.465, 62.93, 94.34075, 126.0045, 157.60975, 188.6595, 219.68975, 251.195), (83, 29.725, 59.45, 89.12375, 118.9995, 148.77575, 178.099, 207.3955, 237.15425), (84, 33.35, 66.7, 99.9925, 133.45775, 166.86525, 199.67975, 232.4645, 265.71175), (85, 42.195, 84.39, 126.51225, 168.681, 210.82825, 252.18475, 293.52575, 335.33775), (86, 25.23, 50.46, 75.6465, 100.833, 126.00575, 150.71375, 175.39425, 200.36325), (87, 1.45, 2.9, 4.3475, 5.795, 7.24, 8.66, 10.075, 11.51), (88, 1.088, 2.174, 3.262, 4.376, 5.494, 6.638, 7.782, 8.958), (89, 8.976, 17.9355, 26.9115, 36.102, 45.3255, 54.7635, 64.2015, 73.92), (90, 6.8, 13.5875, 20.3875, 27.352, 34.3385, 41.4925, 48.6435, 56.009), (91, 1.768, 3.53275, 5.30075, 7.1175, 8.931, 10.803, 12.66525, 14.58925), (92, 6.936, 13.85925, 20.79525, 27.891, 34.974, 42.042, 49.10775, 56.29575), (93, 26.52, 52.99125, 79.51125, 106.69875, 133.8765, 160.81275, 187.7245, 214.9995), (94, 22.848, 45.654, 68.502, 91.834, 115.193, 138.327, 161.424, 184.802), (95, 39.984, 79.8945, 119.8785, 160.558, 201.1895, 241.4535, 281.709, 322.349), (96, 30.328, 60.60025, 90.92825, 121.7555, 152.527, 183.01825, 213.509, 244.2845), (97, 24.752, 49.4585, 74.2105, 99.35025, 124.44275, 149.2895, 174.12525, 199.28325), (98, 42.556, 85.08175, 127.59275, 170.88175, 214.09825, 256.6615, 299.2065, 342.31375), (99, 50.75, 101.5, 152.1625, 203.7605, 255.26175, 305.81275, 356.3235, 407.56925), (100, 41.325, 82.65, 123.90375, 165.8755, 207.8445, 248.928, 289.94125, 331.56525), (101, 15.95, 31.9, 47.8225, 64.014, 80.2055, 95.9865, 111.742, 127.696), (102, 28.565, 57.13, 85.64575, 114.496, 143.368, 171.607, 199.8455, 228.3505), (103, 37.99, 75.98, 113.9045, 152.1825, 190.38275, 227.81925, 265.2385, 303.04825), (104, 39.005, 78.01, 116.94775, 156.16175, 195.26325, 233.65425, 272.05475, 310.792), (105, 41.615, 83.23, 124.77325, 166.53475, 208.212, 249.03225, 289.97025, 331.141), (106, 47.27, 94.54, 141.7285, 189.13975, 236.32825, 282.546, 328.6895, 375.24775), (107, 35.815, 71.63, 107.38325, 143.264, 179.08075, 214.03675, 249.00175, 284.24325), (108, 33.35, 66.7, 99.9925, 133.32475, 166.5995, 199.21975, 231.76475, 264.7035), (110, 14.04, 28.053, 42.093, 56.484, 70.875, 85.668, 100.437, 115.6365), (111, 18.07, 36.10525, 54.17525, 72.6945, 91.21625, 110.248, 129.2475, 148.78925), (112, 6.102, 12.19275, 18.29475, 24.573, 30.85275, 37.095, 43.338, 49.65825), (113, 25.16, 50.27375, 75.43375, 101.248, 127.12075, 152.77325, 178.3945, 204.3395), (114, 21.488, 42.9365, 64.4245, 86.42725, 108.50675, 130.388, 152.23225, 174.35175), (115, 42.16, 84.2425, 126.4025, 169.48775, 212.614, 255.4225, 298.1915, 341.428), (116, 42.024, 83.97075, 125.99475, 168.84675, 211.6215, 254.12925, 296.637, 339.597), (117, 45.049, 90.0645, 135.06725, 181.0535, 226.9945, 272.3565, 317.73025, 363.5955), (118, 42.195, 84.39, 126.51225, 169.54, 212.5365, 254.829, 297.08125, 339.83375), (119, 32.335, 
64.67, 96.94925, 129.8925, 162.7825, 195.04475, 227.29475, 259.853), (120, 24.07, 48.14, 72.1685, 96.67975, 121.147, 145.07075, 169.01675, 193.1055), (121, 14.355, 28.71, 43.04025, 57.605, 72.1455, 86.38875, 100.632, 114.9375), (122, 2.61, 5.22, 7.8255, 10.45975, 13.0895, 15.661, 18.22825, 20.8125), (123, 22.11, 44.2225, 66.297, 88.597, 110.8615, 132.71575, 154.50825, 176.38775), (124, 25.945, 51.9, 77.81075, 103.9625, 130.07875, 155.63825, 181.2085, 206.85), (125, 24.94, 49.88, 74.777, 99.85475, 124.8385, 149.2535, 173.67775, 198.2475), (126, 11.745, 
23.49, 35.21475, 47.00025, 58.764, 70.20675, 81.66825, 93.192), (127, 19.14, 38.28, 57.387, 76.59225, 95.7645, 114.41025, 133.08825, 151.8665), (128, 4.03, 8.05225, 12.08225, 16.26725, 20.46, 24.614, 28.768, 32.9375), (129, 1.17, 2.33775, 3.50775, 4.716, 5.9265, 7.13925, 8.3535, 9.5805), (130, 6.37, 12.72775, 19.09775, 25.627, 32.15625, 38.84475, 45.5455, 52.43), (131, 
3.25, 6.49375, 9.74375, 13.075, 16.40625, 19.81875, 23.2375, 26.75), (132, 8.19, 16.36425, 24.55425, 32.949, 41.34625, 49.96525, 58.588, 67.44925), (133, 9.88, 19.741, 29.621, 39.7445, 49.876, 60.28125, 70.6755, 81.3545), (134, 11.18, 22.3385, 33.5185, 44.9545, 56.42775, 67.9955, 79.579, 91.27325), (135, 18.892, 37.7485, 56.6405, 76.15025, 95.62675, 114.94325, 134.224, 
153.73575), (136, 37.536, 75.003, 112.539, 151.16925, 189.809, 228.053, 266.38925, 305.15775), (137, 49.912, 99.73225, 149.64425, 200.85225, 252.13425, 302.94925, 353.76725, 405.14675), 
(138, 42.568, 85.05775, 127.62575, 171.1875, 214.71225, 257.95225, 301.2065, 344.837), (139, 52.999, 105.992, 158.90525, 213.182, 267.37425, 321.0145, 374.7305, 428.91425), (140, 48.43, 
96.86, 145.2065, 194.6425, 244.156, 292.841, 341.52725, 390.71375), (141, 32.045, 64.09, 96.07975, 128.77325, 161.46575, 193.52575, 225.561, 257.85375), (142, 21.75, 43.5, 65.2125, 87.394, 109.5475, 131.214, 152.88925, 174.6585), (143, 18.568, 37.157, 55.715, 74.63825, 93.522, 111.975, 130.455, 148.9855), (144, 5.776, 11.5615, 17.3375, 23.21525, 29.088, 34.816, 40.5535, 46.28825), (145, 26.6, 53.24375, 79.84375, 106.85875, 133.8345, 160.1585, 186.52625, 212.85925), (146, 38.152, 76.36675, 114.51875, 153.10925, 191.652, 229.275, 266.9575, 304.61375), (147, 26.752, 53.548, 80.3, 107.32175, 134.2995, 160.62225, 186.91475, 213.25025), (148, 3.8, 7.60625, 11.40625, 15.25, 19.0875, 22.825, 26.55, 30.2875), (149, 1.3, 2.5975, 3.8975, 5.225, 
6.5575, 7.92, 9.285, 10.685), (150, 28.08, 56.106, 84.186, 113.03775, 141.97775, 171.23, 200.5165, 230.322), (151, 32.76, 65.457, 98.217, 131.91575, 165.661, 199.805, 234.0085, 268.8135), (152, 15.47, 30.91025, 46.38025, 62.204, 78.04425, 94.27625, 110.5495, 127.2385), (153, 26.26, 52.4695, 78.7295, 105.646, 132.5625, 160.1545, 187.778, 216.1685), (154, 7.8, 15.585, 23.385, 31.38, 39.375, 47.587, 55.792, 64.233), (155, 0.91, 1.81825, 2.72825, 3.661, 4.5955, 5.558, 6.5205, 7.508), (156, 1.04, 2.078, 3.118, 4.184, 5.252, 6.352, 7.452, 8.5825), (157, 18.33, 36.62475, 54.95475, 73.8425, 92.76575, 111.72225, 130.6795, 149.94525), (158, 19.7885, 39.548, 59.34475, 79.80225, 100.27375, 120.54375, 140.81275, 161.31875), (159, 26.248, 52.44775, 78.69575, 105.75875, 132.77975, 159.47125, 186.23675, 213.29275), (160, 20.808, 41.57775, 62.38575, 83.77375, 105.17275, 126.33075, 147.50925, 168.90675), (161, 45.696, 91.308, 137.004, 183.86, 230.7615, 277.13475, 323.55825, 370.3535), (162, 49.328, 98.65275, 147.89875, 198.494, 249.08425, 299.0555, 348.9455, 399.44325), (163, 36.105, 72.21, 108.25275, 145.24, 182.23775, 218.56125, 254.9315, 291.67525), (164, 52.345, 104.69, 156.94475, 210.46575, 263.94475, 316.34975, 368.762, 421.63725), (165, 36.478, 72.9745, 109.409, 146.6525, 183.876, 220.281, 256.68825, 293.322), (166, 43.624, 87.31975, 130.94375, 175.5005, 220.0465, 263.48575, 307.03275, 350.725), (167, 39.064, 78.19225, 117.25625, 157.13375, 197.061, 235.956, 274.90375, 313.95825), (168, 50.92, 101.92375, 152.84375, 204.76325, 256.7035, 307.283, 357.8905, 408.57625), (169, 53.048, 106.18325, 159.23125, 213.15625, 266.994, 319.523, 372.05925, 424.62825), (170, 48.336, 96.7515, 145.0875, 194.03, 242.904, 290.52675, 338.11675, 385.7625), (171, 14.896, 29.8165, 44.7125, 59.78575, 74.82875, 89.5085, 104.145, 118.82475), (172, 0.456, 0.91275, 1.36875, 1.83075, 2.29125, 2.7435, 3.195, 3.64725), (173, 4.68, 9.351, 14.031, 18.81, 23.607, 28.512, 33.426, 38.466), (174, 33.93, 67.79475, 101.72475, 136.3725, 171.15075, 206.712, 242.3385, 278.8785), (175, 27.17, 54.28775, 81.45775, 109.2995, 137.14875, 165.6735, 194.2505, 223.6075), (176, 21.58, 43.1185, 64.6985, 86.817, 108.936, 131.647, 154.3475, 177.69575), (177, 9.88, 19.741, 29.621, 39.748, 49.875, 60.2775, 70.67525, 81.377), (178, 13.65, 27.27375, 40.92375, 54.915, 68.91075, 83.30475, 97.6835, 112.49325), (179, 3.64, 7.273, 10.913, 14.644, 18.382, 22.232, 26.082, 30.044), (180, 15.6, 31.17, 46.77, 62.76, 78.78, 95.28, 111.78, 128.7"""