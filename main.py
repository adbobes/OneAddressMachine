import cpu
import math
import sys

def cmmdc(x, y):

    fileAddress = open('1address.txt', 'w')

    x_int = int(x)
    y_int = int(y)

    if (x_int < y_int):
        x_int, y_int = y_int, x_int
    fileAddress.write("LOAD " + str(y_int) + '\n')
    fileAddress.write("STORE T\n")
    fileAddress.write("LOAD " + str(x_int) + '\n')


    while (x_int != y_int and (x_int > 0 and y_int > 0)):
        if (x_int < y_int):
            x_int, y_int = y_int, x_int
            fileAddress.write("SWAP T\n")
        x_int -= y_int
        fileAddress.write("SUB T\n")

    fileAddress.write("STORE REZ\n")

    fileAddress.write("CLR T\n")
    fileAddress.write("CLR AC\n")

    fileAddress.write("OUT ALL\n")
    fileAddress.close()



def cmmmc(x,y):

    fileAddress = open('1address.txt', 'w')

    x_int = int(x)
    y_int = int(y)


    a_int = int(x_int)
    b_int = int(y_int)

    if (x_int < y_int):
        x_int, y_int = y_int, x_int

    fileAddress.write("LOAD " + str(y_int) + '\n')
    fileAddress.write("STORE T\n")
    fileAddress.write("LOAD " + str(x_int) + '\n')

    while (x_int != y_int and (x_int > 0 and y_int > 0)):
        if (x_int < y_int):
            x_int, y_int = y_int, x_int
            fileAddress.write("SWAP T\n")
        x_int -= y_int
        fileAddress.write("SUB T\n")

    fileAddress.write("LOAD " + str(a_int) + '\n')
    fileAddress.write("MUL " + str(b_int) + '\n')
    fileAddress.write("DIV T\n")
    fileAddress.write("STORE REZ\n")
    fileAddress.write("CLR AC\n")
    fileAddress.write("CLR T\n")

    fileAddress.write("OUT ALL\n")
    fileAddress.close()



def ec2(a, b , c):

    fileAddress = open('1address.txt', 'w')

    a_int = int(a)
    b_int = int(b)
    c_int = int(c)

    delta = int(b_int*b_int - 4*a_int*c_int)
    var = 0

    if(delta > 0):
        var = delta
        var = math.sqrt(var)

    var = int(var)

    fileAddress.write('LOAD ' + '4' + '\n')
    fileAddress.write('MUL '+ a + '\n')
    fileAddress.write('MUL ' + c + '\n')
    fileAddress.write('STORE T\n')
    fileAddress.write('LOAD ' + b + '\n')
    fileAddress.write('MUL ' + b + '\n')
    fileAddress.write('SUB T\n')
    fileAddress.write('STORE REZ\n')

    if delta < 0:
        fileAddress.write('CLR ALL\n')
        fileAddress.write('LOAD -255\n')
        fileAddress.write('STORE T\n')
        fileAddress.write('STORE REZ\n')
        fileAddress.write('OUT ALL\n')

    else:
        fileAddress.write('LOAD ' + b + '\n')
        fileAddress.write('OPP AC\n')
        fileAddress.write('ADD ' + str(var) + '\n')
        fileAddress.write('DIV 2\n')
        fileAddress.write('DIV ' + a + '\n')

        fileAddress.write('STORE T\n')                  #T    =    x2
        fileAddress.write('LOAD ' + b + '\n')
        fileAddress.write('OPP AC\n')
        fileAddress.write('SUB ' + str(var) + '\n')

        fileAddress.write('DIV 2\n')
        fileAddress.write('DIV ' + a + '\n')
        fileAddress.write('CLR REZ\n')
        fileAddress.write('OUT ALL\n')                  #AC   =    x1
    fileAddress.close()


def prim(x):

    fileAddress = open('1address.txt', 'w')

    x_int = int(x)
    div_int = 2
    flag_int = 1
    flag_neg = 0

    fileAddress.write("LOAD " + str(div_int) + '\n')
    fileAddress.write("STORE T\n")
    fileAddress.write("LOAD " + str(x_int) + '\n')

    if x_int < 0:
        fileAddress.write("OPP AC\n")
        x_int = abs(int(x_int))
        flag_neg = 1

    for x in range (2, int(x_int / 2 + 1)):
        if int(x_int) % int(div_int) == 0:
            flag_int = 0
            break
        else:
            fileAddress.write("INC T\n")

    if(x_int == 0 or x_int == 1):
        flag_int = 0

    fileAddress.write("SWAP T\n")
    fileAddress.write("LOAD " + str(flag_int) + '\n')
    fileAddress.write("STORE REZ\n")
    fileAddress.write("CLR AC\n")

    if flag_neg == 1:
        fileAddress.write("OPP T\n")
        fileAddress.write("SWAP T\n")
        fileAddress.write("OUT ALL\n")
    else:
        fileAddress.write("SWAP T\n")
        fileAddress.write("OUT ALL\n")

    fileAddress.close()


def gauss(x):

    fileAddress = open('1address.txt', 'w')
    
    x_int = int(x)
    neg = False

    fileAddress.write("LOAD " + '1' + '\n')
    fileAddress.write("STORE T\n")
    fileAddress.write("CLR AC\n")

    if(x_int < 0):
        x_int = abs(x_int)
        neg = True

    for index in range(x_int):
        fileAddress.write("ADD T\n")
        fileAddress.write("INC T\n")
    fileAddress.write("DEC T\n")

    if neg == True:
        fileAddress.write("OPP AC\n")

    fileAddress.write("OUT ALL\n")


    fileAddress.close()



registrii = cpu.cpu()
fileText = open("binary.txt", "r")
registrii.functionSwitch(fileText)
