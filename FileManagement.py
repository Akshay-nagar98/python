file=open("tops1.txt","w")
file.write("This is file management demo using python.")
file.close()
print("File Written Succesfully")
print("********************************************")


file=open("tops1.txt","r")
print(file.read())
file.close()
print("********************************************")


file=open("tops1.txt","a")
file.write("\nThis is file is now appended.")
file.close()
print("File Appended Successfully")
print("********************************************")


file=open("tops1.txt","r")
print(file.read())
file.close()
print("********************************************")


file=open("tops2.txt","w+")
file.write("This is w+ mode using python.")
print("Current File Position : ",file.tell())
file.seek(10)
print(file.read())
file.close()
print("w+ Operation Completed")
print("********************************************")
