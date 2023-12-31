

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    '''
    from the price table inc. offers, return the total cost of
    goods from a string of skus
    '''
    # initial assumption is that skus is of the form 'ABCAD'
    # therefore need to sum the characters in a string

    # keeping in this format in case things change
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 70,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 20,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 17,
        'Y': 20,
        'Z': 21
    }

    allowed_inputs = list(prices.keys())

    if len(skus) == 0:
        return 0

    # if there are any items in the input that don't match A,B,C, or D it's an illegal input
    if any(item for item in skus if item not in allowed_inputs):
        return -1

    # getting the count of each item, not it's value
    summed_items = {
        item: skus.count(item) for item in allowed_inputs
    }

    # add the T and Y items to S and remove as identical
    summed_items['S'] += summed_items['T'] + summed_items['Y']
    summed_items['T'] = 0
    summed_items['Y'] = 0

    # buy any 3 of (S,T,X,Y,Z) for 45
    # Z=21; S,T,Y all 20, X=17
    # this may need to be calculated before total_cost, TBC
    multi_buy_nums = sum(summed_items[item] for item in ['S','T','X','Y','Z'])
    if multi_buy_nums // 3 > 0:
        multi_buy_cost = (multi_buy_nums // 3)*45
        to_remove = (multi_buy_nums // 3)*3
        # want to get to_remove to 0, taking off the values of Z, then S, then X in that order
        if summed_items['Z'] >= to_remove:
            summed_items['Z'] -= to_remove
            to_remove = 0
        else:
            to_remove -= summed_items['Z']
            summed_items['Z'] = 0
            if summed_items['S'] >= to_remove:
                summed_items['S'] -= to_remove
                to_remove = 0
            else:
                to_remove -= summed_items['S']
                summed_items['S'] = 0
                summed_items['X'] -= to_remove

    else:
        multi_buy_cost = 0

    # multiplying the price of each item with the count of each item
    total_cost = multi_buy_cost + sum([prices[item]*count for item, count in summed_items.items()])

    # 5H for 45, 10H for 80 (for every 5, 5 off, for every 10, 20 off)
    if summed_items['H'] // 10 > 0:
        total_cost -= (summed_items['H'] // 10)*20
        summed_items['H'] = summed_items['H']%10
    if summed_items['H'] // 5 > 0:
        total_cost -= (summed_items['H'] // 5)*5

    # 2K for 120 == 20 off
    if summed_items['K'] // 2 > 0:
        total_cost -= (summed_items['K'] // 2)*20

    # 3N get one M free
    if summed_items['N'] // 3 > 0:
        total_cost -= (min(summed_items['N'] // 2, summed_items['M']))*prices['M']

    # 5P for 200
    if summed_items['P'] // 5 > 0:
        total_cost -= (summed_items['P'] // 5)*50

    # 3R get one Q free (better deal than just Q so supercedes it)
    if summed_items['R'] // 3 > 0:
        total_cost -= (min(summed_items['R'] // 2, summed_items['Q']))*prices['Q']
        # if summed_items['R'] // 2 > summed_items['Q']:
        #     summed_items['Q'] -= summed_items['R'] // 3
        # else:
        #     summed_items['Q'] == 0
        summed_items['Q'] -= 1

    # 3Q for 80 == 10 off
    if summed_items['Q'] // 3 > 0:
        total_cost -= (summed_items['Q'] // 3)*10

    # 3U get one U free
    if summed_items['U'] // 4 > 0:
        total_cost -= (summed_items['U'] // 4)*prices['U']

    # 3V for 130 == for 3 V, 20 off; 2V for 90 == 10 off
    if summed_items['V'] // 3 > 0:
        total_cost -= (summed_items['V'] // 3)*20
        summed_items['V'] = summed_items['V']%3
    if summed_items['V'] // 2 > 0:
        total_cost -= (summed_items['V'] // 2)*10

    # for every 3 F, get one F free
    if summed_items['F'] // 3 > 0:
        total_cost -= (summed_items['F'] // 3)*prices['F']

    if summed_items['E'] // 2 > 0:
        total_cost -= (min(summed_items['E'] // 2, summed_items['B']))*prices['B']  # for every 2 E, get a free B
        summed_items['B'] -= 1
        # if summed_items['E'] // 2 > summed_items['B']:
        #     summed_items['B'] -= summed_items['E'] // 3
        # else:
        #     summed_items['B'] == 0

    if summed_items['A'] // 5 > 0:
        total_cost -= (summed_items['A'] // 5)*50  # new offer, if you buy 5A, you get 50 off
        summed_items['A'] = summed_items['A']%5  # taking off the 5's to try and use the 3's offer

    if summed_items['A'] // 3 > 0:
        total_cost -= (summed_items['A'] // 3)*20

    if summed_items['B'] // 2 > 0:
        total_cost -= (summed_items['B'] // 2)*15

    return total_cost
