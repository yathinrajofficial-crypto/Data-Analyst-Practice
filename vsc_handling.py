#import csv
#with open(r"C:\Users\AnudipCOA\Downloads\python\file_handling\new.csv",'r')as file:
 #   data=csv.reader(file)


import csv
with open(r"C:\Users\AnudipCOA\Downloads\python\file_handling\new.csv",'w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(["product","sales"])
    writer.writerow(["ink",25])
    writer.writerow(["ballpen",10])


 