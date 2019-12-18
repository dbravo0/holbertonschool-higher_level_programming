#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: Python object
 */
void print_python_list_info(PyObject *p)
{
	int i, j, k;

	i = Py_SIZE(p);
	j = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", i);
	printf("[*] Allocated = %d\n", j);

	for (k = 0 ; k < i ; k++)
	{
		printf("Element %d: ", k);
		printf("%s\n", ((PyList_GetItem(p, k))->ob_type)->tp_name);
	}
}
