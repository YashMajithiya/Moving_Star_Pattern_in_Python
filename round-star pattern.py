from time import sleep
from os import system,name

def clear():
	if name == 'nt':
		_ = system('cls')


def p1():
    for i in range(5):
        print("\t   ",end='')
        for j in range(5-i):
            print("     ",end='')
        for k in range(i*2-1):
            print("*    ",end='')
        print("\n")

def p2():
    print("\n\n\n\n\n\n")
    for i in range(4):
        
        print("\t\t\t\t\t\t ",end='')
        
        for j in range(i):
            print("*   ",end='')
        print('\n')
    for i in range(4):
        
        print("\t\t\t\t\t\t ",end='')
        
        for j in range(4-i):
            print("*   ",end='')
        print('\n')

def p3():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for i in range(5):
        print("\t   ",end='')
        for i in range(i+1):
            print("     ",end='')
        for j in range(7-i*2):
            print("*    ",end='')
        print("\n")

def p4():
    print("\n\n\n\n\n\n")
    for i in range(4):
        for j in range(4-i):
            print("    ",end='')
        for j in range(i):
            print("   *",end='')
        print('\n')
    for i in range(4):
        for j in range(i):
            print("    ",end='')
        for j in range(4-i):
            print("   *",end='')
        print('\n')

while True:
    p1()
    sleep(2)
    clear()
    p2()
    sleep(2)
    clear()
    p3()
    sleep(2)
    clear()
    p4()
    sleep(2)
    clear()