#include <Python.h>

static PyObject* hello_world(PyObject* self, PyObject* args) {
    if (!PyArg_ParseTuple(args, "")) return NULL;
    return PyUnicode_FromString("Hello World!");
};

static PyMethodDef hello_methods[] = {
    {"hello_world", hello_world, METH_VARARGS, "Prints Hello World!"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "hello", NULL, -1, hello_methods
};
PyMODINIT_FUNC PyInit_hello(void) { return PyModule_Create(&module); }

