# 堆，是完全二叉树，并且，任一节点元素都大于/小于其子节点的，与搜索树不同的是，左右子节点之间没关系
# 最大/小堆，先建堆，然后上浮(和父节点比较)or下沉(跟孩子节点比较)，一般选下沉，可以只遍历一半的点，
# 因为其中有孩子的点只有一半。以下用的都是下沉
# 在一个堆中，起始位置为0的话，位置为k的父节点位置为k//2，左孩子位置为2k+1和2k+2
步骤一    构造初始堆。
将给定无序序列构造成一个大顶堆（一般升序采用大顶堆，降序采用小顶堆)。
1. 度数为2的结点A，如果它的左右孩子结点的最大值比它大的，将这个最大值和该结点交换
2. 度数为1的结点A，如果它的左孩子的值大于它，则交换
3. 如果结点A被交换到新的位置，还需要和其孩子结点重复上面的过程
调整的结点的起点在n//2，往前，保证所有调整的结点都有孩子结点
步骤二     将堆顶元素与末尾元素进行交换，使末尾元素最大。
步骤三     然后继续调整堆，再将堆顶元素与末尾元素交换，得到第二大元素。如此反复进行交换、重建、交换。

def pile_sort(list_in):
    #首先创建大顶堆，从(length - 2)//2号节点开始到根节点结束以父节点
    creat_head(list_in)
    #然后交换根节点和末尾节点，并且继续调整大顶堆
    for i_last in range(len(list_in)-1,-1,-1):
        list_in[0], list_in[i_last] = list_in[i_last], list_in[0]
        max_head(list_in, i_last, 0)  #注意调整大顶堆的时候父节点一直是0，是从0开始往下到末尾未排序区的最后。
    return list_in
def creat_head(list_in):  # 建堆
    length = len(list_in)
    i_child_max = (length - 2)//2
    for i in range(i_child_max,-1,-1):
        max_head(list_in,length,i)  #注意形成大顶堆时每次是从i还是往下到最后，i是父节点，i一定有孩子，i是从后往前的
def max_head(list_in,i_last,i_root):  # 下沉，list,结束位置，起始位置
    i_left = 2*i_root + 1
    i_right = 2*i_root +2
    i_large = i_root
    if i_left < i_last and list_in[i_left] > list_in[i_large]:
        i_large = i_left
    if i_right < i_last and list_in[i_right] > list_in[i_large]:
        i_large = i_right
    if i_large != i_root:
        list_in[i_root], list_in[i_large] = list_in[i_large], list_in[i_root]
        max_head(list_in, i_last, i_large)  
