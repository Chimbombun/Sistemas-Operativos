def worst_fit(memory, req, start_index):
    # Verificar si la memoria está vacía
    if not memory:
        return None
    
    # Verificar si el tamaño del proceso es mayor que cualquier espacio disponible
    if all(req > (limit - base) for base, limit in memory):
        return None
    
    best_index = -1
    max_size = -1
    
    # Recorrer la memoria desde el índice actual de forma circular
    for i in range(len(memory)):
        idx = (start_index + i) % len(memory)
        base, limit = memory[idx]
        available = limit - base
        
        if available >= req and available > max_size:
            best_index = idx
            max_size = available
    
    if best_index == -1:
        return None  # No hay suficiente espacio disponible para esta solicitud
    
    # Asignar el bloque de memoria
    base, limit = memory[best_index]
    new_base = base + req
    memory[best_index] = (new_base, limit)
    
    return memory, new_base, limit, best_index

# Ejemplo de uso
if __name__ == "__main__":
    memory_blocks = [(0x1000, 0x3000), (0x4000, 0x6000), (0x7000, 0xA000)]
    request_size = 0x800
    start_index = 0  # Índice inicial
    result = worst_fit(memory_blocks, request_size, start_index)
    print(result)
