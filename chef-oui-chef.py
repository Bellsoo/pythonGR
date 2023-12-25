def check_salute(corridor):
    if not isinstance(corridor, str):
        return 0

    salute = 0
    officer_to_right = []
    officer_to_left = []

    for i, direction in enumerate(corridor):
        if direction not in ['-', '>', '<']:
            return 0
        if direction == '>' and '<':
            officer_to_right.append(i)
        elif direction == '<' and '>':
            officer_to_left.append(i)
            salute += len(officer_to_right)

    return salute

print(check_salute("->-------------<-------"))  
print(check_salute("-<------------->-------"))  
print(check_salute("-->>----<<--"))  
print(check_salute("--->--->----->--"))  
print(check_salute("---<---->-->----<<-->"))  
