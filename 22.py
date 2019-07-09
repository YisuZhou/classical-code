# 其实在手写NMS的时候就已经用过了
# 这边给一个两个矩形的IOU


# 左上角x,左上角y，右下角x，右下角y
rect1 = [x11,y11,x12,y12]
rect2 = [x21,y21,x22,y22]

area1 = (x12-x11+1)*(y12-y11+1)
area2 = (x22-x21+1)*(y22-y21+1)

# 交集部分的左
inter_x1 = max(x11,x21)
inter_y1 = max(y11,y21)
# 交集部分的右
inter_x2 = min(x12,x22)
inter_y2 = min(y12,y22)
# 交集部分
inter_w = max(0, inter_x2 - inter_x1)
inter_h = max(0, inter_y2 - inter_y1)
area_inter = inter_w * inter_h

iou = area_inter / (area1 + area2 - area_inter)
