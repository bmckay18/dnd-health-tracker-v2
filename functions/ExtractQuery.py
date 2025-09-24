from config import *

def extract_query(file_name: str):
    """
    Extracts the query from a usp file.

    Args:
        filename (str): the name of the usp without the file extension (e.g. uspInsertData)
    
    Returns:
        str: the query from the file
    """

    file_name += '.sql'
    with open(usp_path / file_name, 'r') as f:
        content = f.read()
    
    return content 