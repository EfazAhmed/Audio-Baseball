import speech_recognition as sr
import random
import pyttsx3
from playsound import playsound
from tkinter import *

# list of phrases that George says if opponent strikes
strike_audio_list = ["Strike1.mp3",
                     'Strike2.mp3',
                     'Strike3.mp3',
                     'Strike4.mp3',
                     'Strike5.mp3']

# list of phrases that George says if opponent home runs
homeRun_audio_list = ['Dont sweat it. You have the next pitch.',
                      'Lets mix it up. Looks like he knows how to hit that now.',
                      'What happenned?',
                      'This is not what we need right now.',
                      'You dont want to be replaced now do you?']

# list of phrases that George says if you choose normal ball
fast_audio_list = ['Sometimes even the most simplest pitches are the best.',
                   'Just dont injure your arm or its game over',
                   'Maybe this time youll beat your fastest pitch record.']

# list of phrases that George says if you choose curve ball
curve_audio_list = ['Remember, straight down the middle.',
                    'Good choice. He wont know what know hit him',
                    'Just dont curve it too much.']

# list of phrases that George says if you choose knuckle ball
knuckle_audio_list = ['Interesting. Not many people use that pitch.',
                      'I wonder where the ball will land this time.',
                      'Lets hope he doesnt embarrass himself missing.']

# list of phrases that George says if you choose slider ball
slider_audio_list = ['I hope you dont hurt your arm.',
                     'Hell probably think its a curveball.',
                     'He wont see whats coming.']

# list of phrases that George says if you choose screw ball
screw_audio_list = ['Time to embarrass him.',
                    'Lets no screw this one up haha.',
                    'Lets screw him over.']

winning_audio_list = ['Great job son. I think its time for the big leagues.',
                      'Amazing game. We couldnt have done it without you.'
                      'Winner winner chicken dinner.'
                      'What a wonderful game! I hope you had fun because I know I did!']

losing_audio_list = ['Lets learn from today what not to do.',
                     'Theres always a next time.',
                     'That was awful. Do better next time.',
                     'Dont worry champ, we almost had them.',
                     'It seems like you have lost the game, but thats okay']


def checker(throw):
    temp = 0
    global fast_rate
    global curve_rate
    global knuckle_rate
    global slider_rate
    global screw_rate

    if throw == "fast":
        temp = fast_rate
        if random_boolean():
            fast_rate = fast_rate - fast_dec
    if throw == "curve":
        temp = curve_rate
        if random_boolean():
            curve_rate = curve_rate - curve_dec
    if throw == "knuckle":
        temp = knuckle_rate
        if random_boolean():
            knuckle_rate = knuckle_rate - knuckle_dec
    if throw == "slider":
        temp = slider_rate
        if random_boolean():
            slider_rate = slider_rate - slider_dec
    if throw == "screw":
        temp = screw_rate
        if random_boolean():
            screw_rate = screw_rate - screw_dec

    temp = random.randint(0, 99)
    global engine
    if temp >= (100 - temp):
        global strikes
        strikes = strikes + 1
        if strikes == 1:
            playsound("StrikeOneSound.mp3")
        if strikes == 2:
            playsound("StrikeTwoSound.mp3")
        if strikes == 3:
            playsound("StrikeThreeSound.mp3")
        strike_audio()
        stating_score()
    else:
        global homeRuns
        homeRuns = homeRuns + 1
        playsound('HomeRunSound.mp3')
        hit_audio()
        stating_score()


def random_boolean():
    num = random.randint(1, 2)
    return num == 1


def strike_audio():
    num = random.randint(1, 5)
    if num == 1:
        playsound('Strike 1.mp3')
    if num == 2:
        playsound('Strike 2.mp3')
    if num == 3:
        playsound('Strike 3.mp3')
    if num == 4:
        playsound('Strike 4.mp3')
    if num == 5:
        playsound('Strike 5.mp3')


def hit_audio():
    num = random.randint(1, 5)
    if num == 1:
        playsound('Hit 1.mp3')
    if num == 2:
        playsound('Hit 2.mp3')
    if num == 3:
        playsound('Hit 3.mp3')
    if num == 4:
        playsound('Hit 4.mp3')
    if num == 5:
        playsound('Hit 5.mp3')


def screw_audio():
    num = random.randint(1, 5)
    if num == 1:
        playsound('Screwball1.mp3')
    if num == 2:
        playsound('Screwball2.mp3')
    if num == 3:
        playsound('Screwball3.mp3')


def slide_audio():
    num = random.randint(1, 5)
    if num == 1:
        playsound('Sliderball1.mp3')
    if num == 2:
        playsound('Sliderball2.mp3')
    if num == 3:
        playsound('Sliderball3.mp3')


def knuckle_audio():
    num = random.randint(1, 5)
    if num == 1:
        playsound('Knuckleball 1.mp3')
    if num == 2:
        playsound('Knuckleball 2.mp3')
    if num == 3:
        playsound('Knuckleball 3.mp3')


def curve_audio():
    num = random.randint(1, 5)
    if num == 1:
        playsound('Curveball 1.mp3')
    if num == 2:
        playsound('Curveball 2.mp3')
    if num == 3:
        playsound('Curveball 3.mp3')


def fast_audio():
    num = random.randint(1, 5)
    if num == 1:
        playsound('Fastball 1.mp3')
    if num == 2:
        playsound('Fastball 2.mp3')
    if num == 3:
        playsound('Fastball 3.mp3')


