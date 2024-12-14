# C扩展调用

## 介绍

C扩展是指通过编写C语言代码并将其编译为共享库（.so或.dll文件），
然后在Python中导入和调用这些C函数。C扩展的主要优势在于它能够显著提高性能，尤其是在处理大量数据或执行复杂计算时
## 准备工作
## 编写C代码
## 编写setup.py文件
## 编译C扩展
`python setup.py build`

## 安装C扩展
`python setup.py install`
## 在Python中调用C扩展
