import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x=np.asarray(x)
    n=x.shape[0]

    mean=np.mean(x)

    variance=np.sum((x-mean)**2)/(n-1)
    std_variance=np.sqrt(variance)
    return (variance,std_variance)


