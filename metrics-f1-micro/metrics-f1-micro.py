def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    TP=[]
    FN=[]
    for i,j in zip(y_true,y_pred):
        if i==j:
            TP.append(i)
        else:
            FN.append(j)
    return (2*len(TP))/(2*len(TP)+len(FN)+len(FN))
            