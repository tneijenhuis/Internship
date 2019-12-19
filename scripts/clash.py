import interfacea as ia
import argparse

parser = argparse.ArgumentParser(description="count intermolecular clashes")
parser.add_argument("structure", help="The path to the pdb file" )
args = parser.parse_args()

mol = ia.read(args.structure)

analyzer = ia.InteractionAnalyzer(mol)
analyzer.get_clashes(cutoff = 0.6)

df = analyzer.itable._table
print(df.shape[0])


