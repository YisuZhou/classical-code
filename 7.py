# 简单回顾NMS
# N个框，每个框有分数，有坐标
# 第一步，找到分数最高的一个框box_max
# 第二步，计算所有框和box_max的IOU
# 第三步，把这个box_max存起来，再把所有IOU超过阈值的框的信息废置
# 重复以上三步，直到所有信息都被废置

# 以下代码为Faster rcnn原版
import numpy as np  
def py_cpu_nms(dets, thresh):  
    """Pure Python NMS baseline."""  
    # 所有图片的坐标信息，字典形式储存？？  
    x1 = dets[:, 0]  
    y1 = dets[:, 1]  
    x2 = dets[:, 2]  
    y2 = dets[:, 3]  
    scores = dets[:, 4]  
  
    areas = (x2 - x1 + 1) * (y2 - y1 + 1) # 计算出所有图片的面积  
    order = scores.argsort()[::-1] # 图片评分按升序排序  
  
    keep = [] # 用来存放最后保留的图片的相应评分  
    while order.size > 0:   
        i = order[0] # i 找到最高分
        keep.append(i) # 保留图片的分数
        
        # 矩阵操作，下面计算的是图片i分别与其余图片相交的矩形的坐标。交集部分[左，右]  
        xx1 = np.maximum(x1[i], x1[order[1:]]) #左上角的 x的交集左
        yy1 = np.maximum(y1[i], y1[order[1:]]) #左上角的 y的交集左
        xx2 = np.minimum(x2[i], x2[order[1:]]) #右下角的 x的交集右
        yy2 = np.minimum(y2[i], y2[order[1:]]) #右下角的 y的交集右
        # 计算出各个相交矩形重叠部分的面积
        w = np.maximum(0.0, xx2 - xx1 + 1)  #重叠部分的宽为x的交集右-x的交集左 +1
        h = np.maximum(0.0, yy2 - yy1 + 1)  #重叠部分的高为y的交集右-y的交集左 +1
        inter = w * h
        # 计算重叠比例
        ovr = inter / (areas[i] + areas[order[1:]] - inter)  # IOU是和其他矩形之间的，所以一共order.size-1个值
  
        #只保留比例小于阙值的图片，其他废置
        inds = np.where(ovr <= thresh)[0]  
        order = order[inds + 1]  # 第一位是最高分值的，所以+1
  
    return keep
