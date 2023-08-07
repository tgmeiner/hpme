MIN = 0.0
MIDDLE = 0.5
MAX = 1.0


def make (value:float):
    if value < MIN:
        return MIN
    
    if value > MAX:
        return MAX
    
    return value

def ensure_valid(t):
    raise TParamError(t) 
