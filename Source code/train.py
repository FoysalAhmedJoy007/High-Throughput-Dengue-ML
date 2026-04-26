from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
import numpy as np
import joblib
import os

def train_models(models, X, y, model_dir):
    cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
    results = {}

    for name, model in models.items():
        aucs = []

        for fold, (tr, te) in enumerate(cv.split(X, y)):
            model.fit(X.iloc[tr], y.iloc[tr])

            prob = model.predict_proba(X.iloc[te])[:,1]
            auc = roc_auc_score(y.iloc[te], prob)

            aucs.append(auc)

            joblib.dump(model, os.path.join(model_dir, f"{name}_fold{fold}.pkl"))

        results[name] = (np.mean(aucs), np.std(aucs))

    return results
