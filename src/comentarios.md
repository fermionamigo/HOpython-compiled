Primero generamos la libreria dinamica poniendo en la linea de comandos
gcc -c -fPIC arrays.c 
gcc -c -fPIC add_two.c 
esto nos genera dos objetos dinamicos que luego metemos en una sola libreria con
gcc -shared arrays.o add_two.o -o mylib.so