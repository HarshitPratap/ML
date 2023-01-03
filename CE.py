import csv
with open("./data.csv","r") as csvfile:
    csvf = csv.reader(csvfile)
    data = list(csvf)
    # print(data)
    # print("\n")
    s = data[1][:-1]
    print(s)
    g = [['?' for i in range(len(s))]for j in range(len(s))]
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
    print("\n Specific hypothesis:- \n",s)
    print("\n General hypothesis:- \n",gh)
