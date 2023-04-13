"""
Test data for MTpy

"""

# =============================================================================
# Imports
# =============================================================================
from pathlib import Path

# =============================================================================

PROFILE = Path(__file__).parent.joinpath("data/profile")
GRID = Path(__file__).parent.joinpath("data/grid")

PROFILE_LIST = list(PROFILE.glob("*.edi"))
GRID_LIST = list(GRID.glob("*.edi"))
