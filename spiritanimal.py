import winsound
import time
import datetime
import random
import os

if not os.path.exists('Data/none_of_your_business.txt'):
    with open('Data/none_of_your_business.txt','w') as f:
        f.write("0")

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
            elif self.name == 'Banana Cat':
                winsound.PlaySound("Sounds/banana-cat.wav", winsound.SND_ASYNC)
            elif self.name == 'alfredo':
                winsound.PlaySound("Sounds/alfredo.wav", winsound.SND_ASYNC)
            else:
                winsound.PlaySound("Sounds/cat-meow-sound-383823.wav", winsound.SND_ASYNC)
        elif self.category == 'Toyota':
            winsound.PlaySound("Sounds/this-is-a-toyota.wav", winsound.SND_ASYNC)

def ChooseAnimal(list):
    animal = random.choice(list)
    with open('Data/none_of_your_business.txt','r') as f:
        if f.readline().strip() == animal.name:
            return ChooseAnimal(list)
    return animal

dogesh = Animal("Dogesh","Dog")
gary = Animal("gary","Cat")
evil_larry = Animal("Evil Larry","Cat")
toyota = Animal("Toyota","Toyota")
alfredo = Animal('alfredo','Cat')
BananaCat = Animal('Banana Cat','Cat')
animals = [alfredo,dogesh,gary,evil_larry,toyota]

print("let's see what's your spirit animal today!")
time.sleep(2)
input("press enter to continue: ")
print("Your spirit animal is...")
time.sleep(2)
flag = False

with open("Data/last_execution.txt","r") as t:
    if datetime.datetime.now().hour >= 23:
        print("Sorry for the disturbance! Banana Cat wants to say something")
        time.sleep(2)
        BananaCat.sound()
        time.sleep(1)
        print("\"It's too late already! LAST thing u should do: \"")
        time.sleep(2)
        print("\"text @myk.ro.wave and GO TO SLEEP!\"")
        time.sleep(2)
        input("press enter to continue: ")
        time.sleep(1)
        flag = True
    last = float(t.readline().strip())

    if (time.time() - last >= 21600) and flag==False:
        print("Sorry for the disturbance! Banana Cat wants to say something")
        time.sleep(4)
        BananaCat.sound()
        time.sleep(1)
        print("\"u have to text @myk.ro.wave by the end of the day\"")
        time.sleep(5)
        print("Or else...")
        time.sleep(2)
        evil_larry.sound()
        time.sleep(1)
        print("LARRY!")
        time.sleep(2)
        input("press enter to continue: ")
        time.sleep(1)
        flag = True

animal = ChooseAnimal(animals)
if flag:
    with open("Data/last_execution.txt","w") as t:
        t.write(str(time.time()))
    print("Your spirit animal is...")
print(animal.name)
animal.sound()
time.sleep(2)

with open('Data/none_of_your_business.txt','w') as f:
    f.write(animal.name)

if animal.category == 'Dog':
    print("Dogesh approves. Tail goes brr. Your day will be amazing!")
    time.sleep(5)
    
elif animal.category == 'Toyota':
    print("Hopefully you find reliable people today just like a...")
    time.sleep(2)
    print("TOYOTA!!!")
    time.sleep(5)

elif animal.category == 'Cat':
    if animal.name == "gary":
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

    elif animal.name == 'Evil Larry':
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

    elif animal.name == 'alfredo':
        print("—Intern at peenar news")
        time.sleep(4)
        print("Alfredo is preparing a small Peenar News update...")
        time.sleep(3)
        print("He's underconfident. This might go well. Or not.")
        time.sleep(3)
        choice = input("Let Alfredo publish it? (yes/no): ")
        if choice.lower() == 'yes':
            print("\"O-oh... okay!\"")
            time.sleep(2)
            print("\"Publishing now... please don't refresh...\"")
            time.sleep(2)
            print("Alfredo gained +1 confidence")
        else:
            print("\"Oops... sorry...\"")
            time.sleep(2)
            print("\"I'll recheck everything. Again.\"")
            time.sleep(2)
            print("\"Bye!\"")
            time.sleep(3)