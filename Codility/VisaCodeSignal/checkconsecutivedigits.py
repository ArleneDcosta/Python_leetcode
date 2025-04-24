
def check_consecutive_digits(s):
    no = [int(char) for char in s]

    while True:
        reslist = []
        i = 0
        changed = False
        while i < len(no):
            j = i
            curr_sum = no[i]
            while j + 1 < len(no) and no[j] == no[j + 1]:
                curr_sum += no[j + 1]
                j += 1
                changed = True  
            
            reslist += [int(c) for c in str(curr_sum)]
            i = j + 1
        
        if not changed:
            break
        no = reslist

    return ''.join(str(char) for char in no)



if __name__ == '__main__':
    print(check_consecutive_digits("66644319333"))