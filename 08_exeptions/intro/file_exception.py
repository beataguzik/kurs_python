import sys

fopen = open('myfile', 'r')

try:
    x = fopen.read()
    print(x)
    x=int(x)
except Exception as mess:
    print('jakis blad', mess)
    #print(sys.exc_info()[0]) # ->pokazuje info co to za bład

finally:
    fopen.close()
    print('zamknieto tryb odczytu pliku')


