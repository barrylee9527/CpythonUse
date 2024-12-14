#include <Python.h>

// 计算平方的函数
static PyObject* square(PyObject* self, PyObject* args) {
    int input;
    if (!PyArg_ParseTuple(args, "i", &input)) {
        return NULL; // 参数解析失败
    }
    return Py_BuildValue("i", input * input); // 返回平方
}

// 定义模块的方法
static PyMethodDef SquareMethods[] = {
    {"square", square, METH_VARARGS, "Calculate the square of a number."},
    {NULL, NULL, 0, NULL} // 结束标志
};

// 定义模块
static struct PyModuleDef squaremodule = {
    PyModuleDef_HEAD_INIT,
    "square", // 模块名称
    NULL, // 模块文档
    -1, // 模块状态
    SquareMethods // 方法列表
};

// 模块初始化函数
PyMODINIT_FUNC PyInit_square(void) {
    return PyModule_Create(&squaremodule);
}
