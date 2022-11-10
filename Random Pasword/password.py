import string, secrets

chrs40 = string.ascii_letters + "0123456789" #Şifre40
numbers40 = string.digits + string.ascii_letters + "0123456789"

chrs30 =  string.digits + string.punctuation #Şifre30
numbers30 = string.digits + string.punctuation

chrs20 = string.ascii_letters + string.digits + string.punctuation +  "0123456789" #Şifre20
numbers20 = string.digits + string.ascii_letters + string.punctuation + "0123456789"

chrs10 = "0123456789" #Şifre10
numbers10 = string.digits + "0123456789"

Uzunluk = input(" Şifreni Seç / Pin Seç: ")

Şifre40_in_chrs40 = "".join(secrets.choice(chrs40) for i in range(int(12)))
Şifre40_in_numbers40 = "".join(secrets.choice(numbers40) for i in range(int(12)))

Şifre30_in_chrs30 = "".join(secrets.choice(numbers30) for i in range(int(12)))
Şifre30_in_number30 = "".join(secrets.choice(numbers30) for i in range(int(12)))

Şifre20_in_chrs20 = "".join(secrets.choice(chrs20) for i in range(int(12)))
Şifre20_in_number20 = "".join(secrets.choice(numbers20) for i in range(int(12)))

Şifre10_in_chrs10 = "".join(secrets.choice(chrs10) for i in range(int(12)))
Şifre10_in_number10 = "".join(secrets.choice(numbers10) for i in range(int(12)))

seç = input(  "Şifre mi / Pin mi?:  ")

print("*******************DEOMS Dıgıtal Company1 Şifre Oluşturucu*******************")

if seç == "Şifre":
    print(Şifre10_in_chrs10)

if seç == "Pin":
        print(Şifre10_in_number10)

if seç == "Şifre":
    print(Şifre20_in_chrs20)

if seç == "Pin":
    print(Şifre20_in_number20)

if seç == "Şifre":
    print(Şifre30_in_chrs30)

if seç == "Pin":
    print(Şifre30_in_number30)

if seç == "Şifre":
    print(Şifre40_in_chrs40)

if seç == "Pin":
    print(Şifre40_in_numbers40)


print("**************Şifre/Pin oluşturucu**************")

print( Şifre10_in_chrs10 )
print( Şifre10_in_number10 )
print( Şifre20_in_chrs20 )
print( Şifre20_in_number20 )
print( Şifre30_in_chrs30 )
print( Şifre30_in_number30 )
print( Şifre40_in_chrs40 )
print( Şifre40_in_numbers40 )



