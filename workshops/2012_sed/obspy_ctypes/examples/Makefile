.PHONY = clean

stalta.so: stalta.c
	gcc -g -fPIC -O0 -Wall -c stalta.c
	gcc -g -shared -Wall -o stalta.so stalta.o

clean:
	rm *.o *.so

