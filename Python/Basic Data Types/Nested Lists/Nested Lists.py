if __name__ == '__main__':
    outer_list = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        outer_list.append([name, score])

        scores.append(score)
        
    min_score = min(scores)
    s = [e for e in scores if e > min_score]
    m = min(s)
    names = []
    for inner_list in outer_list:
        if inner_list[1] == m:
            names.append(inner_list[0])
    
    names.sort()
    for name in names:
        print(name)
