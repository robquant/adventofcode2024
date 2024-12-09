import sys
from operator import itemgetter

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

def count_run(disk, start):
    value = disk[start]
    i = start
    while i < len(disk) and disk[i] == value:
        i += 1
    return i - start

def find_empty_block(empty_block_list, length):
    for block_index, (start, run_length) in enumerate(empty_block_list):
        if run_length >= length:
            return block_index, start
    return None

def compact_full_blocks(disk):
    empty_block_list = []
    occupied_block_list = []
    i = 0
    while i < len(disk):
        run_length = count_run(disk, i)
        if disk[i] == None:
            empty_block_list.append((i, run_length))
        else:
            occupied_block_list.append((disk[i], i, run_length))
        i += run_length
    empty_block_list.sort() # Sort by run length, descending
    occupied_block_list.reverse()
    for block in occupied_block_list:
        block_id, start, run_length = block
        empty_block = find_empty_block(empty_block_list, run_length)
        if empty_block is None:
            continue
        empty_block_index, empty_block_start = empty_block
        # Don't move blocks to the right
        if empty_block_start > start:
            continue
        for i in range(run_length):
            disk[empty_block_start + i] = block_id
            disk[start + i] = None
        _, empty_block_run_length = empty_block_list[empty_block_index]
        empty_block_list[empty_block_index] = (empty_block_start + run_length, empty_block_run_length - run_length)



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

original_disk = disk[:]
compact(disk)
#print_disk(disk)
print("Checksum part 1:", checksum(disk))
compact_full_blocks(original_disk)
print("Checksum part 2:", checksum(original_disk))