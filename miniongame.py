def minion_game(string):
    # your code goes here
    S, K = 0,0 #create player S and player K

    for i in range(len(string)):
        if string[i] in "AEIOU":
            K = K + len(string) - i
        else:
            S = S + len(string) - i        
    if S>K: #compare the results
            print("Stuart"+" " + str(S))
    elif K>S:
            print("Kevin"+" " + str(K))
    else:
            print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
