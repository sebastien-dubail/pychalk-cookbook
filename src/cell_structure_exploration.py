from cookbook_tools import *    
from pychalk import *
from pathlib import Path

print('Loading cell structure from CIF file...')

cell = PyCellStructureUnit(data_path + "/TiN.cif")

print(f"cell volume: {cell.cell_volume} ({cell.cell_a},{cell.cell_b},{cell.cell_c})")
