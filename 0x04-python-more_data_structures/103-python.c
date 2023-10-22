#include <Python.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: The Python list object.
 */
void print_python_list(PyObject *p)
{
    int size, alloc, i;
    PyObject *item;
    
    if (PyList_Check(p))
    {
        size = PyList_Size(p);
        alloc = ((PyListObject *)p)->allocated;
        
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %d\n", size);
        printf("[*] Allocated = %d\n", alloc);
        
        for (i = 0; i < size; i++)
        {
            item = PyObject_GetItem(p, PyLong_FromLong(i));
            if (item != NULL)
            {
                printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
                Py_DECREF(item);
            }
        }
    }
}

/**
 * print_python_bytes - Prints basic info about Python bytes.
 * @p: The Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
    int size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);
    printf("  size: %d\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %d bytes: ", (size + 1 > 10) ? 10 : size + 1);
    
    for (i = 0; i < size + 1 && i < 10; i++)
    {
        printf("%02hhx", str[i]);
        if (i + 1 < size + 1 && i + 1 < 10)
            printf(" ");
    }
    printf("\n");
}
