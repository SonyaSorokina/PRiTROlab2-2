def readFile(text):
    f = open(text, 'r', encoding="UTF-8")
    stackPancakes = []
    while True:
        line = f.readline().strip()
        if not line:
            break
        stackPancakes.append(line)
    return stackPancakes

def flip(seq: list, index: int) -> list:
    return list(reversed(seq[:index])) + (seq[index:])

def pancakes(stackPancakes: list):
    for stack in stackPancakes:
        stack = stack.split(" ")
        stack = list(map(int, stack))
        answ = ' '.join(map(str, stack)) + " | "
        while(True):
            if len(stack)==0:
                break
            if stack.index(max(stack))==(len(stack)-1):
                stack.remove(max(stack))
            elif stack.index(max(stack))==0:
                answ += str(len(stack)) + " "
                stack = flip(stack, (len(stack)))
            else:
                answ += str(stack.index(max(stack)) + 1) + " "
                stack = flip(stack, stack.index(max(stack))+1)
        print(answ + "0")

from os import listdir, getcwd

print(getcwd())
files = [i for i in listdir(getcwd()) if ".txt" in i]

for i, file in enumerate(files, start=1):
    try:
        print(f"Тест {i}")
        pancakes(readFile(file))
    except Exception as e:
        print(e)
