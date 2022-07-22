def merge(values):      # values - это список словарей
    output = {}
    for i in values:
        for key, value in i.items():
            if key not in output:
                output[key] = [value]
            else:
                output[key] += [value]

    return output


result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)