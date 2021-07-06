# ----------------------------------------------------------------
# Name: 1 ADDRESS MACHINE SIMULATOR
# Purpose: Emulate a 1 Adress Machine and calulate basic problems
#
# Authors: Bobes Andrei, Gogu Claudiu, Camen Gabriel
#
# Created: 02/06/2019
# -----------------------------------------------------------------
#
#
# ============ EXTERNAL MODULES ==============

import os

from colorama import Fore, Back

class cpu:
    # ============================================================

    AC = 0  # AC REGISTER
    Result = 0  # REZ REGISTER
    Temp = 0  # T REGISTER
    MAX = 255
    MIN = -255
    STATUS = True  # PROGRAM STATUS
    ProgramCounter = 1  # COMMAND LINE
    OVERFLOW = False  # MEMORY OVERFLOW, MAX VALUE 255
    UNDERFLOW = False  # MEMORY UNDERFLOW, MIN VALUE -255
    InstructionRegister = 0  # INSTRUCTION

    # ===================== ALL OPERATIONS =======================

    # ADD A REGISTER / NUMBER TO ANOTHER REGISTER
    def addNumber(self, valoare):

        if valoare == 'T':
            temporar = int(self.AC) + int(self.Temp)
        elif valoare == 'REZ':
            temporar = int(self.AC) + int(self.Result)
        elif valoare.isdigit() == True:
            temporar = int(self.AC) + int(valoare)
        else:
            self.fault()
            self.exit()

        if int(temporar) > int(self.MAX):
            self.OVERFLOW = True
            self.AC = self.MAX
            self.fault()

        else:
            self.AC = int(temporar)

        self.ProgramCounter += 1

    # SUBSTRECT A REGISTER / NUMBER FROM ANOTHER REGISTER
    def subNumber(self, valoare):



        if valoare == 'T':
            temporar = int(self.AC) - int(self.Temp)
        elif valoare == 'REZ':
            temporar = int(self.AC) - int(self.Result)
        elif valoare.isdigit() == True:
            temporar = int(self.AC) - int(valoare)
        elif valoare[1].isdigit() == True and valoare[0] == '-' and int(valoare) < 0:
                temporar = int(self.AC) + int(valoare)
        else:
            self.fault()
            self.exit()

        if int(temporar) < -255:
            self.UNDERFLOW = True
            self.AC = -255
            self.fault()
        else:
            self.AC = int(temporar)

        self.ProgramCounter += 1

    # MULTIPLE A REGISTER WITH A REGISTER / NUMBER

    def mulNumber(self, valoare):

        if valoare == 'T':
             temporar = int(self.AC) * int(self.Temp)
        elif valoare[0] == '-' and valoare[1].isdigit() == True or valoare.isdigit() == True:
            temporar = int(valoare) * int(self.AC)
        elif valoare == 'REZ':
            temporar = int(self.Result) * int(self.AC)
        else:
            self.fault()
            self.exit()

        if int(temporar) > 255:
            self.OVERFLOW = True
            self.AC = self.MAX
            self.fault()

        elif int(temporar) < -255:
            self.UNDERFLOW = True
            self.AC = -255
            self.fault()
        else:
            self.AC = int(temporar)

        self.ProgramCounter += 1

    # DIVIDE A REGISTER WITH A REGISTER / NUMBER
    def divNumber(self, valoare):

        if valoare == 'T':
            self.AC //= self.Temp

        elif valoare == 'REZ':
            self.AC //= self.Result

        elif valoare.isdigit() == True and valoare != '0':
            self.AC //= int(valoare)

        else:
            self.fault()

        self.ProgramCounter += 1

    # INCREMENT A REGISTER
    def incNumber(self, valoare):

        if valoare == 'T':
            self.Temp += 1
        elif valoare == 'REZ':
            self.Result += 1
        elif valoare == 'AC':
            self.AC += 1
        else:
            self.fault()

        if (self.AC > 255 or self.Result > 255 or self.Temp > 255):
            self.OVERFLOW = True;
            self.fault()
        self.ProgramCounter += 1

    # DECREMENT A REGISTER
    def decNumber(self, valoare):

        if valoare == 'T':
            self.Temp -= 1
        elif valoare == 'REZ':
            self.Result -= 1
        elif valoare == 'AC':
            self.AC -= 1
        else:
            self.fault()

        if (self.AC < -255 or self.Result < -255 or self.Temp < -255):
            self.UNDERFLOW = True
            self.fault()

        self.ProgramCounter += 1

    # OPPOSITE VALUE FOR A REGISTER
    def oppNumber(self, valoare):

        if valoare == 'T':
            if self.Temp > 0:
                self.Temp -= 2 * self.Temp
            else:
                self.Temp = abs(self.Temp)

        elif valoare == 'REZ':
            if self.Result > 0:
                self.Result -= 2 * self.Result
            else:
                self.Result = abs(self.Result)

        elif valoare == 'AC':
            if self.AC > 0:
                self.AC -= 2 * self.AC
            else:
                self.AC = abs(self.AC)
        else:
            self.fault()

        self.ProgramCounter += 1

    # LOAD A REGISTER
    def loadNumber(self, valoare):

        if(valoare[0] == '-' and valoare[1:].isdigit() == True):

            if int(valoare) < -255:
                self.UNDERFLOW = True
                self.fault()
            else:
                self.AC = int(valoare)

        elif valoare.isdigit() == True:

            if int(valoare) > 255:
                self.OVERFLOW = True
                self.fault()
            else:
                self.AC = int(valoare)

        else:
            self.fault()

        self.ProgramCounter += 1

        # STORE A REGISTER TO ANOTHER ONE

    def storeNumber(self, valoare):

        if valoare == 'T':
            self.Temp = self.AC
        elif valoare == 'REZ':
            self.Result = self.AC
        else:
            self.fault()

        self.ProgramCounter += 1

    # PRINT A REGISTER
    def outNumber(self, valoare):

        if valoare == 'AC':
            print(Fore.RED + "AC [", self.AC, "]\n")
        elif valoare == 'REZ':
            print(Fore.YELLOW + "REZ [", self.Result, "]\n")
        elif valoare == 'T':
            print(Fore.CYAN + "T [", self.Temp, "]\n")
        elif valoare == 'ALL':
            print(Fore.RED + "AC [", self.AC, "]\n")
            print(Fore.YELLOW + "REZ [", self.Result, "]\n")
            print(Fore.CYAN + "T [", self.Temp, "]\n")
        else:
            self.fault()

        self.ProgramCounter += 1

    # SWAP REGISTERS

    def swapNumbers(self, valoare):
        if valoare == "T":
             self.Temp, self.AC = self.AC, self.Temp
        elif valoare == "REZ":
            self.Result, self.AC = self.AC, self.Result
        else:
            self.fault()

        self.ProgramCounter += 1

    # HELP COMMAND
    def help(self):
        with open("HELP.txt") as helpFile:
            for line in helpFile:
                print(Fore.GREEN + line.strip())

    # CLEAR REGISTER
    def clear(self, valoare):

        if valoare == 'T':
            self.Temp = 0
        elif valoare == 'REZ':
            self.Result = 0
        elif valoare == 'AC':
            self.AC = 0
        elif valoare == 'ALL':
            self.Temp = 0
            self.Result = 0
            self.AC = 0
        else:
            self.fault()

        self.ProgramCounter += 1

    # EXIT THE PROGRAM
    def exit(self):
        print(Fore.GREEN + Back.RESET + "Press ENTER to exit the program...")
        input()
        return

    # ============================================================

    # SWITCH FUNCTION FOR COMMANDS

    def functionSwitch(self, file):

        if os.stat("binary.txt").st_size != 0:
            open('1address.txt', 'w').close()

        self.conversieBinar()
        cmdFile = open("1address.txt", "r")

        # GET LINE
        for line in cmdFile:

            if line == '\n':
                self.ProgramCounter += 1
                continue

            elif line[0] == ' ' or line[0] == '\t':

                for index in range(0,len(line) - 1):
                    if(line[index] != ' ' and line[index] != '\t'):
                        self.InstructionRegister = line[index]
                        self.fault()
                self.ProgramCounter += 1
                continue

            elif line[0].isalpha() == False:
                self.InstructionRegister = line[0]
                self.fault()
            else:

                # SPLIT THE LINE IN COMMAND + VALUE / REGISTER
                functName = line.split()
                self.InstructionRegister = functName[0]

                # ================= ERRORS =================

                if len(functName) > 2:
                    self.fault()
                    self.exit()

                elif self.STATUS == False:
                    self.exit()

                elif self.OVERFLOW == True:
                    self.exit()

                elif self.UNDERFLOW == True:
                    self.exit()


                # ===========================================

                # ============= ALL FUNCTIONS ===============

                elif functName[0].isdigit() == False and len(functName) == 2:

                    if functName[0] == 'LOAD':
                        valoare = functName[1]
                        self.loadNumber(valoare)

                    elif functName[0] == 'ADD':
                        valoare = functName[1]
                        self.addNumber(valoare)

                    elif (functName[0] == 'SUB'):
                        valoare = functName[1]
                        self.subNumber(valoare)

                    elif functName[0] == 'MUL':
                        valoare = functName[1]
                        self.mulNumber(valoare)

                    elif functName[0] == 'INC':
                        valoare = functName[1]
                        self.incNumber(valoare)

                    elif functName[0] == 'DEC':
                        valoare = functName[1]
                        self.decNumber(valoare)

                    elif functName[0] == 'OPP':
                        valoare = functName[1]
                        self.oppNumber(valoare)

                    elif functName[0] == 'STORE':
                        valoare = functName[1]
                        self.storeNumber(valoare)

                    elif functName[0] == 'OUT':
                        valoare = functName[1]
                        self.outNumber(valoare)

                    elif functName[0] == 'SWAP':
                        valoare = functName[1]
                        self.swapNumbers(valoare)

                    elif functName[0] == 'DIV':
                        valoare = functName[1]
                        self.divNumber(valoare)

                    elif functName[0] == 'HELP':
                        self.help()

                    elif functName[0] == 'CLR':
                        valoare = functName[1]
                        self.clear(valoare)
                    else:
                        self.fault()
                else:
                    self.fault()

    # ==============================================

    # FOR ANY ERROR

    # PROGRAM STATUS
    def fault(self):

        self.STATUS = False
        print(Fore.GREEN + Back.RESET + "Error, Wrong instruction at line ", self.ProgramCounter, "!\n")
        self.BlueScreen()

    # PRINT ALL DETAILS FOR THE ERROR

    def BlueScreen(self):
        print(Fore.GREEN + "CPU REGISTERS: \n")
        print(Fore.BLUE + "Result Register [", self.Result, "]\n")
        print(Fore.RED + "AC Register [", self.AC, "]\n")
        print(Fore.YELLOW + "Temporar Register [", self.Temp, "]\n")
        print(Fore.CYAN + "Status [", self.STATUS, "]\n")
        print(Fore.MAGENTA + "Overflow [", self.OVERFLOW, "]\n")
        print(Fore.MAGENTA + "Underflow [", self.UNDERFLOW, "]\n")
        print(Fore.RED + Back.WHITE + "Program Counter [", self.ProgramCounter, "]\n")
        print(Fore.RED + Back.WHITE + "Instruction Register [", self.InstructionRegister, "]\n")


    def conversieBinar(self):

        contorBinar = 1
        file = open("binary.txt", "r")
        f = open("1address.txt", "a")

        for line in file:
            if line == '\n':
                contorBinar += 1
                continue

            elif len(line) > 16:
                print(Fore.RED + Back.WHITE + "Error binary code, line: ", contorBinar, "\n")
                self.exit()

            else:
                #ERROR 0/1 IN BINARY FILE LINE
                for x in range(1, 15):
                    if line[x] != '1' and line[x] != '0':
                        print(Fore.RED + Back.WHITE + "Error binary code, line: ", contorBinar, "\n")
                        self.exit()

                binar = line

                if binar[:4] == '0001':  # load
                    f.write("LOAD ")

                elif binar[:4] == '0011':  # add
                    f.write("ADD ")

                elif binar[:4] == '0100':  # sub
                    f.write("SUB ")

                elif binar[:4] == '0101':  # mul
                    f.write("MUL ")

                elif binar[:4] == '0111':  # inc
                    f.write("INC ")

                elif binar[:4] == '1000':  # dec
                    f.write("DEC ")

                elif binar[:4] == '1100':  # opp
                    f.write("OPP ")

                elif binar[:4] == '0010':  # store
                    f.write("STORE ")

                elif binar[:4] == '0000':  # out
                    f.write("OUT ")

                elif binar[:4] == '1110':  # swap
                    f.write("SWAP ")

                elif binar[:4] == '0110':  # div
                    f.write("DIV ")

                elif binar[:4] == '1111':  # help
                    f.write("HELP ")

                elif binar[:4] == '1001':  # clr
                    f.write("CLR ")

                value = binar[12:]

                if value == '001\n' or value == '001':
                    f.write("AC\n")

                elif value == '010\n' or value == '010':
                    f.write("REZ\n")

                elif value == '100\n' or value == '100':
                    f.write("T\n")

                elif value == '111\n' or value == '111':
                    f.write("ALL\n")

                else:
                    number = int(binar[4:-4], 2)
                    f.write(str(number) + "\n")

            lastLine = line
            contorBinar += 1



        f.close()

    # =================================================

"""registrii = cpu()
fileText = open("binary.txt", "r")
registrii.functionSwitch(fileText)

print(Fore.GREEN + Back.RESET + "Press ENTER to exit the program...")

"""

# ==================================================
