from config import *

def ExtractQuery(filename: str):
    """
    Extracts the query from a usp file.

    Args:
        filename (str): the name of the usp without the file extension (e.g. uspInsertData)
    
    Returns:
        str: the query from the file
    """

    filename += '.sql'
    with open(usp_path / filename, 'r') as f:
        content = f.read()
    
    return content 