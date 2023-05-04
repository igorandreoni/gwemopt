"""
Module for defining paths to data directories.
"""
from pathlib import Path

DATA_DIR = Path(__file__).parent.absolute().joinpath("data")

DEFAULT_CONFIG_DIR = DATA_DIR.joinpath("config")
DEFAULT_TILING_DIR = DATA_DIR.joinpath("tiling")
DEFAULT_LIGHTCURVE_DIR = DATA_DIR.joinpath("lightcurves")
DEFAULT_BASE_OUTPUT_DIR = Path.home().joinpath("Data/gwemopt/")

TESSELATION_DIR = DATA_DIR.joinpath("tesselations")
REFS_DIR = DATA_DIR.joinpath("refs")

SKYMAP_DIR = DEFAULT_BASE_OUTPUT_DIR.joinpath("skymaps")
SKYMAP_DIR.mkdir(exist_ok=True, parents=True)

test_skymap = DATA_DIR.joinpath("skymaps/S190425z_2_LALInference.fits.gz")