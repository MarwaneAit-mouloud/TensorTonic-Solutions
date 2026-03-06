def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    chunks = []
    step = 0
    while step < len(tokens):   
        chunk = []
        if step > 0:
            start = step - overlap
        else:
            start = 0

        for j in tokens[start : start + chunk_size]:
            chunk.append(j) 
        chunks.append(chunk)
        step = start + chunk_size
        if step >= len(tokens) or overlap >= chunk_size:
            break

    return chunks
        
    