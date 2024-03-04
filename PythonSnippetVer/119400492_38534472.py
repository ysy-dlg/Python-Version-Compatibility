distances = pd.DataFrame(np.subtract.outer(tidx, tidx), tidx, tidx).abs()
