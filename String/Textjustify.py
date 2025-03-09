def consume(line, left, w):
    print(line, left, w)
    if left >= (1 + len(w)):
        line.append(' ')
        line.append(w)
        left -= (1 + len(w))
        return left, True
    
    # justify a line with a single word
    if len(line) == 1:
        print(line,"ONE")
        line.append(' ' * left)
        return 0, False
    #Becuase '' are in even spaces
    holes = len(line) // 2
    print(f"holes {holes}")
    even_pad = left // holes
    print(f"even_pad {even_pad}")
    left -= holes * even_pad
    print(left)
    #the below + int)left > 0 is if there is uneven maxwidth
    for h in range(holes):
        line[1 + 2 * h] += ' ' * (even_pad + int(left > 0))
        print(F"Line:{line},left:{left},1+2h:{1+2*h},holes:{holes},even_pad:{even_pad}")
        left -= 1
    
    return 0, False
    
def fullJustify(words, maxWidth):        
    lines = []
    ln = [words[0]]
    print(f"ln {ln}")
    left = maxWidth - len(words[0])
    print(f"left {left}")
           
    for w in words[1:]:
        left, consumed = consume(ln, left, w)
        if not consumed:
            lines.append(ln)
            left = maxWidth - len(w)
            ln = [w]
                        
    # justify the last line 
    ln.append(' ' * left)
    lines.append(ln)
               
    return ["".join(ln) for ln in lines]

print(fullJustify(["This", "is", "an", "example", "of", "text", "justification","aaaaa"],16))
