class ConnectionError(Exception):
    """Exception for connection to Smart Device"""
    
    def __init__(self, message):
        self.message = message

