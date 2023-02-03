1注释器和简介
    单行注释 #
    Python是一门强类型的语言 ,对象一旦创建类型便不能修改 ,并且是面向对象的解释型 ,缩进要求严格的语言
2变量
    python变量不需要声明直接赋值 ,比如a=1
    Python是一个动态类型的语言 ,可以为变量赋任意类型的值 ,也可以任意修改变量的值

3数值
    Python中的整数的大小没有限制 ,可以是一个无限大的整数
    python是强类型的语言 ,需要类型一样才能进行运算
    None表示空值 ,表示不存在值
4格式化字符串
    创建字符串时 ,可以在字符串中指定占位符
    %s 在字符串中表示任意字符
    %f 浮点数占位符
    %d 整数占位符
    格式化字符串 ,可以通过在字符串前添加一个f来创建一个格式化字符串
    在格式化字符串中可以直接嵌入变量
5类型转换
    类型转换四个函数 int() float() str() bool()
6运算
    算术运算符
        + 加法运算符(如果是两个字符串之间进行加法运算 ,则会进行拼串操作)
        - 减法运算符
        * 乘法运算符(如果将字符串和数字相乘 ,则会对字符串进行复制操作 ,将字符串重复指定次数)
        / 除法运算符 ,运算时结果总会返回一个浮点类型
        // 整除 ,只会保留计算后的整数位 ,总会返回一个整型
        ** 幂运算 ,求一个值的几次幂
        % 取模 ,求两个数相除的余数
    赋值运算符
        = 可以将等号右侧的值赋值给等号左侧的变量
        +=  a += 5 相当于 a = a + 5 
        -=  a -= 5 相当于 a = a - 5 
        *=  a *= 5 相当于 a = a * 5 
        **= a **= 5 相当于 a = a ** 5 
        /=  a /= 5 相当于 a = a / 5 
        //= a //= 5 相当于 a = a // 5 
        %=  a %= 5 相当于 a = a % 5 
    关系运算符
        关系运算符用来比较两个值之间的关系 ,总会返回一个布尔值
        如果关系成立 ,返回True ,否则返回False
        > 比较左侧值是否大于右侧值
        >= 比较左侧的值是否大于或等于右侧的值
        < 比较左侧值是否小于右侧值
        <= 比较左侧的值是否小于或等于右侧的值
        == 比较两个对象的值是否相等
        != 比较两个对象的值是否不相等
        相等和不等比较的是对象的值 ,而不是id
        is 比较两个对象是否是同一个对象 ,比较的是对象的id
        is not 比较两个对象是否不是同一个对象 ,比较的是对象的id
    逻辑运算符
        逻辑运算符主要用来做一些逻辑判断
        not 逻辑非
        not可以对符号右侧的值进行非运算
            对于布尔值 ,非运算会对其进行取反操作 ,True变False ,False变True
            对于非布尔值 ,非运算会先将其转换为布尔值 ,然后再取反
            
        and 逻辑与
        and可以对符号两侧的值进行与运算
        只有在符号两侧的值都为True时 ,才会返回True ,只要有一个False就返回False
        与运算是找False的
        Python中的与运算是短路的与 ,如果第一个值为False ,则不再看第二个值
        
        or 逻辑或
        or 可以对符号两侧的值进行或运算
        或运算两个值中只要有一个True ,就会返回True
        或运算是找True的
        Python中的或运算是短路的或 ,如果第一个值为True ,则不再看第二个值
    
    条件运算符(三元运算符)
        语法: 语句1 if 条件表达式 else 语句2
        执行流程:
        条件运算符在执行时 ,会先对条件表达式进行求值判断
            如果判断结果为True ,则执行语句1 ,并返回执行结果
            如果判断结果为False ,则执行语句2 ,并返回执行结果
        练习:
        现在有a b c三个变量 ,三个变量中分别保存有三个数值 ,
            请通过条件运算符获取三个值中的最大值

    运算符的优先级
        和数学中一样 ,在Python运算也有优先级 ,比如先乘除 后加减
        运算符的优先级可以根据优先级的表格来查询 ,
        在表格中位置越靠下的运算符优先级越高 ,优先级越高的越优先计算
        如果优先级一样则自左向右计算
        关于优先级的表格 ,你知道有这么一个东西就够了 ,千万不要去记
        在开发中如果遇到优先级不清楚的,则可以通过小括号来改变运算顺序

7对象
    - 每个对象中都要保存三种数据
        - id(标识)
            > id用来标识对象的唯一性 ,每一个对象都有唯一的id
            > 对象的id就相当于人的身份证号一样
            > 可以通过id()函数来查看对象的id
            > id是由解析器生成的 ,在CPython中 ,id就是对象的内存地址
            > 对象一旦创建 ,则它的id永远不能再改变

        - type(类型)
            > 类型用来标识当前对象所属的类型
            > 比如:int str float bool 。。。
            > 类型决定了对象有哪些功能
            > 通过type()函数来查看对象的类型
            > Python是一门强类型的语言 ,对象一旦创建类型便不能修改


        - value(值)
            > 值就是对象中存储的具体的数据
            > 对于有些对象值是可以改变的
            > 对象分成两大类 ,可变对象 不可变对象
                可变对象的值可以改变
                不可变对象的值不能改变 ,之前学习的对象都是不可变对象

8条件判断语句(if语句)
    语法:if 条件表达式 : 
            代码块
    执行的流程:if语句在执行时 ,会先对条件表达式进行求值判断 ,
    如果为True ,则执行if后的语句
    如果为False ,则不执行
    默认情况下 ,if语句只会控制紧随其后的那条语句 ,如果希望if可以控制多条语句 ,
    则可以在if后跟着一个代码块
    代码块
    代码块中保存着一组代码 ,同一个代码块中的代码 ,要么都执行要么都不执行
    代码块就是一种为代码分组的机制
    如果要编写代码块 ,语句就不能紧随在:后边 ,而是要写在下一行
    代码块以缩进开始 ,直到代码恢复到之前的缩进级别时结束
    鲁迅说过:
        世上本来没有路 ,走的人多了自然就有了！
        xxxx
    yyyy....
    缩进有两种方式 ,一种是使用tab键 ,一种是使用空格(四个)
    Python的官方文档中推荐我们使用空格来缩进
    Python代码中使用的缩进方式必须统一
    语法:if False : print('你猜我出来么？')

9input()函数
    该函数用来获取用户的输入
    input()调用后 ,程序会立即暂停 ,等待用户输入
    用户输入完内容以后 ,点击回车程序才会继续向下执行
    用户输入完成以后 ,其所输入的的内容会以返回值得形式返回
    注意:input()的返回值是一个字符串
    input()函数中可以设置一个字符串作为参数 ,这个字符串将会作为提示文字显示
    a = input('请输入任意内容:')
    print('用户输入的内容是:',a)
    input()也可以用于暂时阻止程序结束

10if语句
    if-else语句
        语法: 
        if 条件表达式 :
            代码块
        else :
            代码块
        执行流程:
        if-else语句在执行时 ,先对if后的条件表达式进行求值判断
            如果为True ,则执行if后的代码块
            如果为False ,则执行else后的代码块
    
    if-elif-else语句
        语法:
        if 条件表达式 :
            代码块
        elif 条件表达式 :
            代码块
        elif 条件表达式 :
            代码块
        elif 条件表达式 :
            代码块
        else :
            代码块
            
        执行流程:
        if-elif-else语句在执行时 ,会自上向下依次对条件表达式进行求值判断 ,
            如果表达式的结果为True ,则执行当前代码块 ,然后语句结束
            如果表达式的结果为False ,则继续向下判断 ,直到找到True为止
            如果所有的表达式都是False ,则执行else后的代码块
        if-elif-else中只会有一个代码块会执行

11循环语句
    while循环
        循环语句可以使指定的代码块重复指定的次数
        循环语句分成两种 ,while循环 和 for循环
        while循环
        语法:
        while 条件表达式 :
            代码块
        else :
            代码块
        执行流程:
        while语句在执行时 ,会先对while后的条件表达式进行求值判断 ,
            如果判断结果为True ,则执行循环体(代码块) ,
            循环体执行完毕 ,继续对条件表达式进行求值判断 ,以此类推 ,
            直到判断结果为False ,则循环终止 ,如果循环有对应的else ,则执行else后的代码块

        条件表达式恒为True的循环语句 ,称为死循环 ,它会一直运行 ,慎用！
        while True :
            print('hello')

        循环的三个要件(表达式)
        初始化表达式 ,通过初始化表达式初始化一个变量
        i = 0

        条件表达式 ,条件表达式用来设置循环执行的条件
        while i < 10 :
            print(i)
            i += 1
    
    for循环
        语法:
        for 变量 in 序列 :
            代码块

        for循环的代码块会执行多次 ,序列中有几个元素就会执行几次
        没执行一次就会将序列中的一个元素赋值给变量 ,
        所以我们可以通过变量 ,来获取列表中的元素
        通过range()可以创建一个执行指定次数的for循环
        for()循环除了创建方式以外 ,其余的都和while一样 ,
        包括else、包括break continue都可以在for循环中使用
        并且for循环使用也更加简单

12break&continue
    break
    break可以用来立即退出循环语句(包括else)
    continue
    continue可以用来跳过当次循环
    break和continue都是只对离他最近的循环起作用
    pass
    pass是用来在判断或循环语句中占位的

13引入模块
    # 模块 ,通过模块可以对Python进行扩展
    # 引入一个time模块 ,来统计程序执行的时间
    语法:from time import *

