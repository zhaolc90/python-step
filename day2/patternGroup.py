import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('mo.group(1): ' + mo.group(1))
print('mo.group(2): ' + mo.group(2))
print('mo.group():  ' + mo.group())
print('mo.groups(): ' + str(mo.groups()))


areaCode, mainNumber = mo.groups()
print('areaCode: ' + areaCode)
print('mainNumber: ' + mainNumber)
