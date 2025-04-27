lst = ['White', 'Black', 'Red']
lst_2 = ['Red', 'Green']


def differense(lst, lst_2):
    result = set(lst) - set(lst_2)
    return result


print(differense(lst, lst_2))
