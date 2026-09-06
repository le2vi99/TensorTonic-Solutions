import math
from scipy.special import factorial

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """

    f_n = math.factorial(n)

    kth = np.arange(k+1)
    coef = f_n / (factorial(kth) * factorial(n-kth))
    val = (p**kth) * ((1-p)**(n-kth))
    binomials = coef*val
    pmf = binomials[-1].item()
    cdf = binomials.sum().item()
    
    # Write code here
    return {"pmf": pmf, "cdf": cdf}