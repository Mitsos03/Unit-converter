import colorama
from colorama import Fore, Style
# Temperature functions


def celsius_fahrenheit():
    celsius = float(input(Fore.GREEN+"Give celsius value: "))
    fahrenheit = 1.8*celsius+32
    print(Fore.GREEN, fahrenheit, "fahrenheit")


def fahrenheit_celsius():
    fahrenheit = float(input(Fore.GREEN+"Give fahrenheit value: "))
    celsius = (fahrenheit-32)*5556
    print(Fore.GREEN, celsius, "celsius ")


def celsius_kelvin():
    celsius = float(input(Fore.GREEN+"Give celsius value: "))
    kelvin = celsius + 273.15
    print(Fore.GREEN, kelvin, "kelvin")


def kelvin_celsius():
    kelvin = float(input(Fore.GREEN+"Give kelvin value: "))
    celsius = kelvin - 273.15
    print(Fore.GREEN, celsius, "celsius")


def fahrenheit_kelvin():
    fahrenheit = float(input(Fore.GREEN+"Give fahrenheit value: "))
    kelvin = ((fahrenheit-32)*5)/9+273.15
    print(Fore.GREEN, kelvin, "kelvin")


def kelvin_fahrenheit():
     kelvin = float(input(Fore.GREEN+"Give kelvin value: "))
     fahrenheit=(kelvin-273.15)*1.8+32
     print(fahrenheit,"fahrenheit")
# Data functions


def bytes_kb():
    byte = (float(input(Fore.GREEN+"Give byte value: ")))
    kb = byte/2**10
    print(Fore.GREEN, kb, "Kb")


def kb_bytes():
    kb = float(input(Fore.GREEN+"Give kb value: "))
    bytes = kb*2**10
    print(Fore.GREEN, bytes, "bytes")


def bytes_mb():
    bytes = float(input(Fore.GREEN+"Give byte value: "))
    mb = bytes/2**20
    print(mb, "MB")


def mb_bytes():
    mb = float(input(Fore.GREEN+"Give mb value: "))
    byte = mb*2**20
    print(byte, "bytes")


def kb_mb():
    kb = float(input(Fore.GREEN+"Give kb value: "))
    mb = kb/2**10
    print(mb, "MB")


def mb_kb():
    mb = float(input(Fore.GREEN+"Give mb value: "))
    kb = mb*2**10
    print(kb, "KB")


def byte_gb():
    byte = (float(input(Fore.GREEN+"Give byte value: ")))
    gb = byte/2**30
    print(gb, "GB")


def gb_byte():
    gb = (float(input(Fore.GREEN+"Give gb value: ")))
    byte = gb*2**30
    print(byte, "bytes")


def kb_gb():
    kb = (float(input(Fore.GREEN+"Give kb value: ")))
    gb = kb/2**20
    print(gb, "Gb")


def gb_kb():
    gb = (float(input(Fore.GREEN+"Give gb value: ")))
    kb = gb*2**20
    print(kb, "Kb")


def mb_gb():
    mb = (float(input(Fore.GREEN+"Give mb value: ")))
    gb = mb/2**10
    print(gb, "Gb")


def gb_mb():
    gb = (float(input(Fore.GREEN+"Give gb value: ")))
    mb = gb*2**10
    print(mb, "Mb")


def byte_tb():
    byte = (float(input(Fore.GREEN+"Give byte value: ")))
    tb = byte/2**40
    print(tb, "Tb")


def tb_byte():
    tb = (float(input(Fore.GREEN+"Give tb value: ")))
    byte = tb*2**40
    print(byte, "Byte")


def kb_tb():
    kb = (float(input(Fore.GREEN+"Give kb value: ")))
    tb = kb/2**30
    print(tb, "Tb")


def tb_kb():
    tb = (float(input(Fore.GREEN+"Give tb value: ")))
    kb = tb*2**30
    print(kb, "Kb")


def mb_tb():
    mb = (float(input(Fore.GREEN+"Give mb value: ")))
    tb = mb/2**20
    print(tb, "Tb")


def tb_mb():
    tb = (float(input(Fore.GREEN+"Give tb value: ")))
    mb = tb*2**20
    print(mb, "Mb")


