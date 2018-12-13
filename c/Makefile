src = $(wildcard *.c)
obj = $(src:.c=.o)

LDFLAGS = 
CXXFLAGS = -std=c++11 -W -Wall 

main: $(obj)
	$(CC) -o $@ $^ $(LDFLAGS)

.PHONY: clean
clean:
		rm -f $(obj) myprog
