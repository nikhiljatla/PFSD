import csv

header=['Name','ID']
data1=['Nikhil',2000030384]
data2={'Jatla Nikhil',1141,'Nikhil',2000030384}
data3={'Name':'Nikhil','Id':2000030384}

'''with open('Example.csv','w') as f:
    writer=csv.writer(f)
    #Write the Header
    writer.writerow(header)
    #write the data
    writer.writerow(data3)

    #writing multiple data into the csv
with open('Example.csv','w') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    data=[
        ['Nikhil',2000030384],
        ['Jatla Nikhil',1141]
    ]
    writer.writerows(data)
print("Writing Multiple rows Successful")'''

#Reading Multiple rows
with open('Student.csv') as f:
    csvreader=csv.reader(f)
    #header=next(csvreader)
    #print(header)
    rows=[]
    for row in csvreader:
        rows.append(row)
    print(rows)
    #Printing Total No Of Rows In File
    print("Total no of rows: %d" %(csvreader.line_num))
    print("Printing of Data Successfull")