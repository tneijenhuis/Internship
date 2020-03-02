import math
import argparse


def complex_contacts(path, max_dist):
	"""Takes a PDB file and returns intramolecular distance restrains"""

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
	       
			if col1 == "ATOM" and  col3 == "CA":
				residues.append([col3, col5, col6, float(col8), float(col9), float(col10)]) 

	contacts = []
	
	for i in range(len(residues)):
		residue = residues[i]


		for j in range(i, len(residues)):
			target = residues[j]
			if residue[1] != target[1]:
				distance = math.sqrt(math.pow(residue[3] - target[3], 2) + math.pow(residue[4] - target[4], 2) + math.pow(residue[5] - target[5], 2))
				if distance < max_dist:
					contacts.append([residue[1], residue[2], residue[0], target[1], target[2], target[0], 8, 0.0])
					
	return contacts

def main():
	parser = argparse.ArgumentParser(description="Find complex contacts")
	parser.add_argument("complex_pdb", help="The path to the complex pdb file" )
	parser.add_argument("-m", "--maxdist", default = 8, help=" Optional maximal distance of alpha carbons, default = 8", type=int)
	args = parser.parse_args()
	contact_list = complex_contacts(args.complex_pdb,args.maxdist)
	
	for i in range(len(contact_list)):
		contact_res = contact_list[i]
		print("assi (segid {} and resid {} and (name {} or name BB)) (segid {} and resid {} and (name {} or name BB)) {} {} {}".format(contact_res[0], contact_res[1], contact_res[2], contact_res[3], contact_res[4], contact_res[5], contact_res[6], contact_res[6], contact_res[7]))

if __name__ == "__main__":
	main()
