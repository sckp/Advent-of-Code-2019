cleancode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,6,23,27,1,6,27,31,2,31,9,35,1,35,6,39,1,10,39,43,2,9,43,47,1,5,47,51,2,51,6,55,1,5,55,59,2,13,59,63,1,63,5,67,2,67,13,71,1,71,9,75,1,75,6,79,2,79,6,83,1,83,5,87,2,87,9,91,2,9,91,95,1,5,95,99,2,99,13,103,1,103,5,107,1,2,107,111,1,111,5,0,99,2,14,0,0]
def findanswer(cleancode):
    code = cleancode[:]
    
    for i in range(0, len(code), 4):
        op = code[i]
        a = code[code[i+1]]
        b = code[code[i+2]]
        
        if op == 99:
            return code[0]
        elif op == 1:
            code[code[i+3]] = a + b
        elif op == 2:
            code[code[i+3]] = a * b
    
    return code[0]
        
    
for noun in range(0, 100):
    for verb in range(0, 100):
        cleancode[1] = noun
        cleancode[2] = verb
        
        answer = findanswer(cleancode)
        
        if answer == 19690720:
            print(100 * noun + verb)
            break
