# Extracting Data From PDF to CSV file for Final Merit List

import camelot

count=1
for i in range(1,565):
    # First Converting 4 page in pair to csv
    no_of_pages = str(count)+"-"+str(count+3);
    tables = camelot.read_pdf('2018.pdf', pages=no_of_pages, parallel=True);
    
    for j in range(4):
        tables[j].df[2] =tables[j].df[2].str.replace("\n", " ")

    path='Y:\\Direct Second Year\\Analysis\\Rec\\'+str(i)+'.csv'
    
    tables.export(path, f='csv')  
    print(count)
    count = count + 4