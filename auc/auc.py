import numpy as np


def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    fpr = np.array(fpr)
    tpr = np.array(tpr)
    
    if len(fpr) == len(tpr) and len(fpr) >= 2:
        area = np.trapezoid(tpr, x=fpr) # le fpr est sur l'abscisse tandis ce que le tpr est sur l'ordonnée
        
        return float(np.abs(area))
    else:
        return 0.0