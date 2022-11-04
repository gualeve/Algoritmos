from random import randint
from math import inf

item = dict()
infinito = {'k':+inf, 'x':'infinito', 'v':list()}

def insert_item(node, item):
    if len(node) == 0:
        node.append(item)
        node.append(infinito)
    else:
        if item['k'] > node[len(node)-2]['k']:
            node[len(node)-1] = item
            node.append(infinito)
        else:
            for i in range(len(node)):
                if item['k'] < node[i]['k']:
                    insert_item(node[i]['v'], item)
                    return

    return

def criar_item(k, x):
    return {'k': k, 'x': x, 'v': []}

def imprime(tree):
    for i in range(len(tree) - 1):
        print(tree[i]['k'], ' ', end='')
        if len(tree[i]['v']) > 1:
            imprime(tree[i]['v'])
    return

if __name__ == "__main__":
    T = []
    insert_item(T, criar_item(12, 'doze'))
    insert_item(T, criar_item(10, 'dez'))
    insert_item(T, criar_item(17, 'dezessete'))
    insert_item(T, criar_item(15, 'quinze'))
    insert_item(T, criar_item(20, 'vinte'))
    insert_item(T, criar_item(22, 'vinte e dois'))
    insert_item(T, criar_item(13, 'treze'))

    imprime(T)
