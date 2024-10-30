def bf_interpreter(code):
    memory = [0] * 30000
    pointer = 0
    output = ""

    loop = {}
    stack = []
    for idx, cmd in enumerate(code):
        if cmd == "[":
            stack.append(idx)
        elif cmd == "]":
            start = stack.pop()
            loop[start] = idx
            loop[idx] = start
    
    code_pointer = 0
    while code_pointer < len(code):
        cmd = code[code_pointer]

        if cmd == ">":
            pointer += 1
        elif cmd == "<":
            pointer -= 1
        elif cmd == "+":
            memory[pointer] = (memory[pointer] + 1) % 256
        elif cmd == "-":
            memory[pointer] = (memory[pointer] - 1) % 256
        elif cmd == ".":
            output += chr(memory[pointer])
        elif cmd == "[":
            if memory[pointer] == 0:
                code_pointer = loop[code_pointer]
        elif cmd == "]":
            if memory[pointer] != 0:
                code_pointer = loop[code_pointer]
        code_pointer += 1
    return output

print(bf_interpreter(
    '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'
))