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
def read_grid():

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



    #print(a[3])  # 測試輸出用
    return(a)




##---------------------------------------------------------------------------------
## 【測試function】
##---------------------------------------------------------------------------------
zzz=read_grid()
print(zzz)
'''((1, 90, -72), (2, 170, -72), (3, 130, -52), (4, 150, -52), (5, 170, -52), (6, 190, -52), (7, 270, -52), (8, 290, -52), (9, 150, -32), (10, 170, -32), (11, 190, -32), (12, 210, -32), (13, 230, -32), (14, 250, -32), (15, 270, -32), (16, 290, -32), (17, 170, -12), (18, 190, -12), (19, 210, -12), (20, 230, -12), (21, 250, -12), (22, 270, -12), (23, 290, -12), (24, 370, -12), (25, 390, -12), (26, 410, -12), (27, 450, -12), (28, 190, 8), (29, 210, 8), (30, 230, 8), (31, 250, 8), (32, 270, 8), (33, 290, 8), (34, 310, 8), (35, 330, 8), (36, 350, 8), (37, 370, 8), (38, 390, 8), (39, 410, 8), (40, 430, 8), (41, 450, 8), (42, 470, 8), (43, 490, 8), (44, 550, 8), (45, 570, 8), (46, 210, 28), (47, 230, 28), (48, 250, 28), (49, 270, 28), (50, 290, 28), (51, 310, 28), (52, 330, 28), (53, 350, 28), (54, 370, 28), (55, 390, 28), (56, 410, 28), (57, 430, 28), (58, 450, 28), (59, 470, 28), (60, 490, 28), (61, 510, 28), (62, 530, 28), 
(63, 550, 28), (64, 570, 28), (65, 590, 28), (66, 610, 28), (67, 230, 48), (68, 250, 48), (69, 270, 48), (70, 290, 48), (71, 310, 48), (72, 330, 48), (73, 350, 48), (74, 370, 48), (75, 390, 48), (76, 410, 48), (77, 430, 48), (78, 450, 48), (79, 470, 48), (80, 490, 48), (81, 510, 48), (82, 530, 48), (83, 550, 48), (84, 570, 48), (85, 590, 48), (86, 610, 48), (87, 630, 48), (88, 210, 68), (89, 250, 68), (90, 270, 68), (91, 290, 68), (92, 310, 68), (93, 330, 68), (94, 350, 68), (95, 370, 68), (96, 390, 68), (97, 410, 68), (98, 430, 68), (99, 450, 68), (100, 470, 68), (101, 490, 68), (102, 510, 68), (103, 530, 68), (104, 550, 68), (105, 570, 68), (106, 590, 68), (107, 610, 68), (108, 630, 68), (109, 270, 88), (110, 290, 88), (111, 310, 88), (112, 330, 88), (113, 350, 88), (114, 370, 88), (115, 390, 88), (116, 410, 88), (117, 430, 88), (118, 450, 88), (119, 470, 88), (120, 490, 88), (121, 510, 88), (122, 530, 88), (123, 550, 88), (124, 570, 88), (125, 590, 88), (126, 610, 88), (127, 630, 88), (128, 190, 108), (129, 210, 108), (130, 250, 108), (131, 270, 108), (132, 290, 108), (133, 310, 108), (134, 330, 
108), (135, 350, 108), (136, 370, 108), (137, 390, 108), (138, 410, 108), (139, 430, 108), (140, 450, 108), (141, 470, 108), (142, 490, 108), (143, 510, 108), (144, 530, 108), (145, 550, 108), (146, 570, 108), (147, 590, 108), (148, 610, 108), (149, 170, 128), (150, 190, 128), (151, 210, 128), (152, 230, 128), (153, 250, 128), (154, 270, 128), (155, 290, 128), (156, 310, 128), (157, 330, 128), (158, 350, 128), (159, 370, 128), (160, 390, 128), (161, 410, 128), (162, 430, 128), (163, 450, 128), (164, 470, 128), (165, 490, 128), (166, 510, 128), (167, 530, 128), (168, 550, 128), (169, 570, 128), (170, 590, 128), (171, 610, 128), (172, 630, 128), (173, 170, 148), (174, 190, 148), (175, 210, 148), (176, 230, 148), (177, 250, 148), (178, 270, 148), (179, 290, 148), (180, 310, 148), (181, 330, 148), (182, 350, 148), (183, 370, 148), (184, 390, 148), (185, 410, 148), (186, 430, 148), (187, 450, 148), (188, 470, 148), (189, 
490, 148), (190, 510, 148), (191, 530, 148), (192, 550, 148), (193, 570, 148), (194, 590, 148), (195, 610, 148), (196, 630, 148), (197, 190, 168), (198, 210, 168), (199, 230, 168), (200, 250, 168), (201, 270, 168), (202, 290, 168), (203, 310, 168), (204, 330, 168), (205, 350, 168), (206, 370, 168), (207, 390, 168), (208, 410, 168), (209, 430, 168), (210, 450, 168), (211, 470, 168), (212, 490, 168), (213, 510, 168), (214, 530, 168), (215, 550, 168), (216, 570, 168), (217, 590, 168), (218, 610, 168), (219, 630, 168), (220, 650, 168), (221, 250, 188), (222, 270, 188), (223, 290, 188), (224, 310, 188), (225, 330, 188), (226, 350, 188), (227, 370, 188), (228, 390, 188), (229, 410, 188), (230, 430, 188), (231, 450, 188), (232, 470, 188), (233, 490, 188), (234, 510, 188), (235, 530, 188), (236, 550, 188), (237, 570, 188), (238, 590, 188), (239, 610, 188), (240, 630, 188), (241, 650, 188), (242, 250, 208), (243, 270, 208), (244, 290, 208), (245, 310, 208), (246, 330, 208), (247, 350, 208), (248, 370, 208), (249, 390, 208), (250, 410, 208), (251, 430, 208), (252, 450, 208), (253, 470, 208), (254, 490, 208), 
(255, 510, 208), (256, 530, 208), (257, 550, 208), (258, 570, 208), (259, 590, 208), (260, 610, 208), (261, 630, 208), (262, 650, 208), (263, 250, 228), (264, 270, 228), (265, 290, 228), (266, 310, 228), (267, 330, 228), (268, 350, 228), (269, 370, 228), (270, 390, 228), (271, 410, 228), (272, 430, 228), (273, 450, 228), (274, 470, 228), (275, 490, 228), (276, 510, 228), (277, 530, 228), (278, 550, 228), (279, 570, 228), (280, 590, 228), (281, 610, 228), (282, 630, 228), (283, 650, 228), (284, 210, 248), (285, 230, 248), (286, 250, 248), (287, 270, 248), (288, 290, 248), (289, 310, 248), (290, 330, 248), (291, 350, 248), (292, 370, 248), (293, 390, 248), (294, 410, 248), (295, 430, 248), (296, 450, 248), (297, 470, 248), (298, 490, 248), (299, 510, 248), (300, 530, 248), (301, 550, 248), (302, 570, 248), (303, 590, 248), (304, 610, 248), (305, 630, 248), (306, 650, 248), (307, 190, 268), (308, 210, 268), (309, 230, 268), (310, 250, 268), (311, 270, 268), (312, 290, 268), (313, 310, 268), (314, 330, 268), (315, 350, 268), (316, 370, 268), (317, 390, 268), (318, 410, 268), (319, 430, 268), (320, 450, 
268), (321, 470, 268), (322, 490, 268), (323, 510, 268), (324, 530, 268), (325, 550, 268), (326, 570, 268), (327, 590, 268), (328, 610, 268), (329, 630, 268), (330, 190, 288), (331, 210, 288), (332, 230, 288), (333, 250, 288), (334, 270, 288), (335, 290, 288), (336, 310, 288), (337, 330, 288), (338, 350, 288), (339, 370, 288), (340, 390, 288), (341, 410, 288), (342, 430, 288), (343, 450, 288), (344, 470, 288), (345, 490, 288), (346, 510, 288), (347, 530, 288), (348, 550, 288), (349, 210, 308), (350, 230, 308), (351, 250, 308), (352, 270, 308), (353, 290, 308), (354, 310, 308), (355, 330, 308), (356, 350, 308), (357, 370, 308), (358, 390, 308), (359, 410, 308), (360, 430, 308), (361, 450, 308), (362, 470, 308), (363, 490, 308), (364, 510, 308), (365, 530, 308), (366, 550, 308), (367, 230, 328), (368, 250, 328), (369, 270, 328), (370, 290, 328), (371, 310, 328), (372, 330, 328), (373, 350, 328), (374, 370, 328), (375, 
390, 328), (376, 410, 328), (377, 430, 328), (378, 450, 328), (379, 470, 328), (380, 490, 328), (381, 510, 328), (382, 530, 328), (383, 550, 328), (384, 250, 348), (385, 270, 348), (386, 290, 348), (387, 310, 348), (388, 330, 348), (389, 350, 348), (390, 370, 348), (391, 390, 348), (392, 410, 348), (393, 430, 348), (394, 450, 348), (395, 470, 348), (396, 490, 348), (397, 510, 348), (398, 530, 348), (399, 290, 368), (400, 310, 368), (401, 330, 368), (402, 350, 368), (403, 370, 368), (404, 390, 368), (405, 410, 368), (406, 430, 368), (407, 450, 368), (408, 470, 368), (409, 490, 368), (410, 510, 368), (411, 530, 368), (412, 310, 388), (413, 330, 388), (414, 350, 388), (415, 370, 388), (416, 390, 388), (417, 410, 388), (418, 430, 388), (419, 450, 388), (420, 470, 388), (421, 490, 388), (422, 510, 388), (423, 530, 388), (424, 310, 408), (425, 330, 408), (426, 350, 408), (427, 370, 408), (428, 390, 408), (429, 410, 408), (430, 430, 408), (431, 450, 408), (432, 470, 408), (433, 490, 408), (434, 510, 408), (435, 290, 428), (436, 310, 428), (437, 330, 428), (438, 350, 428), (439, 370, 428), (440, 390, 428), 
(441, 410, 428), (442, 430, 428), (443, 450, 428), (444, 470, 428), (445, 490, 428), (446, 210, 448), (447, 230, 448), (448, 250, 448), (449, 290, 448), (450, 310, 448), (451, 330, 448), (452, 350, 448), (453, 370, 448), (454, 390, 448), (455, 410, 448), (456, 430, 448), (457, 450, 448), (458, 470, 448), (459, 190, 468), (460, 210, 468), (461, 230, 468), (462, 250, 468), (463, 270, 468), (464, 290, 468), (465, 310, 468), (466, 330, 468), (467, 350, 468), (468, 370, 468), (469, 390, 468), (470, 410, 468), (471, 430, 468), (472, 450, 468), (473, 190, 488), (474, 210, 488), (475, 230, 488), (476, 250, 488), (477, 270, 488), (478, 290, 488), (479, 310, 488), (480, 330, 488), (481, 350, 488), (482, 370, 488), (483, 390, 488), (484, 410, 488), (485, 430, 488), (486, 450, 488), (487, 210, 508), (488, 230, 508), (489, 250, 508), (490, 270, 508), (491, 290, 508), (492, 310, 508), (493, 330, 508), (494, 350, 508), (495, 370, 508), (496, 390, 508), (497, 410, 508), (498, 430, 508), (499, 150, 528), (500, 170, 528), (501, 210, 528), (502, 230, 528), (503, 250, 528), (504, 270, 528), (505, 290, 528), (506, 310, 
528), (507, 330, 528), (508, 350, 528), (509, 370, 528), (510, 390, 528), (511, 410, 528), (512, 430, 528), (513, 170, 548), (514, 190, 548), (515, 210, 548), (516, 230, 548), (517, 250, 548), (518, 270, 548), (519, 290, 548), (520, 310, 548), (521, 330, 548), (522, 350, 548), (523, 370, 548), (524, 390, 548), (525, 410, 548), (526, 430, 548), (527, 110, 568), (528, 130, 568), (529, 150, 568), (530, 170, 568), (531, 190, 568), (532, 210, 568), (533, 230, 568), (534, 250, 568), (535, 270, 568), (536, 290, 568), (537, 310, 568), (538, 330, 568), (539, 350, 568), (540, 370, 568), (541, 390, 568), (542, 410, 568), (543, 110, 588), (544, 130, 588), (545, 150, 588), (546, 170, 588), (547, 190, 588), (548, 210, 588), (549, 230, 588), (550, 250, 588), (551, 270, 588), (552, 290, 588), (553, 310, 588), (554, 330, 588), (555, 350, 588), (556, 370, 588), (557, 390, 588), (558, 130, 608), (559, 150, 608), (560, 170, 608), (561, 
190, 608), (562, 210, 608), (563, 230, 608), (564, 250, 608), (565, 270, 608), (566, 290, 608), (567, 310, 608), (568, 330, 608), (569, 350, 608), (570, 370, 608), (571, 130, 628), (572, 150, 628), (573, 170, 628), (574, 190, 628), (575, 210, 628), (576, 230, 628), (577, 250, 628), (578, 270, 628), (579, 290, 628), (580, 310, 628), (581, 330, 628), (582, 350, 628), (583, 370, 628), (584, 90, 648), (585, 130, 648), (586, 150, 648), (587, 170, 648), (588, 190, 648), (589, 210, 648), (590, 230, 648), (591, 250, 648), (592, 270, 648), (593, 290, 648), (594, 310, 648), (595, 330, 648), (596, 350, 648), (597, 370, 648), (598, 90, 668), (599, 110, 668), (600, 130, 668), (601, 150, 668), (602, 170, 668), (603, 190, 668), (604, 210, 668), (605, 230, 668), (606, 250, 668), (607, 270, 668), (608, 290, 668), (609, 310, 668), (610, 330, 668), (611, 350, 668), (612, 370, 668), (613, 110, 688), (614, 130, 688), (615, 150, 688), (616, 170, 688), (617, 190, 688), (618, 210, 688), (619, 230, 688), (620, 250, 688), (621, 270, 688), (622, 290, 688), (623, 310, 688), (624, 330, 688), (625, 350, 688), (626, 370, 688), (627, 390, 688), (628, 50, 708), (629, 70, 708), (630, 130, 708), (631, 150, 708), (632, 170, 708), (633, 190, 708), (634, 210, 708), (635, 230, 708), (636, 250, 708), (637, 270, 708), (638, 290, 708), (639, 310, 708), (640, 330, 708), (641, 350, 708), (642, 370, 708), (643, 390, 708), (644, 70, 728), (645, 90, 728), (646, 130, 728), (647, 150, 728), (648, 170, 728), (649, 190, 728), (650, 210, 728), (651, 230, 728), (652, 250, 728), (653, 270, 728), (654, 290, 728), (655, 310, 728), (656, 330, 728), (657, 350, 728), (658, 370, 728), (659, 390, 728), (660, 70, 748), (661, 90, 748), (662, 130, 748), (663, 150, 748), (664, 170, 748), (665, 190, 748), (666, 210, 748), (667, 230, 748), (668, 250, 748), (669, 270, 748), (670, 290, 748), (671, 310, 748), (672, 330, 748), (673, 350, 748), (674, 370, 748), (675, 390, 748), (676, 410, 748), (677, 70, 768), (678, 90, 768), (679, 110, 768), (680, 130, 768), (681, 150, 768), (682, 170, 768), (683, 190, 768), (684, 210, 768), (685, 230, 768), (686, 250, 768), (687, 270, 768), (688, 290, 768), (689, 310, 768), (690, 330, 768), (691, 350, 768), (692, 370, 768), (693, 390, 768), (694, 410, 768), (695, 70, 788), (696, 90, 788), (697, 130, 788), (698, 150, 788), (699, 170, 788), (700, 190, 788), (701, 210, 788), (702, 230, 788), (703, 250, 788), (704, 270, 788), (705, 290, 788), (706, 310, 788), (707, 330, 788), (708, 350, 788), (709, 370, 788), (710, 390, 788), (711, 410, 788), (712, 10, 808), (713, 90, 808), (714, 110, 808), (715, 
130, 808), (716, 150, 808), (717, 170, 808), (718, 190, 808), (719, 210, 808), (720, 230, 808), (721, 250, 808), (722, 270, 808), (723, 290, 808), (724, 10, 828), (725, 90, 828), (726, 110, 828), (727, 130, 828), (728, 150, 828), (729, 190, 828), (730, 210, 828), (731, 230, 828), (732, 250, 828), (733, 270, 828), (734, 290, 828), (735, 310, 828), (736, 90, 848), (737, 110, 848), (738, 130, 848), (739, 150, 848), (740, 210, 848), (741, 230, 848), (742, 250, 848), (743, 270, 848), (744, 290, 848), (745, 310, 848), (746, 330, 848), (747, 110, 868), (748, 
130, 868), (749, 150, 868), (750, 210, 868), (751, 230, 868), (752, 250, 868), (753, 270, 868), (754, 290, 868), (755, 310, 868), (756, 330, 868), (757, 150, 888), (758, 210, 888), (759, 230, 888), (760, 250, 888), (761, 270, 888), (762, 290, 888), (763, 310, 888), (764, 330, 888), (765, 350, 888), (766, 310, 908), (767, 330, 908), (768, 350, 908), (769, 310, 928), (770, 330, 928), (771, 350, 928), (772, 370, 928), (773, 330, 948), (774, 350, 948), (775, 370, 948), (776, 350, 968), (777, 370, 968), (778, 410, 988), (779, 430, 988), (780, 430, 1028), (781, 450, 1028), (782, 390, 1048), (783, 430, 1048), (784, 450, 1048), (785, 390, 1068), (786, 410, 1068), (787, 430, 1068), (788, 450, 1068), (789, 410, 1088), (790, 430, 1088), (791, 450, 1088), (792, 470, 1088), (793, 430, 1108), (794, 450, 1108), (795, 470, 1108), (796, 450, 1128), (797, 470, 1128))'''