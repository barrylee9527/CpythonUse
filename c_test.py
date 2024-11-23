from ctypes import *
solib = cdll.LoadLibrary("test.so")
arr = (c_int * 3)(1,2,3)
for i in range(0, len(arr)):
    print(arr[i],end=" ")
solib.test.restype = POINTER(c_int)
res = solib.test(byref(arr),6)
for i in res[0:3]:
    print("res1",i)

solib.test.restype = POINTER(c_int)
res2 = solib.test(arr,6)
for i in res2[0:3]:
    print("res2",i)
pValue = pointer(c_int(5))
solib.FunPoint.restype = POINTER(c_int)
res2 = solib.FunPoint(pValue)
print(res2.contents)
## 传递指针
# 定义一个指向c_int的指针
# c_int(0) 代表的是这个c_int变量的值为0，即c_int(6)代表变量值为6，而不是申请了一个拥有6个c_int变量的数组
pValue = pointer(c_int(0))
# C语言函数原型：void FunPoint(int *pValue);
solib.FunPoint(pValue)
 
 
## 传递引用
# value = c_int(0)
# C语言函数原型：void FunByref(int &value);
# solib.FunByref(byref(value))
 
 
## 传递数组指针
# data:一个指向(拥有6个c_int类型的元素的数组)的指针
data = (c_int * 6)(1,2,3,4,5,6)
# C语言函数原型：void FunArray(int *arr, int size);
FunArray_res = solib.FunArray(data, 6)
print("FunArray_res",FunArray_res)
 
## 传递结构体指针
class StructureTmp(Structure):
    _fields_ = [
        ('name', c_int),
        ('age', c_int),
    ]
 
# data2:一个指向(拥有6个结构体 StructureTmp 类型的元素的数组)的指针
data2 = (StructureTmp * 6)()
# C语言函数原型：void FunStructArray(StructureTmp *arr, int size);
Struct_Ptr = POINTER(StructureTmp)
# 约定函数的传入参数的类型
solib.FunStructArray.argtypes = [Struct_Ptr, c_int]
FunStructArray_res = solib.FunStructArray(data2, c_int(6))
print(FunStructArray_res)
 
## 传递字符串
snSize = 64
# 下面两种方法都可以
sn = (c_char * snSize)(2)
sn = create_string_buffer(''.encode('utf-8'), snSize)
# C语言函数原型：void FunStr(char *pStr, int size);
solib.FunStr(sn, c_int(snSize))
# 输出字符串
print('GetSn = ' + str(sn.value))


## 约定函数的返回值的类型
# C语言函数原型：int Fun1();
solib.Fun1.restype = c_int
ret = solib.Fun1()
print(ret)
 
## 函数返回char *（字符串）
# C语言函数原型：char * FunStr();
solib.FunStr_1.restype = c_char_p
print("str :" + str(solib.FunStr_1()))