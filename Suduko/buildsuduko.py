import random

puzzle=[]
for row in range(9):
    prow=[]
    while len(prow) < 9:
        item=random.randint(1,9)
        if item not in prow:
            prow.append(item)
            #print (row, prow, item, len(prow))
            
    puzzle.append(prow)
    
newfile=open("newsuduko.txt", 'w')    
for row in puzzle:
    print(row)
    newfile.write( " ".join( str(item) for item in row ) + '\n')
    
newfile.close()