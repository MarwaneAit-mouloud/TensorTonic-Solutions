def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    output={}
    for sentence in sentences:
        for word in sentence:
            if word in output:
                output[word]+=1
            else:
                output[word]=1
    return output 