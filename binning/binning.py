def binning(values: list, num_bins: int) -> list:
    """
    Returns the equal-width bin index of every value.
    """
    # Write code here
    min_val=min(values)
    max_val=max(values)
    if min_val==max_val:
        return [0]*len(values)
    w=(max_val-min_val)/num_bins
    result=[]
    for x in values:
        bin_index=int((x-min_val)/w)
        clamped_id=min(bin_index,num_bins-1)
        result.append(clamped_id)
    return result    
    pass