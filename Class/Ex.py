try :
    klu1=open("File.txt","w")
    try:
        klu1.write("This Is S1 Section")
    finally:
        klu1.close()
except IOError:
    print("File Not Found")
else:
    print("The File Opened Successfully")
    klu1.close()