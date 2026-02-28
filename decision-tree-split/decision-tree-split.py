def gini(labels):
    pk=[]
    for i in set(labels):
        count_k=labels.count(i)
        total=len(labels)
        pk.append(count_k/total)
    return 1 - sum(pk*pk for pk in pk)

def decision_tree_split(X, y):
    n_samples = len(X)
    if n_samples == 0:
        return None, None
    
    n_features = len(X[0])
    parent_impurity = gini(y)
    
    best_gain = -1
    best_feature = None
    best_threshold = None
    
    for feature_idx in range(n_features):
        feature_values = sorted(set([row[feature_idx] for row in X]))
        thresholds=[]
        for i in range(len(feature_values)-1):
            if feature_values[i+1] :
                thresholds.append((feature_values[i]+feature_values[i+1])/2)
            else :
                break
        unique_thresholds = sorted(set(thresholds))
        
        for threshold in unique_thresholds:
            left_y = []
            right_y = []
            
            for i in range(n_samples):
                if X[i][feature_idx] <= threshold:
                    left_y.append(y[i])
                else:
                    right_y.append(y[i])
            
            if not left_y or not right_y:
                continue
            
            w_left = len(left_y) / n_samples
            w_right = len(right_y) / n_samples
            child_impurity = (w_left * gini(left_y)) + (w_right * gini(right_y))
            
            gain = parent_impurity - child_impurity
            
            if gain > best_gain:
                best_gain = gain
                best_feature = feature_idx
                best_threshold = threshold
                
    return best_feature, best_threshold