14列表
    []代表列表 ,语法:my_list=[] ,列表存储的数据 ,我们称为元素
    转化为列表 ,语法:list()
    一个列表中可以存储多个元素 ,也可以在创建列表时 ,来指定列表中的元素 ,
    列表可以同时存储不同类型的元素
    列表中的对象都会按照插入的顺序存储到列表中
    第一个插入的对象保存到第一个位置 ,第二个保存到第二个位置
    我们可以通过索引(index)来获取列表中的元素
    索引是元素在列表中的位置 ,列表中的每一个元素都有一个索引
    索引是从0开始的整数 ,列表第一个位置索引为0 ,第二个位置索引为1 ,第三个位置索引为2 ,以此类推
  
    my_list = [10,20,30,40,50]
    通过索引获取列表中的元素
    语法:my_list[索引] my_list[0]
    print(my_list[4])
    如果使用的索引超过了最大的范围 ,会抛出异常
    print(my_list[5]) IndexError: list index out of range

    获取列表的长度 ,列表中元素的个数
    len()函数 ,通过该函数可以获取列表的长度
    获取到的长度的值 ,是列表的最大索引 + 1
    语法:len(my_list)

15切片
    切片指从现有列表中 ,获取一个子列表
    创建一个列表 ,一般创建列表时 ,变量的名字会使用复数
    stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']

    列表的索引可以是负数
    如果索引是负数 ,则从后向前获取元素 ,-1表示倒数第一个 ,-2表示倒数第二个 以此类推
    print(stus[-2])

    通过切片来获取指定的元素
    语法:列表[起始:结束] 
    通过切片获取元素时 ,会包括起始位置的元素 ,不会包括结束位置的元素
    做切片操作时 ,总会返回一个新的列表 ,不会影响原来的列表
    起始和结束位置的索引都可以省略不写
    如果省略结束位置 ,则会一直截取到最后
    如果省略起始位置 ,则会从第一个元素开始截取
    如果起始位置和结束位置全部省略 ,则相当于创建了一个列表的副本
    print(stus[1:])
    print(stus[:3])
    print(stus[:])
    print(stus)

    语法:列表[起始:结束:步长] 
    步长表示 ,每次获取元素的间隔 ,默认值是1
    print(stus[0:5:3])
    步长不能是0 ,但是可以是负数
    print(stus[::0]) ValueError: slice step cannot be zero
    如果是负数 ,则会从列表的后部向前边取元素
    print(stus[::-1])

16可变序列的通用操作
    + 和 *
    +可以将两个列表拼接为一个列表
    my_list = [1,2,3] + [4,5,6]

    * 可以将列表重复指定的次数
    my_list = [1,2,3] * 5

    print(my_list)

    创建一个列表
    stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精','沙和尚','沙和尚']

    in 和 not in
    in用来检查指定元素是否存在于列表中
    如果存在 ,返回True ,否则返回False
    not in用来检查指定元素是否不在列表中
    如果不在 ,返回True ,否则返回False
    print('牛魔王' not in stus)
    print('牛魔王' in stus)

    len()获取列表中的元素的个数

    min() 获取列表中的最小值
    max() 获取列表中的最大值
    arr = [10,1,2,5,100,77]
    print(min(arr) , max(arr))

    两个方法(method) ,方法和函数基本上是一样 ,只不过方法必须通过 对象.方法() 的形式调用
    xxx.print() 方法实际上就是和对象关系紧密的函数
    s.index() 获取指定元素在列表中的第一次出现时索引
    print(stus.index('沙和尚'))
    index()的第二个参数 ,表示查找的起始位置  , 第三个参数 ,表示查找的结束位置
    print(stus.index('沙和尚',3,7))
    如果要获取列表中没有的元素 ,会抛出异常
    print(stus.index('牛魔王')) ValueError: '牛魔王' is not in list
    s.count() 统计指定元素在列表中出现的次数
    print(stus.count('牛魔王'))

17修改元素
    创建一个列表
    stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']

    print("修改前:",stus)
    修改列表中的元素
    直接通过索引来修改元素
    stus[0] = 'sunwukong'
    stus[2] = '哈哈'
    通过del来删除元素
    del stus[2] # 删除索引为2的元素

    print('修改后:',stus)

    stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']

    print("修改前:",stus)

    通过切片来修改列表
    在给切片进行赋值时 ,只能使用序列
    stus[0:2] = ['牛魔王','红孩儿'] 使用新的元素替换旧元素
    stus[0:2] = ['牛魔王','红孩儿','二郎神']
    stus[0:0] = ['牛魔王'] # 向索引为0的位置插入元素
    当设置了步长时 ,序列中元素的个数必须和切片中元素的个数一致
    stus[::2] = ['牛魔王','红孩儿','二郎神']

    通过切片来删除元素
    del stus[0:2]
    del stus[::2]
    stus[1:3] = []

    print('修改后:',stus)

    以上操作 ,只适用于可变序列
    s = 'hello'
    s[1] = 'a' 不可变序列 ,无法通过索引来修改
    可以通过 list() 函数将其他的序列转换为list
    s = list(s)
    print(s)
18列表的方法
    stus = ['孙悟空','猪八戒','沙和尚','唐僧']
    print('原列表:',stus)

    append() 
    向列表的最后添加一个元素
    stus.append('唐僧')

    insert()
    向列表的指定位置插入一个元素
    参数:
    1.要插入的位置
    2.要插入的元素
    stus.insert(2,'唐僧')

    extend()
    使用新的序列来扩展当前序列
    需要一个序列作为参数 ,它会将该序列中的元素添加到当前列表中
    stus.extend(['唐僧','白骨精'])
    stus += ['唐僧','白骨精']

    clear()
    清空序列
    stus.clear()

    pop()
    根据索引删除并返回被删除的元素

    result = stus.pop(2) # 删除索引为2的元素
    result = stus.pop() # 删除最后一个
    print('result =',result)

    remove()
    删除指定值得元素 ,如果相同值得元素有多个 ,只会删除第一个
    stus.remove('猪八戒')

    reverse()
    用来反转列表
    stus.reverse()

    sort()
    用来对列表中的元素进行排序 ,默认是升序排列
    如果需要降序排列 ,则需要传递一个reverse=True作为参数
    my_list = list('asnbdnbasdabd')
    my_list = [10,1,20,3,4,5,0,-2]

    print('修改前',my_list)

    my_list.sort(reverse=True)
    print('修改后',my_list)
    # print('修改后:',stus)

19range()
    是一个函数 ,可以用来生成一个自然数的序列 ,该函数需要三个参数1.起始位置(可以省略 ,默认是0) 2.结束位置3.步长(可以省略 ,默认是1)

20元组 tuple
    元组是一个不可变的序列 ,也是一个不可变对象。
    它的操作的方式基本上和列表是一致的
    所以你在操作元组时 ,就把元组当成是一个不可变的列表就ok了
    一般当我们希望数据不改变时 ,就使用元组 ,其余情况都使用列表
    用()创建元组 ,语法:my_tuple = ()
    当元组不是空元组时 ,括号可以省略
    如果元组不是空元组 ,它里边至少要有一个,
    语法:my_tuple = 40,
    元组的解包(解构)
    解包指就是将元组当中每一个元素都赋值给一个变量
    a,b,c,d = my_tuple
    在对一个元组进行解包时 ,变量的数量必须和元组中的元素的数量一致
    也可以在变量前边添加一个* ,这样变量将会获取元组中所有剩余的元素
    不能同时出现两个或以上的*变量

21字典
    使用 {} 来创建字典 ,语法:d={}
        创建一个保护有数据的字典
    语法:
    {key:value,key:value,key:value}
    字典的值可以是任意对象
    字典的键可以是任意的不可变对象(int、str、bool、tuple ...) ,但是一般我们都会使用str
        字典的键是不能重复的 ,如果出现重复的后边的会替换到前边的
        字典的键值对可以换行 ,隔开
    d = {
    'name':'孙悟空' , 
    'age':18 , 
    'gender':'男' , 
    'name':'sunwukong'
    }

    print(d , type(d))

    需要根据键来获取值
    print(d['name'],d['age'],d['gender'])

    如果使用了字典中不存在的键 ,会报错
    print(d['hello']) KeyError: 'hello'

    使用 dict()函数来创建字典
    每一个参数都是一个键值对 ,参数名就是键 ,参数名就是值(这种方式创建的字典 ,key都是字符串),语法:d = dict(name='孙悟空',age=18,gender='男') 

    len() 获取字典中键值对的个数
    print(len(d))

    in 检查字典中是否包含指定的键
    not in 检查字典中是否不包含指定的键
    print('hello' in d)

    获取字典中的值 ,根据键来获取值
    语法:d[key]
    print(d['age'])

    n = 'name'
    print(d[n])

    通过[]来获取值时 ,如果键不存在 ,会抛出异常 KeyError
    get(key[, default]) 该方法用来根据键来获取字典中的值
    如果获取的键在字典中不存在 ,会返回None
    也可以指定一个默认值 ,来作为第二个参数 ,这样获取不到值时将会返回默认值
    print(d.get('name'))
    print(d.get('hello','默认值'))

    修改字典
    d[key] = value 如果key存在则覆盖 ,不存在则添加
    d['name'] = 'sunwukong' # 修改字典的key-value
    d['address'] = '花果山' # 向字典中添加key-value

    print(d)
    setdefault(key[, default]) 可以用来向字典中添加key-value
    如果key已经存在于字典中 ,则返回key的值 ,不会对字典做任何操作
    如果key不存在 ,则向字典中添加这个key ,并设置value
    result = d.setdefault('name','猪八戒')
    result = d.setdefault('hello','猪八戒')

    print('result =',result)
    print(d)

    update([other])
    将其他的字典中的key-value添加到当前字典中
    如果有重复的key ,则后边的会替换到当前的
    d = {'a':1,'b':2,'c':3}
    d2 = {'d':4,'e':5,'f':6, 'a':7}
    d.update(d2)

    print(d)

    popitem()
    随机删除字典中的一个键值对 ,一般都会删除最后一个键值对
    删除之后 ,它会将删除的key-value作为返回值返回
    返回的是一个元组 ,元组中有两个元素 ,第一个元素是删除的key ,第二个是删除的value
    当使用popitem()删除一个空字典时 ,会抛出异常 KeyError: 'popitem(): dictionary is empty'
    d.popitem()
    result = d.popitem()

    pop(key[, default])
    根据key删除字典中的key-value
    会将被删除的value返回！
    如果删除不存在的key ,会抛出异常
    如果指定了默认值 ,再删除不存在的key时 ,不会报错 ,而是直接返回默认值
    result = d.pop('d')
    result = d.pop('z','这是默认值')

    del d['z'] z不存在 ,报错
    result = d.popitem()
    result = d.popitem()
    result = d.popitem()
    result = d.popitem()

    clear()用来清空字典
    d.clear()

    print('result =',result)
    print(d)

    copy()
    该方法用于对字典进行浅复制
    复制以后的对象 ,和原对象是独立 ,修改一个不会影响另一个
    注意 ,浅复制会简单复制对象内部的值 ,如果值也是一个可变对象 ,这个可变对象不会被复制
    d = {'a':1,'b':2,'c':3}
    d2 = d.copy()
    d['a'] = 100

    d = {'a':{'name':'孙悟空','age':18},'b':2,'c':3}
    d2 = d.copy()
    d2['a']['name'] = '猪八戒'

    print('d = ',d , id(d))
    print('d2 = ',d2 , id(d2))

    字典的遍历
    keys() 该方法会返回字典的所有的key
    该方法会返回一个序列 ,序列中保存有字典的所有的键
    d = {'name':'孙悟空','age':18,'gender':'男'}

    通过遍历keys()来获取所有的键
    for k in d.keys() :
        print(k , d[k])

    values()
    该方法会返回一个序列 ,序列中保存有字典的左右的值
    for v in d.values():
        print(v)

    items()
    该方法会返回字典中所有的项
    它会返回一个序列 ,序列中包含有双值子序列
    双值分别是 ,字典中的key和value
    print(d.items())
    for k,v in d.items() :
        print(k , '=' , v)

