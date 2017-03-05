import ctypes as C
mate = C.CDLL('./mylib.so')

#=================================
# Suma de dos punto flotante de C.
#=================================

mate.add_float.restype = C.c_float #"Declaramos" que el resultado de llamar a la funcion es un punto flotante de C.
mate.add_float.argtypes = [C.c_float,C.c_float] #"Declaramos" que los argumnetos de la funcion son un punto flotante de C.

x_1=C.c_float(1.1)
x_2=C.c_float(10.10)
print 'add_float', mate.add_float(x_1,x_2)

# Suma de dos enteros de C.
math.add_int.restype = C.c_int #"Declaramos" que el resultado de llamar a la funcion es un entero de C.
math.add_int.argtypes = [C.c_int,C.c_int] #"Declaramos" que los argumnetos de la funcion son enteros de C.

n_1_1=C.c_int(1)
n_2=C.c_int(10)
print 'add_int', math.add_int(n_1,n_2)

# Suma de dos enteros C pasados por referencia.
x_1 = C.c_float(1.1)
x_2 = C.c_float(-0.10)
res = C.c_float()
mate.add_float_ref(C.byref(x_1),C.byref(x_2),C.byref(res))
print 'add_float_ref', res.value
print 'type add_float_ref',res

# Suma de dos enteros C pasados por referencia.
n_1 = C.c_int(10)
n_2 = C.c_int(-1)
res = C.c_int()
mate.add_int_ref(C.byref(n_1),C.byref(n_2),C.byref(res))
print 'add_int_ref', res.value
print 'type add_int_ref',res

# Suma de arrays con una funcion de C.
n=C.cint(2)
par1 = (C.c_int*2) (0,1)
par2 = (C.c_int*2) (1,0)
out = (C.c_int*2) ()
math.add_int_array(C.byref(par1),C.byref(par2),C.byref(out),n)

print 'add_int_array', out[0], out[1], out[2]