# I have used 'while' strings so the user can try again if he mispells a word or inserts a word that isn't a valid answer.

title = "sewers' secrets"
print(title.upper())

print()

print('You are a traveler and has just gotten into a city')
print('It is late at night and you are hungry')
print()
print('You notice there are a few establishments opened')
print('but the streets look desert')

print('What will you do?')

inn = 'INN'
restaurant = 'RESTAURANT'
walk = 'WALK'
next = False
wrong = 'Please, insert one of the uppercased words'

while next == False:
  check_1 = input(f'Look for an {inn}, look for a {restaurant} or {walk} around the city? ')
  
  if check_1.upper() == inn:
    print()
    print('You walk a few blocks on the main street and you find')
    print('an old building with a sign saying "The sleepy Ogre inn".')
    inn = True
    next = True
    
  elif check_1.upper() == restaurant:
    print()
    print('You walk a few blocks on the main street and you find')
    print('a small house with a sign saying: "The Hungry Troll')
    restaurant = True
    next = True
    
  elif check_1.upper() == walk:
    print()
    print('You walk around the city for some time. As you had noticed before')
    print("there are no one on the streets, but you get to the central square of the city")
    walk = True
    next = True
    
  else:
    print()
    print(wrong)
    print()
print()


  
if inn == True:
  first_floor =  'FIRST'
  second_floor = 'SECOND'
  print('When you get into the Inn there is a reception desk and behind it')
  print('you see an old man with a big scar on his right eye and a big gray mustache')
  print()
  print('He says:')
  print()
  print('We have two rooms available')
  print('we have one on the FIRST floor and another on the SECOND floor')
  print()
  scene_2 = False

  while scene_2 == False:
    room = input('In which one will you stay? ')
    print()
    
    if room.upper() == first_floor:
      bed = 'BED'
      open_1 = 'OPEN'
      print('The receptionist gives you the keys of the room and says:')
      print()
      print("It doesn't matter what you hear don't go to the second floor until sunrise")
      print()
      print('You go to your room and find a small bedroom, a very simple bed on the left, and a window on the opposite wall')
      print('you lay on the bed to sleep and a few moments later you hear weird sounds coming from the upper floor')
      print('it sounded like a growl and heavy steps. suddenly you hear a stamp right above you and someone screams.')

      scene_2 = True
      
      print('What do you do?')
      
      scene_5 = False
      while scene_5 == False:
        first_door = input(f'Do you stay in {bed} or {open_1} the door? ')
        print()

        if first_door.upper() == bed:
          bed = True
          scene_5 = True
          print('You stayed in your bed, eventually the noises ceased and the morning came.')
          print('you go out your room and everything seems normal.')
          print()
          print('Your stay in this city is over')

        elif first_door.upper() == open_1:
          open_1 = True
          scene_5 = True
          print('You slowly open the door, everything is dark, something makes you go towards the stairs')
          print('For a very fast moment you see a pair of big yellow eyes glowing in the dark.')
          print('then you feel an excruciating pain on your chest and feel something warm and thick coming out of it and from your mouth')

        else:
          scene_5 = False
          print()
          print(wrong)
          print()
      
    elif room.upper() == second_floor:
      stay = 'STAY'
      open_2 = 'OPEN'
      print('The receptionist gives you the keys of the room and says:')
      print()
      print("It doesn't matter what you hear don't open the door until sunrise")
      print()
      print('You go to your room and find a small bedroom, a very simple bed on the left, and a window on the opposite wall')
      print('There are weird marks on the walls like someone had marked them with a knife or something very sharp')
      print('you lay on the bed to sleep and a few moments later you hear weird sounds coming from the next bedroom')
      print('it sounded like a growl and heavy steps. suddenly you hear a stamp right beside you and someone screams.')

      scene_2 = True
      
      print('What do you do?')

      scene_6 = False
      while scene_6 == False:
        second_door = input(f'Do you {stay} in bed or {open_2} the door? ')

        if second_door.upper() == stay:
          stay = True
          scene_6 = True

          print('You stayed in your bed as you were told,  eventually the noises ceased and the morning came.')
          print('You go out of your room and notice the same marks you saw in your room on the hall walls')
          print(' you also notice there are some red marks on the walls, on the floor and on the ceiling')
          print()
          print('Your stay in this city is over')

        elif second_door.upper() == open_2:
          open_2 = True
          scene_6 = True

          print('You slowly open the door, you cannot see anything')
          print('you start hearing a growl behind you.')
          print('Then you feel an excruciating pain on your back and feel something warm and thick coming out of it and from your mouth')
        else:
          scene_6 = False
          print()
          print(wrong)
          print()

    else:
      scene_2 = False
      print()
      print(wrong)
      print()

      
  
