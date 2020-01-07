import argparse

def find_gap(pdb):
	 
	"""Finds and prints location of gaps in monomeric protein structures"""

	with open(pdb) as file:
		res = 0
		for line in file:
			ident = line[0:6].strip()       #identifier
			if ident == "ATOM":
				resnmbr = line[22:26].strip()
				resnmbr = int(resnmbr)      #resnmbr
				if resnmbr == res or resnmbr == res + 1:
					res = resnmbr
				elif res == 0:
					res = resnmbr

				else :
					print("gap between {} and {}".format(res, resnmbr))
					res = resnmbr



def main():
	parser = argparse.ArgumentParser(description="count intermolecular clashes")
	parser.add_argument("structure", help="The path to the pdb file" )
	args = parser.parse_args()
	find_gap(args.structure)

	
if __name__ == "__main__":
	main()
