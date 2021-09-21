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
