def kmh_mph():
    kmh = (float(input(Fore.GREEN+"Give kmh value: ")))
    mph = kmh/1.60934
    print(mph, "Mp/h")


def mph_kmh():
    mph = (float(input(Fore.GREEN+"Give mph value: ")))
    kmh = mph*1.60934
    print(kmh, "Kmph")


def kmh_ma():
    kmh = (float(input(Fore.GREEN+"Give kmh value: ")))
    mach = kmh/1225.08
    print(mach, "Mach")


def ma_kmh():
    macht = (float(input(Fore.GREEN+"Give macht value: ")))
    kmh = macht*1225.08
    print(kmh, "Kmh")


def mph_ma():
    mph = (float(input(Fore.GREEN+"Give mph value: ")))
    macht = mph*0.001303
    print(macht, "Macht")


def ma_mph():
    macht = (float(input(Fore.GREEN+"Give macht value: ")))
    mph = macht/0.001303
    print(mph, "Mph")


def kmh_kn():
    kmh = (float(input(Fore.GREEN+"Give kmh value: ")))
    kn = kmh*0.539957
    print(kn, "Knots")


def kn_kmh():
    kn = (float(input(Fore.GREEN+"Give knot value: ")))
    kmh = kn/0.539957
    print(kmh, "Kmph")


def mph_kn():
    mph = (float(input(Fore.GREEN+"Give mph value: ")))
    kn = mph*0.868976
    print(kn, "Knots")


def kn_mph():
    kn = (float(input(Fore.GREEN+"Give knot value: ")))
    mph = kn/0.868976
    print(mph, "Mph")


def ma_kn():
    macht = (float(input(Fore.GREEN+"Give macht value: ")))
    kn = macht*661.490281
    print(kn, "Knots")


def kn_ma():
    kn = (float(input(Fore.GREEN+"Give knot value: ")))
    ma = kn/661.490281
    print(ma, "Macht")


def kmh_c():
    kmh = (float(input(Fore.GREEN+"Give kmh value: ")))
    c = kmh/(107925285*10**9)
    print(c, "Speed of light")


def c_kmh():
    c = (float(input(Fore.GREEN+"Give speed of light value: ")))
    kmh = c*1079252848.8 
    print(kmh, "Kmh")


def mph_c():
    mph = (float(input(Fore.GREEN+"Give mph value: ")))
    c = mph/670616629
    print(c, "Speed of light")


def c_mph():
    c = (float(input(Fore.GREEN+"Give speed of light value: ")))
    mph = c*670616629
    print(mph, "Mph")


def ma_c():
    ma = (float(input(Fore.GREEN+"Give macht value: ")))
    c = ma/874030
    print(c, "Speed of light")


def c_macht():
    c = (float(input(Fore.GREEN+"Give speed of light value: ")))
    macht = c*874030
    print(macht, "Macht")


def kn_c():
    kn = (float(input(Fore.GREEN+"Give knot value: ")))
    c = kn/58249918
    print(c, "Speed of light")


def c_kn():
    c = (float(input(Fore.GREEN+"Give speed of light value: ")))
    kn = c*58249918
    print(kn, "Knots")
