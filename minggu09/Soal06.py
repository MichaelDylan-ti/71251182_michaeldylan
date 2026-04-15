import re
import random
import string

teks = input("Masukkan teks: ")

pola_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
daftar_email = re.findall(pola_email, teks)

def buat_password():
    karakter = string.ascii_letters + string.digits
    return ''.join(random.choice(karakter) for _ in range(8))

for email in daftar_email:
    username = email.split("@")[0]
    password = buat_password()
    print(f"{email} username: {username} , password: {password}")