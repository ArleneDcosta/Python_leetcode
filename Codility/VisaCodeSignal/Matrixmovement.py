
def gravity(box):
    transposed = list(zip(*box))
    rotated_box = [list(row)[::-1] for row in transposed]

    rows = len(rotated_box)
    cols = len(rotated_box[0])

    for col in range(0,cols):
        stack = []
        for row in range(0,rows):
            if rotated_box[row][col] == '#':
                stack.append('#')
                rotated_box[row][col] = '_'
            if rotated_box[row][col] == '*':
                prevrow = row - 1
                while(len(stack) > 0):
                    rotated_box[prevrow][col] = stack.pop()
                    prevrow -= 1
        if len(stack) > 0:
            prevrow = rows - 1
            while(len(stack) > 0):
                rotated_box[prevrow][col] = stack.pop()
                prevrow -= 1
                    
    return rotated_box


if __name__ == '__main__':
    box = [['_','#','_'],['#','_','#'],['#','#','#']]

    box = gravity(box)
    for row in box:
        print(" ".join(row))