elif restaurant == True:
    
  eggs = 'EGGS'
  corn = 'CORN'
  print('You get into The Hungry Troll and a skinny, black haired young man')
  print('with a bang covering his right eye comes to you')
  print('he asks you to follow him to a table and he hands you a menu')
  print('on the menu there are only two options:')
  print()
  print(f'boiled {eggs} and roasted {corn}')
  print()
  scene_3 = False
  while scene_3 == False:    
    food = input('Which one will you choose? ')
    print()
    
    if food.upper() == eggs:

        eat = 'EAT'
        privacy = 'PRIVACY'

        print('The skinny guy quikly goes to the kitchen and comes back a few moments later with three green and stinky eggs')
        print('He puts them in front of you and stays there, staring at you as he was expecting for something')
        scene_3 = True
        print()
        print('What will you do? ')
        print()

        scene_7 = False
        while scene_7 == False:
          stink = input(f'Will you {eat} the eggs in front of the waiter or you will ask for some {privacy}? ')
          print()

          if stink.upper() == eat:

            scene_7 = True
            eat = True

            print('You decide to eat the eggs in front of the waiter')
            print('You take one of those weird eggs in your hand. it definitely does not look safe')
            print('but when you try it it is simply the best boiled egg you have tasted in your life')
            print('The waiter tells you it was his recipe and he gets very happy when you tell him you liked it.')
            print('after that he tells you where to find a good place to spend the night safely')
            print()
            print('Your stay in this city is over')

          elif stink.upper() == privacy:
            
            scene_7 = True
            privacy = True

            print('You tell the waiter you would like some privacy')
            print('he gets a little upset but he leaves you with the eggs')
            print('You take one of those weird eggs in your hand. it definitely does not look safe')
            print('but when you try it it is simply the best boiled egg you have tasted in your life')
            print('The waiter tells you it was his recipe and he gets very happy when you tell him you liked it.')
            print('after that he tells you where to find a good place to spend the night safely')
            print()
            print('Your stay in this city is over')

          else:
            scene_7 = False
            print()
            print(wrong)
            print()


    elif food.upper() == corn:
        
      look = 'LOOK'
      keep = 'KEEP'
      print('The waiter frowns and slowly walks to the kitchen. a few moments later he comes back with three roasted corn cobs covered in butter')
      print('They really look tasty and smell very well. when you are ready to eat them you feel as someone is observing you')
      scene_3 = True
      print()
      print('What will you do?')
      print()

      scene_8 = False
      while scene_8 == False:
        check = input(f'Will you {look} around to check if there is anyone looking at you or you will {keep} eating your corn? ')
        print()
      
        if check.upper() == look:
          scene_8 = True
          look = True
          print('you look around and you see the cook in the kitchen staring at you waiting for you to try the roasted corn')
          print('He looks very aprehensive, and when you taste the corn it is actually very good')
          print('when he sees you liked it he leaves the kitchen to talk to you')
          print('He invites you to spend the night at his house so you would not have to worry.')
          print()
          print('Your stay in this city is over')

        elif check.upper() == keep:
          scene_8 = True
          keep = True
          print('You start eating your corn quickly because it looks really good')
          print('and you realize it is one of the best roasted corn cobs you have ever eaten')
          print('when you are distracted with your corn the cook pops out of nowhere to talk to you')
          print('he is really happy you are enjoying his special dish')
          print('He invites you to spend the night at his house so you would not have to worry.')
          print()
          print('Your stay in this city is over')

        else:
          scene_8 = False
          print()
          print(wrong)
          print()

    else:
      print()
      print(wrong)
      print()
      scene_3 = False

