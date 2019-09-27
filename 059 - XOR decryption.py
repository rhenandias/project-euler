# -*- coding: utf-8 -*-
#Problem 059 - XOR decryption
import itertools as it

alphabet = "abcdefghijklmnopqrstuvwxyz"

data = []
with open("059 - XOR decryption - Data.txt", 'r') as input_file:
    for line in input_file:
        data = [int(i) for i in line.split(',')]
        
keys = ["".join(i) for i in it.product(alphabet, repeat = 3)] 

message = []
for key in keys:
    cur_message = []
    cycle = 0
    for encrypted_char in data:
        decrypted_char = chr(encrypted_char ^ ord(key[cycle]))
        cycle = 0 if cycle == 2 else cycle + 1
        cur_message.append(decrypted_char)
    message.append("".join(cur_message))

for i in message:
    if i.count(" the "):
        message = i

message = [ord(i) for i in message]

print(sum(message))