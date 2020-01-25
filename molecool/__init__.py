"""
molecool
A python package for analyzing and visualizing xyz file. For MolSSI Best Practices Workshop
"""

# Add imports here
from .functions import *

# Handle versioneer
from ._version import get_versions
from .measure import calculate_angle, calculate_distance
from .visualize import draw_molecule, draw_bond_histogram
from .molecule import build_bond_list
from .atom_data import atomic_weights, atom_colors
import molecool.io

versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