22集合
    使用 {} 来创建集合
    s = {10,3,5,1,2,1,2,3,1,1,1,1} # <class 'set'>
    s = {[1,2,3],[4,6,7]} TypeError: unhashable type: 'list'
    使用 set() 函数来创建集合
    s = set() # 空集合
    可以通过set()来将序列和字典转换为集合
    s = set([1,2,3,4,5,1,1,2,3,4,5])
    s = set('hello')
    s = set({'a':1,'b':2,'c':3}) # 使用set()将字典转换为集合时 ,只会包含字典中的键

    创建集合
    s = {'a' , 'b' , 1 , 2 , 3 , 1}

    使用in和not in来检查集合中的元素
    print('c' in s)

    使用len()来获取集合中元素的数量
    print(len(s))

    add() 向集合中添加元素
    s.add(10)
    s.add(30)

    update() 将一个集合中的元素添加到当前集合中
      update()可以传递序列或字典作为参数 ,字典只会使用键
    s2 = set('hello')
    s.update(s2)
    s.update((10,20,30,40,50))
    s.update({10:'ab',20:'bc',100:'cd',1000:'ef'})

    {1, 2, 3, 100, 40, 'o', 10, 1000, 'a', 'h', 'b', 'l', 20, 50, 'e', 30}
    pop()随机删除并返回一个集合中的元素
    result = s.pop()

    remove()删除集合中的指定元素
    s.remove(100)
    s.remove(1000)

    clear()清空集合
    s.clear()

    copy()对集合进行浅复制

    print(result)
    print(s , type(s))

    集合的运算
        在对集合做运算时 ,不会影响原来的集合 ,而是返回一个运算结果
        创建两个集合
        s = {1,2,3,4,5}
        s2 = {3,4,5,6,7}

        & 交集运算
        result = s & s2 # {3, 4, 5}

        | 并集运算
        result = s | s2 # {1,2,3,4,5,6,7}

        - 差集
        result = s - s2 # {1, 2}

        ^ 异或集 获取只在一个集合中出现的元素
        result = s ^ s2 # {1, 2, 6, 7}

        <= 检查一个集合是否是另一个集合的子集
        如果a集合中的元素全部都在b集合中出现 ,那么a集合就是b集合的子集 ,b集合是a集合超集
        a = {1,2,3}
        b = {1,2,3,4,5}

        result = a <= b # True
        result = {1,2,3} <= {1,2,3} # True
        result = {1,2,3,4,5} <= {1,2,3} # False

        < 检查一个集合是否是另一个集合的真子集
        如果超集b中含有子集a中所有元素 ,并且b中还有a中没有的元素 ,则b就是a的真超集 ,a是b的真子集
        result = {1,2,3} < {1,2,3} # False
        result = {1,2,3} < {1,2,3,4,5} # True

        >= 检查一个集合是否是另一个的超集
        > 检查一个集合是否是另一个的真超集
        print('result =',result)

23函数
    函数的简介
        定义一个函数
        def fn() :
            print('这是我的第一个函数！')
            print('hello')
            print('今天天气真不错！')

        打印fn
        print(fn) <function fn at 0x03D2B618>
        print(type(fn)) <class 'function'>

        fn是函数对象  fn()调用函数
        print是函数对象 print()调用函数
        fn()

        定义一个函数 ,可以用来求任意两个数的和
        def sum() :
            a = 123
            b = 456
            print(a + b)

        sum()

        定义函数时指定形参
        def fn2(a , b) :
            # print('a =',a)
            # print('b =',b)
            print(a,"+",b,"=",a + b)

        调用函数时 ,来传递实参
        fn2(10,20)
        fn2(123,456)
    
    函数的参数
        求任意三个数的乘积
        def mul(a,b,c):
            print(a*b*c)

        根据不同的用户名显示不同的欢迎信息   
        def welcome(username):
            print('欢迎',username,'光临')

        mul(1,2,3)   
        welcome('孙悟空') 

        定义一个函数
        定义形参时 ,可以为形参指定默认值
        指定了默认值以后 ,如果用户传递了参数则默认值没有任何作用
          如果用户没有传递 ,则默认值就会生效
        def fn(a = 5 , b = 10 , c = 20):
            print('a =',a)
            print('b =',b)
            print('c =',c)

        fn(1 , 2 , 3)
        fn(1 , 2)
        fn()

        实参的传递方式
        位置参数
        位置参数就是将对应位置的实参复制给对应位置的形参
        第一个实参赋值给第一个形参 ,第二个实参赋值给第二个形参 。。。
        fn(1 , 2 , 3)

        关键字参数
        关键字参数 ,可以不按照形参定义的顺序去传递 ,而直接根据参数名去传递参数
        fn(b=1 , c=2 , a=3)
        print('hello' , end='')
        位置参数和关键字参数可以混合使用
        混合使用关键字和位置参数时 ,必须将位置参数写到前面
        fn(1,c=30)

        def fn2(a):
            print('a =',a)

        函数在调用时 ,解析器不会检查实参的类型
        实参可以传递任意类型的对象
        b = 123
        b = True
        b = 'hello'
        b = None
        b = [1,2,3]

        fn2(b)    
        fn2(fn)

        def fn3(a , b):
            print(a+b)

        fn3(123,"456")

        def fn4(a):
            在函数中对形参进行重新赋值 ,不会影响其他的变量
            a = 20
            a是一个列表 ,尝试修改列表中的元素
            如果形参执行的是一个对象 ,当我们通过形参去修改对象时
              会影响到所有指向该对象的变量
            a[0] = 30
            print('a =',a,id(a))

        c = 10   
        c = [1,2,3] 

        fn4(c)
        fn4(c.copy())
        fn4(c[:])

        print('c =',c,id(c))
    
    不定长的参数
        定义一个函数 ,可以求任意个数字的和
        def sum(*nums):
            定义一个变量 ,来保存结果
            result = 0
            遍历元组 ,并将元组中的数进行累加
            for n in nums :
                result += n
            print(result)


        sum(123,456,789,10,20,30,40)

        在定义函数时 ,可以在形参前边加上一个* ,这样这个形参将会获取到所有的实参
        它将会将所有的实参保存到一个元组中
        a,b,*c = (1,2,3,4,5,6)

        *a会接受所有的位置实参 ,并且会将这些实参统一保存到一个元组中(装包)
        def fn(*a):
            print("a =",a,type(a))

        fn(1,2,3,4,5)
        带星号的形参只能有一个
        带星号的参数 ,可以和其他参数配合使用
        第一个参数给a ,第二个参数给b ,剩下的都保存到c的元组中
        def fn2(a,b,*c):
            print('a =',a)
            print('b =',b)
            print('c =',c)

        可变参数不是必须写在最后 ,但是注意 ,带*的参数后的所有参数 ,必须以关键字参数的形式传递
        第一个参数给a ,剩下的位置参数给b的元组 ,c必须使用关键字参数
        def fn2(a,*b,c):
            print('a =',a)
            print('b =',b)
            print('c =',c)

        所有的位置参数都给a ,b和c必须使用关键字参数
        def fn2(*a,b,c):
            print('a =',a)
            print('b =',b)
            print('c =',c)

        如果在形参的开头直接写一个*,则要求我们的所有的参数必须以关键字参数的形式传递
        def fn2(*,a,b,c):
            print('a =',a)
            print('b =',b)
            print('c =',c)
        fn2(a=3,b=4,c=5)

        *形参只能接收位置参数 ,而不能接收关键字参数
        def fn3(*a) :
            print('a =',a)

        **形参可以接收其他的关键字参数 ,它会将这些参数统一保存到一个字典中
          字典的key就是参数的名字 ,字典的value就是参数的值
        **形参只能有一个 ,并且必须写在所有参数的最后
        def fn3(b,c,**a) :
            print('a =',a,type(a))
            print('b =',b)
            print('c =',c)

        fn3(b=1,d=2,c=3,e=10,f=20)

        参数的解包(拆包)
        def fn4(a,b,c):
            print('a =',a)
            print('b =',b)
            print('c =',c)

        创建一个元组
        t = (10,20,30)

        传递实参时 ,也可以在序列类型的参数前添加星号 ,这样他会自动将序列中的元素依次作为参数传递
        这里要求序列中元素的个数必须和形参的个数的一致
        fn4(*t)    

        创建一个字典
        d = {'a':100,'b':200,'c':300}
        通过 **来对一个字典进行解包操作
        fn4(**d)

