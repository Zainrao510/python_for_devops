file = open('data.txt','r')
print(file.read()) #read() method reads the entire content of the file and returns it as a string.
file.close()

#Better method: with with use karne se file automatically close ho jati hai
with open('server.log','r') as file:
     content = file.read()
print(content) #read() method reads the entire content of the file and returns it as a string. The file is automatically closed after the with block.   

#DevOps log processing mein ye bohat useful hai:
with open("server.log", "r") as file:
    for line in file:
        print(line.strip())


#Find errors in the log file: Ye actual DevOps automation ka example hai.
with open("server.log", "r") as file:
    for line in file:
        if "error" in line.lower(): #lower() method converts the string to lowercase, making the search case-insensitive.
            print(line.strip()) #strip() method removes any leading and trailing whitespace characters from the string.



#Write to a file
#w ka matlab write.Agar file already exist karti hai, w purana content replace kar deta hai.
with open("output.txt", "w") as file:
    file.write("This is a new line in the output file.")

#Append : Existing content ko preserve karte hue new content add karna: 
# a ka matlab append. Agar file already exist karti hai, a purana content preserve kar deta hai aur new content add kar deta hai.
with open("output.txt", "a") as file:
    file.write("\nThis is an appended line in the output file.")

#File modes
#Mode	Meaning
#r	Read
#w	Write
#a	Append
#r+	Read + Write    

   