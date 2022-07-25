def generate_ip():
    from random import randrange
    ip_gen = [str(randrange(256)) for _ in range(4)]
    ip_gen = '.'.join(ip_gen)
    return ip_gen


print(generate_ip())
