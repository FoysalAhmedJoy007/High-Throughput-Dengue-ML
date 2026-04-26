import numpy as np

def prepare_features(counts, meta, degs):
    sig = degs[(degs['padj'] < 0.05) & (degs['log2FoldChange'].abs() > 1)]
    genes = counts.index.intersection(sig.iloc[:,0])

    X = np.log1p(counts.loc[genes]).T
    samples = X.index.intersection(meta.index)

    X = X.loc[samples]
    y = meta.loc[samples, 'condition']

    label_map = {'convalescent': 0, 'acute': 1}
    y = y.astype(str).str.lower().map(label_map)

    return X, y
