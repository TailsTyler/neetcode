


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1:
        return 1
    window = [] # substring being examined for max len
    l = 0 #left end of window
    r = 0 # right end of window
    biggest = 0 # max substring len found
    ##print("len(s): ", len(s))
    while r < len(s):
        #next = s[r]
        #adding to window
        while not s[r] in window:
            window.append(s[r]) 
            r += 1
            if r == len(s):
                biggest = max(biggest,len(window))
                #print("max " + str(biggest))
                return biggest
            #print("r: ", r, " ", window)
        biggest = max(biggest,len(window))
        #print("max " + str(biggest))
        #removing from window
        while l < r:
            found_dupe = False
            if s[l] == s[r]:
                found_dupe = True
            l += 1
            window.pop(0)
            #print("l: ", l, " ", window)
            if found_dupe:
                break
    return biggest

print(lengthOfLongestSubstring('sadb'))