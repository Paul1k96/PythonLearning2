def build_query_string(params):
    output = []
    for key, value in params.items():
        output += [str(key) + '=' + str(value)]
    output = '&'.join(sorted(output))
    return output


print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))