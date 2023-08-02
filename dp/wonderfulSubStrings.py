from collections import defaultdict
#Notes: Two characters consecutively or 2 strings consec will make parity 0
#if its even will wish to be retrieved again or else will just remain in the dictionary
#Full 0 means entire string
def wonderfulSubstrings(word):
    mask = 0
    cnt  = defaultdict(int)
    cnt[0] = 1 #base case
    print(cnt)
    ans  = 0
    #Here we dont have to find the length has not storing index
    # Here we need to find the count of substrings
    for c in word:
        index = ord(c) - ord('a')
        mask ^= (1 << index)
        #at most 1 it means 0 odd appearances and 1 . 1 is handled below
        #Capturing even no of strings

        #When captured first time its value will be zero but second time it will be initialized aldready so plus one
        ans += cnt[mask]
        print('Even',index, cnt[mask], mask,ans)

        #Capturing odd no of strings with the character
        for i in range(10):

            preMask = mask ^ (1 << i)
            #if its end then only the last letter means letter odd value if start or mid then from that till eos will be considered
            print(i,cnt[preMask],mask,preMask,ans)
            ans += cnt[preMask]

        #Adding the odd value to the existing value
        cnt[mask] +=1
        print(cnt,ans)
    return ans

print(wonderfulSubstrings("abaaa"))
#print(0^ (1 << 1))
#aab a is not working
#when par is 0 remeber 2 chars are together or 2 substrings are togehter
'''First part: we only care about if a letter is odd or even count, so we can track the current state of the string from [0...i] using a bitmask. 1 will mean that character is odd and 0 will mean that character is even. For example, "1001" means d has odd count, c even, b even, a odd

To calculate the answer: We go through from index 0 to the length of the string, updating the state of the string 
from [0...current index]. If we have seen our current state before (say [0...j] has the same state as [0...i], 
that means the substring between j and i has an even count of all characters. Think about each new character as 
flicking it's own light switch. Flicking a switch an even amount of times results in no change. So if we see that we 
have previously run into the current state, we know there is a substring with even count of all characters in between that state and the current state. We add however many times we have previously run into the current state.
 This is because if we've run into the state once before, say at j, we know [j...current index] has even count of all characters. So we add 1 to our answer. If we've run into the state twice before, say at j and i, we know that [j... current index] has even count of all characters and [i...current index] has even count of all characters, so we add 2.

Next we tackle the part where one character can be odd. If there is one character which occurs an odd amount of times 
between [previous index... current index], and all other characters are even, that means we only need to 
flick one switch to turn our current state into the previous one. We try flicking each switch and see if we 
have run into that state before. If we have that means we have a wonderful substring because only 1 character 
appears an odd number of times between [previous index... current index]. Again we add the number of times we have 
previously run into the state, because of the same reason as above. If we've seen the state at j, then [j...current] 
has only 1 odd character, and if we've seen it at j and i, then [j...current] and [i...current] 
have only 1 odd character, etc.'''