24返回值
    返回值就是函数执行以后返回的结果
    可以通过 return 来指定函数的返回值
    可以之间使用函数的返回值 ,也可以通过一个变量来接收函数的返回值

    def sum(*nums):
        定义一个变量 ,来保存结果
        result = 0
        遍历元组 ,并将元组中的数进行累加
        for n in nums :
            result += n
        print(result)

    sum(123,456,789)
    

    return 后边跟什么值 ,函数就会返回什么值
    return 后边可以跟任意的对象 ,返回值甚至可以是一个函数
    def fn():
        # return 'Hello'
        # return [1,2,3]
        # return {'k':'v'}
        def fn2() :
            print('hello')

        return fn2 # 返回值也可以是一个函数

    r = fn() # 这个函数的执行结果就是它的返回值
    # r()
    # print(fn())
    # print(r)

    # 如果仅仅写一个return 或者 不写return ,则相当于return None 
    def fn2() :
        a = 10
        return 

    # 在函数中 ,return后的代码都不会执行 ,return 一旦执行函数自动结束
    def fn3():
        print('hello')
        return
        print('abc')

    # r = fn3()
    # print(r)

    def fn4() :
        for i in range(5):
            if i == 3 :
                # break 用来退出当前循环
                # continue 用来跳过当次循环
                return # return 用来结束函数
            print(i)
        print('循环执行完毕！')

    # fn4()

    def sum(*nums):
        # 定义一个变量 ,来保存结果
        result = 0
        # 遍历元组 ,并将元组中的数进行累加
        for n in nums :
            result += n
        return result

    r = sum(123,456,789)

    # print(r + 778)

    def fn5():
        return 10

    # fn5 和 fn5()的区别
    print(fn5) # fn5是函数对象 ,打印fn5实际是在打印函数对象 <function fn5 at 0x05771BB8>
    print(fn5()) # fn5()是在调用函数 ,打印fn5()实际上是在打印fn5()函数的返回值 10

25文档字符串
    help()是Python中的内置函数
    通过help()函数可以查询python中的函数的用法
    语法:help(函数对象)
    help(print) # 获取print()函数的使用说明

    文档字符串(doc str)
    在定义函数时 ,可以在函数内部编写文档字符串 ,文档字符串就是函数的说明
    当我们编写了文档字符串时 ,就可以通过help()函数来查看函数的说明
    文档字符串非常简单 ,其实直接在函数的第一行写一个字符串就是文档字符串

26作用域(scope)& 命名空间(namespace)
    作用域指的是变量生效的区域
        b = 20 # 全局变量

        def fn():
            a = 10 # a定义在了函数内部 ,所以他的作用域就是函数内部 ,函数外部无法访问
            print('函数内部:','a =',a)
            print('函数内部:','b =',b)

        fn()    
        

        print('函数外部:','a =',a)
        print('函数外部:','b =',b)

        在Python中一共有两种作用域
        全局作用域
        - 全局作用域在程序执行时创建 ,在程序执行结束时销毁
        - 所有函数以外的区域都是全局作用域
        - 在全局作用域中定义的变量 ,都属于全局变量 ,全局变量可以在程序的任意位置被访问
        
        函数作用域
        - 函数作用域在函数调用时创建 ,在调用结束时销毁
        - 函数每调用一次就会产生一个新的函数作用域
        - 在函数作用域中定义的变量 ,都是局部变量 ,它只能在函数内部被访问
        
        变量的查找
        - 当我们使用变量时 ,会优先在当前作用域中寻找该变量 ,如果有则使用 ,
            如果没有则继续去上一级作用域中寻找 ,如果有则使用 ,
            如果依然没有则继续去上一级作用域中寻找 ,以此类推
            直到找到全局作用域 ,依然没有找到 ,则会抛出异常
                NameError: name 'a' is not defined

        def fn2():
            def fn3():
                print('fn3中:','a =',a)
            fn3()

        fn2()    

        a = 20

        def fn3():
            # a = 10 # 在函数中为变量赋值时 ,默认都是为局部变量赋值
            # 如果希望在函数内部修改全局变量 ,则需要使用global关键字 ,来声明变量
            global a # 声明在函数内部的使用a是全局变量 ,此时再去修改a时 ,就是在修改全局的a
            a = 10 # 修改全局变量
            print('函数内部:','a =',a)

        fn3()
        print('函数外部:','a =',a)


    命名空间(namespace)
        命名空间指的是变量存储的位置 ,每一个变量都需要存储到指定的命名空间当中
        每一个作用域都会有一个它对应的命名空间
        全局命名空间 ,用来保存全局变量。函数命名空间用来保存函数中的变量
        命名空间实际上就是一个字典 ,是一个专门用来存储变量的字典

        locals()用来获取当前作用域的命名空间
        如果在全局作用域中调用locals()则获取全局命名空间 ,如果在函数作用域中调用locals()则获取函数命名空间
        返回的是一个字典
        scope = locals() # 当前命名空间
        print(type(scope))
        print(a)
        print(scope['a'])
        向scope中添加一个key-value
        scope['c'] = 1000 # 向字典中添加key-value就相当于在全局中创建了一个变量(一般不建议这么做)

        def fn4():
            a = 10
            scope = locals() # 在函数内部调用locals()会获取到函数的命名空间
            scope['b'] = 20 # 可以通过scope来操作函数的命名空间 ,但是也是不建议这么做

            globals() 函数可以用来在任意位置获取全局命名空间
            global_scope = globals()
            # print(global_scope['a'])
            global_scope['a'] = 30
        fn4()    

27递归
    递归是解决问题的一种方式 ,它和循环很像
    它的整体思想是 ,将一个大问题分解为一个个的小问题 ,直到问题无法分解时 ,再去解决问题
    递归式函数的两个要件
    1.基线条件
        - 问题可以被分解为的最小问题 ,当满足基线条件时 ,递归就不在执行了
    2.递归条件
        - 将问题继续分解的条件
    递归和循环类似 ,基本是可以互相代替的 ,
    循环编写起来比较容易 ,阅读起来稍难
    递归编写起来难 ,但是方便阅读
    10! = 10 * 9!
    9! = 9 * 8!
    8! = 8 * 7!
    ...
    1! = 1

    def factorial(n):
    '''
        该函数用来求任意数的阶乘

        参数:
            n 要求阶乘的数字
    '''
    # 基线条件 判断n是否为1 ,如果为1则此时不能再继续递归
    if n == 1 :
        # 1的阶乘就是1 ,直接返回1
        return 1

    # 递归条件    
    return n * factorial(n-1)

28高阶函数
    接收函数作为参数 ,或者将函数作为返回值的函数是高阶函数
    当我们使用一个函数作为参数时 ,实际上是将指定的代码传递进了目标函数

    创建一个列表
    l = [1,2,3,4,5,6,7,8,9,10]

    定义一个函数
      可以将指定列表中的所有的偶数 ,保存到一个新的列表中返回

    定义一个函数 ,用来检查一个任意的数字是否是偶数
    def fn2(i) :
        if i % 2 == 0 :
            return True

        return False    

    这个函数用来检查指定的数字是否大于5
    def fn3(i):
        if i > 5 :
            return True    
        return False

    def fn(func , lst) :

        '''
            fn()函数可以将指定列表中的所有偶数获取出来 ,并保存到一个新列表中返回

            参数:
                lst:要进行筛选的列表
        '''
        # 创建一个新列表
        new_list = []

        # 对列表进行筛选
        for n in lst :
            # 判断n的奇偶
            if func(n) :
                new_list.append(n)
            # if n > 5 :
            #     new_list.append(n)

                


        # 返回新列表
        return new_list

    # def fn4(i):
    #     if i % 3 == 0:
    #         return True    
    #     return False

    def fn4(i):
        return i % 3 == 0
            
    # print(fn(fn4 , l))

    # filter()
    # filter()可以从序列中过滤出符合条件的元素 ,保存到一个新的序列中
    # 参数:
    #  1.函数 ,根据该函数来过滤序列(可迭代的结构)
    #  2.需要过滤的序列(可迭代的结构)
    # 返回值:
    #   过滤后的新序列(可迭代的结构)

    # fn4是作为参数传递进filter()函数中
    #   而fn4实际上只有一个作用 ,就是作为filter()的参数
    #   filter()调用完毕以后 ,fn4就已经没用
    # 匿名函数 lambda 函数表达式 (语法糖)
    #   lambda函数表达式专门用来创建一些简单的函数 ,他是函数创建的又一种方式
    #   语法:lambda 参数列表 : 返回值
    #   匿名函数一般都是作为参数使用 ,其他地方一般不会使用

    def fn5(a , b):
        return a + b

    # (lambda a,b : a + b)(10,20)
    # 也可以将匿名函数赋值给一个变量 ,一般不会这么做
    fn6 = lambda a,b : a + b
    # print(fn6(10,30))


    r = filter(lambda i : i > 5 , l)
    # print(list(r))

    # map()
    # map()函数可以对可跌倒对象中的所有元素做指定的操作 ,然后将其添加到一个新的对象中返回
    l = [1,2,3,4,5,6,7,8,9,10]

    r = map(lambda i : i ** 2 , l)

    # print(list(r))

    # sort()
    # 该方法用来对列表中的元素进行排序
    # sort()方法默认是直接比较列表中的元素的大小
    # 在sort()可以接收一个关键字参数  , key
    #   key需要一个函数作为参数 ,当设置了函数作为参数
    #   每次都会以列表中的一个元素作为参数来调用函数 ,并且使用函数的返回值来比较元素的大小
    l = ['bb','aaaa','c','ddddddddd','fff']
    # l.sort(key=len)

    l = [2,5,'1',3,'6','4']
    l.sort(key=int)
    # print(l)

    # sorted()
    # 这个函数和sort()的用法基本一致 ,但是sorted()可以对任意的序列进行排序
    #   并且使用sorted()排序不会影响原来的对象 ,而是返回一个新对象

    l = [2,5,'1',3,'6','4']
    # l = "123765816742634781"

    print('排序前:',l)
    print(sorted(l,key=int))
    print('排序后:',l)

