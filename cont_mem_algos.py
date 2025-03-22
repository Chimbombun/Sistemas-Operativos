def worst_fit(memory, req: int, index: int):
    if type(memory) != list or not memory or req <= 0 or index < 0 or index >= len(memory):
        return None

    memory_blocks = memory.copy()
    n_blocks = len(memory_blocks)
    best_fit_index = -1
    best_block = None
    max_remaining = -1

    pos = index
    for _ in range(n_blocks):
        base, size = memory_blocks[pos]
        if size >= req:
            remaining = size - req
            if remaining > max_remaining:
                max_remaining = remaining
                best_block = (base, size)
                best_fit_index = pos
        pos = (pos + 1) % n_blocks

    if best_fit_index == -1:
        return None

    base, size = best_block

    if size == req:
        del memory_blocks[best_fit_index]
        new_index = best_fit_index % len(memory_blocks) if memory_blocks else 0
        return memory_blocks, base, req, new_index
    else:
        memory_blocks[best_fit_index] = (base + req, size - req)
        return memory_blocks, base, req, best_fit_index

