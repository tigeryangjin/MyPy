square_func = lambda x: x * 3
function_product = lambda F, m: lambda x: F(x) * m
print(square_func(3))
print(function_product(square_func, 3)(4))
