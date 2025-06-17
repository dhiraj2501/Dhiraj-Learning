birthdays = {'Jetha':' Jan 1','Daya':'Jan 2','Bapuji':'April 2','Sundar':'Feb 29'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name =='':
            break
        
    if name in birthdays:
        print(birthdays[name]+ '\'s birthday is of'+ name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name]=bday
        print('Birtday database updated')