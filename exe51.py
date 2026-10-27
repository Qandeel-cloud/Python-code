#  functions of file handling
# if its seek(10) that means it will start reading next from 10th position
# seek (allow to move the current position within the file to a specific point). the position is specified i bytes
# with open('myfile.txt', 'r') as f:
    
    # move to the 10th byte in the file
    # f.seek(10)
    # read the next 5 bytes
    # print(f.tell())
    # data = f.read(5)
    # print(data)

    # f.tell() tells us kha tak seek hoa ha means kha tak read hoa ha 

    # f.truncate() btata ha k yha tak read kro mare file ko simply bs itny characters tak read krna
    # like seek btata ha k kha se read krn ha or yeah btaata ha kha tak read krna ha 

with open('myfile2.txt', 'w') as f:
    f.write("Hello world")
    f.truncate(7)



