import sys
import re

inf = sys.argv[1] if len(sys.argv) > 1 else 'input'

with open(inf) as f:
    numbers = re.findall(r'(\d+)', f.read())
    reg_a = int(numbers[0])
    reg_b = int(numbers[1])
    reg_c = int(numbers[2])
    program = [int(x) for x in numbers[3:]]

def get_combo_value(operand, reg_a, reg_b, reg_c):
    if operand <= 3:
        return operand
    elif operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c
    else:
        raise ValueError("Invalid combo operand")

output = []
ip = 0

while ip < len(program):
    opcode = program[ip]
    operand = program[ip + 1]

    if opcode == 0:  # adv
        reg_a //= 2 ** get_combo_value(operand, reg_a, reg_b, reg_c)
    elif opcode == 1:  # bxl
        reg_b ^= operand
    elif opcode == 2:  # bst
        reg_b = get_combo_value(operand, reg_a, reg_b, reg_c) % 8
    elif opcode == 3:  # jnz
        if reg_a != 0:
            ip = operand
            continue
    elif opcode == 4:  # bxc
        reg_b ^= reg_c
    elif opcode == 5:  # out
        output.append(get_combo_value(operand, reg_a, reg_b, reg_c) % 8)
    elif opcode == 6:  # bdv
        reg_b = reg_a // 2 ** get_combo_value(operand, reg_a, reg_b, reg_c)
    elif opcode == 7:  # cdv
        reg_c = reg_a // 2 ** get_combo_value(operand, reg_a, reg_b, reg_c)
    else:
        raise ValueError("Invalid opcode")

    ip += 2

print(",".join(map(str, output)))