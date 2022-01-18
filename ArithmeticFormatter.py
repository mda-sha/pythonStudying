import re

def printResult(res, max_len):
    listLen = len(res)
    i = 0
    while i < listLen:
        spaces = max_len[i] + 2 - sym_in_num(res[i])
        while spaces > 0:
            print(" ", end='')
            spaces -= 1
        print(res[i], end='')
        print("    ", end='')
        i += 1

def count_problems(a, b, oper, max_len):
    res = list()
    i = 0
    for x in oper:
        if x == '-':
            res.append(a[i] - b[i])
        if x == '+':
            res.append(a[i] + b[i])
        i += 1
    return res

def sym_in_num(num):
    n = num
    s = 0
    if num < 0:
        num *= -1
    while num > 0 and s < 5:
        num = int(num / 10)
        s += 1
    if n < 0:
        s += 1
    return(s)

def max_len_list(a, b):
    max_len = list()
    i = 0
    listLen = len(a)
    while i < listLen:
        tmp = sym_in_num(a[i])
        tmp2 = sym_in_num(b[i])
        if tmp >= tmp2:
            max_len.append(tmp)
        else:
            max_len.append(tmp2)
        i += 1
    return(max_len)

def print_line(a, max_len, oper, op):
    i = 0
    listLen = len(a)
    while i < listLen:
        if op == True:
            print(oper[i], end = "")
        if op == False:
            spaces = max_len[i] + 2 - sym_in_num(a[i])
        else:
            spaces = max_len[i] + 1 - sym_in_num(a[i])
        while spaces > 0:
            print(" ", end = '')
            spaces -= 1
        print(a[i], end = '')
        print("    ", end = "")
        i += 1

def print_problems(a, b, oper, max_len):
    print_line(a, max_len, oper, False)
    print("")
    print_line(b, max_len, oper, True)
    print("")
    for i in max_len:
        while i + 2 > 0:
            print("-", end = '')
            i -= 1
        spaces = 4
        while spaces > 0:
            print(" ", end = '')
            spaces -= 1
    print('')

def arithmetic_arranger(problems, printRes=None):

    a = list()
    b = list()
    oper = list()
    for problem in problems:
        tmp_a = re.findall("^-*[0-9]+ ", problem)
        tmp_b = re.findall(" -*[0-9]+$", problem)
        if not tmp_a or not tmp_b:
            return("Error: Numbers must only contain digits.")        
        tmp_a = int(tmp_a[0].strip())
        tmp_b = int(tmp_b[0].strip())
        if tmp_a > 9999 or tmp_b > 9999 or tmp_a < -999 or tmp_b < -999:
            return("Error: Numbers cannot be more than four digits.")
        a.append(tmp_a)
        b.append(tmp_b)
        tmp = re.findall(" \+ ", problem)
        if not tmp:
            tmp = re.findall(" - ", problem)
        if not tmp:
            return("Error: Operator must be \'+\' or \'-\'")
        oper.append(tmp[0].strip())
    if len(a) > 5:
        return("Error: Too many problems.")

    max_len = max_len_list(a, b)
    res = count_problems(a, b, oper, max_len)
    print_problems(a, b, oper, max_len)
    if printRes == True:
        printResult(res, max_len)
        print('')

    arranged_problems = list()
    for i in res:
        arranged_problems.append(str(i))
    return(arranged_problems)

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "50  - 40"]))