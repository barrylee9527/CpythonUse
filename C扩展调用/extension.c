//写一个可以让python调用的函数
//  Created by 陈希 on 14-7-24.
//
//

#include <stdio.h>
//引入include目录下的Python.h文件
#include "include/Python.h"
void initextension();
//定义一个函数，该函数将在C中调用
int add(int a, int b)
{
    return a+b;
}



//定义一个函数，该函数将在python中调用

static PyObject* py_add(PyObject* self, PyObject* args)
{
    int a, b;
    int res;
    if(!PyArg_ParseTuple(args, "ii", &a, &b))
    {
        return NULL;
    }
    res = add(a, b);
    return Py_BuildValue("i", res);
}

//定义一个函数列表，这个列表中的函数都将在python中调用
static PyMethodDef myMethods[] = {
    {"add", py_add, METH_VARARGS},
    {NULL, NULL}
};

//初始化函数
void initextension()
{
    Py_InitModule("extension", myMethods);
}

