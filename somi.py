f = open("demofile2.txt", "w")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
# a=f.read()
# print(a)
print(f.read())