def gb_tb():
    gb = (float(input(Fore.GREEN+"Give gb value: ")))
    tb = gb/2**10
    print(tb, "Tb")


def tb_gb():
    tb = (float(input(Fore.GREEN+"Give tb value: ")))
    gb = tb*2**10
    print(gb, "Gb")
# Time Functions


def sec_minutes():
    sec = (int(input(Fore.GREEN+"Give sec value: ")))
    minutes = sec/60
    print(minutes, "Minutes")


def minutes_sec():
    minutes = (int(input(Fore.GREEN+"Give min value: ")))
    sec = minutes*60
    print(sec, "secs")


def sec_hour():
    sec = (int(input(Fore.GREEN+"Give sec value: ")))
    hour = sec/3600
    print(hour, "Hours")


def hour_sec():
    hour = (int(input(Fore.GREEN+"Give hour value: ")))
    sec = hour*3600
    print(sec, "secs")


def minutes_hour():
    minutes = (int(input(Fore.GREEN+"Give min value: ")))
    hour = minutes/60
    print(hour, "Hours")


def hour_minutes():
    hour = (int(input(Fore.GREEN+"Give hour value: ")))
    minutes = hour*60
    print(minutes, "Minutes")


def sec_day():
    sec = (int(input(Fore.GREEN+"Give sec value: ")))
    day = sec/86400
    print(day, "Days")


def day_sec():
    day = (int(input(Fore.GREEN+"Give day value: ")))
    sec = day*86400
    print(sec, "Secs")


def minutes_day():
    minutes = (int(input(Fore.GREEN+"Give min value: ")))
    day = minutes/1440
    print(day, "Day")


def day_minutes():
    day = (int(input(Fore.GREEN+"Give day value: ")))
    minutes = day*1440
    print(minutes , "Minutes")


def hour_day():
    hour = (int(input(Fore.GREEN+"Give hour value: ")))
    day = hour/24
    print(day, "Days")


def day_hour():
    day = (int(input(Fore.GREEN+"Give day value: ")))
    hour = day*24
    print(hour, "Hours")


def sec_week():
    sec = (int(input(Fore.GREEN+"Give sec value: ")))
    week = sec/604800
    print(week, "Weeks")


def week_sec():
    week = (int(input(Fore.GREEN+"Give week value: ")))
    sec = week*604800
    print(sec, "Sec")


def minute_week():
    minute = (int(input(Fore.GREEN+"Give min value: ")))
    week = minute*9.92063492*10**-5
    print(week, "Weeks")


def week_minute():
    week = (int(input(Fore.GREEN+"Give week value: ")))
    minute = week*1080
    print(minute, "Minutes")


def hour_week():
    hour = (int(input(Fore.GREEN+"Give hour value: ")))
    week = hour*0.00595238095
    print(week , "Weeks")


def week_hour():
    week = (int(input(Fore.GREEN+"Give week value: ")))
    hour = week/0.00595238095
    print(hour, "Hours")


def day_week():
    day = (int(input(Fore.GREEN+"Give day value: ")))
    week = day/7
    print(week, "Weeks")


def week_day():
    week = (int(input(Fore.GREEN+"Give week value: ")))
    day = week*7
    print(day, "Days")


def sec_year():
    sec = (int(input(Fore.GREEN+"Give sec value: ")))
    year = sec/31536000
    print(year, "Years")


def year_sec():
    year = (int(input(Fore.GREEN+"Give year value: ")))
    sec = year*31536000
    print(sec, "Sec")


def minute_year():
    minute = (int(input(Fore.GREEN+"Give min value: ")))
    year = minute*1.90132588*10**-6
    print(year, "Years")


def year_minute():
    year = (int(input(Fore.GREEN+"Give year value: ")))
    minute = year*525600
    print(minute, "Minutes")


def hour_year():
    hour = (int(input(Fore.GREEN+"Give hour value: ")))
    year = hour/8760
    print(year, "Years")


def year_hour():
    year = (int(input(Fore.GREEN+"Give year value: ")))
    hour = year*8760
    print(hour, "Hours")


