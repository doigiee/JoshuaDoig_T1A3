day_left = 3
days = 0
level= 1

while days < 3 or level < 100:
    print ('you have {days_left} until the town festival and have used {days} with you blob and your blobs level is {level}')
    # offer activity 
    # print (what_activity)
    if input() == str('walk'):
        level += 35
        day_left -= 1 
        print(f'your blob went up 35 levels congrats your new level is {level} you have days {day_left}')
    
    elif input() == str('eat'):
        level += 25
        print(f'your blob went up 25 levels congrats your new level is {level} you have days {day_left}')
    
    elif input() == str('play'):
        level += 40
        print(f'you and your blob had a great afternoon together playing ,your blob went up 35 levels congrats your new level is {level} you have days {day_left}') 
    