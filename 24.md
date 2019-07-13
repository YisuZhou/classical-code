基本上有两个想法  
  
一是  
从几何上通过切割计算面积。  
先通过两条线段的交点，计算出两个矩形的交点。  
会有两种情况，相交部分是直角三角形，或是有一对角为直角的四边形  
后者可切分成两个直角三角形计算面积  
以上可得出相交部分的面积  
https://blog.csdn.net/cjbww/article/details/76973073  
  
二是  
通过计数的方式  
用cv2.fillPoly分别填充两个矩形  
再用cv2.bitwise_and/or求出交/并集  
计算交集的像素点个数为多少  
https://blog.csdn.net/wuguangbin1230/article/details/80609477  
