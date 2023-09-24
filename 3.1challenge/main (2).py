def linearSearchProduct (productList, targetProduct):
  indices = []

  for index, product in enumerate(productList): 
    if product == targetProduct:
     indices.append(index)

    return indices


# Example usage:
Products = [  "shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
Target2 = "shoes"
Result = linearSearchProduct(Products, target)
print(Result)                        
