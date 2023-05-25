items = ['lat', 'wod', 'nam', 'źdżbło']

with open('example.txt', 'w', encoding='utf-8') as fopen:
    # fopen.write('linia1\n')
    # fopen.write('linia2\n')
    # fopen.write('linia3')

#########################################
    fopen.write('\n'.join(items))