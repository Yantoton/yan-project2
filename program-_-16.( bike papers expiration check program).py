years = [2026]
months =['jan','feb','mar','apr','may','jun']
days = range(1,31)
for y in years:
    for m in months:
        for d in days:
            if y==2026 and m=='jun' and d==3:
                print(f"{y}_{m}_{d}:your bike papers is expired go and update ur bike papers")
            else:
                print(f"{y}_{m}_{d}:your bike papers is not expired")
            print(f"report_{y}_{m}_{d}.cuv")
