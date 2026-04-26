import pandas as pd

def load_data(counts_path, meta_path, deg_path):
    counts = pd.read_csv(counts_path).set_index('gene_id')
    meta = pd.read_csv(meta_path)
    degs = pd.read_csv(deg_path)

    meta['sample_id'] = meta['gene_id'].astype(str).str.replace(r'^X', '', regex=True)
    meta = meta.set_index('sample_id')

    return counts, meta, degs
