SVM 线性分类器  
  
距离最接近的数据点称为 支持向量（support vector）。  
支持向量定义的沿着分隔线的区域称为 间隔（margin） 。  
  
在三维情形下，SVM寻找一个 平面（plane），而在更高维度下，SVM寻找一个 超平面（hyperplane），二维直线和三维平面在任意维度上的推广。  
这也正是支持向量得名的由来。在高维下，数据点是多维向量，间隔的边界也是超平面。支持向量位于间隔的边缘，“支撑”起间隔边界超平面。  
SVM 允许通过惩罚因子 C 指定愿意接受多少误差。C 越大，容许度越低。  
  
可以被一条直线（更一般的，一个超平面）分割的数据称为 线性可分（linearly separable）数据。  
超平面起到 线性分类器（linear classifier）的作用。  
  
SVM 擅长寻找超平面的技术，但数据却是非线性可分的。那我们需要将数据投影到一个线性可分的空间，然后在那个空间寻找超平面！  
Cover定理，投影到高维空间后，数据 更可能线性可分。  
核（kernels）就是为了实现到高维空间的投影。找到合适的核函数即可实现线性可分。  
核函数接受原始空间中两个数据点作为输入，可以 直接给出投影空间中的点积。  
核函数，比如 多项式（Polynomial）、 径向基函数（Radial Basis Function，RBF） 、 Sigmoid 。  
  
SVM的目标是在正确分类的前提下，最大化间隔宽度  
目标函数是二次的，约束条件是线性的，这是一个凸二次规划问题。是不等式约束的优化问题    
拉格朗日对偶（Lagrange Duality）变换，可以进一步将其转换为 对偶变量（dual variable） 优化问题  
为什么SVM需要把原始问题转化成对偶问题：  
（从minmax的原始问题，转化为maxmin的对偶问题，一者，获得近似解，二者，转化为对偶问题后，更容易求解。）  
1 对偶问题将原始问题中的约束转为了对偶问题中的等式约束  
2 方便核函数的引入  
3 改变了问题的复杂度。由求特征向量w转化为求比例系数a，在原始问题下，求解的复杂度与样本的维度有关，即w的维度。在对偶问题下，只与样本数量有关。  
4 求解更高效，因为只用求解比例系数a，而比例系数a只有支持向量才为非0，其他全为0  
  
另，SVM采用的损失函数是hingle loss  
https://blog.csdn.net/lz_peter/article/details/79614556  
https://blog.csdn.net/fendegao/article/details/79968994  
  
推导参考  
https://blog.csdn.net/xiaocong1990/article/details/83037848  
https://blog.csdn.net/b285795298/article/details/81977271  
http://www.sohu.com/a/309305122_717210
