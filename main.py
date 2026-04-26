from src.data_loader import load_data
from src.preprocessing import prepare_features
from src.models import get_models
from src.train import train_models
from src.config import *
import os

if __name__ == "__main__":
    counts, meta, degs = load_data(
        os.path.join(RAW_DIR, "counts.csv"),
        os.path.join(RAW_DIR, "meta.csv"),
        os.path.join(RAW_DIR, "degs.csv"),
    )

    X, y = prepare_features(counts, meta, degs)

    models = get_models(SEED)

    results = train_models(models, X, y, MODEL_DIR)

    print(results)
