import sys

s=open('sudoko.txt', 'r')
puzzle=[]
reference=set('123456789')
print("Sudoko grid")
for line in s:
    print( line.rstrip('\n').split(' ') )
    puzzle.append(line.rstrip('\n').split(' '))

print("\nCheck Rows")
for row in range(0, 9):
    check=set(puzzle[row][0:9])
    if (check-reference == set()) and (reference-check == set()): print('Row %d Good' % row) 
    else: print('Row %d Bad' % row)
    
print("\nCheck Columns")
for col in range(0, 9):
    temp = [ row[col] for row in puzzle ]
    #check=set(temp)
    if (set(temp)-reference == set()) and (reference-set(temp) == set()): print('Col %d Good' % col) 
    else: print('Col %d Bad' % col)

print("\nCheck 3x3 boxes")
box=0
for row in range(0,9,3):
    check=[]; temp=[]
    for col in range(0,9,3):
        check=[]; temp=[]
        for coffset in range(0,3):
            for roffset in range(0,3):
                temp.append(puzzle[row+roffset][col+coffset])
        if (set(temp)-reference == set()) and (reference-set(temp) == set()): print('Box %d Good' % box)
        else: print('Box %d Bad' % box)
        box=box+1