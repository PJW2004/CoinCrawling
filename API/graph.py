import matplotlib.pyplot as plt
from .lookup import look

top_10_price_l = [0.1]*10

def graph_show(coins=None):
    coin = coins.split('\n')[:-1]
    print(coin)
    for x, _ in enumerate(coin):
        print(top_10_price_l)
        if x != 9:
            _ = (_[3:].split('-')[0])
        else:
            _ = (_[4:].split('-')[0])
        data = look(coinname=_.lower())
        market_conditions, percent, url = data.real_time()

        top_10_price_l[x] = float(market_conditions[1:].replace(',', ''))

    print(top_10_price_l)
    plt.subplot(2, 2, 1)
    plt.plot(top_10_price_l, label='price')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.barh(coin, top_10_price_l)

    plt.show()