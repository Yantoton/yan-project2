files = [' Report.csv ',' Data.csv ',' final.TXT ']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv').title()
    print(f"Processing : {file}")


files = [
       'data1.csv',
        'report.pdf',
        'data2.txt',
        'docoment.csv']
for file in files:
    if not file.endswith('.csv'):
        print(f'{file} csv file is not complete')
        pass
else:
    print(f"All csv files are complete")
