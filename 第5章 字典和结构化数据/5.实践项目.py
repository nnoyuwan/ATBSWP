# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/9 12:24 下午


# 5.6.1 好玩游戏的物品清单
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number of items: ' + str(total))


# displayInventory(stuff)

# 5.6.2 列表到字典的函数，针对好玩游戏物品清单
inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
            # inventory.setdefault(item, 0)
            inventory[item] = 1
        else:
            inventory[item] += 1


addToInventory(inv, dragonLoot)
displayInventory(inv)
