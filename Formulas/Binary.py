#Binary conversions
def bin_dec():
    bina=(input(Fore.GREEN+"Give a binary value:"))
    dec=int(bina,2)
    print(dec)
def dec_bin():
    dec=int(input(Fore.GREEN+"Give a decimical value:"))
    bina=bin(dec)[2:]
    print(bina)
def dec_hex():
    dec=int(input(Fore.GREEN+"Give a decimical value:"))
    hexa=hex(dec)[2:]
    print(hexa)
def bin_hex():
    bina=(input(Fore.GREEN+"Give a binary value:"))
    hexa=hex(int(bina,2))[2:]
    print(hexa)
def hex_dec():
    hexa=(input(Fore.GREEN+"Give a hexadecimal value:"))
    dec=int(hexa,16)
    print(dec)
def hex_bin():
    hexa=int((input(Fore.GREEN+"Give a hexadecimal value:")),16)
    bina=bin(hexa)[2:]
    print(bina)