29闭包
    将函数作为返回值返回 ,也是一种高阶函数
    这种高阶函数我们也称为叫做闭包 ,通过闭包可以创建一些只有当前函数能访问的变量
      可以将一些私有的数据藏到的闭包中

    def fn():

        a = 10

        # 函数内部再定义一个函数
        def inner():
            print('我是fn2' , a)

        # 将内部函数 inner作为返回值返回   
        return inner

    # r是一个函数 ,是调用fn()后返回的函数
    # 这个函数实在fn()内部定义 ,并不是全局函数
    # 所以这个函数总是能访问到fn()函数内的变量
    r = fn()    

    # r()

    # 求多个数的平均值
    # nums = [50,30,20,10,77]

    # sum()用来求一个列表中所有元素的和
    # print(sum(nums)/len(nums))

    形成闭包的要件
      ① 函数嵌套
      ② 将内部函数作为返回值返回
      ③ 内部函数必须要使用到外部函数的变量
    def make_averager():
        # 创建一个列表 ,用来保存数值
        nums = []

        # 创建一个函数 ,用来计算平均值
        def averager(n) :
            # 将n添加到列表中
            nums.append(n)
            # 求平均值
            return sum(nums)/len(nums)

        return averager

    averager = make_averager()

30装饰器
    f = begin_end(fn)
    f2 = begin_end(add)
    f3 = begin_end(mul)

    r = f()
    r = f2(123,456)
    r = f3(123,456)
    print(r)
    向begin_end()这种函数我们就称它为装饰器
      通过装饰器 ,可以在不修改原来函数的情况下来对函数进行扩展
      在开发中 ,我们都是通过装饰器来扩展函数的功能的
    在定义函数时 ,可以通过@装饰器 ,来使用指定的装饰器 ,来装饰当前的函数
      可以同时为一个函数指定多个装饰器 ,这样函数将会安装从内向外的顺序被装饰 

    def fn3(old):
        '''
            用来对其他函数进行扩展 ,使其他函数可以在执行前打印开始执行 ,执行后打印执行结束

            参数:
                old 要扩展的函数对象
        '''
        # 创建一个新函数
        def new_function(*args , **kwargs):
            print('fn3装饰~开始执行~~~~')
            # 调用被扩展的函数
            result = old(*args , **kwargs)
            print('fn3装饰~执行结束~~~~')
            # 返回函数的执行结果
            return result

        # 返回新函数        
        return new_function

    @fn3
    @begin_end
    def say_hello():
        print('大家好~~~')

    say_hello()

31类
    类的简介
        使用MyClass创建一个对象
        使用类来创建对象 ,就像调用一个函数一样
        语法:mc = MyClass() # mc就是通过MyClass创建的对象 ,mc是MyClass的实例
        mc mc_2 mc_3 mc_4 都是MyClass的实例 ,他们都是一类对象
        isinstance()用来检查一个对象是否是一个类的实例
        result = isinstance(mc_2,MyClass)
        result = isinstance(mc_2,str)
        现在我们通过MyClass这个类创建的对象都是一个空对象
        也就是对象中实际上什么都没有 ,就相当于是一个空的盒子
        可以向对象中添加变量 ,对象中的变量称为属性
        语法:对象.属性名 = 属性值

    定义类
        class Person :
        在类的代码块中 ,我们可以定义变量和函数
        在类中我们所定义的变量 ,将会成为所有的实例的公共属性
        所有实例都可以访问这些变量
        name = 'swk' # 公共属性 ,所有实例都可以访问

        在类中也可以定义函数 ,类中的定义的函数 ,我们称为方法
        这些方法可以通过该类的所有实例来访问

        def say_hello(self) :
        方法每次被调用时 ,解析器都会自动传递第一个实参
        第一个参数 ,就是调用方法的对象本身 ,
          如果是p1调的 ,则第一个参数就是p1对象
          如果是p2调的 ,则第一个参数就是p2对象
        一般我们都会将这个参数命名为self

        say_hello()这个方法 ,可以显示如下格式的数据:
          你好！我是 xxx
          在方法中不能直接访问类中的属性
        print('你好！我是 %s' %self.name)

        # 创建Person的实例
        p1 = Person()
        p2 = Person()

        print(p2.name)

        调用方法 ,对象.方法名()
        方法调用和函数调用的区别
        如果是函数调用 ,则调用时传几个参数 ,就会有几个实参
        但是如果是方法调用 ,默认传递一个参数 ,所以方法中至少要定义一个形参


        修改p1的name属性
        p1.name = '猪八戒'
        p2.name = '沙和尚'

        p1.say_hello() # '你好！我是 猪八戒'
        p2.say_hello() # '你好！我是 沙和尚'

        # del p2.name # 删除p2的name属性

    对象的初始化
        class Person :
        在类中可以定义一些特殊方法(魔术方法)
        特殊方法都是以__开头 ,__结尾的方法
        特殊方法不需要我们自己调用 ,不要尝试去调用特殊方法
        特殊方法将会在特殊的时刻自动调用
        学习特殊方法:
          1.特殊方法什么时候调用
          2.特殊方法有什么作用
        创建对象的流程
        p1 = Person()的运行流程
          1.创建一个变量
          2.在内存中创建一个新对象
          3.__init__(self)方法执行
          4.将对象的id赋值给变量

        init会在对象创建以后离开执行
        init可以用来向新创建的对象中初始化属性
        调用类创建对象时 ,类后边的所有参数都会依次传递到init()中
        def __init__(self,name):
            # print(self)
            # 通过self向新建的对象中初始化属性
            self.name = name

        def say_hello(self):
            print('大家好 ,我是%s'%self.name)


        目前来讲 ,对于Person类来说name是必须的 ,并且每一个对象中的name属性基本上都是不同
        而我们现在是将name属性在定义为对象以后 ,手动添加到对象中 ,这种方式很容易出现错误
        我们希望 ,在创建对象时 ,必须设置name属性 ,如果不设置对象将无法创建
          并且属性的创建应该是自动完成的 ,而不是在创建对象以后手动完成
        p1 = Person()
        # 手动向对象添加name属性
        p1.name = '孙悟空'

        p2 = Person()
        p2.name = '猪八戒'

        p3 = Person()
        p3.name = '沙和尚'

        p3.say_hello()

        p1 = Person('孙悟空')
        p2 = Person('猪八戒')
        p3 = Person('沙和尚')
        p4 = Person('唐僧')
        p1.__init__() 不要这么做

        print(p1.name)
        print(p2.name)
        print(p3.name)
        print(p4.name)

        p4.say_hello()

32封装
        封装是面向对象的三大特性之一
        封装指的是隐藏对象中一些不希望被外部所访问到的属性或方法
        如何隐藏一个对象中的属性？
        - 将对象的属性名 ,修改为一个外部不知道的名字
        如何获取(修改)对象中的属性？
        - 需要提供一个getter和setter方法使外部可以访问到属性
        - getter 获取对象中的指定属性(get_属性名)
        - setter 用来设置对象的指定属性(set_属性名)
        使用封装 ,确实增加了类的定义的复杂程度 ,但是它也确保了数据的安全性
        1.隐藏了属性名 ,使调用者无法随意的修改对象中的属性
        2.增加了getter和setter方法 ,很好的控制的属性是否是只读的
        如果希望属性是只读的 ,则可以直接去掉setter方法
        如果希望属性不能被外部访问 ,则可以直接去掉getter方法
        3.使用setter方法设置属性 ,可以增加数据的验证 ,确保数据的值是正确的
        4.使用getter方法获取属性 ,使用setter方法设置属性
        可以在读取属性和修改属性的同时做一些其他的处理
        5.使用getter方法可以表示一些计算的属性
    举例
        lass Dog:
        '''
            表示狗的类
        '''
        def __init__(self , name , age):
            self.hidden_name = name
            self.hidden_age = age

        def say_hello(self):
            print('大家好 ,我是 %s'%self.hidden_name) 

        def get_name(self):
            '''
                get_name()用来获取对象的name属性
            '''    
            # print('用户读取了属性')
            return self.hidden_name

        def set_name(self , name):
            # print('用户修改了属性')
            self.hidden_name = name

        def get_age(self):
            return self.hidden_age

        def set_age(self , age):
            if age > 0 :
                self.hidden_age = age    

            d = Dog('旺财',8)

            # d.say_hello()

            # 调用setter来修改name属性 
            d.set_name('小黑')
            d.set_age(-10)

            # d.say_hello()
            print(d.get_age())

            class Rectangle:
        
    表示矩形的类
         def __init__(self,width,height):
            self.hidden_width = width
            self.hidden_height = height

        def get_width(self):
            return self.hidden_width

        def get_height(self):
            return self.hidden_height   

        def set_width(self , width):
            self.hidden_width = width 

        def set_height(self , height):
            self.hidden_height = height 

        def get_area(self):
            return self.hidden_width * self.hidden_height        

        r = Rectangle(5,2)  
        r.set_width(10)
        r.set_height(20)

        print(r.get_area())     
        
        
        可以为对象的属性使用双下划线开头 ,__xxx
        双下划线开头的属性 ,是对象的隐藏属性 ,隐藏属性只能在类的内部访问 ,无法通过对象访问
        其实隐藏属性只不过是Python自动为属性改了一个名字
        实际上是将名字修改为了 ,_类名__属性名 比如 __name -> _Person__name
        class Person:
            def __init__(self,name):
                self.__name = name

            def get_name(self):
                return self.__name

            def set_name(self , name):
                self.__name = name        

        p = Person('孙悟空')

        print(p.__name) __开头的属性是隐藏属性 ,无法通过对象访问
        p.__name = '猪八戒'
        print(p._Person__name)
        p._Person__name = '猪八戒'

        print(p.get_name())

        使用__开头的属性 ,实际上依然可以在外部访问 ,所以这种方式我们一般不用
        一般我们会将一些私有属性(不希望被外部访问的属性)以_开头
        一般情况下 ,使用_开头的属性都是私有属性 ,没有特殊需要不要修改私有属性
        class Person:
            def __init__(self,name):
                self._name = name

            def get_name(self):
                return self._name

            def set_name(self , name):
                self._name = name   

        p = Person('孙悟空')

        print(p._name)

    装饰器和封装

        class Person:
        def __init__(self,name,age):
            self._name = name
            self._age = age

        property装饰器 ,用来将一个get方法 ,转换为对象的属性
        添加为property装饰器以后 ,我们就可以像调用属性一样使用get方法
        使用property装饰的方法 ,必须和属性名是一样的
        @property    
        def name(self):
            print('get方法执行了~~~')
            return self._name

        # setter方法的装饰器:@属性名.setter
        @name.setter    
        def name(self , name):
            print('setter方法调用了')
            self._name = name        

        @property
        def age(self):
            return self._age

        @age.setter    
        def age(self , age):
            self._age = age   

        p = Person('猪八戒',18)

        p.name = '孙悟空'
        p.age = 28

        print(p.name,p.age)

