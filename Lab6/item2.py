def length(txt):
    def loop(lst, mode):
        if not lst:
            return mode
        if mode % 2 == 0 :
            a = '*'
        else :
            a = '~'
        print(lst[:1] + (a),end = '')
        return loop(lst[1:], mode + 1)
    return loop(txt,0)
print('\n'+str(length(input("Enter Input : "))))