elif walk == True:
    bush = 'BUSH'
    away = 'AWAY'
    print('The central square is big and there is a huge tree in the middle and many smaller ones around.')
    print("There are a few lamps so you don't have a good visibility.")
    print('There are also some bushes along the boarders of the square.')
    print()
    print('Suddenly, you hear a weird noise coming from the bushes behind you')
    print()
    print('What will you do?')
    print()

    scene_4 = False
    while scene_4 == False:  
      noise = input(f'check the {bush} or walk {away}? ')

      if noise.upper() == bush:
        scene_4 = True
        investigate = 'INVESTIGATE'
        safe = 'SAFE'
        print('You approach the bushes carefully and a cat jumps out from the bush and runs away scared')
        print('like something had frightened him a lot.')
        print('you feel as someone or something has been watching you for a while now.')
      
        print()

        print('What do you do?')
        print()

        scene_9 = False
        while scene_9 == False:
          goosebump = input(f'Will you {investigate} the place or go after a {safe} place? ')

          if goosebump.upper() == investigate:

            investigate = True
            scene_9 = True

            print('you take a better look at the dark square and the plants around')
            print('Everything seems completely desert, until you approach one of the bushes')
            print('For a moment you see what looks like thick gray fur and in the next moment you fall on the ground')
            print('you cannot feel your legs anymore')
            print(' it is too dark to distinguish anything. you stop feeling the rest of your boddy and everything becames dark')

          elif goosebump.upper() == safe:

            safe = True
            scene_9 = True

            print('you start walking fast away from the square')
            print('eventually for the first time you see a person in this city')
            print('It was a woman wearing a long coat, she was redhaired and was carrying a heavy suitcase')
            print(' She looks at you and tells you that you should not be at the street at that time')
            print('and that she would take you to a safe place.')
            print('She takes you to a house where you are able to sleep cozy and warm')
            print('You decide to leave the city on the next day') 
          
          else:
            scene_9 = False
            print()
            print(wrong)
            print()
      
      elif noise.upper() == away:
        scene_4 = True
        go = 'GO'
        decline = 'DECLINE'
        print('You leave the square quickly trying to find a safe place where you can stay')
        print('You find an inn but it is closed, so you bump into a big man wearing a coat and a hat.')
        print('he was very muscular and he seemed to be carrying very heavy metal things')
        print()
        print('He looks at you and says:')
        print()
        print("You shouldn't be on the streets by this time, come with me, I'll take you to a safe place.")
        print()
        print('What will you do?')
        print()

        scene_10 = False
        while scene_10 == False:
          stranger = input(f'Will you {go} with him, or you will {decline} his offer? ')
          print()

          if stranger.upper() == go:
            go = True
            scene_10 = True

            print('He tells you there are dangerous things in this city and he was there to make the city safer')
            print('while you walk with him you try to see what he carries and you see a handle of a sword')
            print('you cannot tell what kind of sword that is, but you also notice something that seems to be a big gun')
            print('hanging from his shoulder')
            print('he takes you to a house where you are able to sleep cozy and warm')
            print('You decide to leave the city on the next day')

          elif stranger.upper() == decline:

            decline = True
            scene_10 = True

            print('He tells you there are dangerous things in this city and he was there to make the city safer')
            print('you think he is a very suspecious man and leave him there')
            print('while you are wandering trying to find a place to stay, you pass in front of a manhole')
            print('you notice a pair of big yellow eyes staring you in a moment')
            print('and in the other moment you are being dragged into the manhole until no one saw you again')

          else:
            scene_10 = False
            print()
            print(wrong)
            print()
      else:
        print()
        print(wrong)
        print()
        scene_4 = False

