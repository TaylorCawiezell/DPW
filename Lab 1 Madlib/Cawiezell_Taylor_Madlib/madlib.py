# input variables
input1 = raw_input('Choose a word (1)Awesome (2)Aweful (3)Awesomeful ')
input2 = raw_input('Choose a word (1)Hero (2)Moderately atractive nice guy (3)Banana ')
input3 = raw_input("Choose a word (1)Life (2)Banana's (3)Goat ")
input4 = raw_input('Choose a word (1)Guy (2)Akward dental assistant (3)Soup ')
input5 = raw_input('Choose a number ')
input6 = raw_input('Choose another number ')
input7 = raw_input('Choose another number ')

#Responce arrays empty to be appended
res1 = []
res2 = []
res3 = []
res4 = []

'''
If statements that choose what selection to be appended
'''
if input1 == '1':
    res1.append('Awesome')
elif input1 == '2':
    res1.append('Aweful')
elif input1 == '3':
    res1.append('Awesomeful')
else:
    pass

if input2 == '1':
    res2.append('Hero')
elif input2 == '2':
    res2.append('Moderately atractive nice guy')
elif input2 == '3':
    res2.append('Banana')
else:
    pass

if input3 == '1':
    res3.append('Life')
elif input3 == '2':
    res3.append("Banana's")
elif input3 == '3':
    res3.append('Goat')
else:
    pass

if input4 == '1':
    res4.append('Guy')
elif input4 == '2':
    res4.append("Akward dental assistant")
elif input4 == '3':
    res4.append('Soup')
else:
    pass
#end of if statements

#Creating a variable that makes statements display correctly
r1 = ''.join(res1)
r2 = ''.join(res2)
r3 = ''.join(res3)
r4 = ''.join(res4)
#Turning String's into intiger
r5 = int(input5)
r6 = int(input6)
r7 = int(input7)

#function calculating defence
def damage_calc(a, d):
    damage = a - d
    return damage
#inserting paramaters
defend = damage_calc(r5, r6);

#attack calculation
super_attack = r5 * 2

#for loop showing how many times X screamed
for i in range(0,10):
    i = i+1

#Dictionary for the end of the story
end = dict()
end = {'end':'The End!'}

#displaying story
story = '''
This is a story of {r1} proportions about a {r2}. This {r1} story will utterly change the way you feel about {r3}! Once upon a time a {r2} met a evil {r4} that made his {r1} journey begin. The evil {r4} gave the {r2} a {r1} curse. {r1}!! He cried as he took the {r1} sword and drove it in the {r3} of the {r4} and it did {r5} damage then he used a glowing atack that did {super_attack} he defended wich was {defend} damage, the {r2} screamed {i} times and died. After the {r1} battle the {r2} rated the battle a {r7} on a scale of 10. {end[end]}
'''
story = story.format(**locals())

#printing formated story 
print story