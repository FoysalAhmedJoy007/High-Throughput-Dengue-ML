from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

def get_models(seed=42):
    """Returns the study's core model suite."""
    return {
        "rf": RandomForestClassifier(
            n_jobs=-1, 
            class_weight="balanced", 
            random_state=seed
        ),
        "xgb": XGBClassifier(
            objective="binary:logistic",
            eval_metric="logloss",
            random_state=seed
        ),
        "l1_logreg": Pipeline([
            ("scaler", StandardScaler()),
            ("lr", LogisticRegression(
                penalty="l1", 
                solver="liblinear", 
                class_weight="balanced", 
                random_state=seed
            ))
        ])
    }
