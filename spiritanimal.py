import winsound
import time
import random

class Animal:
    def __init__(self,name,category):
        self.name = name
        self.category = category

    def sound(self):
        if self.category == 'Dog':
            winsound.PlaySound("Sounds/dog-bark-sound-450454.wav", winsound.SND_ASYNC)
        elif self.category == 'Cat':
            if 'evil' in self.name.lower():
                winsound.PlaySound("Sounds/evil_larry.wav", winsound.SND_ASYNC)
            else:
                winsound.PlaySound("Sounds/cat-meow-sound-383823.wav", winsound.SND_ASYNC)
        elif self.category == 'Toyota':
            winsound.PlaySound("Sounds/this-is-a-toyota.wav", winsound.SND_ASYNC)

dogesh = Animal("Dogesh","Dog")
gary = Animal("gary","Cat")
evil_larry = Animal("Evil Larry","Cat")
pharchuran = Animal("Toyota","Toyota")
animals = [dogesh, gary, evil_larry, pharchuran]

print("let's see what's your spirit animal today!")
time.sleep(2)
print("enter anything to continue")
input()
print("Your spirit animal is...")
time.sleep(2)
animal = random.choice(animals)
print(animal.name)
time.sleep(2)

if animal.category == 'Dog':
    animal.sound()
    print("Dogesh approves. Tail goes brr. Your day will be amazing!")
    time.sleep(5)
    
elif animal.name == 'Evil Larry':
    animal.sound()
    print("Larry: How many Evil Larry tokens do you have?")
    tokens = input('Your answer: ')
    if int(tokens) <= 0:
        print('Larry is having mercy on you today :)')
        time.sleep(5)
    else:
        print(f'Evil Larry has stolen all your tokens')
        time.sleep(1)
        print("Enjoy!")
        time.sleep(5)
    
elif animal.name == "gary":
    animal.sound()
    print('gary has brought brownies for you!')
    time.sleep(2)
    thanks = input('Say thank you to gary: ')
    if 'thank you' in thanks.lower() or 'thank u' in thanks.lower():
        print('Thanks accepted! Have a good day!')
        time.sleep(5)
    else:
        print('Thanks not accepted :(')
        time.sleep(1)
        print("Larry is arriving tonight, be ready for it!")
        time.sleep(3)
        print("Not Larry but...")
        time.sleep(2)
        winsound.PlaySound("Sounds/evil_larry.wav", winsound.SND_ASYNC)
        print("EVIL Larry ;)")
        time.sleep(5)
    
elif animal.category == 'Toyota':
    animal.sound()
    print("Hopefully you find reliable people today just like a...")
    time.sleep(3)
    print("TOYOTA!!!")
    time.sleep(5)