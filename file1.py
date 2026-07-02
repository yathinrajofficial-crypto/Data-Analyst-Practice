#'''with open(r"C:\Users\AnudipCOA\Downloads\python\file_handling\textfile.txt",'r') as file:
 #   data=file.read()
  #  print(data)'''


with open(r"C:\Users\AnudipCOA\Downloads\python\file_handling\textfile.txt",'r') as file:
    for line in file:
            for word in line:
                print(word) 
        