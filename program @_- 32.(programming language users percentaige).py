import termplotlib as tpl

users = [100,80,70,40,30]
languages = ["Python","Java","C++","Ruby","Visual Basic"]
for i in range(len(users)):
    totals=[f"in 2026 programming language user list:{languages[i]+ ":" + str(users[i])+"% Users"}"]
    for j in range(len(totals)):
        print(totals[j])
