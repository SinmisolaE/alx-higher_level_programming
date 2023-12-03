#include <Python.h>

/**
 *  print_python_list_info - prints info about python
 *  @p: python list
 *  Return: nain
 */
void print_python_list_info(PyObject *p)
{
	int size, allocate, i;
	PyObject *objct;

	size = PyList_Size(p);
	allocate = PyList_GET_SIZE(p);

	printf("[*] Size of Python List = %d", size);
	printf("[*] Allocated = %d", allocate);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		objct = PyList_GetItem(p, i);
		printf("%s\n", PyObject_Type(objct)->tp_name);
	}
}
