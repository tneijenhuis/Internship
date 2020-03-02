#----------------------------------------------------------------------------------------
# This script is called as:
#
#    chimera --nogui --script "CCcalculate_wref.py <pdb file> <reference PDB> <map> <resolution> "
#
# A synthetic map of the PDB structure with the resolution of the experimental map
# will be generated and fitted on the experimental map with n searches.
# After fitting, the correlation of the best fitted structure is measured
#----------------------------------------------------------------------------------------
import chimera
import VolumeViewer
import sys
from MoleculeMap import molmap
from FitMap.fitcmd import fitmap
from Measure import measure
import Midas


res = float(sys.argv[4])

models = chimera.openModels.open(sys.argv[1])

refs= chimera.openModels.open(sys.argv[2])

em_map = VolumeViewer.open_volume_file(sys.argv[3])[0]

model = models[0]
ref = refs[0]

modellist = []
reflist = []
for atom in model.atoms:
    if "CA" == atom.name:
        modellist.append(atom)
        

for atom in ref.atoms:
    if len(reflist) == len(modellist):
        continue   
    if "CA" == atom.name:
        reflist.append(atom)

if len(reflist) == 0:
    modellist = []
    reflist = []
    for atom in model.atoms:
        if atom.name == "CB":
            modellist.append(atom)
    for atom in ref.atoms:
        if len(reflist) == len(modellist):
            continue 
        if atom.name == "CB":
            reflist.append(atom)
  


Midas.match(modellist, reflist)

synth_map = molmap.molecule_map(model.atoms, res)
select = chimera.selection.ItemizedSelection([synth_map])
fitmap(select, em_map, listFits = False)

measure.correlation("correlation", [synth_map], [em_map])
