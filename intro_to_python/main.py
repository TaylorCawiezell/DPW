#one line comments

first_name = 'kermit'
last_name = 'de frog'

#response = raw_input('Enter your name: ')
#print "Hey I herd you say you're name is", response

birth_year = 1991
current_year = 2014
age = current_year - birth_year
print 'You are ' + str(age) + " years old"

#int(var) --turn string to intiger
budget = 55

if budget > 100:
    brand = 'nikes'
    print 'Yeah man cool ' + brand
elif budget > 50:
    print 'Thats some good payless shoes'
elif budget > 20:
    print 'Awe that is no fun'
else:
    pass

characters = ['leia','luke','chewy','lando']
characters.append('obi')
#print characters[0]

movies = dict() #create dictionary object
movies = {'starwars':'darth vader', 'silence':'man'}
print movies['starwars']

#while loop--
'''
i = 0
while (i<9):
    print 'the count is', i
    i = i+1
'''

#for loop--
'''
for i in range(0,10):
    print 'the count is', i
    i = i+1
'''

rappers = ['Tupac','Big','Puff']
for r in rappers:
    #print r
    pass

#functions -------
x = 2
def calc_area(h, w):
    area = h * w
    return area + x

a = calc_area(20, 40);
print 'My area is ' + str(a) + ' sqft'

title = 'contact us'
body = 'contact us at contact@us.com'
message = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
'''

message = message.format(**locals())
print message


