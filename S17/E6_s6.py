def order_words(chain):
    chainlist = chain.split("-")
    chainlist.sort()
    return "-".join(chainlist)

print(order_words("python-variable-funcion-computadora-monitor"))
