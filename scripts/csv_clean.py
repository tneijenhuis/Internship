import argparse

def clean_csv(file):

	linenmbr = 0
	new_csv = ""
	with open(file) as f:
		for line in f:
			linenmbr += 1
			if linenmbr == 1:
				header = line
				new_csv += line
			else:
				if line == header:
					continue
				else:
					new_csv += line

	return new_csv



def main():
	parser = argparse.ArgumentParser(description="removes accidental extra headers insite of the csv")
	parser.add_argument("csv", help="The path to the csv file" )
	args = parser.parse_args()
	new_csv = clean_csv(args.csv)
	
	print(new_csv)
	
if __name__ == "__main__":
	main()