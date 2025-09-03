def list2string(mylist):
    if mylist == []:
        return ''
    mylist[-1] = 'and ' + str(mylist[-1])
    myStr = ''
    for item in mylist:

        if mylist.index(item) < len(mylist)-1:
            myStr = myStr + str(item) + ', '

        else:
            myStr = myStr + str(item)

    return myStr

spam = ['apples', 'bananas', 'tofu', 'cats']
print(list2string(spam))
print(list2string([]))
