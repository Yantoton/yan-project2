attempts = 0
while attempts <2:
    answer = input("did u like car?... (yes/no):")
    if answer == 'yes':
        print('welcome in jdm page!>>>')
        break
    elif answer =='no':
            print('sorry this page is not for u')
            break
    else:
        attempts+=1
    print("keep raceing & drifting")
