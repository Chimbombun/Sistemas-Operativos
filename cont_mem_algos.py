def cont_mem_algos(memory, req, start_index):
    if not memory:
        return None

    normalized_memory = []
    index_map = []

    for i, (base, limit_or_size) in enumerate(memory):
        base, limit_or_size = int(base), int(limit_or_size)

        if limit_or_size < base:
            limit = base + limit_or_size
        else:
            limit = limit_or_size

        if limit <= base:
            continue

        normalized_memory.append((base, limit))
        index_map.append(i)

    if not normalized_memory:
        return None

    best_index = -1
    max_size = -1

    for i in range(len(normalized_memory)):
        idx = (start_index + i) % len(normalized_memory)
        base, limit = normalized_memory[idx]
        available = limit - base

        if available >= req and available > max_size:
            best_index = idx
            max_size = available

    if best_index == -1:
        return None

    base, limit = normalized_memory[best_index]
    new_base = base + req

    if new_base == limit or limit == 0:
        removed_index = index_map.pop(best_index)
        normalized_memory.pop(best_index)
        if best_index >= len(normalized_memory):
            best_index = 0
        return normalized_memory, base, limit, removed_index
    else:
        normalized_memory[best_index] = (new_base, limit)
        return normalized_memory, base, limit, index_map[best_index]

if __name__ == "__main__":
    memory_blocks = [(0x00A00000, 0x000C0000), (0x000B0000, 0x000D0000), (0x00C00000, 0x000C0000)]
    request_size = 0x000D0000
    start_index = 2
    result = worst_fit(memory_blocks, request_size, start_index)
    print(result)
