f = open('myfile.txt', 'r')
text = f.read()
print(text)
f.close()

f = open('myfile2.txt', 'a')
# text = f.write()
f.write("me and only me")

# print(text)
f.close()