from pychalk import *
from pathlib import Path

# Resolve the data directory path relative to the current module location
data_path = Path(__file__).parent.parent.joinpath("data").resolve().as_posix()

# Resolve the output directory path and create it if it doesn't exist
output_dir = Path(__file__).parent.parent.joinpath("output").resolve()
output_dir.mkdir(parents=True, exist_ok=True)

# Convert the output directory path to POSIX format for compatibility
output_path = output_dir.as_posix()