33继承
    # 定义一个类 Animal(动物)
    #   这个类中需要两个方法:run() sleep() 
    class Animal:
        def run(self):
            print('动物会跑~~~')

        def sleep(self):
            print('动物睡觉~~~')

        def bark(self):
            print('动物嚎叫~~~')   

    定义一个类 Dog(狗)
      这个类中需要三个方法:run() sleep() bark()
    class Dog:
        def run(self):
            print('狗会跑~~~')

        def sleep(self):
            print('狗睡觉~~~')

        def bark(self):
            print('汪汪汪~~~') 

    有一个类 ,能够实现我们需要的大部分功能 ,但是不能实现全部功能
    如何能让这个类来实现全部的功能呢？
      ① 直接修改这个类 ,在这个类中添加我们需要的功能
          - 修改起来会比较麻烦 ,并且会违反OCP原则
      ② 直接创建一个新的类
          - 创建一个新的类比较麻烦 ,并且需要大量的进行复制粘贴 ,会出现大量的重复性代码
      ③ 直接从Animal类中来继承它的属性和方法
          - 继承是面向对象三大特性之一
          - 通过继承我们可以使一个类获取到其他类中的属性和方法
          - 在定义类时 ,可以在类名后的括号中指定当前类的父类(超类、基类、super)
              子类(衍生类)可以直接继承父类中的所有的属性和方法
              
     通过继承可以直接让子类获取到父类的方法或属性 ,避免编写重复性的代码 ,并且也符合OCP原则
      所以我们经常需要通过继承来对一个类进行扩展

    class Dog(Animal):
        def bark(self):
            print('汪汪汪~~~') 

        def run(self):
            print('狗跑~~~~')    

    class Hashiqi(Dog):
        def fan_sha(self):
            print('我是一只傻傻的哈士奇')        

    d = Dog()
    h = Hashiqi()

    d.run()
    d.sleep()
    d.bark()

    r = isinstance(d , Dog)
    r = isinstance(d , Animal)
    print(r)

    在创建类时 ,如果省略了父类 ,则默认父类为object
      object是所有类的父类 ,所有类都继承自object
    class Person(object):
        pass

    issubclass() 检查一个类是否是另一个类的子类
    print(issubclass(Animal , Dog))
    print(issubclass(Animal , object))
    print(issubclass(Person , object))

    isinstance()用来检查一个对象是否是一个类的实例
      如果这个类是这个对象的父类 ,也会返回True
      所有的对象都是object的实例
    print(isinstance(print , object))

    父类中的所有方法都会被子类继承 ,包括特殊方法 ,也可以重写特殊方法
    class Dog(Animal):

        def __init__(self,name,age):
            # 希望可以直接调用父类的__init__来初始化父类中定义的属性
            # super() 可以用来获取当前类的父类 ,
            #   并且通过super()返回对象调用父类方法时 ,不需要传递self
            super().__init__(name)
            self._age = age

        def bark(self):
            print('汪汪汪~~~') 

        def run(self):
            print('狗跑~~~~')   

        @property
        def age(self):
            return self._age

        @age.setter    
        def age(self,age):
            self._age = name        

        d = Dog('旺财',18) 

    print(d.name)       
    print(d.age)       


    重写
        定义一个类 Animal(动物)
          这个类中需要两个方法:run() sleep() 
        class Animal:
        def run(self):
            print('动物会跑~~~')

        def sleep(self):
            print('动物睡觉~~~')


        class Dog(Animal):
        def bark(self):
            print('汪汪汪~~~') 

        def run(self):
            print('狗跑~~~~')    


        如果在子类中如果有和父类同名的方法 ,则通过子类实例去调用方法时 ,
          会调用子类的方法而不是父类的方法 ,这个特点我们成为叫做方法的重写(覆盖 ,override)
        创建Dog类的实例
        d = Dog()

        d.run()

        当我们调用一个对象的方法时 ,
          会优先去当前对象中寻找是否具有该方法 ,如果有则直接调用
          如果没有 ,则去当前对象的父类中寻找 ,如果父类中有则直接调用父类中的方法 ,
          如果没有 ,则去父类的父类中寻找 ,以此类推 ,直到找到object ,如果依然没有找到 ,则报错
        class A(object):
        def test(self):
            print('AAA')

        class B(A):
        def test(self):
            print('BBB')

        class C(B):
        def test(self):
            print('CCC')   

        # 创建一个c的实例
        c = C()
        c.test()

    多重继承
    class A(object):
    def test(self):
        print('AAA')

    class B(object):
        def test(self):
            print('B中的test()方法~~')

        def test2(self):
            print('BBB') 

    在Python中是支持多重继承的 ,也就是我们可以为一个类同时指定多个父类
      可以在类名的()后边添加多个类 ,来实现多重继承
      多重继承 ,会使子类同时拥有多个父类 ,并且会获取到所有父类中的方法
    在开发中没有特殊的情况 ,应该尽量避免使用多重继承 ,因为多重继承会让我们的代码过于复杂
    如果多个父类中有同名的方法 ,则会现在第一个父类中寻找 ,然后找第二个 ,然后找第三个。。。
      前边父类的方法会覆盖后边父类的方法
    class C(A,B):
        pass

    类名.__bases__ 这个属性可以用来获取当前类的所有父类    
    print(C.__bases__) (<class '__main__.B'>,)
    print(B.__bases__) (<class 'object'>,)

    print(C.__bases__) # (<class '__main__.A'>, <class '__main__.B'>)

    c = C()

    c.test()

34多态
    多态是面向对象的三大特征之一
    多态从字面上理解是多种形态
    狗(狼狗、藏獒、哈士奇、古牧 。。。)
    一个对象可以以不同的形态去呈现

    定义两个类
    class A:
        def __init__(self,name):
            self._name = name

        @property
        def name(self):
            return self._name
            
        @name.setter
        def name(self,name):
            self._name = name   

    class B:
        def __init__(self,name):
            self._name = name

        def __len__(self):
            return 10

        @property
        def name(self):
            return self._name
            
        @name.setter
        def name(self,name):
            self._name = name   

    class C:
        pass


    a = A('孙悟空')
    b = B('猪八戒')
    c = C()

    定义一个函数
    对于say_hello()这个函数来说 ,只要对象中含有name属性 ,它就可以作为参数传递
    这个函数并不会考虑对象的类型 ,只要有name属性即可
    def say_hello(obj):
        print('你好 %s'%obj.name)

    在say_hello_2中我们做了一个类型检查 ,也就是只有obj是A类型的对象时 ,才可以正常使用 ,
    其他类型的对象都无法使用该函数 ,这个函数就违反了多态
    违反了多态的函数 ,只适用于一种类型的对象 ,无法处理其他类型对象 ,这样导致函数的适应性非常的差
    注意 ,向isinstance()这种函数 ,在开发中一般是不会使用的！
    def say_hello_2(obj):
        # 做类型检查
        if isinstance(obj , A):
            print('你好 %s'%obj.name)    
    say_hello(b)    
    say_hello_2(b)

    鸭子类型
    如果一个东西 ,走路像鸭子 ,叫声像鸭子 ,那么它就是鸭子

    len()
    之所以一个对象能通过len()来获取长度 ,是因为对象中具有一个特殊方法__len__
    换句话说 ,只要对象中具有__len__特殊方法 ,就可以通过len()来获取它的长度
    l = [1,2,3]
    s = 'hello'

    # print(len(l))
    # print(len(s))
    print(len(b))
    print(len(c))

    面向对象的三大特征:
    封装
        - 确保对象中的数据安全
    继承
        - 保证了对象的可扩展性
    多态
        - 保证了程序的灵活性

35类的属性和方法
    class A(object):

    类属性
    实例属性
    类方法
    实例方法
    静态方法

    类属性 ,直接在类中定义的属性是类属性
      类属性可以通过类或类的实例访问到
      但是类属性只能通过类对象来修改 ,无法通过实例对象修改
    count = 0

    def __init__(self):
        # 实例属性 ,通过实例对象添加的属性属于实例属性
        #   实例属性只能通过实例对象来访问和修改 ,类对象无法访问修改
        self.name = '孙悟空'

    实例方法
      在类中定义 ,以self为第一个参数的方法都是实例方法
      实例方法在调用时 ,Python会将调用对象作为self传入  
      实例方法可以通过实例和类去调用
          当通过实例调用时 ,会自动将当前调用对象作为self传入
          当通过类调用时 ,不会自动传递self ,此时我们必须手动传递self
    def test(self):
        print('这是test方法~~~ ' , self)    

    类方法    
    在类内部使用 @classmethod 来修饰的方法属于类方法
    类方法的第一个参数是cls ,也会被自动传递 ,cls就是当前的类对象
      类方法和实例方法的区别 ,实例方法的第一个参数是self ,而类方法的第一个参数是cls
      类方法可以通过类去调用 ,也可以通过实例调用 ,没有区别
    @classmethod
    def test_2(cls):
        print('这是test_2方法 ,他是一个类方法~~~ ',cls)
        print(cls.count)

    静态方法
    在类中使用 @staticmethod 来修饰的方法属于静态方法  
    静态方法不需要指定任何的默认参数 ,静态方法可以通过类和实例去调用  
    静态方法 ,基本上是一个和当前类无关的方法 ,它只是一个保存到当前类中的函数
    静态方法一般都是一些工具方法 ,和当前类无关
    @staticmethod
    def test_3():
        print('test_3执行了~~~')


    a = A()
    实例属性 ,通过实例对象添加的属性属于实例属性
    a.count = 10
    A.count = 100
    print('A ,',A.count) 
    print('a ,',a.count) 
    print('A ,',A.name) 
    print('a ,',a.name)   

    a.test() 等价于 A.test(a)

    A.test_2() 等价于 a.test_2()

    A.test_3()
    a.test_3()
