df = pd.read_csv(
    "datafile.csv", 
    sep="\s+", 
    names=["lvl12", "etime", "press", ...],
    dtype=str
)