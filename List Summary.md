## Python内置对象类型——“列表(list)”的综述 

### 一、列表的基本知识和应用特点

### 1 基本知识

#### 1.1 列表的定义
列表是Python中最基本的一种数据类型，由一系列按特定顺序排列的元素组成，可以创建包含字母表中所有字母(A～Z,a~z)、数字0～9或字符串的列表。也可以将任何东西加入列表，其中的元素之间可以有关系，也可以没有任何关系。在Python中，可以用一个方括号([])来表示列表，并用逗号来分隔其中的元素，另外列表中的数据项不需要具有相同的类型。列表可以进行的操作包括访问、索引、切片、添加元素、删除元素、查找、统计变化和应用其他函数。

#### 1.2 创建列表
列表在创建时，可以给它指定一个名称，以便后续使用这个列表，创建时，用方括号表示列表，各元素之间用逗号分隔，如下所示：


```python
list1 = [1, 2, 3, 4, 5]
list2 = ['lucky','happy','nice','sunshine']
list3 = ["a","b","c","d","e"]
list4 = ['red','green',1998,'blue','777']
print(list1)
print(list2)
print(list3)
print(list4)
```

#### 1.3 访问列表中的元素
访问列表中的元素包括索引和切片两种情况，列表是有序集合，因此要访问列表中的任何元素，只需要把该元素的位置或索引告诉Python即可。
如果要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内即可。注意在Python中，第一个列表元素的索引为0，而不
是1，这与列表操作的底层实现相关。所以根据这种计数方法，要访问列表中的任何元素，都可以将其位置减1，并将结果作为索引。如果要访问
最后一个列表元素，不仅可以通过上述方法进行访问，还可以将索引指定为-1，这样就可以返回最后一个列表元素。下图是列表中的索引和值的
对应关系。

