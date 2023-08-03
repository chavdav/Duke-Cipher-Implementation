`cipher.py` implements one of the example ciphers taught as part of Duke's Pre-College ["Exploring Cryptography Through Gamified Programming"](https://learnmore.duke.edu/program/exploring-cryptography-through-gamified-programming) course.

`cipher_break.py` demonstrates a simple brute-force attack against the cipher, and succeeds in a matter of seconds on a standard laptop machine.

`cipher_break2.py` illustrates the importance of key length, as a brute-force attack against the same cipher using a key that's triple the original length would take over 100 years.
