import math
import argparse

def complex_clash(path):

    """Takes a complex pdb file and returns the amount if intramolecular clashes"""

    with open(path) as file:
        residues = []
        for line in file:
            col1 = line[0:6].strip()    #identifier
            col3 = line[12:17].strip()  #atom type
            col5 = line[21:22].strip()  #chain
            col6 = line[23:27].strip()  #residue number
            col8 = line[30:38].strip()  #x position
            col9 = line[38:46].strip()  #y position
            col10 = line[46:54].strip() #z position
            col13 = line[72:76].strip() #atom
            if col1 == "ATOM" and col13 != "H":
                residues.append([col3, col5, col6, float(col8), float(col9), float(col10)]) 

    contacts = []
    clashes = 0
    for i in range(len(residues)):
        residue = residues[i]
        for j in range(i + 1, len(residues)):
            target = residues[j]
            if residue[1] != target[1]:
                distance = math.sqrt(math.pow(residue[3] - target[3], 2) + math.pow(residue[4] - target[4], 2) + math.pow(residue[5] - target[5], 2))
                if distance <= 3:
                    interact = "{}{}{}{}".format(residue[1], residue[2], target[1], target[2])
                    if interact not in contacts:
                        clashes +=1
                        contacts.append(interact)

    return clashes, contacts

def main():
    parser = argparse.ArgumentParser(description="Find complex clashes")
    parser.add_argument("complex_pdb", help="The path to the complex pdb file" )
    parser.add_argument("-c", "--clashlist", help="if True, gives a list of clashing residues", action="store_true")
    args = parser.parse_args()
    clashes, contacts = complex_clash(args.complex_pdb)
    
    print(clashes)

    if args.clashlist:
        print(contacts)

if __name__ == "__main__":
    main()