def day_year():
    day = (int(input(Fore.GREEN+"Give day value: ")))
    year = day/365
    print(year, "Years")


def year_day():
    year = (int(input(Fore.GREEN+"Give year value: ")))
    day = year*365
    print(day, "Days")


def week_year():
    week = (int(input(Fore.GREEN+"Give week value: ")))
    year = week/52
    print(year, "Years")


def year_week():
    year = (int(input(Fore.GREEN+"Give year value: ")))
    week = year*52
    print(week, "Weeks")
# Distance functions


def mili_cm():
    mili = (float(input(Fore.GREEN+"Give mm value: ")))
    cm = mili/10
    print(cm, "Cm")


def cm_mili():
    cm = (float(input(Fore.GREEN+"Give cm value: ")))
    mili = cm*10
    print(mili, "Mm")


def mili_meter():
    mili = (float(input(Fore.GREEN+"Give mm value: ")))
    metre = mili/1000
    print(metre, "M")


def meter_mili():
    metre = (float(input(Fore.GREEN+"Give m value: ")))
    mili = metre*1000
    print(mili, "Mm")


def cm_meter():
    cm = (float(input(Fore.GREEN+"Give cm value: ")))
    metre = cm/100
    print(metre, "M")


def meter_cm():
    metre = (float(input(Fore.GREEN+"Give m value: ")))
    cm = metre*100
    print(cm, "Cm")


def mili_km():
    mili = (float(input(Fore.GREEN+"Give mm value: ")))
    km = mili/100000
    print(km, "Km")


def km_mili():
    km = (float(input(Fore.GREEN+"Give km value: ")))
    mili = km*1000000
    print(mili, "Mm")


def cm_km():
    cm = (float(input(Fore.GREEN+"Give cm value: ")))
    km = cm/100000
    print(km, "Km")


def km_cm():
    km = (float(input(Fore.GREEN+"Give km value: ")))
    cm = km*100000
    print(cm, "Cm")


def metre_km():
    metre = (float(input(Fore.GREEN+"Give m value: ")))
    km = metre/1000
    print(km, "Km")


def km_metre():
    km = (float(input(Fore.GREEN+"Give km value: ")))
    metre = km*1000
    print(metre)


def mili_mile():
    mili = (float(input(Fore.GREEN+"Give mm value: ")))
    mile = mili/1609344
    print(mile, "Miles")


def mile_mili():
    mile = (float(input(Fore.GREEN+"Give mile value: ")))
    mili = mile*1609344
    print(mili, "Mm")


def cm_mile():
    cm = (float(input(Fore.GREEN+"Give cm value: ")))
    mile = cm/160934.4
    print(mile, "Mile")


def mile_cm():
    mile = (float(input(Fore.GREEN+"Give mile value: ")))
    cm = mile*160934.4
    print(cm, "Cm")


def metre_mile():
    metre = (float(input(Fore.GREEN+"Give m value: ")))
    mile = metre/1609.344
    print(mile, "Mile")


def mile_metre():
    mile = (float(input(Fore.GREEN+"Give mile value: ")))
    metre = mile*609.344
    print(metre, "M")


def km_mile():
    km = (float(input(Fore.GREEN+"Give km value: ")))
    mile = km/1.609344
    print(mile, "Mile")


def mile_km():
    mile = (float(input(Fore.GREEN+"Give mile value: ")))
    km = mile*1.609344
    print(km, "Km")


def mili_inch():
    mili = (float(input(Fore.GREEN+"Give mm value: ")))
    inch = mili/25.4
    print(inch, "Inch")


def inch_mili():
    inch = (float(input(Fore.GREEN+"Give inch value: ")))
    mili = inch*25.4
    print(mili, "Mm")


def cm_inch():
    cm = (float(input(Fore.GREEN+"Give cm value: ")))
    inch = cm/2.54
    print(inch, "Inch")


def inch_cm():
    inch = (float(input(Fore.GREEN+"Give inch value: ")))
    cm = inch*2.54
    print(cm, "Cm")


def metre_inch():
    metre = (float(input(Fore.GREEN+"Give m value: ")))
    inch = metre/00.254
    print(inch, "Inch")


