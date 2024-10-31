import argparse

def bf_interpreter(code):
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
                user_input = input()
                memory[pointer] = ord(user_input[0]) if user_input else 0
                input_pointer += 1

        code_pointer += 1
    return output


def run_file(path):
    with open(path, 'r') as f:
        code = f.read()
    return bf_interpreter(code)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help='path to bf file')
    args = parser.parse_args()

    output = run_file(args.file)
    print(output)
        