def loser_audio():
    num = random.randint(1, 5)
    if num == 1:
        playsound('Loser 1.mp3')
    if num == 2:
        playsound('Loser 2.mp3')
    if num == 3:
        playsound('Loser 3.mp3')


def winner_audio():
    num = random.randint(1, 5)
    if num == 1:
        playsound('Winner 1.mp3')
    if num == 2:
        playsound('Winner 2.mp3')
    if num == 3:
        playsound('Winner 3.mp3')


def stating_score():
    engine.say('Your opponent has ' + str(strikes) + ' strikes and ' + str(homeRuns) + ' home runs')
    print('Your opponent has ' + str(strikes) + ' strikes and ' + str(homeRuns) + ' home runs')
    engine.runAndWait()


def fast_ball(sample):
    global engine
    global first_time
    if "fast" in sample or "speed" in sample:
        print('You said: {}'.format(sample))
        fast_audio()
        checker("fast")
    else:
        first_time = False


def curve_ball(sample):
    global engine
    global first_time
    if "curve" in sample or "curvy" in sample:
        print('You said: {}'.format(sample))
        curve_audio()
        checker("curve")
    else:
        first_time = False


def knuckle_ball(sample):
    global engine
    global first_time
    if "knuckle" in sample or "nuck" in sample:
        print('You said: {}'.format(sample))
        knuckle_audio()
        checker("knuckle")
    else:
        first_time = False


def slider_ball(sample):
    global engine
    global first_time
    if "slider" in sample or "slide" in sample:
        print('You said: {}'.format(sample))
        slide_audio()
        checker("slider")
    else:
        first_time = False


def screw_ball(sample):
    global engine
    global first_time
    if "Screw" in sample or "crew" in sample:
        print('You said: {}'.format(sample))
        screw_audio()
        checker("screw")
    else:
        first_time = False


def start_game():
    global strikes
    global homeRuns
    global first_time
    global fast_dec
    global curve_dec
    global knuckle_dec
    global slider_dec
    global screw_dec
    global fast_rate
    global curve_rate
    global knuckle_rate
    global slider_rate
    global screw_rate
    global engine
    global finished_game

    r = sr.Recognizer()

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 175)
    engine.setProperty('voice', voices[0].id)

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        playsound('Greeting.mp3')
        audio = r.listen(source)

        start = ""

        try:
            start = r.recognize_google(audio)
            print('You said: {}'.format(start))
        except:
            playsound('Sorry.mp3')

        if "y" in start or "es" in start:
            playsound('Intro.mp3')
        elif "n" in start or "no" in start:
            playsound('Shame.mp3')

        while True:
            if "y" in start or "es" in start or "I am" in start and finished_game is False:
                if first_time:
                    stating_score()
                playsound('Throw.mp3')
                print('How would you like to throw the ball?')

            audio1 = r.listen(source)
            try:
                answer = r.recognize_google(audio1)
                fast_ball(answer)
                curve_ball(answer)
                knuckle_ball(answer)
                slider_ball(answer)
                screw_ball(answer)
            except:
                playsound('Sorry.mp3')
                first_time = False

            if homeRuns == 3 and finished_game is False:
                loser_audio()
                playsound('Again.mp3')
                finished_game = True
            if strikes == 3 and finished_game is False:
                playsound("VictorySound.mp3")
                winner_audio()
                playsound('Love2.mp3')
                playsound('Again.mp3')
                finished_game = True

            if finished_game is True:
                audio2 = r.listen(source)

                try:
                    start = r.recognize_google(audio2)
                    print('You said: {}'.format(start))
                    if "no thank you" in start or "no" in start or "n" in start:
                        playsound('Reject.mp3')
                        break
                    if "y" in start or "es" in start:
                        playsound('TryAgain.mp3')
                        strikes = 0
                        homeRuns = 0
                        fast_rate = 80
                        curve_rate = 85
                        knuckle_rate = 75
                        slider_rate = 90
                        screw_rate = 80
                        first_time = True;
                        continue
                    else:
                        break
                except:
                    playsound('Sorry.mp3')


strikes = 0
homeRuns = 0
first_time = True
fast_dec = 17
curve_dec = 18
knuckle_dec = 15
slider_dec = 20
screw_dec = 17
fast_rate = 80
curve_rate = 85
knuckle_rate = 75
slider_rate = 90
screw_rate = 80
engine = pyttsx3.init()
finished_game = False;

start_game()

# root = Tk()  # Creates the Window named root
# root.title("Audio Baseball")  # Names the window
# root.geometry("496x400")  # Sets the size of the window
# root.resizable(height=True, width=False)  # Prevents the window from changing size
# canvas = Canvas(root, bg="blue", width=496, height=400)
# canvas.pack(expand=YES, fill=BOTH)
# bg = PhotoImage(file='Bg.png')
# canvas.create_image(50, 10, image=bg, anchor=NW)
# tFrame = Frame(root, bg="white", width=480, height=200)
# tFrame.place(x=250, y=110, anchor=CENTER)

# start_button = Button(canvas, width=100, bg='black', fg='white', command=lambda: start_game())
# start_button.pack()
# random_button = Button(canvas, width=100, bg='red', fg='white', command=lambda: start_game())
# random_button.pack()
# root.mainloop()  # Runs the root
