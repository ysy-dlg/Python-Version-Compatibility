def my_fn(x, b, a):
    y = np.zeros_like(x)
    nonzero = x != 0
    x = x[nonzero]
    y[nonzero] = b*(1/np.tanh(x/a) - a/x)
    return y