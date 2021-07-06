import main
import os
from tkinter import *
import tkinter as tk


#=============###################################DECLARAT

screen = Tk()
screen.title("1 ADDRESS MACHINE")
screen.minsize(1320, 720)
screen.resizable(False, False)
screen.iconbitmap('./sheets/icon.ico')
screen.configure(background = '#404040')


################################################VARIABILE

v_f = tk.IntVar()
entry_text_1 = tk.StringVar()
entry_text_2 = tk.StringVar()
entry_text_3 = tk.StringVar()

##################################################FUNCTII


#INCHIDE FIS ADS && LOG && OUT


def ads_log_out_close():
    ads_code.delete("1.0", END)
    log.delete("1.0", END)
    open('1address.txt', 'w').close()
    open('binary.txt', 'w').close()
    open('OUTPUT.txt', 'w').close()

#OBIECT MAIN CPU CPU


def reg_main_cpu():
    registrii = main.cpu.cpu()
    fileText = open("binary.txt", "r")
    registrii.functionSwitch(fileText)


#SCRIE IN ADS CODUL


def write_ads():
    outfile_a = open('1address.txt', 'r')
    ads_code.insert("1.0", outfile_a.read())


#SCRIE IN LOG - OUTPUT


def write_log():
    outfile_o = open('OUTPUT.txt', 'r')
    log.insert("1.0", outfile_o.read())


#SCRIE CODUL


def write_file():
    ads_log_out_close()

    outfile_b = open('binary.txt', 'w')
    outfile_a = open('1address.txt', 'w')

    text_entry = entry_code.get('1.0', END)

    Status = True
    StatusB = True
    contor_linii = 1

    if(len(text_entry) <= 15):
        StatusB = False

    else:
        contor = 0
        for index in range(len(text_entry) - 1):
            contor += 1
            if text_entry[index] != '1' and text_entry[index] != '0' and text_entry[index] != '\n':
                StatusB = False
                break

            if contor == 16:
                contor_linii += 1
                contor = 0


    if StatusB == True:
        outfile_b.write(text_entry)
        outfile_b.close()

    elif text_entry[0].isalpha():
        outfile_a.write(text_entry)
        outfile_a.close()

    else:
        with open("OUTPUT.txt", 'w') as text_file:
            if len(text_entry) > 1:
                print(f"Error, Wrong input on line " + str(contor_linii) + "\n", file = text_file)
        Status = False

    if Status == True or StatusB == True:
        reg_main_cpu()

    write_ads()

    write_log()


def case_functions(obt):
    ads_log_out_close()

    x = entry_x.get()
    y = entry_y.get()
    z = entry_z.get()

    if x.isdigit() != True and y.isdigit() != True and z[1:].isdigit() != True and z[0].isdigit() != True:
        with open("OUTPUT.txt", 'w') as text_file:
            print(f"Error, Wrong input!\n", file = text_file)
    else:
        if obt == 0:
            main.cmmdc(x,y)
        elif obt == 1:
            main.cmmmc(x,y)
        elif obt == 2:
            main.ec2(x,y,z)
        elif obt == 3:
            main.prim(z)
        elif obt == 4:
            main.gauss(z)

    reg_main_cpu()

    write_ads()

    write_log()


########################################################LABEL-URI

logo_img = PhotoImage(file = "./sheets/333333.png")

label_1 = Label(screen ,bg = "#404040",  text = "LOGO1")
label_1.grid(row = 0, column = 0, padx = 8, pady = 10, sticky = N )
label_1.config(image = logo_img)


###########################################################BUTOANE


#START BUTTON

start_functions = PhotoImage(file = "./sheets/2.png")

start_button = Button(screen, text = "START", command = write_file, bg = '#c5c7c9')
start_button.grid(row = 2, column = 1, pady = 15, sticky = S)
start_button.config(image = start_functions, borderwidth = 0, relief = 'flat')

#FUNCTION BUTTON

img_functions = PhotoImage(file = "./sheets/1.png")

function_button = Menubutton(screen, text = "FUNCTIONS", bg = '#c5c7c9')
function_button.grid(row = 0, column = 1)
menu_function = Menu(function_button, tearoff=False)
function_button.configure(menu = menu_function)
function_button.config(image = img_functions, highlightbackground = '#33363a')



#INTRARE STANGA

entry_code = tk.StringVar()



entry_code = Text(screen, width = 50, height = 32, bg = '#33363a', fg = 'white')
entry_code.insert('1.0', "Type here `HELP ME` and press the start button for  more information!")
entry_code.grid(row = 1, column = 0, padx = 16)


#SCROLLBAR STANGA


scrollbar_ec = Scrollbar(screen, orient = VERTICAL, command = entry_code.yview)
entry_code['yscroll'] = scrollbar_ec.set
scrollbar_ec.grid(row = 1, column = 0, sticky = N+E+S)


#ADRESA MIJLOC


ads_code = Text(screen, width = 50, height = 32, bg = '#33363a', fg = 'white')
ads_code.grid(row = 1, column = 1, padx = 16)


#SCROLL MIJLOC


scrollbar_ads = Scrollbar(screen ,orient = VERTICAL, command = ads_code.yview)
ads_code['yscroll'] = scrollbar_ads.set
scrollbar_ads.grid(row = 1, column = 1, sticky = N+E+S)


#LOG DREAPTA


log = Text(screen, width = 50, height = 32,bg = '#33363a', fg = 'white')
log.grid(row = 1, column = 2, padx = 16)


#SCROLL DREAPTA


scrollbar_log = Scrollbar(screen ,orient = VERTICAL, command = log.yview)
log['yscroll'] = scrollbar_log.set
scrollbar_log.grid(row = 1, column = 2, sticky = N+E+S)


#ENTRY BUTTON


entry_x = Entry(screen, textvariable = entry_text_1, bg = '#33363a', fg = 'white')                #X\A
entry_text_1.set("X \ A")
entry_x.grid(row = 0, column = 1, sticky = W, ipady = 5)

entry_y = Entry(screen, textvariable = entry_text_2, bg = '#33363a', fg = 'white')                #Y\B
entry_text_2.set("Y \ B")
entry_y.grid(row = 0, column = 1, sticky = E, ipady = 5)

entry_z = Entry(screen, textvariable = entry_text_3, bg = '#33363a', fg = 'white')                #C\PRIME\GAUSS
entry_text_3.set("C \ PRIME \ GAUSS")
entry_z.grid(row = 0, column = 1, sticky = S, pady = 10, ipady = 5)


#######################################################MENIU FUNCTII


menu_function.add_radiobutton(variable = v_f, background = '#33363a', foreground = 'white', label ="CMMDC (X,Y)", command = lambda: case_functions(0))
menu_function.add_radiobutton(variable = v_f, background = '#33363a', foreground = 'white', label ="CMMMC (X,Y)", command = lambda: case_functions(1))
menu_function.add_radiobutton(variable = v_f, background = '#33363a', foreground = 'white', label ="EC2 (A,B,C)", command = lambda: case_functions(2))
menu_function.add_radiobutton(variable = v_f, background = '#33363a', foreground = 'white', label ="PRIME (C)", command = lambda: case_functions(3))
menu_function.add_radiobutton(variable = v_f, background = '#33363a', foreground = 'white', label ="GAUSS (C)", command = lambda: case_functions(4))


tk.mainloop()

if os.stat("1address.txt").st_size != 0:
    open('1address.txt', 'w').close()

if os.stat("binary.txt").st_size != 0:
    open('binary.txt', 'w').close()
