def counter_function():
    yield 1
    yield 2
    yield 3

contador = counter_function()

print(next(contador))  # Saída: 1
print(next(contador))  # Saída: 2
print(next(contador))  # Saída: 3