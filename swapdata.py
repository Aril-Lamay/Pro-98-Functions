def swap():
    pathf1 = 'C:/Users/arill/OneDrive/Desktop/VS code/Python Code/Project-98/file1.txt'
    pathf2 = 'C:/Users/arill/OneDrive/Desktop/VS code/Python Code/Project-98/file2.txt'
    
    with open(pathf1,'r') as a:
        file1 = a.read()

    with open(pathf2,'r') as b:
        file2 = b.read()

    with open(pathf1,'w') as a:
        a.write(file2)

    with open(pathf2,'w') as b:
        b.write(file1)

swap()