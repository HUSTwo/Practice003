#计算三角形的面积函数
a=float(input('请输入三角形a边的边长：'))
##input函数读到的是一个字符串，而我们a需要的是一个浮点数，所以要加上一个float
b==float(input('请输入三角形b边的边长：'))
c==float(input('请输入三角形c边的边长：'))


h=(a+b+c)/2
area = (h*(h-a)*(h-b)*(h-c))**0.5
print(area)