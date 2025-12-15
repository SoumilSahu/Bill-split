---------------------------
Soumil Sahu @ 2025
---------------------------

.....................................................
How to write transactions into the values.dat file:
.....................................................

The file will be read as space separated values (' ')

The first line should be of the form, 

    Type Payer Amount Person1 Person2 Person3 

Thereon each line should be a transaction of the form,

    Cab Person1 500 100 200 200

The "Amount" is paid by the "Payer", and under the column of the 
payer his/her part has to be written. As in the example P1 paid 500, but
his/her own share is 100 so that is separately entered. Multiple payers 
for a single transaction can also be added by comma separation, and their 
corresponding amounts should also be comma separated in the same order.

Each line need to end with a space ' '. It is important otherwise '\n' 
won't be space separated from the last entry of the line.

If a transaction has equal division among some of people it can be 
written as,

    Clothes Person3 900 e e 0

This means amount for 'Clothes' was paid by Person3 and is equally owed 
by Person1 and Person2.

An example entry to values.dat file,

Type Payer Amt P1 P2 P3 P4 
Cab P1 500 100 100 100 200 
Food P2,P4 300,400 200 400 50 50 
Clothes P4 900 e e e 0 

Note: Spelling of names should be consistent, and take care of the order 
in which owed amounts are entered. 

.....................................................
How to use the code:
.....................................................

In the running directory make a file of name "file_name.dat" and enter the 
transaction values according to the prescription mentioned above.

Open a python terminal, and import the function split from module bill_split:

    >> from bill_split import split

Now run the following line:

    >> split("file_name.dat")

.....................................................
Additional notes:
.....................................................
The round off multiple of 0.01 rupees error:
The code rounds off to nearest second deimal place upon taking into
account equal split values. As a result often the actual total cost
of that transaction differs the total recorded values by +/- some multiple
of 0.01 . This balance value is randomly added/subtracted to one of 
the person involved in the transaction :) called the 'bakra'.