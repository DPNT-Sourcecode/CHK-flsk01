

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    '''
    from the price table inc. offers, return the total cost of
    goods from a string of skus
    '''
    # initial assumption is that skus is of the form 'ABCAD'
    # therefore need to sum the characters in a string

    # the basic price table as an object, no offers involved yet
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    skus = skus.upper() # string formatting

    if len(skus) == 0:
        return 0

    # if there are any items in the input that don't match A,B,C, or D it's an illegal input
    if any(item for item in skus if item not in ['A','B','C','D']):
        return -1

    # getting the count of each item, not it's value
    summed_items = {
        item: skus.count(item) for item in ['A','B','C','D']
    }

    # multiplying the price of each item with the count of each item
    total_cost = sum([prices[item]*count for item, count in summed_items.items()])

    # case of offers on A and B (3A = 130, 2B = 45)
    # this is equivalent to "for every 3 A you buy, 20 off", "for every 2 B you buy, 15 off"
    if 'A' in summed_items.keys() and summed_items['A'] // 3 > 0:
        total_cost -= (summed_items['A'] // 3)*20
    if 'B' in summed_items.keys() and summed_items['B'] // 2 > 0:
        total_cost -= (summed_items['B'] // 2)*15

    return total_cost



