import sys

def print_disk(disk):
    s = []
    for block in disk:
        if block == None:
            s.append(".")
        else:
            s.append(str(block))
    print("".join(s))

def compact(disk):
    i, j = 0, len(disk) - 1
    while True:
        while disk[i] != None :
            i += 1
        while disk[j] == None:
            j -= 1
        if i >= j:
            break
        disk[i] = disk[j]
        disk[j] = None

def compact_full_blocks(disk):
    pass

def checksum(disk):
    return sum(pos * i for pos, i in enumerate(disk) if i != None)

inf = sys.argv[1] if len(sys.argv) > 1 else "input"
input = open(inf).readline().strip()

disk = []
block_id = 0
block_counter = 0
for block in input:
    length = int(block)
    if block_counter % 2 == 0:
        disk += [block_id] * length
        block_id += 1
    else:
        disk += [None] * length
    block_counter += 1

compact(disk)
print_disk(disk)
print(checksum(disk))
