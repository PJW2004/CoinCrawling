import requests.exceptions
import os

def lookup_():
    from API.lookup import look
    user = input('조회하고 싶은 코인을 입력 : ')
    if user == '코인조회':
        print(coins)
        print(f'''그외 : {len(ather)}...
=================================================''')
        lookup_()

    elif user == '시세 그래프':
        from API.graph import graph_show
        graph_show(coins=coins)
        lookup_()
    
    elif user == '':
        lookup_()

    else:
        try:
            if user not in 'exit':
                data = look(coinname=user.lower())
                market_conditions, percent, url = data.real_time()
                
                print(f'{user}의 현재 시세 : {market_conditions}\npercnet >> {percent}\nLink >> {url}')
                print('=================================================')
                
                lookup_()
        except AttributeError:
            print('코인이 존재하지 않습니다.')
            lookup_()


if __name__ == '__main__':
    try:
        try:
            from API.coin import ather, coins
            lookup_()
        except ModuleNotFoundError:
            os.system('pip install -r requirements.txt')
            print('시스템을 다시 켜 주세요')
    except requests.exceptions.ConnectionError:
        print('와이파이 연결후 시도해 주세요.')
