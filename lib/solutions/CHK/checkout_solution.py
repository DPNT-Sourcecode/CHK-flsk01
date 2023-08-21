

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

    # if there are any items in the input that don't match A,B,C, or D it's an illegal input
    if any(item for item in skus not in ['A','B','C','D']):
        return -1

    # getting the count of each item, not it's value
    summed_items = {
        item: skus.count(item) for item in ['A','B','C','D']
    }

    # case of offers on A and B (3A = 130, 2B = 45)
    costs = {}
    if summed_items['A'] // 3 > 0:
        costs['A'] = (summed_items['A'] // 3)*50
        costs['A'] += 


    raise NotImplementedError()

# Our price table and offers:
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+






