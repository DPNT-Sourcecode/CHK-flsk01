

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
        'D': 15,
        'E': 40
    }

    # putting as object for further tests
    allowed_inputs = ['A','B','C','D','E']

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

    # TODO: look at A's offers to "favour the customer"
    # if i have 15 A and I use the 5 offer, then 15*50 - 3*50 = 600
    # or if i use the 3 offer, then 15*50 - 5*20 = 650 which is less of a deal
    # if i have 18 A, then i need to use the 5 offer on 15 items, and the 3 offer on 3


    # case of offers on A and B (3A = 130, 2B = 45)
    # this is equivalent to "for every 3 A you buy, 20 off", "for every 2 B you buy, 15 off"
    if 'A' in summed_items.keys():
        if summed_items['A'] // 5 > 0:
            total_cost -= (summed_items['A'] // 5)*50 # new offer, if you buy 5A, you get 50 off
        elif summed_items['A'] // 3 > 0:
            total_cost -= (summed_items['A'] // 3)*20
    if 'B' in summed_items.keys() and summed_items['B'] // 2 > 0:
        total_cost -= (summed_items['B'] // 2)*15
    if 'E' in summed_items.keys() and summed_items['E'] // 2 > 0:
        if 'B' in summed_items.keys():
            total_cost -= (summed_items['E'] // 2)*prices['B'] # for every 2 E, get a free B

    return total_cost


# updated info !
# Our price table and offers:
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+


# Notes:
#  - The policy of the supermarket is to always favor the customer when applying special offers.
#  - All the offers are well balanced so that they can be safely combined.
#  - For any illegal input return -1

# In order to complete the round you need to implement the following method:
#      checkout(String) -> Integer

# Where:
#  - param[0] = a String containing the SKUs of all the products in the basket
#  - @return = an Integer representing the total checkout value of the items







