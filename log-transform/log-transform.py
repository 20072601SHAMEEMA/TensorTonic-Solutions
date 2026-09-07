import math

def log_transform(values: list) -> list:
    """
    Returns the log1p-transformed values rounded to four decimals.
    """
    # Write code here
    return [round(math.log1p(x),4)for x in values]
    pass