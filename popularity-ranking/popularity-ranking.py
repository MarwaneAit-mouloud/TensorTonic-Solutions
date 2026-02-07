def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    outputs=[]
    for item in items:
        average_rating,num_votes=item
        weighted_rating=(num_votes/(min_votes+num_votes)*average_rating)+(min_votes/(min_votes+num_votes)*global_mean)
        outputs.append(weighted_rating)
    return outputs