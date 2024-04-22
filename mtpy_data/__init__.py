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

FWD_FAULTS = Path(__file__).parent.joinpath("forward_models/Faults")
FWD_HALFSPACE = Path(__file__).parent.joinpath("forward_models/HalfSpace")
FWD_CONDUCTIVE_CUBE = Path(__file__).parent.joinpath(
    "forward_models/HalfSpaceSQC"
)
FWD_RESISTIVE_CUBE = Path(__file__).parent.joinpath(
    "forward_models/HalfSpaceSQR"
)
FWD_LAYERED_HALFSPACE = Path(__file__).parent.joinpath(
    "forward_models/LayeredHalfSpace"
)
FWD_NEAR_SURFACE_CONDUCTIVE_CUBE = Path(__file__).parent.joinpath(
    "forward_models/NearSquareConductor"
)
FWD_NE_CONDUCTOR = Path(__file__).parent.joinpath("forward_models/NEConductor")
FWD_NE_FAULTS = Path(__file__).parent.joinpath("forward_models/NEFaults")

PROFILE_LIST = list(PROFILE.glob("*.edi"))
GRID_LIST = list(GRID.glob("*.edi"))

### FORWARD list of EDI files for a GRID
FWD_FAULTS_GRID_LIST = list(FWD_FAULTS.glob("*.edi"))
FWD_HALFSPACE_GRID_LIST = list(FWD_HALFSPACE.glob("*.edi"))
FWD_CONDUCTIVE_CUBE_GRID_LIST = list(FWD_CONDUCTIVE_CUBE.glob("*.edi"))
FWD_RESISTIVE_CUBE_GRID_LIST = list(FWD_RESISTIVE_CUBE.glob("*.edi"))
FWD_LAYERED_HALFSPACE_GRID_LIST = list(FWD_LAYERED_HALFSPACE.glob("*.edi"))
FWD_NEAR_SURFACE_CONDUCTIVE_CUBE_GRID_LIST = list(
    FWD_NEAR_SURFACE_CONDUCTIVE_CUBE.glob("*.edi")
)
FWD_NE_CONDUCTOR_GRID_LIST = list(FWD_NE_CONDUCTOR.glob("*.edi"))
FWD_NE_FAULTS_GRID_LIST = list(FWD_NE_FAULTS.glob("*.edi"))
FWD_FAULTS_GRID_LIST = list(FWD_FAULTS.glob("*.edi"))
FWD_HALFSPACE_GRID_LIST = list(FWD_HALFSPACE.glob("*.edi"))
FWD_CONDUCTIVE_CUBE_GRID_LIST = list(FWD_CONDUCTIVE_CUBE.glob("*.edi"))
FWD_RESISTIVE_CUBE_GRID_LIST = list(FWD_RESISTIVE_CUBE.glob("*.edi"))
FWD_LAYERED_HALFSPACE_GRID_LIST = list(FWD_LAYERED_HALFSPACE.glob("*.edi"))
FWD_NEAR_SURFACE_CONDUCTIVE_CUBE_GRID_LIST = list(
    FWD_NEAR_SURFACE_CONDUCTIVE_CUBE.glob("*.edi")
)
FWD_NE_CONDUCTOR_GRID_LIST = list(FWD_NE_CONDUCTOR.glob("*.edi"))
FWD_NE_FAULTS_GRID_LIST = list(FWD_NE_FAULTS.glob("*.edi"))

### FORWARD list of EDI files for a PROFILE
FWD_FAULTS_PROFILE_LIST = list(FWD_FAULTS.glob("*ew.edi"))
FWD_HALFSPACE_PROFILE_LIST = list(FWD_HALFSPACE.glob("*ew.edi"))
FWD_CONDUCTIVE_CUBE_PROFILE_LIST = list(FWD_CONDUCTIVE_CUBE.glob("*ew.edi"))
FWD_RESISTIVE_CUBE_PROFILE_LIST = list(FWD_RESISTIVE_CUBE.glob("*ew.edi"))
FWD_LAYERED_HALFSPACE_PROFILE_LIST = list(FWD_LAYERED_HALFSPACE.glob("*ew.edi"))
FWD_NEAR_SURFACE_CONDUCTIVE_CUBE_PROFILE_LIST = list(
    FWD_NEAR_SURFACE_CONDUCTIVE_CUBE.glob("*ew.edi")
)
FWD_NE_CONDUCTOR_PROFILE_LIST = list(FWD_NE_CONDUCTOR.glob("*ew.edi"))
FWD_NE_FAULTS_PROFILE_LIST = list(FWD_NE_FAULTS.glob("*ew.edi"))
FWD_FAULTS_PROFILE_LIST = list(FWD_FAULTS.glob("*ew.edi"))
FWD_HALFSPACE_PROFILE_LIST = list(FWD_HALFSPACE.glob("*ew.edi"))
FWD_CONDUCTIVE_CUBE_PROFILE_LIST = list(FWD_CONDUCTIVE_CUBE.glob("*ew.edi"))
FWD_RESISTIVE_CUBE_PROFILE_LIST = list(FWD_RESISTIVE_CUBE.glob("*ew.edi"))
FWD_LAYERED_HALFSPACE_PROFILE_LIST = list(FWD_LAYERED_HALFSPACE.glob("*ew.edi"))
FWD_NEAR_SURFACE_CONDUCTIVE_CUBE_PROFILE_LIST = list(
    FWD_NEAR_SURFACE_CONDUCTIVE_CUBE.glob("*ew.edi")
)
FWD_NE_CONDUCTOR_PROFILE_LIST = list(FWD_NE_CONDUCTOR.glob("*ew.edi"))
FWD_NE_FAULTS_PROFILE_LIST = list(FWD_NE_FAULTS.glob("*ew.edi"))
