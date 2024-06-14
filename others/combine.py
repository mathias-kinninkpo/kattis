def more_one_char(char):
    return char if len(char) > 1 else 0

def delete(chaine):
    while 0 in chaine:
        del(chaine[chaine.index(0)])
    return sorted(chaine, key= lambda x : len(x))

def combinason(string):
    chaines = list()
    n = 1
    while n < len(string):
        for i in range(len(string)):
            for j in range(n, len(string)):
                chaines.append(string[i:n] + string[j])
        n += 1  
    return delete(list(map(more_one_char , chaines)))

if __name__ == '__main__':  
    chaine = input()
    print(combinason(chaine) + combinason(chaine[::-1]))