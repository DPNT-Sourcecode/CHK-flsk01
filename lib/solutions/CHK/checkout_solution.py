

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
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
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

    # multiplying the price of each item with the count of each item
    total_cost = sum([prices[item]*count for item, count in summed_items.items()])

    # 5H for 45, 10H for 80 (for every 5, 5 off, for every 10, 20 off)
    if summed_items['H'] // 10 > 0:
        total_cost -= (summed_items['H'] // 10)*20
        summed_items['H'] = summed_items['H']%10
    if summed_items['H'] // 5 > 0:
        total_cost -= (summed_items['H'] // 5)*5

    # 2K for 150
    if summed_items['K'] // 2

    # for every 3 F, get one F free
    if summed_items['F'] // 3 > 0:
        total_cost -= (summed_items['F'] // 3)*prices['F']

    if summed_items['E'] // 2 > 0:
        total_cost -= (min(summed_items['E'] // 2, summed_items['B']))*prices['B']  # for every 2 E, get a free B
        summed_items['B'] -= 1

    if summed_items['A'] // 5 > 0:
        total_cost -= (summed_items['A'] // 5)*50  # new offer, if you buy 5A, you get 50 off
        summed_items['A'] = summed_items['A']%5  # taking off the 5's to try and use the 3's offer

    if summed_items['A'] // 3 > 0:
        total_cost -= (summed_items['A'] // 3)*20

    if summed_items['B'] // 2 > 0:
        total_cost -= (summed_items['B'] // 2)*15

    return total_cost

# A new item has arrived. Item F.
# Our marketing team wants to try rewording the offer to see if it affects consumption
# Instead of multi-pricing this item they want to say "buy 2Fs and get another F free"
# The offer requires you to have 3 Fs in the basket.

# Our price table and offers:
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# +------+-------+------------------------+