36垃圾回收
    就像我们生活中会产生垃圾一样 ,程序在运行过程当中也会产生垃圾
    程序运行过程中产生的垃圾会影响到程序的运行的运行性能 ,所以这些垃圾必须被及时清理
    没用的东西就是垃圾
    在程序中没有被引用的对象就是垃圾 ,这种垃圾对象过多以后会影响到程序的运行的性能
    所以我们必须进行及时的垃圾回收 ,所谓的垃圾回收就是讲垃圾对象从内存中删除
    在Python中有自动的垃圾回收机制 ,它会自动将这些没有被引用的对象删除 ,
    所以我们不用手动处理垃圾回收

    class A:
        def __init__(self):
            self.name = 'A类'

        # del是一个特殊方法 ,它会在对象被垃圾回收前调用
        def __del__(self):
            print('A()对象被删除了~~~',self)

    a = A()
    b = a # 又使用一个变量b ,来引用a对应的对象

    print(a.name)

    # a = None # 将a设置为了None ,此时没有任何的变量对A()对象进行引用 ,它就是变成了垃圾
    # b = None
    # del a
    # del b
    input('回车键退出...')


37特殊方法(魔术方法)
    特殊方法都是使用__开头和结尾的
    特殊方法一般不需要我们手动调用 ,需要在一些特殊情况下自动执行

    # 定义一个Person类
    class Person(object):
        """人类"""
        def __init__(self, name , age):
            self.name = name
            self.age = age

        # __str__()这个特殊方法会在尝试将对象转换为字符串的时候调用
        # 它的作用可以用来指定对象转换为字符串的结果  (print函数)  
        def __str__(self):
            return 'Person [name=%s , age=%d]'%(self.name,self.age)        

        # __repr__()这个特殊方法会在对当前对象使用repr()函数时调用
        # 它的作用是指定对象在 ‘交互模式’中直接输出的效果    
        def __repr__(self):
            return 'Hello'        

        # object.__add__(self, other)
        # object.__sub__(self, other)
        # object.__mul__(self, other)
        # object.__matmul__(self, other)
        # object.__truediv__(self, other)
        # object.__floordiv__(self, other)
        # object.__mod__(self, other)
        # object.__divmod__(self, other)
        # object.__pow__(self, other[, modulo])
        # object.__lshift__(self, other)
        # object.__rshift__(self, other)
        # object.__and__(self, other)
        # object.__xor__(self, other)
        # object.__or__(self, other)

        # object.__lt__(self, other) 小于 <
        # object.__le__(self, other) 小于等于 <=
        # object.__eq__(self, other) 等于 ==
        # object.__ne__(self, other) 不等于 !=
        # object.__gt__(self, other) 大于 >
        # object.__ge__(self, other) 大于等于 >= 
        
        # __len__()获取对象的长度

        # object.__bool__(self)
        # 可以通过bool来指定对象转换为布尔值的情况
        def __bool__(self):
            return self.age > 17

        # __gt__会在对象做大于比较的时候调用 ,该方法的返回值将会作为比较的结果
        # 他需要两个参数 ,一个self表示当前对象 ,other表示和当前对象比较的对象
        # self > other
        def __gt__(self , other):
            return self.age > other.age


        # 创建两个Person类的实例        
        p1 = Person('孙悟空',18)
        p2 = Person('猪八戒',28)

        # 打印p1
        # 当我们打印一个对象时 ,实际上打印的是对象的中特殊方法 __str__()的返回值
        # print(p1) # <__main__.Person object at 0x04E95090>
        # print(p1)
        # print(p2)

        # print(repr(p1))

        # t = 1,2,3
        # print(t) # (1, 2, 3)

        # print(p1 > p2)
        # print(p2 > p1)

        # print(bool(p1))

        # if p1 :
        #     print(p1.name,'已经成年了')
        # else :
        #     print(p1.name,'还未成年了')

38模块
    模块(module)
    模块化 ,模块化指将一个完整的程序分解为一个一个小的模块
      通过将模块组合 ,来搭建出一个完整的程序
    不采用模块化 ,统一将所有的代码编写到一个文件中
    采用模块化 ,将程序分别编写到多个文件中
      模块化的有点:
          ① 方便开发
          ② 方便维护
          ③ 模块可以复用！

    在Python中一个py文件就是一个模块 ,要想创建模块 ,实际上就是创建一个python文件
    注意:模块名要符号标识符的规范

    在一个模块中引入外部模块
    ① import 模块名 (模块名 ,就是python文件的名字 ,注意不要py)
    ② import 模块名 as 模块别名
      - 可以引入同一个模块多次 ,但是模块的实例只会创建一个
      - import可以在程序的任意位置调用 ,但是一般情况下 ,import语句都会统一写在程序的开头
      - 在每一个模块内部都有一个__name__属性 ,通过这个属性可以获取到模块的名字
      - __name__属性值为 __main__的模块是主模块 ,一个程序中只会有一个主模块
          主模块就是我们直接通过 python 执行的模块
    import test_module as test

    # print(test.__name__)
    print(__name__)


    import m

    # 访问模块中的变量:模块名.变量名
    # print(m.a , m.b)

    # m.test2()

    p = m.Person()

    print(p.name)

    def test2():
        print('这是主模块中的test2')


    也可以只引入模块中的部分内容
    语法 from 模块名 import 变量,变量....
    from m import Person
    from m import test
    from m import Person,test
    from m import * # 引入到模块中所有内容 ,一般不会使用
    p1 = Person()
    print(p1)
    test()
    test2()

    也可以为引入的变量使用别名
    语法:from 模块名 import 变量 as 别名
    from m import test2 as new_test2

    test2()
    new_test2()

    from m import *
    print(_c)

    import xxx
    import xxx as yyy
    from xxx import yyy , zzz , fff
    from xxx import *
    from xxx import yyy as zz

39包
    包 Package
    包也是一个模块
    当我们模块中代码过多时 ,或者一个模块需要被分解为多个模块时 ,这时就需要使用到包
    普通的模块就是一个py文件 ,而包是一个文件夹
    包中必须要一个一个 __init__.py 这个文件 ,这个文件中可以包含有包中的主要内容
    from hello import a , b

    print(a.c)
    print(b.d)

    __pycache__ 是模块的缓存文件
    py代码在执行前 ,需要被解析器先转换为机器码 ,然后再执行
    所以我们在使用模块(包)时 ,也需要将模块的代码先转换为机器码然后再交由计算机执行
    而为了提高程序运行的性能 ,python会在编译过一次以后 ,将代码保存到一个缓存文件中
    这样在下次加载这个模块(包)时 ,就可以不再重新编译而是直接加载缓存中编译好的代码即可

40python的标准库
    开箱即用
    为了实现开箱即用的思想 ,Python中为我们提供了一个模块的标准库
    在这个标准库中 ,有很多很强大的模块我们可以直接使用 ,
      并且标准库会随Python的安装一同安装
    sys模块 ,它里面提供了一些变量和函数 ,使我们可以获取到Python解析器的信息
      或者通过函数来操作Python解析器
    引入sys模块
    import sys

    pprint 模块它给我们提供了一个方法 pprint() 该方法可以用来对打印的数据做简单的格式化
    import pprint

    sys.argv
    获取执行代码时 ,命令行中所包含的参数
    该属性是一个列表 ,列表中保存了当前命令的所有参数
    print(sys.argv)

    sys.modules
    获取当前程序中引入的所有模块
    modules是一个字典 ,字典的key是模块的名字 ,字典的value是模块对象
    pprint.pprint(sys.modules)

    sys.path
    他是一个列表 ,列表中保存的是模块的搜索路径
    ['C:\\Users\\lilichao\\Desktop\\resource\\course\\lesson_06\\code',
    'C:\\dev\\python\\python36\\python36.zip',
    'C:\\dev\\python\\python36\\DLLs',
    'C:\\dev\\python\\python36\\lib',
    'C:\\dev\\python\\python36',
    'C:\\dev\\python\\python36\\lib\\site-packages']
    pprint.pprint(sys.path)

    sys.platform
    表示当前Python运行的平台
    print(sys.platform)

    sys.exit()
    函数用来退出程序
    sys.exit('程序出现异常 ,结束！')
    print('hello')

    os 模块让我们可以对操作系统进行访问
    import os

    os.environ
    通过这个属性可以获取到系统的环境变量
    pprint.pprint(os.environ['path'])

    os.system()
    可以用来执行操作系统的名字
    os.system('dir')
    os.system('notepad')

41异常
    print('hello')
    try:
        # try中放置的是有可能出现错误的代码
        print(10/0)
    except:
        # except中放置的是出错以后的处理防暑
        print('哈哈哈 ,出错了~~~')
    else:
        print('程序正常执行没有错误')    
    print('你好')

    print('异常出现前')

    l = []
    try:
        # print(c)
        # l[10]
        # 1 + 'hello'
        print(10/0)
    except NameError:
        # 如果except后不跟任何的内容 ,则此时它会捕获到所有的异常
        # 如果在except后跟着一个异常的类型 ,那么此时它只会捕获该类型的异常
        print('出现 NameError 异常')
    except ZeroDivisionError:
        print('出现 ZeroDivisionError 异常')
    except IndexError:
        print('出现 IndexError 异常')
    # Exception 是所有异常类的父类 ,所以如果except后跟的是Exception ,他也会捕获到所有的异常
    # 可以在异常类后边跟着一个 as xx 此时xx就是异常对象
    except Exception as e :
        print('未知异常',e,type(e))
    finally :
        print('无论是否出现异常 ,该子句都会执行')

    print('异常出现后')

    也可以自定义异常类 ,只需要创建一个类继承Exception即可
    class MyError(Exception):
    pass

    def add(a,b):
    # 如果a和b中有负数 ,就向调用处抛出异常
    if a < 0 or b < 0:
        # raise用于向外部抛出异常 ,后边可以跟一个异常类 ,或异常类的实例
        # raise Exception    
        # 抛出异常的目的 ,告诉调用者这里调用时出现问题 ,希望你自己处理一下
        # raise Exception('两个参数中不能有负数！')  
        raise MyError('自定义的异常')
        
        # 也可以通过if else来代替异常的处理
        # return None
    r = a + b
    return r

    print(add(-123,456))    

