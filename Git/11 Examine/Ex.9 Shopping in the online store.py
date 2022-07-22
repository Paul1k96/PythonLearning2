dict_of_customers = {}
for _ in range(int(input())):
    client, product, cnt = input().split()
    tmp_product = {product: int(cnt)}
    if client in dict_of_customers:
        if product in dict_of_customers[client]:
            dict_of_customers[client][product] += int(cnt)
        else:
            dict_of_customers[client].update(tmp_product)
    else:
        dict_of_customers[client] = tmp_product

# for debug
# print(dict_of_customers)

for key, value in sorted(dict_of_customers.items()):
    print(key, ':', sep='')

    for key_vale, value_value in sorted(value.items()):
        print(key_vale, value_value)
