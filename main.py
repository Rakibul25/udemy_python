# file1 = open("myfile.txt","w") 
# L = ["This is Delhi \n","This is Paris \n","This is London \n"]  
# file1.writelines(L) 
# file1.close()
file1 = open("myfile.txt","r")
file1.seek(0)
print(file1.read())
