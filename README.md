# KEY-TRANSPOSITION-CIPHER-cryptography-


Key Transposition Cipher
The Key Transposition Cipher is a simple encryption technique that involves rearranging the characters of a message according to a provided key. This cipher provides a way to scramble the message
making it difficult to understand without the corresponding key for decryption.

How it Works
Encryption:
Start with a plain text message that you want to encrypt.
Choose a key, which is a sequence of characters that will determine the transposition pattern.
Write the plain text message row by row into a grid, following the length of the key.
Order the columns of the grid based on the numerical order of characters in the key.
Read the encrypted message from the transposed columns of the grid.


Decryption:
Start with an encrypted message that you want to decrypt.
Obtain the key that was used for encryption.
Determine the number of rows needed in the grid based on the length of the key.
Create an empty grid with the determined number of rows and the same number of columns as the key length.
Fill the grid by writing down the encrypted message row by row.
Order the columns of the grid based on the numerical order of characters in the key.
Read the decrypted message from the original order of the columns in the grid.

NOTE:-
     The "z" in this application is used to fill the empty spaces in the last row of two dimensition arryay so that no spaces are seen in cipher text.The character Z is removed later while decrypting
