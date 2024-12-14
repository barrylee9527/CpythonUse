# Cython的安装与使用方法

## 安装Cython

Cython是Python语言的一个扩展，可以将Python代码转换为C语言，从而提高运行效率。

Cython的安装方法有两种：

1. 通过pip安装：

```
pip install cython
```

2. 通过源码安装：

下载Cython的源码包，解压后进入源码目录，执行以下命令：

```
python setup.py install
```
## 编译Cython代码

Cython代码需要编译成C语言代码才能运行，可以使用以下命令编译：

```
python setup.py build_ext --inplace
```


## 使用Cython

Cython的使用方法很简单，只需要在Python代码中导入`cython`模块，然后在需要转换的函数上添加`cdef`关键字，并在函数的第一行添加`cpdef`关键字，即可将Python函数转换为C语言函数。

例如，假设有一个Python函数`add(a, b)`，我们想将其转换为C语言函数，可以这样写：

```python
from cython import cython

@cython.cfunc
def add(int a, int b):
    return a + b

@cython.ccall
def add_c(int a, int b):
    return a + b
```

1. `@cython.cfunc`：表示将Python函数转换为C语言函数。
2. `@cython.ccall`：表示将Python函数转换为C语言函数，并将返回值类型声明为`int`。

然后，就可以像调用普通Python函数一样调用转换后的C语言函数：

```python
print(add(1, 2))
print(add_c(1, 2))
```

1. `add(1, 2)`：调用Python函数`add(a, b)`，并将`a=1`和`b=2`作为参数传入。
2. `add_c(1, 2)`：调用Python函数`add_c(a, b)`，并将`a=1`和`b=2`作为参数传入。
# Cython还可以把Python代码转换为C代码
# 将Python代码转换为C代码的方法
# 1. 使用Cython的`cdef`关键字将Python函数转换为C函数
# 2. 使用Cython的`ctypedef`关键字声明C语言类型
# 3. 使用Cython的`cpdef`关键字将Python函数转换为C函数，并声明返回值类型
# 4. 使用Cython的`cimport`关键字导入C语言模块
# 5. 使用Cython的`cclass`关键字声明C语言类
