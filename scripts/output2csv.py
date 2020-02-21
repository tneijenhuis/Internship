import argparse

def make_csv(file, rowsplit="."):
	with open(file) as f:
		csv = ""
		for line in f:
			line = line.strip()
			if line == rowsplit:
				csv = csv[:-1] + "\n"						
			else:
				csv += line + ","
	return csv



def main():
	parser = argparse.ArgumentParser(description="Converts a concatonated file to a CSV file")
	parser.add_argument("input_file", help="Path to concatonated file")
	args = parser.parse_args()
	new_file = make_csv(args.input_file)
	print(new_file)
	

if __name__ == '__main__':
	main()