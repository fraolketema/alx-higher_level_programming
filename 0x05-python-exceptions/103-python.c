#include <Python.h>


void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *element;

    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n[*] Size of the Python List = %zd\n[*] Allocated = %zd\n", size, ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        element = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
        
        if (PyBytes_Check(element)) {
            printf("[.] bytes object info\n");
            printf("  size: %zd\n", PyBytes_Size(element));

            printf("  trying string: %s\n", PyBytes_AsString(element));
            printf("  first 10 bytes: ");
            Py_ssize_t min_size = PyBytes_Size(element) < 10 ? PyBytes_Size(element) : 10;

            for (Py_ssize_t j = 0; j < min_size; j++) {
                printf("%02x ", (unsigned char)PyBytes_AsString(element)[j]);
            }
            printf("\n");
        }
        else if (PyFloat_Check(element)) {
            printf("[.] float object info\n");
            printf("  value: %f\n", PyFloat_AsDouble(element));
        }
        else if (PyList_Check(element)) {
            print_python_list(element);
        }
    }
}


void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);

    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first 10 bytes: ");
    Py_ssize_t min_size = size < 10 ? size : 10;

    for (i = 0; i < min_size; i++) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", PyFloat_AsDouble(p));
}
