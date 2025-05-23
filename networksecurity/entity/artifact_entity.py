from dataclasses import dataclass
# dataclass - decorator which creates variable for empty class(used for classes without functions)

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
    
@dataclass
class DataValidationArtifact:
    validation_status:bool
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path:str
    