![](https://cdn.jsdelivr.net/gh/CheneyLu-71/Pictures/2020-11-1/1604204871924-picture1.png)

![](https://cdn.jsdelivr.net/gh/CheneyLu-71/Pictures/2020-11-1/1604204878697-picture2.png)

一次可以访问一个或多个列表元素，通过下面的例子说明。


```python
list_ = [1,3,'green','Lucy',"a","c",2000,"hello"]
print(list_[0])     # 返回列表第1个元素
print(list_[1:3])   # 返回列表第2、3个元素
print(list_[-1])    # 返回列表最后一个元素
print(list_[:-2])   # 返回第1至倒数第2个元素
```

    索引是指使用中括号[]来定位数据元素，不仅可以定位到单个元素，也可以定位到多个元素。
    切片返回的是和被切片对象相同类型对象的副本。要创建切片，可以指定要使用的第一个元素和最后一个元素的索引。下面举例说明索引和切片的区别。


```python
list_ = [1,3,'green',"a","c",[4,5,6],"hello"]
# 索引
print(list_[3])
print(list_[5][2])
# 切片
print(list_[0:6:2])
print(list_[::-1])
```

#### 1.4 更新列表元素 
一般创建的列表都是动态的，可以随着程序的运行更新列表，更新列表元素包括修改、添加和删除元素。

##### 1.4.1 修改列表元素
修改列表元素时，可以指定列表名和要修改的元素的索引，再指定该元素的新值，比如有一个颜色列表，要把第3个元素改成紫色，可以这样操作。


```python
color = ['blue','dark','green','orange','pink','yellow','red']
print(color)
color[2] = 'purple'
print(color)
```

##### 1.4.2 在列表中添加元素
在列表中添加元素主要有两种情况：
    * 在列表末端添加元素——append函数
    * 在列表中插入元素——insert函数
append()方法可以动态地创建列表，可以把各个元素依次添加到一个空列表中；insert()方法可以在列表的任何位置添加新元素，
需要指定新元素的索引和值。通过以下例子来说明这两种情况。


```python
# append()方法
color = ['blue','dark','green','orange','pink']
print(color)
color.append('red')  # 在列表末端直接添加一个新元素
print(color)

# 创建空列表，并一个个添加数字
num = []
for i in range(10):
    num.append(i)
print(num)
```


```python
# insert()方法
color = ['blue','dark','green','orange','pink']
print(color)
color.insert(1,'red')  # 在索引1处插入新元素
print(color)
```

    ['blue', 'dark', 'green', 'orange', 'pink']
    ['blue', 'red', 'dark', 'green', 'orange', 'pink']


##### 1.4.3 删除列表元素
如果不想要列表中的某个或某些元素，可以将它从列表中删除，Python提供了三种从列表中删除元素的方法，包括del( ),pop( ),remove( )，
具体阐述这三种方法的用法。
    
1.使用del( )语句删除元素

    如果可以确定要删除的元素在列表中的具体位置，可以直接使用del()语句删除某个元素，并且该操作之后不能
    继续使用被del的元素。


```python
list_ = [1,3,'green',"a","c",[4,5,6],"hello"]
print(list_)
del list_[2]    # 删除索引为2的因素（第三个因素）
print(list_)
del list_[4][0]
print(list_)
```

    [1, 3, 'green', 'a', 'c', [4, 5, 6], 'hello']
    [1, 3, 'a', 'c', [4, 5, 6], 'hello']
    [1, 3, 'a', 'c', [5, 6], 'hello']


2.使用pop( )语句删除元素
    
    如果想要从列表中删除某个元素并继续使用它的值，可以使用pop()语句删除列表末端的元素，如果确定要删除元素的索引，
    也可以弹出列表中任何位置的元素。pop()最大的好处是可以继续使用这个被弹出的元素。


```python
# 弹出列表末端的元素
color = ['blue','dark','green','orange','pink']
print(color)
colorpop = color.pop()
print(color)
print(colorpop)   # 可以继续使用被弹出的元素

# 弹出某一位置的元素
colorpop = color.pop(1)
print(color)
print(f'My favorite color is {colorpop} !')   # 可以继续使用被弹出的元素
```

    ['blue', 'dark', 'green', 'orange', 'pink']
    ['blue', 'dark', 'green', 'orange']
    pink
    ['blue', 'green', 'orange']
    My favorite color is dark !


3.使用remove( )语句删除元素
    
    如果不知道要删除的元素位置，但是知道要删除元素的值，可以使用remove()方法。并且该方法只删除第一个指定的值，
    如果要删除的值在列表中出现多次，就需要用循环来判断是否删除了所有这样的值。


```python
list_1 = [1,3,'green',"a","c",4,'green',3,"d",3]
print(list_1)
list_1.remove(4)
print(list_1)
list_1.remove('green')   # 只删除第一个green
print(list_1)
```

    [1, 3, 'green', 'a', 'c', 4, 'green', 3, 'd', 3]
    [1, 3, 'green', 'a', 'c', 'green', 3, 'd', 3]
    [1, 3, 'a', 'c', 'green', 3, 'd', 3]


#### 1.5 查找列表元素


```python
find = [1,3,4,'a','b','green','lucky']
print(4 in find)
print('a' not in find)  # 查找a是否在字符串里
print('d' not in find)
```

    True
    False
    True


#### 1.6 列表的拼接、重复和嵌套

##### 1.6.1 列表的拼接
列表支持拼接操作，可以将两个列表通过加号“+”或者extend方法拼接成一个列表。


```python
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d']
list_new = list1 + list2   # 使用“+”进行拼接
print(list_new)
```

    [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd']



```python
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d']
list1.extend(list2)    # 使用a.extend(b)进行拼接
print(list1)
```

    [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd']


##### 1.6.2 列表的重复
如果想要重复某一个列表多次，可以使用“*”进行重复。


```python
repeat = [1,2,3,'a','c','green']
print(repeat * 3)    # 将字符串重复3次
```

    [1, 2, 3, 'a', 'c', 'green', 1, 2, 3, 'a', 'c', 'green', 1, 2, 3, 'a', 'c', 'green']


##### 1.6.3 列表的嵌套
一个列表中可以嵌套一个或者多个列表，可以在列表中创建其他列表，也可以进行索引、切片等其它操作。


```python
list1 = [1,2,3,4]
list2 = ['a','b','c','d']
new_list =  [list,list2]
print(new_list)
print(new_list[1][2])
```

    [<class 'list'>, ['a', 'b', 'c', 'd']]
    c


### 2 应用特点

#### 2.1 组织列表
创建列表时，列表中元素的顺序是无法预测的，也不是可以完全控制的，需要将列表以特定的顺序呈现信息，这时就要对列表进行排序。
有时候希望保留列表元素最初的排列顺序，有时候需要调整排列顺序，Python中有不同的语法可以实现这些目标。

##### 2.1.1 永久性排序
sort( )方法可以对列表进行永久性排序，也就是永久地修改了列表元素的排列顺序，无法恢复到原来的排列顺序。如果想要逆序排序，可以修改传递参数reverse=True。


```python
_list = ['Mac','ysl','Gucci','lancome','Armani']
_list.sort()   # 永久修改，无法恢复
print(_list)
_list.sort(reverse = True) 
print(_list)   # 逆序排列
```

    ['Armani', 'Gucci', 'Mac', 'lancome', 'ysl']
    ['ysl', 'lancome', 'Mac', 'Gucci', 'Armani']


##### 2.1.2 临时排序
sorted( )方法既可以保留列表元素原来的排列顺序，也可以以特定的顺序呈现列表元素，如果想要逆序排序，同样可以修改传递参数reverse=True。


```python
_list = ['Mac','ysl','Gucci','lancome','Armani']
print(sorted(_list))   # 临时修改
print(_list)             # 输出的还是原来的列表顺序
print(sorted(_list,reverse = True))   # 逆序排列
print(_list)   # 依旧没有改变原始列表的顺序
```

    ['Armani', 'Gucci', 'Mac', 'lancome', 'ysl']
    ['Mac', 'ysl', 'Gucci', 'lancome', 'Armani']
    ['ysl', 'lancome', 'Mac', 'Gucci', 'Armani']
    ['Mac', 'ysl', 'Gucci', 'lancome', 'Armani']


##### 2.1.3 反向打印列表元素
如果要反向打印出列表中的各个元素，可使用reverse( )方法，这仅仅是反转列表元素的排列顺序。


```python
_list = ['Mac','ysl','Gucci','lancome','Armani']
_list.reverse()
print(_list)
```

    ['Armani', 'lancome', 'Gucci', 'ysl', 'Mac']


#### 2.2 遍历列表
如果想要遍历列表中的所有元素，对每个元素执行相同的操作，可以使用for循环完成操作，最后将遍历的元素打印出来。编写for循环时，对于用于存储列表中每个值的临时变量，可指定任何名称，一般可以用i表示，但是如果选择描述单个列表元素的有意义的名称会更加有帮助。


```python
_list = ['Mac','ysl','Gucci','lancome','Armani']
for i in _list:
    print(i)
```

    Mac
    ysl
    Gucci
    lancome
    Armani


另外在for循环中可以执行更多操作，可以对每个因素进行不同的操作。用for循环处理数据是一种对数据集进行整体操作的很好的方式。比如下面的代码就是在遍历列表之后，对列表元素进行了处理。


```python
color = ['red','pink','blue','dark','orange']
for col in color:
    print("What is your favorite color?")
    print(f"My favorite color is {col}")
```

    What is your favorite color?
    My favorite color is red
    What is your favorite color?
    My favorite color is pink
    What is your favorite color?
    My favorite color is blue
    What is your favorite color?
    My favorite color is dark
    What is your favorite color?
    My favorite color is orange


#### 2.3 创建数值列表
列表可以用于存储数字集合，Python中有些工具可以高效处理数值列表，如range( )可以生成一系列的数字，并将它们打印出来。不仅可以使用range( )打印数据，而且可以使用range( )创建数字列表并进行统计计算。


```python
# 使用range打印数字
for value in range(1,6):  #输出1-5的整数
    print(value)
```

    1
    2
    3
    4
    5



```python
# 使用range创建数值列表
num1 = list(range(1,8))
print(num1)

num2 = list(range(1,10,2))   # 指定步长
print(num2)

num3 = list(range(10,1,-2))  # 倒序输出
print(num3)
```

    [1, 2, 3, 4, 5, 6, 7]
    [1, 3, 5, 7, 9]
    [10, 8, 6, 4, 2]


#### 2.4 列表的统计计算
Python中提供了专门处于数字列表的函数，可以进行简单的统计计算。比如可以利用max( )、min( )函数计算最大值和最小值，利用sum( )对列表元素求和，利用len( )计算列表的长度，利用count( )统计某个元素在列表中出现的次数等等。


```python
# 计算一个列表中的最大值、最小值、总和
dig = [1,2,3,4,5,6,7,8,9,10]
print(f"最大值为：{max(dig)}")
print(f"最小值为：{min(dig)}")
print(f"总和为：{sum(dig)}")
print(f"列表长度为：{len(dig)}")

dig_ = [1,1,2,1,2,3,5,6,4,5,6,6]
print(dig_.count(1))

```

    最大值为：10
    最小值为：1
    总和为：55
    列表长度为：10
    3


#### 2.5 列表解析
列表解析方法的最大优点就是简洁，只需要编写一行代码就可以生成列表，它将for循环和创建新元素的代码合并成一行，并自动添加新元素。


```python
# 用列表解析的方法输出列表数值的平方
squares = [value ** 2 for value in range(1,6)]
print(squares)
```

    [1, 4, 9, 16, 25]


#### 2.6 使用列表中的一部分
##### 2.6.1 遍历切片 
如果要遍历列表的部分元素，可以在for循环中使用切片操作，这样就可以只选择需要的元素。


```python
# 遍历切片
color = ['red','pink','blue','dark','orange']
for col in color[:3]:    #只遍历前三个元素
    print(col)   
```

    red
    pink
    blue


##### 2.6.2 复制列表
根据既有列表创建全新的列表，可以进行复制操作，复制列表时，可以创建一个包含整个列表的切片，同时省略起始索引和终止索引即可。


```python
# 复制列表
color = ['red','pink','blue','dark','orange']
for col in color[:]:    # 复制列表
    print(col)    
```

    red
    pink
    blue
    dark
    orange


#### 2.7 不可变得列表--元组
列表是可以修改的，但是有时候需要创建一系列不可修改的元素，元组就可以满足这种需求。不可变的列表被称为元组，使用圆括号来表示。定义元组后，可以像访问列表
一样访问元组的元素。


```python
# 创建元组
dim = (20,45,67,98)
print(dim[1])
print(dim[2])
for i in dim:  # 遍历元组中的元素
    print(i)
```

    45
    67
    20
    45
    67
    98


### 二、列表与数组之间的异同

### 1 列表和数组定义

    列表(List)是Python中最基本的数据结构，它可以作为一个方括号内的逗号分隔值出现，列表的数据项不需要具有相同的类型。在List中的数据类型保存的是数据的存放的地址，简单的说就是指针，并非数据。

    Python原生没有数组(array)的概念，这点不同于Java之类的面向对象语言。数组是Numpy库中所定义的，所以在使用数组之前必须下载安装Numpy库。Numpy中封装的array有很强大的功能，里面存放的都是相同的数据类型，每个元素在内存中都有相同存储大小的区域。Numpy数组的维数称为秩（rank），秩就是轴的数量，即数组的维度，一维数组的秩为1，二维数组的秩为2，以此类推。在NumPy中，每一个线性的数组称为是一个轴（axis），也就是维度（dimensions）。
    
    Python中原生的列表使用起来很像数组，但是两者有本质的区别。

### 2 列表与数组之间的不同之处
    （1）Python中的list是python的内置数据类型，可以直接使用；而array不是Python的内置数据类型，它是在Numpy类型中定义的，所以使用之前需要import numpy。
    （2）两者的存储效率和输入输出性能不同。Numpy专门针对数组的操作和运算进行了设计，存储效率和输入输出性能远优于Python中的嵌套列表，数组越大，Numpy的优势就越明显。
    （3）打印出来的列表成员之间是用","分隔的；而数组成员之间是用" "分隔的。
    （4）列表中可以包含任何数据类型(数字、字符串、字母)，也可以包含另一个列表；array的数据成员必须是相同数据类型属性。


```python
# 列表的创建
List = [1,2,'a','f','green',[3,4,'b']]   # 可以是不同的类型
print(List)   # 输出的列表各元素之间以“，”分隔
```

    [1, 2, 'a', 'f', 'green', [3, 4, 'b']]



```python
# 数组的创建
import numpy as np
Array = np.array([1,2,3,4,5])   # 必须是相同的类型
print(Array)        # 输出的数组各元素之间以“ ”分隔
Array2 = np.array(['a','b','c'])
print(Array2)
```

    [1 2 3 4 5]
    ['a' 'b' 'c']


    （5）列表是一维的；array数组是可以多维的，数组的每个维度之间用换行分隔开，单个维度内的数组成员也以换行分隔开,每个并列（单个）维度内的成员个数需要一致，不同维度的成员个数可以不一样。


```python
# 列表是一维的
List = [1,2,'a','s','green',[3,4,5],'b']  
print(List)

# 数组可以是多维的
Array = np.array([[1,2,3],[4,5,6],[7,8,9]])    
print(Array)

Array2 = np.array([[1,2,3,4],  
                  ['a','b','c'],
                  ['green','red','yellow']])
print(Array2)
```

    [1, 2, 'a', 's', 'green', [3, 4, 5], 'b']
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [list([1, 2, 3, 4]) list(['a', 'b', 'c']) list(['green', 'red', 'yellow'])]


    （6）列表创建时参数就是list，而Numpy创建数组时，参数既可以是列表list，也可以是元组tuple。


```python
a = np.array((1,2,3))     # 参数是tuple
print(type(a))

b = np.array([4,5,6])     # 参数是list
print(type(b))
```

    <class 'numpy.ndarray'>
    <class 'numpy.ndarray'>


    （7）列表没有shape，通过len()计算列表中成员(元素)的个数，成员以最外层的[ ]中的逗号","来分隔；array有形状大小shape，即维度，获取的方式有np.shape(a) 或者a.shape，即可得到数组的大小。


```python
# 获取列表元素的个数
List = [1,2,'a','s','green',[3,4,5],'b']  
print(len(List))

# 获取数组的维度
Array = np.array([[1,2,3],[4,5,6],[7,8,9]])   
print(np.shape(Array))
print(Array.shape)
```

    7
    (3, 3)
    (3, 3)


    （8）创建列表的方式比较单一，但是Numpy中有多种创建数组的方式，比如用ones, zeros，eye创建特殊的数组，用arange和linspace创建数组。


```python
# 创建列表
List1 = [1,2,3,'a','b','green','red']
print(List1)
List2 = list(range(1,10))
print(List2)

# 创建数组
Array1 = np.array([[1,2,3],[4,5,6]])    
Array2 = np.ones([3,3])    # 根据shape生成一个全1数组
Array3 = np.zeros([2,3])   # 根据shape生成一个全0数组
Array4 = np.eye(3)         # 创建一个正方的3*3单位矩阵，对角线为1，其余为0
Array5 = np.arange(5)      # 创建一个序列数组
Array6 = np.linspace(1,10,5)     # 把1-10均分成5份
print(Array1)
print(Array2)
print(Array3)
print(Array4)
print(Array5)
print(Array6)
```

    [1, 2, 3, 'a', 'b', 'green', 'red']
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [[1 2 3]
     [4 5 6]]
    [[1. 1. 1.]
     [1. 1. 1.]
     [1. 1. 1.]]
    [[0. 0. 0.]
     [0. 0. 0.]]
    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    [0 1 2 3 4]
    [ 1.    3.25  5.5   7.75 10.  ]


    （9）列表和数组的运算不完全相同。
        *列表中的加法运算表示把两个数组拼接起来，列表之间没有减法、乘除运算。
        *数组中的加法运算表示把数组中的元素对应求和，数组之间有减法、乘除运算。
        *列表乘上一个数字n，表示重复n次列表中的元素；而数组乘上一个数字n，表示数组中的每个元素乘以n。
        *列表求均值的方式和数组不同，数组可以直接使用mean()函数。


```python
List1 = [1,2,3]
List2 = [4,5,6]
List_new = List1 + List2    # 加法运算表示把两个数组拼接起来
print(List_new)   

Array1 = np.array([1,2,3])
Array2 = np.array([4,5,6])
Array_new = Array1 + Array2  # 加法运算表示把数组中的元素对应求和
print(Array_new)
```

    [1, 2, 3, 4, 5, 6]
    [5 7 9]



```python
Array1 = np.array([1,2,3])
Array2 = np.array([4,5,6])   
Array_new = Array1 * Array2     # 可以进行乘法运算
print(Array_new)
```

    [ 4 10 18]



```python
List1 = [1,2,3]
List_new = List1 * 3    # 表示列表重复3次
print(List_new)

Array1 = np.array([1,2,3])
Array_new = Array1 * 3    # 表示数组各元素乘以3
print(Array_new)
```

    [1, 2, 3, 1, 2, 3, 1, 2, 3]
    [3 6 9]



```python
List = [1,3,5,7,9]
mean_list = sum(List) / len(List)   # 列表计算均值，总和/长度
print(mean_list)
Array = np.array([1,3,5,7,9])  
mean_arr = np.mean(Array)          # 数组计算均值
print(mean_arr)
```

    5.0
    5.0


    （8）Numpy中连接数组的方式与列表list不同，列表可以直接通过加号（+）连接数组，但是Numpy可以通过concatenate、stack、hstack、vstack连接数组。
    * numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组，格式如下：numpy.concatenate((a1, a2, ...), axis)
    * numpy.stack 函数用于沿新轴连接数组序列，格式如下：numpy.stack(arrays, axis)
    * numpy.hstack是numpy.stack函数的变体，它通过水平堆叠来生成数组。
    * numpy.vstack是numpy.stack函数的变体，它通过垂直堆叠来生成数组。


```python
a = np.array([[1,2],[3,4]])
print(a)
print('\n')
b = np.array([[5,6],[7,8]])
print(b)
print('\n')
print(np.concatenate((a,b)))    # 沿0轴连接
print('\n')
print(np.concatenate((a,b),axis=1))   # 沿1轴连接
```

    [[1 2]
     [3 4]]
    
    
    [[5 6]
     [7 8]]
    
    
    [[1 2]
     [3 4]
     [5 6]
     [7 8]]
    
    
    [[1 2 5 6]
     [3 4 7 8]]



```python
print(np.stack((a,b),0))   # 沿轴0堆叠两个数组
print('\n')
print(np.stack((a,b),1))   # 沿轴1堆叠两个数组
print('\n')
print(np.hstack((a,b)))    # 通过水平堆叠生成数组
print('\n')
print(np.vstack((a,b)))    # 通过垂直堆叠生成数组
```

    [[[1 2]
      [3 4]]
    
     [[5 6]
      [7 8]]]
    
    
    [[[1 2]
      [5 6]]
    
     [[3 4]
      [7 8]]]
    
    
    [[1 2 5 6]
     [3 4 7 8]]
    
    
    [[1 2]
     [3 4]
     [5 6]
     [7 8]]


    （8）数组可以修改形状，返回指定大小的新数组，而列表不可以。numpy.resize()函数返回指定大小的新数组。   


```python
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
print('\n')
b = np.resize(a,(3,2))    # 修改数组的形状
print(b)
print(b.shape)
```

    [[1 2 3]
     [4 5 6]]
    (2, 3)
    
    
    [[1 2]
     [3 4]
     [5 6]]
    (3, 2)


### 3 列表与数组之间的相同之处
    （1）列表和数组都是以方括号“[]”包围的数据集合。
    （2）两者对象的内容可以通过索引或切片来访问和修改。列表可以通过序号（索引）访问其中成员，成员序号从0开始，数组也通过索引号（下标）来访问数组元素,数组每个维度的元素的起始索引号为0。


```python
# 列表的索引和切片
list_ = [1,3,'green',"a","c",[4,5,6],"hello"]
# 索引
print(list_[3])
print(list_[5][2])
# 切片
print(list_[0:6:2])
print(list_[::-1])
```

    a
    6
    [1, 'green', 'c']
    ['hello', [4, 5, 6], 'c', 'a', 'green', 3, 1]



```python
# 数组的索引和切片
arr_ = np.arange(10)
# 索引
print(arr_[3])
print(arr_[2:])
print(arr_[:-1])
# 切片
s = slice(2,9,2)    #通过内置的slice函数进行切片操作
print(arr_[s])
b = arr_[2:9:2]        #通过冒号分隔切片参数start:stop:step来进行切片操作
print(b)
```

    3
    [2 3 4 5 6 7 8 9]
    [0 1 2 3 4 5 6 7 8]
    [2 4 6 8]
    [2 4 6 8]


    （3）两种数据类型可以相互转换。 
    
    * list→array：np.array(a)
    * array→list：a.tolist()


```python
List = [1,2,3,4,5]
Array = np.arange(5)    
print(type(np.array(List)))   # 列表转化成数组
print(type(Array.tolist()))   # 数组转化成列表
```

    <class 'numpy.ndarray'>
    <class 'list'>


    （4）列表和数组都可以修改元素，都可以增加、插入、删除
    
     前面介绍过list的修改元素方法，现在介绍一下数组的修改元素方法：
     
     1.numpy.append 函数在数组的末尾添加值，追加操作会分配整个数组，并把原来的数组复制到新数组中；
     2.numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值，插入没有原地的，函数会返回一个新数组；
     3.numpy.delete 函数返回从输入数组中删除指定子数组的新数组；
     4.numpy.unique 函数用于去除数组中的重复元素。


```python
# 1.在数组中增加元素
a = np.array([[1,2,3],[4,5,6]])
print(a)
print('\n')
print(np.append(a,[7,8,9]))  # 向数组添加元素，没有传入axis参数，则会默认展开数组
print('\n')
print (np.append(a,[[7,8,9]],axis = 0))    # 沿轴0添加元素
print ('\n')
print (np.append(a,[[4,5,6],[7,8,9]],axis = 1))   # 沿轴1添加元素
```

    [[1 2 3]
     [4 5 6]]
    
    
    [1 2 3 4 5 6 7 8 9]
    
    
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    
    
    [[1 2 3 4 5 6]
     [4 5 6 7 8 9]]



```python
# 2.在数组中插入元素
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print('\n')
print(np.insert(a,3,[10,11]))   # 没有传入axis参数，插入之前数组会被展开
print('\n')
print(np.insert(a,1,[10],axis=0))  # 沿轴0进行广播
print('\n')
print(np.insert(a,1,10,axis=1))   # 沿轴1进行广播
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    
    
    [ 1  2  3 10 11  4  5  6  7  8  9]
    
    
    [[ 1  2  3]
     [10 10 10]
     [ 4  5  6]
     [ 7  8  9]]
    
    
    [[ 1 10  2  3]
     [ 4 10  5  6]
     [ 7 10  8  9]]



```python
# 3.删除数组中的元素
a = np.arange(12).reshape(3,4)
print(a)
print('\n')
print(np.delete(a,4))   # 没有传入axis参数，删除之前数组会被展开
print('\n')
print(np.delete(a,1,axis=0))   # 删除第二行
print('\n')
print(np.delete(a,0,axis=1))   # 删除第一列
```

    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    
    
    [ 0  1  2  3  5  6  7  8  9 10 11]
    
    
    [[ 0  1  2  3]
     [ 8  9 10 11]]
    
    
    [[ 1  2  3]
     [ 5  6  7]
     [ 9 10 11]]



```python
# 4.去除数组中的重复元素
a = np.array([1,2,2,3,3,4,4,5,3,4,6,7,8,9,4])
print(a)
print('\n')
print(np.unique(a))
```

    [1 2 2 3 3 4 4 5 3 4 6 7 8 9 4]
    
    
    [1 2 3 4 5 6 7 8 9]


    （5）列表和数组都可以进行简单的统计计算
    
     前面介绍了列表的一些统计计算函数，所以介绍一下数组的统计计算方法：

     1.numpy.amin()和numpy.amax()用于计算数组中的元素沿指定轴的最小值和最大值；
     2.numpy.ptp()函数计算数组中元素最大值与最小值的差（最大值 - 最小值）；
     3.numpy.mean() 函数返回数组中元素的算术平均值，如果提供了轴，则沿其计算；
     4.numpy.median() 函数用于计算数组 a 中元素的中位数（中值）。


```python
arr = np.array([[2,5,4],[1,8,6],[3,6,9]])
print(np.amin(arr,1))   # 沿轴1计算最小值
print(np.amin(arr,0))   # 沿轴0计算最小值
print(np.amax(arr,1))   # 沿轴1计算最大值
print(np.amax(arr,0))   # 沿轴0计算最大值
print(np.ptp(arr,1))    # 沿轴1计算极差
print(np.ptp(arr,0))    # 沿轴1计算极差
print(np.mean(arr,1))   # 沿轴1计算均值
print(np.mean(arr,0))   # 沿轴1计算均值
print(np.median(arr,1))   # 沿轴1计算中位数
print(np.median(arr,0))   # 沿轴1计算中位数
```

    [2 1 3]
    [1 5 4]
    [5 8 9]
    [3 8 9]
    [3 7 6]
    [2 3 5]
    [3.66666667 5.         6.        ]
    [2.         6.33333333 6.33333333]
    [4. 6. 6.]
    [2. 6. 6.]


    （6）列表和数组都可以进行排序。列表的主要排序方法是sort()、sorted()；数组的排序方法也是sort()（但是数组的sort方法不是永久修改），另外可以利用argsort()返回的是数组值从小到大的索引值。


```python
# 列表的排序
List = [2,3,1,6,3,9,4,8]
List.sort()
print(List)                # 是永久修改排序
# 数组的排序
Array = np.array([2,3,1,6,3,9,4,8])
print(np.sort(Array))      # 返回排序结果
print(Array)               # 返回原来的数组，不是永久修改
print(np.argsort(Array))   # 返回索引值
```

    [1, 2, 3, 3, 4, 6, 8, 9]
    [1 2 3 3 4 6 8 9]
    [2 3 1 6 3 9 4 8]
    [2 0 1 4 6 3 7 5]


    （7）列表和数组都可以用for循环进行遍历，来输出所有元素。


```python
List = list(range(10))   
for i in List:         # 遍历列表
    print(i)
arr = np.arange(0,24).reshape((2,3,4))
for i in arr:         # 遍历数组
    print(i)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    [[12 13 14 15]
     [16 17 18 19]
     [20 21 22 23]]

