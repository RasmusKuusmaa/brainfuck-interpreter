def bf_interpreter(code, input=''):
    memory = [0] * 30000
    pointer = 0
    output = ""
    input_pointer = 0
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
        elif cmd == ",":
            if input_pointer < len(input):
                memory[pointer] = ord(input[input_pointer])
                input_pointer += 1
            else:
                memory[pointer] = 0
        code_pointer += 1
    return output


def run_file(path, input=''):
    with open(path, 'r') as f:
        code = f.read()
    return bf_interpreter(code, input)

#capturing live input; output = run_file('./helloworld.bf', input())

output = run_file('./helloworld.bf')
print(output)
    