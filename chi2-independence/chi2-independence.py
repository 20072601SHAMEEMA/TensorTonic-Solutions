import numpy as np

def chi2_independence(C: list) -> dict:
    """
    Returns a dictionary with chi2 and expected.
    """
    # Write code here
    obs=np.array(C)
    row_total=np.sum(obs,axis=1)
    col_total=np.sum(obs,axis=0)
    total=np.sum(obs)
    expected =np.outer(row_total,col_total)/total
    chi2=np.sum((obs-expected)**2/expected)
    return {"chi2": float(chi2),"expected": expected}
    pass