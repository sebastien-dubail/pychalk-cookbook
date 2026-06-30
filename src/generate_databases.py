from cookbook_tools import *
from pychalk import *
from pathlib import Path

def build_database_with_seed(source, output):
    path = Path(__file__).parent.parent.resolve().as_posix()

    print("Loading theoretical model...")
    model = PyChalkElectronsTheoreticalModel(source)

    print("Creating acquisition setup...")
    acquisition_setup = model.create_default_acquisition_setup(360)
    acquisition_setup.BeamType = PyChalkParticleBeamType.Electrons
    acquisition_setup.tilt_axis = PyChalkGeometryAxis.X

    print("Generating seeded database...")
    database = model.generate_seeded_database(output, acquisition_setup, size=2500, seed=42)
    ca = database.load_chunk(0)
    labels = ca.labels.to_numpy_float()
    vectors = ca.theoretical_data.to_numpy_float()

    print(f"\nlabels shape: {labels.shape}")
    print(f"labels elements: {labels.size}")
    print("\nlabels first 3 cols:")
    print(labels[:, :3])

    print(f"\nvectors shape: {vectors.shape}")
    print(f"vectors elements: {vectors.size}")
    print("\nvectors first 3 cols:")
    print(vectors[:, :3])



def load_chunks_from_database(output: str):
    
    print("Loading database model...")
    database = PyChalkTheoreticalDatabase(output);

    for i in range(database.chunk_count):
        print(f"\nLoading chunk {i} of {database.chunk_count}...")
        ca = database.load_chunk(i)
        labels = ca.labels.to_numpy_float()
        vectors = ca.theoretical_data.to_numpy_float()
        print(f"\nlabels shape: {labels.shape}")
        print(f"labels elements: {labels.size}")
        print(f"\nvectors shape: {vectors.shape}")
        print(f"vectors elements: {vectors.size}")


source_file = data_path + "/TheoreticalModel.crdtm"
output_file = output_path + "/database.crddb"

build_database_with_seed(source_file, output_file)
load_chunks_from_database(output_file)

