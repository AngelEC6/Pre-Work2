import random
def trick():
  number_the_person_choose = input("Give me a number in binary ")
  binary_number_in_decimal = 0
  number_by_number = list(number_the_person_choose)
  number_by_number.reverse()
  times_iterated = 0
  for number in number_by_number:
    if number == "1":
      binary_number_in_decimal = binary_number_in_decimal + (pow(2, times_iterated))
    times_iterated = times_iterated + 1
  print(f'Your binary number in decimal form is {binary_number_in_decimal}.')
def hello(): 
  user_response_hello = input("Hi\nHow has your day been? ")
  user_response_hello = user_response_hello.split()
  good_day = 1
  for response in user_response_hello:
    if response == "good":
      print("Thats good\nMy day has been pretty good too")
      good_day = 2
      break
    elif response == "bad":
      print("I'm sorry to hear that I hope your day get better")
      good_day = 2
      break
    elif response == "great":
      print("Thats good\nMy day has been pretty good too")
      good_day = 2
      break
    elif response == "fine":
      print("Thats good\nMy day has been pretty good too")
      good_day = 2
      break
    elif response == "horrible":
      print("I'm sorry to hear that I hope your day get better")
      good_day = 2
      break
    elif response == "awful":
      print("I'm sorry to hear that I hope your day get better")
      good_day = 2
      break
    elif response == "ok":
      print("Thats good\nMy day has been pretty good too")
      good_day = 2
      break
  if good_day == 1:
    print("That's very interesting")
sports_topic_prompts = ["Did you see the game last night?", "What's your favorite sport?", "I like sports they're fun"]
sprom = random.choice(sports_topic_prompts)
videogame_topic_prompts = ["What is your favorite videogame?", "Have you played any good videogames lately?", "How often do you play video games?"]
vprom = random.choice(videogame_topic_prompts)
food_topic_prompts = ["What's your favorite food?", "I reall like chocolate\nDo you?", "To what restaurant do you go most often?"]
fprom = random.choice(food_topic_prompts)
coding_topic_prompts = ["What languages can you code in?","Have you ever coded anything?","Do you like coding?"]
cprom = random.choice(coding_topic_prompts)
tv_topic_prompts = ["What's your favorite TV show?", "Have you been watching any TV shows lately?","How often do you watch tv?"]
tprom = random.choice(tv_topic_prompts)
music_topic_prompts = ["What's your favorite song?", "Which kinds of music do you like?", "What bands do you listen to?"]
mprom = random.choice(music_topic_prompts)
def talking_about_topics():
  topic_choice = input("So what would you like to talk about? ")
  topic_choice = topic_choice.split()
  for topic in topic_choice:
    if topic == "sports":
      sresponse = input(sprom)
      if sprom == "Did you see the game last night?":
        if sresponse == "yes":
          print("I saw it too\nIt was awesome")
        if sresponse == "no":
          print("It sucks you missed it\nIt was pretty awesome")
      if sprom == "What's your favorite sport?":
        if sresponse == "soccer":
          print("No way that's my favorite sport too")
        else:
          print("I like that one too but it's not my favorite")
    elif topic == "videogames":
      vresponse = input(vprom)
      if vprom == "What is your favorite videogame?":
        if vresponse == "Borderlands 3":
          print("You have good taste\nThat's my favorite videogame too")
        else:
          print("That's a good one but personally it's not my favorite")
      if vprom == "Have you played any good videogames lately?":
        print("Oh I've heard of that one its really good\nI've been thinking of playing it")
      if vprom == "How often do you play video games?":
        print("I play a little less often than that\nBut were pretty much on the same boat")
    elif topic == "food":
      fresponse = input(fprom)
      if fprom == "What's your favorite food?":
        if fresponse == "Chiken Alfredo":
          print("Woah you that's my favorite too")
        else:
          print("I like that dish too but it definitely isn't my favorite")
      if fprom == "I reall like chocolate\nDo you?":
        if fresponse == "no":
          print("That sucks you're really missing out")
        if fresponse == "yes":
          print("I see you have great taste")
      if  fprom == "To what restaurant do you go most often?":
        if fresponse == "Olive Garden":
          print("Oh cool I go there all the time too")
        else:
          print("I don't go there super often but whenever I go its really good")
    elif topic == "coding":
      cresponse = input(cprom)
      if cprom == "What languages can you code in?":
        if cresponse == "Python":
          print("Hey that's the language I'm coded in")
        else:
          print("Oh that's cool")
      if cprom == "Have you ever coded anything?":
        if cresponse == "yes":
          input("What did you make?")
          print("Woah that's super cool")
        else:
          input("Oh that's ok")
      if cprom == "Do you like coding?":
        if cresponse == "no":
          print("Oh that sucks I was made using code")
        if cresponse == "yes":
          print("That's good because I was made usign code")
    elif topic == "TV":
      tresponse = input(tprom)
      if tprom == "What's your favorite TV show?":
        if tresponse == "The office":
          print("No way that's my favorite too")
        else:
          print("Oh that's a good show\nBut personally it's not my favorite")
      if tprom == "Have you been watching any TV shows lately?":
        if tresponse == "yes":
          input("What show is it?")
          print("Oh I've heard of that show but I haven't watched it yet")
        else:
          print("Oh that's cool")
      if tprom == "How often do you watch tv?":
        print("Well were pretty much on the same boat")
    elif topic == "music":
      mresponse = input(mprom)
      if mprom == "What's your favorite song?":
        if mresponse == "Sheperd of Fire":
          print("Oh that's my favorite song too it's really good")
        else:
          print("That song is pretty good but personall it's not my favorite")
      if mprom == "Which kinds of music do you like?":
        mresponse = mresponse.list()
        for m in mresponse:
          if m == "rock":
            print("I love that music too")
            break
          else:
            print("Oh those genres are cool")
            break
      if mprom == "What bands do you listen to?":
        mresponse = mresponse.list()
        for m in mresponse:
          if m == "Avenged Sevenfold":
            print("I love that band too")
            break
          else:
            print("Oh those bands are cool")
            break
    
hello()
user_response = "yes"
while user_response == "yes":
  talking_about_topics()
  sprom = random.choice(sports_topic_prompts)
  vprom = random.choice(videogame_topic_prompts)
  fprom = random.choice(food_topic_prompts)
  cprom = random.choice(coding_topic_prompts)
  tprom = random.choice(tv_topic_prompts)
  mprom = random.choice(music_topic_prompts)
  user_response = input("Would you like to keep talking? ")
trick_reponse = input("Would you like to see a trick before you go?")
if trick_reponse == "yes":
  trick()
print("Ok it was nice talking to you\nBye")