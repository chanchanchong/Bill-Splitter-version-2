cat_cafe = {}
while True:
    try:
        cafe, n = input().split()
    except ValueError:
        break
    cat_cafe[int(n)] = cafe
print(cat_cafe[max(cat_cafe.keys())])
