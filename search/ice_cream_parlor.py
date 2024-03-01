def icecreamParlor(m, arr):
    a_dic = {}
    for idx, a in enumerate(arr):
        if a in a_dic:
            a_dic[a].append(idx)
        else:
            a_dic[a] = [idx]
    res = []
    print(a_dic)
    for key in a_dic:
        if m-key in a_dic:
            if m-key == key and len(a_dic[key])==2:
               res = [a_dic[m-key][0]+1, a_dic[key][1]+1]
               break
            elif m-key != key:
               res = [a_dic[m-key][0]+1, a_dic[key][0]+1]
               break
    return sorted(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()