42文件的操作
    打开文件
        open(file, mode='r', buffering=-1, encoding_=None, errors=None, newline=None, closefd=True, opener=None)
        使用open函数来打开一个文件
        参数:
          file 要打开的文件的名字(路径)
        返回值:
          返回一个对象 ,这个对象就代表了当前打开的文件

        创建一个变量 ,来保存文件的名字
        如果目标文件和当前文件在同一级目录下 ,则直接使用文件名即可
        file_name = 'demo.txt'

        在windows系统使用路径时 ,可以使用/来代替 \
        或者可以使用 \\ 来代替 \
        或者也可以使用原始字符串
        file_name = 'hello\\demo.txt'
        file_name = r'hello\demo.txt'

        表示路径 ,可以使用..来返回一级目录
        file_name = '../hello/demo.txt'

        如果目标文件距离当前文件比较远 ,此时可以使用绝对路径
        绝对路径应该从磁盘的根目录开始书写
        file_name = r'C:\Users\lilichao\Desktop\hello.txt'

        file_obj = open(file_name) # 打开 file_name 对应的文件

        print(file_obj)
    关闭文件
        打开文件
        file_name = 'demo.txt'

        调用open()来打开文件
        file_obj = open(file_name)

        当我们获取了文件对象以后 ,所有的对文件的操作都应该通过对象来进行
        读取文件中的内容
        read()方法 ,用来读取文件中的内容 ,它会将内容全部保存为一个字符串返回
        content = file_obj.read()

        print(content)

        关闭文件
        调用close()方法来关闭文件
        file_obj.close()

        with ... as 语句
        with open(file_name) as file_obj :
            在with语句中可以直接使用file_obj来做文件操作
            此时这个文件只能在with中使用 ,一旦with结束则文件会自动close()
            print(file_obj.read())


        file_name = 'hello'

        try:
            with open(file_name) as file_obj :
                print(file_obj.read())
        except FileNotFoundError:
            print(f'{file_name} 文件不存在~~')

    文件的读取
        file_name = 'demo2.txt'
        try:
            调用open()来打开一个文件 ,可以将文件分成两种类型
            一种 ,是纯文本文件(使用utf-8等编码编写的文本文件)
            一种 ,是二进制文件(图片、mp3、ppt等这些文件)
            open()打开文件时 ,默认是以文本文件的形式打开的 ,但是open()默认的编码为None
              所以处理文本文件时 ,必须要指定文件的编码
            with open(file_name,encoding='utf-8') as file_obj:
                通过 read() 来读取文件中的内容
                如果直接调用read()它会将文本文件的所有内容全部都读取出来
                  如果要读取的文件较大的话 ,会一次性将文件的内容加载到内存中 ,容易导致内存泄漏
                  所以对于较大的文件 ,不要直接调用read()
                help(file_obj.read)
                read()可以接收一个size作为参数 ,该参数用来指定要读取的字符的数量
                  默认值为-1 ,它会读取文件中的所有字符
                  可以为size指定一个值 ,这样read()会读取指定数量的字符 ,
                      每一次读取都是从上次读取到位置开始读取的
                      如果字符的数量小于size ,则会读取剩余所有的
                      如果已经读取到了文件的最后了 ,则会返回''空串
                content = file_obj.read(-1)
                content = file_obj.read(6)
                content = file_obj.read(6)
                content = file_obj.read(6)
                content = file_obj.read(6)
                # print(content)
                # print(len(content))
        except FileNotFoundError :
            print(f'{file_name} 这个文件不存在！')

        # 读取大文件的方式
        file_name = 'demo.txt'

        try:
            with open(file_name,encoding='utf-8') as file_obj:
                # 定义一个变量 ,来保存文件的内容
                file_content = ''
                # 定义一个变量 ,来指定每次读取的大小
                chunk = 100
                # 创建一个循环来读取文件内容
                while True:
                    # 读取chunk大小的内容
                    content = file_obj.read(chunk)

                    # 检查是否读取到了内容
                    if not content:
                        # 内容读取完毕 ,退出循环
                        break

                    # 输出内容
                    # print(content,end='')
                    file_content += content

        except FileNotFoundError :
            print(f'{file_name} 这个文件不存在！')
        print(file_content)

        import pprint
        import os
        file_name = 'demo.txt'

        with open(file_name , encoding='utf-8') as file_obj:
            # readline()
            # 该方法可以用来读取一行内容
            # print(file_obj.readline(),end='')
            # print(file_obj.readline())
            # print(file_obj.readline())

            # readlines()
            # 该方法用于一行一行的读取内容 ,它会一次性将读取到的内容封装到一个列表中返回
            # r = file_obj.readlines()
            # pprint.pprint(r[0])
            # pprint.pprint(r[1])
            # pprint.pprint(r[2])

            for t in file_obj:
                print(t)

    文件的写入
        file_name = 'demo5.txt'

        使用open()打开文件时必须要指定打开文件所要做的操作(读、写、追加)
        如果不指定操作类型 ,则默认是 读取文件  , 而读取文件时是不能向文件中写入的
        r 表示只读的
        w 表示是可写的 ,使用w来写入文件时 ,如果文件不存在会创建文件 ,如果文件存在则会截断文件
          截断文件指删除原来文件中的所有内容
        a 表示追加内容 ,如果文件不存在会创建文件 ,如果文件存在则会向文件中追加内容
        x 用来新建文件 ,如果文件不存在则创建 ,存在则报错
        + 为操作符增加功能
          r+ 即可读又可写 ,文件不存在会报错
          w+
          a+
        with open(file_name , 'w' , encoding='utf-8') as file_obj:
        with open(file_name , 'r+' , encoding='utf-8') as file_obj:
        with open(file_name , 'x' , encoding='utf-8') as file_obj:
            write()来向文件中写入内容 ,
            如果操作的是一个文本文件的话 ,则write()需要传递一个字符串作为参数
            该方法会可以分多次向文件中写入内容
            写入完成以后 ,该方法会返回写入的字符的个数
            file_obj.write('aaa\n')
            file_obj.write('bbb\n')
            file_obj.write('ccc\n')
            r = file_obj.write(str(123)+'123123\n')
            r = file_obj.write('今天天气真不错')
            print(r)
    文件的二进制
        file_name = 'c:/Users/lilichao/Desktop/告白气球.flac'
        读取模式
        t 读取文本文件(默认值)
        b 读取二进制文件
        with open(file_name , 'rb') as file_obj:
            读取文本文件时 ,size是以字符为单位的
            读取二进制文件时 ,size是以字节为单位
            print(file_obj.read(100))

            将读取到的内容写出来
            定义一个新的文件
            new_name = 'aa.flac'

            with open(new_name , 'wb') as new_obj:

                定义每次读取的大小
                chunk = 1024 * 100

                while True :
                    从已有的对象中读取数据
                    content = file_obj.read(chunk)

                    内容读取完毕 ,终止循环
                    if not content :
                        break

                    将读取到的数据写入到新对象中
                    new_obj.write(content)

    读取文件的位置
        with open('demo.txt','rb') as file_obj:
        print(file_obj.read(100))
        print(file_obj.read(30))

        seek() 可以修改当前读取的位置
        file_obj.seek(55)
        file_obj.seek(80,0)
        file_obj.seek(70,1)
        file_obj.seek(-10,2)
        seek()需要两个参数
            第一个 是要切换到的位置
            第二个 计算位置方式
                可选值:
                    0 从头计算 ,默认值
                    1 从当前位置计算
                    2 从最后位置开始计算

            print(file_obj.read())

            # tell() 方法用来查看当前读取的位置
            print('当前读取到了 -->',file_obj.tell())

        with open('demo2.txt','rt' , encoding='utf-8') as file_obj:
            # print(file_obj.read(100))
            # print(file_obj.read(30))

            # seek() 可以修改当前读取的位置
            file_obj.seek(9)
            # seek()需要两个参数
            #   第一个 是要切换到的位置
            #   第二个 计算位置方式
            #       可选值:
            #           0 从头计算 ,默认值
            #           1 从当前位置计算
            #           2 从最后位置开始计算

            print(file_obj.read())

            # tell() 方法用来查看当前读取的位置
            print('当前读取到了 -->',file_obj.tell())

    文件的其他操作
        import os
        from pprint import pprint

        os.listdir() 获取指定目录的目录结构
        需要一个路径作为参数 ,会获取到该路径下的目录结构 ,默认路径为 . 当前目录
        该方法会返回一个列表 ,目录中的每一个文件(夹)的名字都是列表中的一个元素
        r = os.listdir()

        os.getcwd() 获取当前所在的目录
        r = os.getcwd()

        os.chdir() 切换当前所在的目录 作用相当于 cd
        os.chdir('c:/')

        r = os.getcwd()

        创建目录
        os.mkdir("aaa") # 在当前目录下创建一个名字为 aaa 的目录

        删除目录
        os.rmdir('abc')

        open('aa.txt','w')
        删除文件
        os.remove('aa.txt')

        os.rename('旧名字','新名字') 可以对一个文件进行重命名 ,也可以用来移动一个文件
        os.rename('aa.txt','bb.txt')
        os.rename('bb.txt','c:/users/lilichao/desktop/bb.txt')

        pprint(r)