def inch_metre():
    inch = (float(input(Fore.GREEN+"Give inch value: ")))
    metre = inch*00.254
    print(metre, "M")


def km_inch():
    km = (float(input(Fore.GREEN+"Give km value: ")))
    inch = km/0.0000254
    print(inch, "Inch")


def inch_km():
    inch = (float(input(Fore.GREEN+"Give inch value: ")))
    km = inch*0.0000254
    print(km, "Km")


def mile_inch():
    mile = (float(input(Fore.GREEN+"Give mile value: ")))
    inch = mile/63360
    print(inch, "Inch")


def inch_mile():
    inch = (float(input(Fore.GREEN+"Give inch value: ")))
    mile = inch*63360
    print(mile, "Mile")


def mili_foot():
    mili = (float(input(Fore.GREEN+"Give mm value: ")))
    foot = mili/304.8
    print(foot, "Foot")


def foot_mili():
    foot = (float(input(Fore.GREEN+"Give foot value: ")))
    mili = foot*304.8
    print(mili, "Mm")


def cm_foot():
    cm = (float(input(Fore.GREEN+"Give cm value: ")))
    foot = cm/30.48
    print(foot, "Foot")


def foot_cm():
    foot = (float(input(Fore.GREEN+"Give foot value: ")))
    cm = foot*30.48
    print(cm, "Cm")


def metre_foot():
    metre = (float(input(Fore.GREEN+"Give m value: ")))
    foot = metre/0.3048
    print(foot, "Foot")


def foot_metre():
    foot = (float(input(Fore.GREEN+"Give foot value: ")))
    metre = foot*0.3048
    print(metre, "M")


def km_foot():
    km = (float(input(Fore.GREEN+"Give km value: ")))
    foot = km/0.0003048
    print(foot, "Foot")


def foot_km():
    foot = (float(input(Fore.GREEN+"Give foot value: ")))
    km = foot*0.0003048
    print(km, "Km")


def inch_foot():
    inch = (float(input(Fore.GREEN+"Give inch value: ")))
    foot = inch/12
    print(foot, "Foot")


def foot_inch():
    foot = (float(input(Fore.GREEN+"Give foot value: ")))
    inch = foot*12
    print(inch, "Inch")


def mile_foot():
    mile = (float(input(Fore.GREEN+"Give mile value: ")))
    foot = mile/0.000189393939
    print(foot, "Foot")


def foot_mile():
    foot = (float(input(Fore.GREEN+"Give foot value: ")))
    mile = foot*0.000189393939
    print(mile, "Mile")
# Velocity Functions


