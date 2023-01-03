import csv
with open("./data.csv","r") as csf:
    csvf = csv.reader(csf)
    data = list(csvf)
    s = data[1][:-1]
    g = [['?' for i in range(len(s))] for j in range(len(s))]

    for i in data:
        if i[-1] == "yes":
            for j in range(len(s)):
                if i[j] != s[j]:
                    s[j] = "?"
                    g[j][j] = "?"
        elif i[-1] == "no":
            for j in range(len(s)):
                if i[j] != s[j]:
                    g[j][j] = s[j]
                else:
                    g[j][j] = "?"
    gh = []
    for i in g:
        for j in i:
            if j != "?":
                gh.append(i)
    print(s)
    print(gh)
