# OneAddressMachine
 
Simulates an machine with one address instructions.

Such instruction format has a single explicit address field and uses an implied accumulator (AC) register for all data manipulation.

![GUI](/preview/example.png)


### Important
* max value for any register is limited to -255 ~ 255;
* all address machine commands will be written in binary code in "binary.txt" file and converted to address machine commands in "1address.txt" file;
* the application can run also the address machine commands from "1address.txt" file;
* for any errors in "1address.txt" file, the program will receive a "bluescreen" (log with details about the error);
* for any errors in "binary.txt" file, the program will print the line with that error;
* "binary.txt" file must end with a blank line.

### List of commands

* ac - accumulator register (for operations)
* rez - result register (to store the result)
* t - temporal register (to store temporary value)

* out(ac/rez/t/all) - print all register on screen
* load(number) - write value in ac register
* store(register) - store value in a register (t, rez, ac)
* add(registers/numbers) - add a number to register ac
* sub(registers/numbers) - subtract a value from register ac
* mul(registers/numbers) - multiple register ac with a value
* div(registers/numbers) - divide register ac with a value
* inc(register) - increment a register
* dec(register) - decrement a register
* clr(register) - clear a register
* opp(register) - opposite the value of a register
* swap(register) - swap value of temporary registers and accumulator registers

### List of binary commands

* the size of binary line must be 15 bits split in: (oppr/bbbbbbbb/reg)
* convention 1 - if the function doesn't use a number, the space allocated for 'bbbbbbbb' must be filled with 0s
* convention 2 - if the function doesn't use a register, the space allocated for 'reg'must be filled with 0s

(oppr/bbbbbbbb/reg)
oppr - 4 bits for operations
b - 8 bits for number in base 2
reg - 3 bits for register