def kmh_mph():
    kmh = (float(input(Fore.GREEN+"Give kmh value: ")))
    mph = kmh/1.60934
    print(mph, "Mph")


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
    print(kmh, "Kmph")


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
    print(kmh, "Kmph")


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
# Main code
cont = "yes" or "Yes"
cont2 = "other"
while cont2 == "other":
    print(Fore.LIGHTMAGENTA_EX +
          "\n1)Temperature\n2)Data\n3)Time\n4)Distance\n5)Velocity\n6)Exit")
    choice1 = input(Fore.YELLOW+"Give a number: ")
    # Temperature
    if choice1 == "1":
        while cont == "yes" or "Yes":
            print(Fore.LIGHTCYAN_EX+"Conversions:\n1)Celsius-->fahrenheit\n2)Celsius-->Kelvin\n3)Fahrenheit-->Celsius\n4)Fahrenheit-->Kelvin\n5)Kelvin-->Celsius\n6)Kelvin-->Fahrenheit")
            choice = input(Fore.YELLOW+"Give a number: ")
            if choice == "1":
                celsius_fahrenheit()
            elif choice == "2":
                celsius_kelvin()
            elif choice == "3":
                fahrenheit_celsius()
            elif choice == "4":
                fahrenheit_kelvin()
            elif choice == "5":
                kelvin_celsius()
            elif choice == "6":
                kelvin_fahrenheit()
            else:
                print("invalid input")
            cont = input(Fore.MAGENTA+"Continue? 1)Yes/2)No/3)other: ")
            if cont == "2":
                print(Fore.LIGHTRED_EX+"Goodbye (: ")
                break
            elif cont == "3":
                break
    # Data
    if choice1 == "2":
        while cont == "yes" or "Yes":
            print(Fore.LIGHTCYAN_EX+"Conversions:\n1)Byte\n2)Kb\n3)Mb\n4)Gb\n5)Tb")
            choice = input(Fore.YELLOW+"Give a number: ")
            if choice == "1":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions:\n1)Byte-->Kb\n2)Byte-->Mb\n3)Byte-->Gb\n4)Byte-->Tb")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    bytes_kb()
                elif choice2 == "2":
                    bytes_mb()
                elif choice2 == "3":
                    byte_gb()
                elif choice2 == "4":
                    byte_tb()
                else:
                    print("invalid input")
                    break
            if choice == "2":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions:\n1)Kb-->Byte\n2)Kb-->Mb\n3)Kb-->Gb\n4)Kb-->Tb")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    kb_bytes()
                elif choice2 == "2":
                    kb_mb()
                elif choice2 == "3":
                    kb_gb()
                elif choice2 == "4":
                    kb_tb()
                else:
                    print("invalid input")
                    break
            if choice == "3":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions:\n1)Mb-->Byte\n2)Mb-->Kb\n3)Mb-->Gb\n4)Mb-->Tb")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    mb_bytes()
                elif choice2 == "2":
                    mb_kb()
                elif choice2 == "3":
                    mb_gb()
                elif choice2 == "4":
                    mb_tb()
                else:
                    print("invalid input")
                    break
            if choice == "4":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions:\n1)Gb-->Byte\n2)Gb-->Kb\n3)Gb-->Mb\n4)Gb-->Tb")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    gb_byte()
                elif choice2 == "2":
                    gb_kb()
                elif choice2 == "3":
                    gb_mb()
                elif choice2 == "4":
                    gb_tb()
                else:
                    print("invalid input")
                    break
            if choice == "5":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions:\n1)Tb-->Byte\n2)Tb-->Kb\n3)Tb-->Mb\n4)Tb-->Gb")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    tb_byte()
                elif choice2 == "2":
                    tb_kb()
                elif choice2 == "3":
                    tb_mb()
                elif choice2 == "4":
                    tb_gb()
                else:
                    print("invalid input")
                    break
            cont = input(
                Fore.MAGENTA+"Continue? 1)Yes/2)No/3)other Conversion: ")
            if cont == "2":
                print(Fore.LIGHTRED_EX+"Goodbye (: ")
                break
            elif cont == "3":
                break
    # Time
    if choice1 == "3":
        while cont == "yes" or "Yes":
            print(Fore.LIGHTCYAN_EX +
                  "Conversions\n1)Sec\n2)Minutes\n3)Hours\n4)Days\n5)Week\n6)Year")
            choice = input("Give a number: ")
            if choice == "1":
                print(
                    Fore.LIGHTCYAN_EX+"\n1)Sec-->Minutes\n2)Sec-->Hours\n3)Sec-->Days\n4)Sec-->Weeks\n5)Sec-->Year")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    sec_minutes()
                elif choice2 == "2":
                    sec_hour()
                elif choice2 == "3":
                    sec_day()
                elif choice2 == "4":
                    sec_week()
                elif choice2=="5":
                    sec_year()
                else:
                    print("invalid input")
            if choice == "2":
                print(Fore.LIGHTCYAN_EX+"Conversions:\n1)Minute-->Sec\n2)Minute-->Hours\n3)Minute-->Days\n4)Minute-->Weeks\n5)Minute-->Years")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    minutes_sec()
                elif choice2 == "2":
                    minutes_hour()
                elif choice2 == "3":
                    minutes_day()
                elif choice2 == "4":
                    minute_week()
                elif choice2 == "5":
                    minute_year()
                else:
                    print("invalid input")
            if choice == "3":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions:\n1)Hour-->Sec\n2)Hour-->Minutes\n3)Hour-->Days\n4)Hour-->Weeks\n5)Hour-->Years")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    hour_sec()
                elif choice2 == "2":
                    hour_minutes()
                elif choice2 == "3":
                    hour_day()
                elif choice2 == "4":
                    hour_week()
                elif choice2 == "5":
                    hour_year()
                else:
                    print("invalid input")
            if choice == "4":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions:\n1)Day-->Sec\n2)Day-->Minutes\n3)Day-->Hours\n4)Day-->Weeks\n5)Day-->Years")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    day_sec()
                elif choice2 == "2":
                    day_minutes()
                elif choice2 == "3":
                    day_hour()
                elif choice2 == "4":
                    day_week()
                elif choice2 == "5":
                    day_year()
                else:
                    print("invalid input")
            if choice == "5":
                print((Fore.LIGHTCYAN_EX+"Conversions:\n1)Week-->Sec\n2)Week-->Minutes\n3)Week-->Hours\n4)Week-->Days\n5)Week-->Years"))
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    week_sec()
                elif choice2 == "2":
                    week_minute()
                elif choice2 == "3":
                    week_hour()
                elif choice2 == "4":
                    week_day()
                elif choice2 == "5":
                    week_year()
                else:
                    print("invalid input")
            if choice == "6":
                print((Fore.LIGHTCYAN_EX+"Conversions:\n1)Year-->Sec\n2)Year-->Minutes\n3)Year-->Hours\n4)Year-->Days\n5)Year-->Weeks"))
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    year_sec()
                elif choice2 == "2":
                    year_minute()
                elif choice2 == "3":
                    year_hour()
                elif choice2 == "4":
                    year_day()
                elif choice2 == "5":
                    year_week()
                else:
                    print("invalid input")
            cont = input(
                Fore.MAGENTA+"Continue? 1)Yes/2)No/3)other Conversion: ")
            if cont == "2":
                print(Fore.LIGHTRED_EX+"Goodbye (: ")
                break
            elif cont == "3":
                break
    # Distance
    if choice1 == "4":
        while cont == "yes" or "Yes":
            print(Fore.LIGHTCYAN_EX +
                  "Conversions\n1)Mm\n2)Cm\n3)M\n4)Km\n5)Mile\n6)Inch\n7)Foot")
            choice = input("Give a number: ")
            if choice == "1":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions\n1)Mm-->Cm\n2)Mm-->M\n3)Mm-->Km\n4)Mm--Mile\n5)Mm-->inch\n6)Mm-->foot")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    mili_cm()
                elif choice2 == "2":
                    mili_meter()
                elif choice2 == "3":
                    mili_km()
                elif choice2 == "4":
                    mili_mile()
                elif choice2 == "5":
                    mili_inch()
                elif choice2 == "6":
                    mili_foot()
            if choice == "2":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions\n1)Cm-->Mm\n2)Cm-->M\n3)Cm-->Km\n4)Cm--Mile\n5)Cm-->inch\n6)Cm-->foot")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    cm_mili()
                elif choice2 == "2":
                    cm_meter()
                elif choice2 == "3":
                    cm_km()
                elif choice2 == "4":
                    cm_mile()
                elif choice2 == "5":
                    cm_inch()
                elif choice2 == "6":
                    cm_foot()
            if choice == "3":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions\n1)M-->Mm\n2)M-->Cm\n3)M-->Km\n4)M--Mile\n5)M-->inch\n6)M-->foot")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    meter_mili()
                elif choice2 == "2":
                    meter_cm()
                elif choice2 == "3":
                    metre_km()
                elif choice2 == "4":
                    metre_mile()
                elif choice2 == "5":
                    metre_inch()
                elif choice2 == "6":
                    metre_foot()
            if choice == "4":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions\n1)Km-->Mm\n2)Km-->Cm\n3)Km-->M\n4)Km--Mile\n5)Km-->inch\n6)Km-->foot")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    km_mili()
                elif choice2 == "2":
                    km_cm()
                elif choice2 == "3":
                    km_metre()
                elif choice2 == "4":
                    km_mile()
                elif choice2 == "5":
                    km_inch()
                elif choice2 == "6":
                    km_foot()
            if choice == "5":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions\n1)Mile-->Mm\n2)Mile-->Cm\n3)Mile-->M\n4)Mile--Km\n5)Mile-->inch\n6)Mile-->foot")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    mile_mili()
                elif choice2 == "2":
                    mile_cm()
                elif choice2 == "3":
                    mile_metre()
                elif choice2 == "4":
                    mile_km()
                elif choice2 == "5":
                    mile_inch()
                elif choice2 == "6":
                    mile_foot()
            if choice == "6":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions\n1)Inch-->Mm\n2)Inch-->Cm\n3)Inch-->M\n4)Inch--Km\n5)Inch-->Mile\n6)Inch-->foot")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    inch_mili()
                elif choice2 == "2":
                    inch_cm()
                elif choice2 == "3":
                    inch_metre()
                elif choice2 == "4":
                    inch_km()
                elif choice2 == "5":
                    inch_mile()
                elif choice2 == "6":
                    inch_foot()
            if choice == "7":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions\n1)Foot-->Mm\n2)Foot-->Cm\n3)Foot-->M\n4)Foot--Km\n5)Foot-->Mile\n6)Foot-->inch")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    foot_mili()
                elif choice2 == "2":
                    foot_cm()
                elif choice2 == "3":
                    foot_metre()
                elif choice2 == "4":
                    foot_km()
                elif choice2 == "5":
                    foot_mile()
                elif choice2 == "6":
                    foot_inch()
            cont = input(
                Fore.MAGENTA+"Continue? 1)Yes/2)No/3)other Conversion: ")
            if cont == "2":
                print(Fore.LIGHTRED_EX+"Goodbye (: ")
                break
            elif cont == "3":
                break
    # Velocity
    if choice1 == "5":
        while cont == "yes" or "Yes":
            print(Fore.LIGHTCYAN_EX +
                  "Conversions\n1)Kmph\n2)Mph\n3)Mach\n4)Kn\n5)C(speed of light)")
            choice = input("Give a number: ")
            if choice == "1":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions\n1)Kmph-->Mph\n2)Kmph-->Macht\n3)Kmph-->Knots\n4)Kmph-->C")
                choice2 = input("Give a number: ")
                if choice2 == '1':
                    kmh_mph()
                elif choice2 == "2":
                    kmh_ma()
                elif choice2 == "3":
                    kmh_kn()
                elif choice2 == "4":
                    kmh_c()
            if choice == "2":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions\n1)Mph-->Kmph\n2)Mph-->Macht\n3)Mph-->Knots\n4)Mph-->C")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    mph_kmh()
                elif choice2 == "2":
                    mph_ma()
                elif choice2 == "3":
                    mph_kn()
                elif choice2 == "4":
                    mph_c()
            if choice == "3":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions\n1)Macht-->Kmph\n2)Macht-->Mph\n3)Macht-->Knots\n4)Macht-->C")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    ma_kmh()
                elif choice2 == "2":
                    ma_mph()
                elif choice2 == "3":
                    ma_kn()
                elif choice2 == "4":
                    ma_c()
            if choice == "4":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions\n1)Knots-->Kmph\n2)Knots-->Mph\n3)Knots-->Macht\n4)Knots-->C")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    kn_kmh()
                elif choice2 == "2":
                    kn_mph()
                elif choice2 == "3":
                    kn_ma()
                elif choice2 == "4":
                    kn_c()
            if choice == "5":
                print(
                    Fore.LIGHTCYAN_EX+"Conversions\n1)C-->Kmph\n2)C-->Mph\n3)C-->Macht\n4)C-->Knots")
                choice2 = input("Give a number: ")
                if choice2 == "1":
                    c_kmh()
                elif choice2 == "2":
                    c_mph()
                elif choice2 == "3":
                    c_macht()
                elif choice2 == "4":
                    c_kn()
            cont = input(
                Fore.MAGENTA+"Continue? 1)Yes/2)No/3)other Conversion: ")
            if cont == "2":
                print(Fore.LIGHTRED_EX+"Goodbye (: ")
                break
            elif cont == "3":
                break
# main programm brake
    if cont == "2":
        break
    elif choice1 == "6":
        print(Fore.LIGHTRED_EX+"Goodbye (: ")
        break
