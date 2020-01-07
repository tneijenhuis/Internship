import argparse

def remove_anisou(pdb):

	"""Takes a PDB file and removes ANISOU data"""
	
	with open(pdb) as file:
		new_file = ""
		for line in file:
			if line[0:6] != "ANISOU":
				new_file += line

	return new_file

def main():
	parser = argparse.ArgumentParser(description="count intermolecular clashes")
	parser.add_argument("structure", help="The path to the pdb file" )
	args = parser.parse_args()
	new_file = remove_anisou(args.structure)

	print(new_file)

if __name__ == "__main__":
	main()