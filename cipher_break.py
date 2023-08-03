import string
from textwrap import wrap

array_len = 6

def calc_fibonacci_key(key):
    next_key = []
    for i in range(0, len(key)-1):
        next_key.append((key[i] + key[i+1])%10)
    next_key.append((key[-1] + key[0])%10)
    return next_key

def create_fibonacci_subkeys(key, n):
    subkeys = []
    prev_key = key
    for _ in range(0, n):
        curr_key = calc_fibonacci_key(prev_key)
        prev_key = curr_key
        subkeys.append(curr_key)
    return subkeys
        
key = [5,2,1,4,3,6]
subkeys = create_fibonacci_subkeys(key, 3)

def print_array(arr):
    for row in arr:
        print(row)
        
def shift_row_by(arr, row, shift):
    l = len(arr[0])
    mod_shift = l - shift%l
    arr[row] = arr[row][mod_shift:] + arr[row][:mod_shift]
    return arr
    
def shift_col_by(arr, col, shift):
    total_rows = len(arr)
    new_arr = [row[:] for row in arr]
    for i, row in enumerate(arr):
        next_row = (i+shift)%total_rows
        new_arr[next_row][col] = row[col]
    return new_arr

alpha_nums = list(string.ascii_uppercase) + list(range(10))
def shift_col_chars_by(arr, col, shift):
    new_arr = [row[:] for row in arr]
    for row in new_arr:
        row[col] = alpha_nums[(alpha_nums.index(row[col]) + shift)%36]
    return new_arr

plaintext = "THIS IS A SECRET MESSAGE THAT WE NEED TO HIDE"
print("Plaintext: " + plaintext)
plaintext = plaintext.replace(" ", "")

print("Subkeys:")
print_array(subkeys)

print("Plaintext arr:")
plaintext_arr = []
for idx, string in enumerate(wrap(plaintext, array_len)):
    plaintext_arr.append(list(string))

print_array(plaintext_arr)
ciphertext = [row[:] for row in plaintext_arr]

for i in range(0, len(ciphertext[0])):
    ciphertext = shift_col_by(ciphertext, i, subkeys[0][i])

for i in range(0, len(ciphertext)):
    ciphertext = shift_row_by(ciphertext, i, subkeys[1][i])

print("Array after encryption:")
for i in range(0, len(ciphertext)):
    ciphertext = shift_col_chars_by(ciphertext, i, subkeys[2][i])
print_array(ciphertext)

def decrypt(ciphertext, key):
    subkeys = create_fibonacci_subkeys(key, 3)
    for i in range(0, len(ciphertext)):
        ciphertext = shift_col_chars_by(ciphertext, i, -subkeys[2][i])
    for i in range(0, len(ciphertext)):
        ciphertext = shift_row_by(ciphertext, i, -subkeys[1][i])
    for i in range(0, len(ciphertext[0])):
        ciphertext = shift_col_by(ciphertext, i, -subkeys[0][i])
    return ciphertext

def inc_key(key, idx):
    key[idx] += 1
    if((key[idx]) == 10):
        key[idx] = 0
        if(idx != 0):
            inc_key(key, idx - 1)
    return key

test_key = [0] * 6

for i in range(0, 1000000):
    print(test_key)
    result = decrypt(ciphertext, test_key)
    if(plaintext_arr == result):
        print("SUCCESS!")
        print_array(result)
        print("Key:")
        print(test_key)
        exit()
    test_key = inc_key(test_key, len(test_key) - 1)