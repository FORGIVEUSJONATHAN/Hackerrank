def sorting(string): 
    lc = [] #lower case
    uc = [] #upper case
    od = [] #odd
    ed = [] #even
    for x in string:
        if x.islower():
            lc.append(x)
        elif x.isupper():
            uc.append(x)
        elif x.isdigit():
            if int(x)%2==0:
                ed.append(x)
            else:
                od.append(x)

    result = ''.join(sorted(lc)+sorted(uc)+sorted(od)+sorted(ed))
    return (result)

    
if __name__=='__main__':
    
    S = input()
    print (sorting(S))
