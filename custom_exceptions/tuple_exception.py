class TupleException(Exception):
    def __init__(self, message = 'The tuple was missing required paramters'):
        super().__init__(message)