def adjacentElementsProduct(inputArray):
    current_max = inputArray[0] * inputArray[1]
    for i in range(len(inputArray)-1):
        if inputArray[i] * inputArray[i+1] > current_max:
            current_max = inputArray[i] * inputArray[i+1]
    return current_max