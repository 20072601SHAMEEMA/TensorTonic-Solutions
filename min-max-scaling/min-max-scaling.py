import numpy as np
def min_max_scaling(data: list) -> list:
    """
    Returns each data column scaled to the range from 0 through 1.
    """
    # Write code here
    arr=np.array(data,dtype=float)
    col_min=np.min(arr,axis=0)
    col_max=np.max(arr,axis=0)
    col_range=col_max-col_min
    safe_range=np.where(col_range==0,1.0,col_range)
    scaled_arr=(arr-col_min)/safe_range
    return scaled_arr.tolist()
    pass