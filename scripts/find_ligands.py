import argparse
	
def find_ligands(path):
	"""returns a list containing the ligands present in a file"""

	with open(path) as file:
		ligands = []
		for line in file:
			col1 = line[0:6].strip()
			if col1 == "HETATM":
				col4 = line[17:20].strip()      #residue
				if col4 not in ligands:
					ligands.append(col4)
		return ligands 


def main():
	parser = argparse.ArgumentParser(description="Find ligands in pdb file")
	parser.add_argument("pdb", help="The path to the pdb file" )
	args = parser.parse_args()
	ligand_list = find_ligands(args.pdb)
	
	for i in range(len(ligand_list)):
		print(ligand_list[i])

if __name__ == "__main__":
	main()