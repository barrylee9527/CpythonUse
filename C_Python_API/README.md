`gcc -shared -o square.so -fPIC $(python3-config --cflags) square.c $(python3-config --ldflags)
`