from dataclasses import dataclass
# dataclass - decorator which creates variable for empty class(used for classes without functions)

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
    


