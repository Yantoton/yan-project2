def work(hour):
    """this function show working hour
    and how many hours you are working that will show you"""
    for hours in range(1,hour):
        print(f"Today you are nonstop working on {hours}: hours")
    print("stop working & take some rest")

print(work.__doc__)
work(8)
