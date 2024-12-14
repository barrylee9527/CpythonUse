#include <stdio.h>
int* test(int *data,int size)
{
    return data;
}

int* test2(int raw_data[],int size)
{
    int arr[3];
    for (int j = 0; j<3; j = j + 1)
	{
		arr[j] = (int)(raw_data[j] + raw_data[j + 1]);
	}
	return arr;
}
int* FunPoint(int *pValue)
{
    return pValue;
}
int FunArray(int *arr, int size)
{
    return arr[0];
}
typedef struct {
    int name;
    int age;
}StructureTmp;
int FunStructArray(StructureTmp *arr, int size)
{
    int a = 3;
    return arr->name;
}
void FunStr(char *pStr, int size)
{

}
char * FunStr_1()
{
    return "dsaf";
}
int Fun1()
{
    return 5;
}