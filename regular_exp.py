def isPhoneNumber(text):
    if len(text) != 7:
        return False
    
    for i in range(0,3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    return True
print(isPhoneNumber('222-221'))

chk_string = 'Please contact any of the following numbers for support: 123-456, 987-654, 456-789, 321-654, 654-987, or 789-123. Our representatives are available 24/7 at these numbers. Additionally, you can reach our customer service at 234-567 or 890-123 for urgent inquiries. If none of these lines are available, try 543-210 or 678-345.'
check_str  = 'Please contact any of the following numbers for support: 221-123-4256, 211-987-6514, 345-456-7869, 654-321-6554, 767-654-9867, or 347-789-1523. Our representatives are available 24/7 at these numbers. Additionally, you can reach our customer service at 534-234-4567 or 876-590-1254 for urgent inquiries. If none of these lines are available, try 343-543-2510 or 654-578-3465.'

for i in range(len(chk_string)):
    chunk = chk_string[i:i+7]
    if isPhoneNumber(chunk):
        print('Number found:',chunk)
print('\n')

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#mo = phoneNumRegex.search('My number is 412-555-2324.')
mo = phoneNumRegex.search(check_str)
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

heroRegex = re.compile(r'Batman|Catman')
mo1 = heroRegex.search(r'Batman kicked bossDK and Catman')
print(mo1.group())

batRex = re.compile(r'(Bat|Cat|Dober)man')
mo2 = batRex.search(r'Catman: Batman kicked bossDK and Catman')
print(mo2.group())
