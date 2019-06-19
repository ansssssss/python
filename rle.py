def userInput():
    user = input("""1. Enter RLE
2. Display ASCII art
3. Convert to ASCII art
4. Convert to RLE
5. Quit
Enter a choice: """)
    if user == "1":
        enterRle()
    elif user == "2":
        displayArt()
    elif user == "3":
        convertArt()
    elif user == "4":
        convertRle()
    elif user == "5":
        print("Exiting...")
        quit()
    else:
        print("Invalid input")

def enterRle():
    rle = []
    noOfLines = 0
    while noOfLines < 2:
        noOfLines = input("Number of lines: ")
        if noOfLines.isnumeric():
            noOfLines = int(noOfLines)
            if int(noOfLines) < 2:
                print("Must be greater than 2 lines")
        else:
            noOfLines = 0
            print("Enter a number")
        
            
        
    for i in range(noOfLines):
        line = input("Enter line of RLE: ")
        rle.append(line)
    asciiDisplay(rle)

def asciiDisplay(rle):
    for i in range(0,len(rle)):
        display = ""
        for j in range(len(rle[i])//3):
            xd = 3*j
            onething = rle[i][xd:xd+3]
            length = int(onething[0:2])
            char = onething[2:]
            display += length * char
        print(display)
       


def displayArt():
    namefile = input("Enter name of file with .txt: ")
    f=open(namefile,"r")
    print(f.read())
    f.close()
        


def convertArt(): 
    namefile = input("Enter name of file with .txt: ")
    f=open(namefile,"r")
    lines = f.read().splitlines()
    asciiDisplay(lines)

def convertRle():
    q=""
    namefile = input("Enter name of file with .txt: ")
    f=open(namefile,"r")
 
    lines = f.read()
    linelength = len(lines)
    f.close()
    count = 1
    prev = ''
    lst = []
    for character in lines:
        if character != prev:
            if prev:
                if count < 10:
                    count = "0" + str(count)
                if prev != "\n":
                    entry = str(count)+prev
                else:
                    entry = "\n"
                lst.append(entry)

            count = 1

            prev = character
        else:
            count += 1
            
    else:
        if count < 10:
            count = "0" + str(count)
        if  character != "\n":
            entry = str(count)+character
        else:
            entry = "\n"
        lst.append(entry)
    for i in range(len(lst)):
        q += lst[i]
    newname = input("Enter new file name: ")
    with open(newname+".txt","w") as f:
        f.write(q)
        print("Your file has been saved as",newname+".txt!")
        print("With RLE: ~",str(len(q)),"bytes")
        print("Uncompressed: ~",str(linelength),"bytes")
        if linelength < len(q):
            print("RLE file is bigger than uncompressed, so it's better not to use it in this case! Bigger by:",str(len(q)-linelength),"bytes!")
        else:
            print("Congrats, you shrunk your file size by:", str(linelength-len(q)),"bytes!")
        


 
                
            
            

while True:
    userInput()
