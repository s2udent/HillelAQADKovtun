from random import choice


def toss_a_coin():
    coin_list = ['head', 'tail']
    return choice(coin_list)


if __name__ == '__main__':
    print(toss_a_coin())
