import argparse


def renumber(file):
	"""Takes a PDB file and returns intramolecular distance restrains"""
	ids = ["ATOM", "HETATOM", "TER"]
	atomnmbr = 0
	new_pdb = ""
	with open(file) as f:
		for line in f:
			identifier = line[0:6].strip()
			if identifier in ids:
				atomnmbr += 1
				atomstr = str(atomnmbr)
				while len(atomstr) < 5:
					atomstr = " " + atomstr
				new_pdb = new_pdb + line.replace(line[6:11], atomstr)
	return new_pdb
				




def main():
	parser = argparse.ArgumentParser(description="Find complex contacts")
	parser.add_argument("pdb_file", help="The path to the pdb file" )
	args = parser.parse_args()
	new_pdb = renumber(args.pdb_file)
	print(new_pdb)
	
if __name__ == "__main__":
	main()