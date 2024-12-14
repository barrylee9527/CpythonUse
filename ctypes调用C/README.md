# ctypes调用C

## 简介

ctypes是Python的外部函数库，它可以让你调用C/C++库中的函数。

## 用法

### 编写C代码

#### 编译成动态库

1. 编写C代码，并编译成动态库。
2. 使用`gcc -shared -o libxxx.so xxx.c`命令编译成动态库。
3. 在Linux系统中，可以使用以下命令：
`gcc -shared -o test.so -fPIC test.c`
`-fPIC`选项表示生成位置无关代码（Position-independent code，PIC）
4. 在Windows系统中，可以使用以下命令：
`gcc -shared -o test.dll test.c`

## Python调用C

### 加载动态库

使用`cdll.LoadLibrary()`函数加载动态库。

```python
import ctypes

# 加载动态库
lib = ctypes.cdll.LoadLibrary('./libxxx.so')
```

### 调用函数

使用`lib.xxx()`函数调用C函数。

```python
# 调用C函数
lib.xxx(arg1, arg2, arg3)
```


