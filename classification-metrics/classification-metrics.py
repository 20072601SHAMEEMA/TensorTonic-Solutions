import numpy as np

def classification_metrics(y_true: list[int], y_pred: list[int], average: str = "micro", pos_label: int = 1) -> dict:
    """
    Returns a dictionary containing accuracy, precision, recall, and f1 rounded to six decimals.
    """
    # Write code here
    y_true=np.array(y_true)
    y_pred=np.array(y_pred)
    accuracy = np.mean(y_true == y_pred)
    classes=np.unique(np.concatenate([y_true,y_pred]))
    if average=="binary":
        classes=np.array([pos_label])
    precisions,recalls,f1s,supports=[],[],[],[]   
    total_tp=total_fp=total_fn=0
    for c in classes:
        tp=np.sum((y_pred==c)&(y_true==c))
        fp=np.sum((y_pred==c)&(y_true!=c))
        fn=np.sum((y_pred!=c)&(y_true==c))
        support=np.sum(y_true==c)
        total_tp+=tp
        total_fp+=fp
        total_fn+=fn
        p=tp/(tp+fp) if(tp+fp)>0 else 0.0
        r=tp/(tp+fn) if(tp+fn)>0 else 0.0
        f=2*p*r/(p+r) if(p+r)>0 else 0.0
        precisions.append(p)
        recalls.append(r)
        f1s.append(f)
        supports.append(support)
    if average == "micro":
        p_final = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
        r_final = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0
        f1_final = 2 * p_final * r_final / (p_final + r_final) if (p_final + r_final) > 0 else 0.0
    elif average == "macro":
        p_final = np.mean(precisions)
        r_final = np.mean(recalls)
        f1_final = np.mean(f1s)
    elif average == "weighted":
        total_support = np.sum(supports)
        if total_support > 0:
            p_final = np.average(precisions, weights=supports)
            r_final = np.average(recalls, weights=supports)
            f1_final = np.average(f1s, weights=supports)
        else:
            p_final = r_final = f1_final = 0.0
    elif average == "binary":
        p_final, r_final, f1_final = precisions[0], recalls[0],        f1s[0]

    return {
        "accuracy": round(float(accuracy), 6),
        "precision": round(float(p_final), 6),
        "recall": round(float(r_final), 6),
        "f1": round(float(f1_final), 6)
    }
    pass