def displayInventory(inventory):
    print('Inventory:')
    items = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        items += v
    print('Total number of items: ' + str(items))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item]=inventory[item]+1
    return inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
