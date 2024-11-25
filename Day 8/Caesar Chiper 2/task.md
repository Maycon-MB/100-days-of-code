TODO-1:
Create a function called decrypt() that takes original_text and shift_amount as 2 inputs.

TODO-2:
Inside the decrypt() function, shift each letter of the original_text forwards in the alphabet backwards by the shift_amount and print the decrypted text.

 Hint 1 
You can multiply any number by -1 to make it a negative number.
TODO-3:
Combine the encrypt() and decrypt() functions into a single function called caesar().
Use the value of the user chosen direction variable to determine which functionality to use.
call the caesar function instead of encrypt/decrypt and pass in all three variables direction/text/shift.
 Hint 2 
Remember that when you multiply a number by -1 it will reverse its sign. e.g. 3 + ( 5 * -1) is the same as 3 - 5.
 Hint 3 
It should say:
Here is the encoded result: XXX

or

Here is the decoded result: XXX