import os
import pyaes

## Abre o arquivo Criptografado

file_name = "junior.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Insere a chave para descriptografar

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Remove o arquivo criptografado

os.remove(file_name)

## Cria o novo arquivo descriptografado

new_file = "junior.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
