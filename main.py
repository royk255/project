end = "yes"


def build_int(s):
    new_res = ''
    for i, c in enumerate(s):
        if (c in op_list):
            res = float(new_res)
            return (res, s[i:])
            break
        else:
            new_res += c
            print(new_res)


def calc(line):
    res = []
    sum = 0
    while line:
        if line[0] == '=':
            break

        # if line[0] not in op_list and
        if line[1] == '(':
            if line[2] not in op_list:
                temp = calc("+" + line[2:])
            else:
                temp = calc(line[2:])
            if line[0] == '+':
                res.append(temp[0])
            if line[0] == '-':
                res.append(-1 * temp[0])
            if line[0] == '*':
                res.append(res.pop() * temp[0])
            if line[0] == '/':
                res.append(res.pop() / temp[0])
            line = temp[1]
            while res:
                sum = sum + res.pop()
            line = temp[1]
            continue
        if line[0] == ')':
            while res:
                sum = sum + res.pop()
            return (sum, line[1:])

        print(f'line = {line}')
        temp = build_int(line[1:])

        if line[0] == '+':
            res.append(temp[0])
        if line[0] == '-':
            res.append(-1 * temp[0])
        if line[0] == '*':
            res.append(res.pop() * temp[0])
        if line[0] == '/':
            res.append(res.pop() / temp[0])
        line = temp[1]
    while res:
        sum = sum + res.pop()
    return (sum, line[0:])


while end == "yes":
    line = input("Enter something to calculate: ");
    # line = '5-3*6+8*4'
    op_list = ['+', '-', '*', '/', '=', '(', ')']
    res = []

    if "=" not in line:
        line += "="
    line = line.replace(" ", "")

    new_line = ""
    power = False
    if line[0] not in op_list:
        line = "+" + line
    for q in range(len(line)):
        if line[q] == "^":
            for z in range(int(line[q + 1]) - 1):
                new_line += "*" + line[q - 1]
            power = True
        else:
            if power:
                power = False
            else:
                new_line = new_line + line[q]
    line = new_line
    new_line = ""

    sum = calc(line)
    print(sum)
    def simle_eq(line):
    newLine = line.split("=")
    line = newLine[0]+newLine[1]
    line_n = ""
    line_x = ""
    s = line
    while line:
        while line[0] not in op_list:
            new_res = ''
            for i, c in enumerate(s):
            if (c in op_list):
                res = new_re
                return (res, s[i:])
                break
            else:
                new_res += c
                print(new_res)

    end = input("Do you want to continue (yes / no): ")
    while end != "yes" and end != "no":
        end = input("Do you want to continue (yes / no): ")
