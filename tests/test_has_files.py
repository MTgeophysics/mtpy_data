import unittest

from mtpy_data import (
    PROFILE,
    GRID,
    FWD_FAULTS,
    FWD_HALFSPACE,
    FWD_CONDUCTIVE_CUBE,
    FWD_RESISTIVE_CUBE,
    FWD_LAYERED_HALFSPACE,
    FWD_NEAR_SURFACE_CONDUCTIVE_CUBE,
    FWD_NE_CONDUCTOR,
    FWD_NE_FAULTS,
    PROFILE_LIST,
    GRID_LIST,
    FWD_FAULTS_GRID_LIST,
    FWD_HALFSPACE_GRID_LIST,
    FWD_CONDUCTIVE_CUBE_GRID_LIST,
    FWD_RESISTIVE_CUBE_GRID_LIST,
    FWD_LAYERED_HALFSPACE_GRID_LIST,
    FWD_NEAR_SURFACE_CONDUCTIVE_CUBE_GRID_LIST,
    FWD_NE_CONDUCTOR_GRID_LIST,
    FWD_NE_FAULTS_GRID_LIST,
    FWD_FAULTS_PROFILE_LIST,
    FWD_HALFSPACE_PROFILE_LIST,
    FWD_CONDUCTIVE_CUBE_PROFILE_LIST,
    FWD_RESISTIVE_CUBE_PROFILE_LIST,
    FWD_LAYERED_HALFSPACE_PROFILE_LIST,
    FWD_NEAR_SURFACE_CONDUCTIVE_CUBE_PROFILE_LIST,
    FWD_NE_CONDUCTOR_PROFILE_LIST,
    FWD_NE_FAULTS_PROFILE_LIST,
)


class TestHasFiles(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.edi_lists = [
            PROFILE_LIST,
            GRID_LIST,
            FWD_FAULTS_GRID_LIST,
            FWD_HALFSPACE_GRID_LIST,
            FWD_CONDUCTIVE_CUBE_GRID_LIST,
            FWD_RESISTIVE_CUBE_GRID_LIST,
            FWD_LAYERED_HALFSPACE_GRID_LIST,
            FWD_NEAR_SURFACE_CONDUCTIVE_CUBE_GRID_LIST,
            FWD_NE_CONDUCTOR_GRID_LIST,
            FWD_NE_FAULTS_GRID_LIST,
            FWD_FAULTS_PROFILE_LIST,
            FWD_HALFSPACE_PROFILE_LIST,
            FWD_CONDUCTIVE_CUBE_PROFILE_LIST,
            FWD_RESISTIVE_CUBE_PROFILE_LIST,
            FWD_LAYERED_HALFSPACE_PROFILE_LIST,
            FWD_NEAR_SURFACE_CONDUCTIVE_CUBE_PROFILE_LIST,
            FWD_NE_CONDUCTOR_PROFILE_LIST,
            FWD_NE_FAULTS_PROFILE_LIST,
        ]

        self.edi_paths = [
            PROFILE,
            GRID,
            FWD_FAULTS,
            FWD_HALFSPACE,
            FWD_CONDUCTIVE_CUBE,
            FWD_RESISTIVE_CUBE,
            FWD_LAYERED_HALFSPACE,
            FWD_NEAR_SURFACE_CONDUCTIVE_CUBE,
            FWD_NE_CONDUCTOR,
            FWD_NE_FAULTS,
        ]

    def test_list_not_empty(self):
        for index, edi_list in enumerate(self.edi_lists):
            with self.subTest(f"{index}"):
                self.assertTrue(len(edi_list) > 0)

    def test_paths_exists(self):
        for index, edi_path in enumerate(self.edi_paths):
            with self.subTest(f"{index}"):
                self.assertTrue(edi_path.exists())


if __name__ == "__main__":
    unittest.main()
