line = "ATOM   2542  CG  LYS F  29     147.375 232.317 162.666  1.00 45.28           C"

col1 = line[0:6].strip()        #identifier
col2 = line[6:12].strip()       #atomnmbr
col3 = line[12:17].strip()      #atom
col4 = line[17:20].strip()      #residue
col5 = line[21].strip()         #chain
col6 = line[22:26].strip()      #resnmbr
col7 = line[26].strip()         #?
col8 = line[30:38].strip()      #X
col9 = line[38:46].strip()      #Y      
col10 = line[46:54].strip()     #z
col11 = line[54:60].strip()     #occupancy
col12 = line[60:66].strip()     #Temperature factor
col13 = line[72:76].strip()     #Segment identifer
col14 = line[76:78].strip()     #element symbol
col15 = line[79:81].strip()

print(line)
print(col1)
print(col2)
print(col3)
print(col4)
print(col5)
print(col6)
print(col7)
print(col8)
print(col9)
print(col10)
print(col11)
print(col12)
print(col13)
print(col14)
print(col15)