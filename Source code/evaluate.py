import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score

def plot_roc(models, X, y, save_path):
    plt.figure()

    for name, model in models.items():
        prob = model.predict_proba(X)[:,1]
        fpr, tpr, _ = roc_curve(y, prob)
        auc = roc_auc_score(y, prob)

        plt.plot(fpr, tpr, label=f"{name} AUC={auc:.3f}")

    plt.legend()
    plt.savefig(save_path, dpi=300)
