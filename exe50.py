# f= open('myfile.txt', 'r')
# i=0
# while True:
#     i=i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print (f"Students marks  {i} of Maths: {m1} ")
#     print (f"Students marks  {i} of English: {m2} ")
#     print (f"Students marks  {i} of SST: {m3} ")


#     # if not line:
#     #     break
#     print(line)

f= open('myfile2.txt', 'w')
lines = ('Line 1','Line 2','Line 3')
for line in lines:
      f.write(line + '\n')
f.close()

