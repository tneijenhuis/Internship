#----------------------------------------------------------------------------------------
# This script is called as:
#
#    chimera --nogui --script "CCcalculate <pdb file> <map> <resolution> <n searches>"
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

res = float(sys.argv[3])
search = int(sys.argv[4])

models = chimera.openModels.open(sys.argv[1])
model = models[0]
synth_map = molmap.molecule_map(model.atoms, res)

em_map = VolumeViewer.open_volume_file(sys.argv[2])[0]
select = chimera.selection.ItemizedSelection([synth_map])
fit_list = fitmap(select, em_map, search = search, listFits = False)

measure.correlation("correlation", [synth_map], [em_map])
