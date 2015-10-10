# introducing how items will be found via numerology.
print ('''      ----------------------------------------------------------------------------
      Finding lost objects with the help of numbers is an old and proven method
      of tapping into your subconscious.  As with other aspects of life where the 
      relationship between cause and effect is obscured, doubts have no effect on
      the reality of what takes place.  Hence, if you find it difficult to create
      a nine-digit number, perhaps because you feel too self-conscious, changing 
      your mind ten times in the process, remember that no matter how you reach 
      the final number, it is the number that tells all.  Period.
      -----------------------------------------------------------------------------''')
print 'I am here to help you.'
# interaction with client, asks for name.
# questions if item lost?
 #asks person if they lost an object.

name = raw_input('Tell me your name. ')

    #check for response and return response
while True: 
    response = raw_input( "%s, Have you lost any object?  " % (name.capitalize()))
    # should check if intput is yes/no otherwise prompt user again to input correctly.
    if (response !='yes'  and  response != 'no'):
        print('Please answer "yes" or "no".')
        continue
    #if input correct then check for these conditions.    
    if response == "no":
        print "Thank you for visiting, %s." % (name.capitalize())
        break        
    if response == "yes":
        print "%s, concentrate on lost object and" % (name.capitalize()),"\n","                             _________"  
        number = raw_input("Input a nine-digit number:  ")   
        # sepearate each digit and add them to get a whole number.
        total_sum = sum(int(x) for x in number.strip())
        # testing condition that user enters 9 digits and the sum is greater than or equal to 6
        while (len(number) != 9 or total_sum <6):
            print "Either you did not enter a nine-digit number or the sum of your numbers is less then 6.  Please enter again."
            number = raw_input("input  a nine-digit number:")   
            # sepearate each digit and add them to get a whole number.
            total_sum = sum(int(x) for x in number.strip())
        
        # use total_sum to output a result    
        if total_sum  == 6:
            print ("It is near cleaning material or footgear.  Be careful not to blame someone else.")
            break
        elif total_sum == 7:
            print ("It is near items of clothing.")
            break
        elif total_sum == 8: 
            print ("Someone you dislike will deliver it to you.")
            break
        elif total_sum  == 9:
            print ("It is in the possession of a young person, but this person is not aware of that.  It will be presented to you innocently as a gift.")
            break
        elif total_sum == 10:
            print ("Look for it in the room you occupy most during your waking hours; not necessarily in your own house.")
            break
        elif total_sum == 11:
            print ("The object is close to a large body of water, such as a lake, pond, or ocean.")
            break
        elif total_sum == 12:
            print ("It is in a safe place, and you will find it while looking for something else.  It is better not to look for it.")
            break
        elif total_sum == 13:
            print ("It is in your clothes closet, possibly in a box containing shoes or a hat.")
            break
        elif total_sum  == 14:
            print ("It is under water.  You may need a plumber to recover it. If the object is made of cloth, look among your umbrellas, coats, and head or neck gear.")
            break
        elif total_sum == 15:
            print ("It is near animals or items kept for animals.  A child will be involved with the recovery of this object.")
            break
        elif total_sum == 16:
            print ("Without being consciously aware of it, you desired to lose it--permanently.")
            break
        elif total_sum == 17:
            print ("It is close to expensive items stored in a small place.")
            break
        elif total_sum == 18:
            print ("It is near soft objects, pillows, clothing, towels, or blankets.  You will find it and lose it again.  You will not retrieve it the second time.")
            break
        elif total_sum == 19:
            print ("It is near your house, but not near water.  Look around dry dirt or sand. ")
            break
        elif total_sum == 20:
            print (" It is close to water inside the house.  Look near the sink, in the bathroom, or around the water heater.")
            break
        elif total_sum == 21:
            print ("You will find it in a small storage area, possibly a file cabinet. Also look in your briefcase or purse.")  
            break
        elif total_sum == 22:
            print (" You will find it shortly, possibly through a dream.")
            break
        elif total_sum == 23:
            print ("It is not far from where you are at this time.  Look under or inside furniture.")
            break
        elif total_sum == 24:
            print ("Look in places where you used to store it in the past.  Also, ask other members of the household to look for it; they have a better chance of retrieving it.") 
            break
        elif total_sum == 25:
            print ("It is surrounded by something white, or a source of light.  It is not far away from you.")
            break
        elif total_sum == 26:
            print ("An older man, probably a relative, knows where to find it, but is not aware that you are looking for it. ")
        elif total_sum == 27:
            print ("It's in the garage, possibly inside a car.  It is damaged.")
            break
        elif total_sum == 28:
            print ("Someone else has found it and is unwilling to surrender it to the rightful owner.  This is a Karmic Lesson in detachment.")
            break
        elif total_sum == 29:
            print ("Someone close to you will return it to you. This person is either much older than you are, or is a very young child.")
            break
        elif total_sum == 30:
            print ("You lost the object while you were enjoying yourself in the company of children, probably during a creative endeavor.  Look among toys or art materials.")
            break
        elif total_sum== 31:
            print ("It is near moving water, not far from the house. You will find it.")
            break
        elif total_sum== 32:
            print ("It is in a high place, probably outside the house or on a window ledge.")
            break
        elif total_sum== 33:
            print ("It is near a religious artifact that has been stored.  Also, look where you store Christmas decorations.")
            break
        elif total_sum== 34:
            print ("It is near a light source in your house or in your place of work.")
            break
        elif total_sum== 35:
            print ("It is near running water inside the house. It is  not visible without moving other items.")
            break
        elif total_sum== 36:
            print ("It is in the possession of someone close to you.   Look in the closets and storage places of other members of your household.")
            break
        elif total_sum== 37:
            print ("Look near a religious artifact, in your house or in the house to the east of you.")
            break
        elif total_sum == 38:
            print ("It was lost on your way to a place you visit regularly, such as a grocery store, a friend's home in the neighborhood, or your place of work.  It is visible and in the open.")
            break
        elif total_sum == 39:
            print ("It is in a high place.  The items surrounding it are related to play or creative activities.")
            break
        elif total_sum == 40:
            print (" It is surrounded by soft material, possibly as a form of safekeeping and protection.")
            break
        elif total_sum == 41:
            print ("It is low in a closet or near footgear.")
            break
        elif total_sum == 42:
            print ("It is in a place where cooking is done, probably not your own house.  Call restaurants or other places you visited.")
            break
        elif total_sum == 43:
            print ("It is near a place of rest, a bed or a lounge.  It may also be between folded sheets or blankets.")
            break
        elif total_sum == 44:
            print ("The object is in a dirty place, or in a part of the house that is being remodeled, and it will be found by a worker.")
            break
        elif total_sum == 45:
            print ("You pass it closely every day.  Keep your eyes open.")
            break
        elif total_sum == 46:
            print ("Ask a coworker, in particular the one your feel close to.  Wait a few days from now before asking.")
            break
        elif total_sum == 47:
            print ("More than one person is aware of the location of the object. One is a liar. Question your subordinates.")
            break
        elif total_sum == 48:
            print ("It is close to water or cooking utensils.  Also, look in any place your store alcoholic beverages.")
            break
        elif total_sum == 49:
            print ("Don't bother looking for it.  The chances of finding it are remote, and it has already been badly damaged.")
            break 
        elif total_sum == 50:
            print ("It has been moved since you lost it.  Look inside carrying cases or vehicles of transportation.")
            break 
        elif total_sum== 51:
            print ("It is in a church or another place of worship.  It may also be in a place of healing, such as a hospital.")
            break
        elif total_sum== 52:
            print ("At least one person has handled the object since you lost it, probably someone you have never met, but who is close to someone you know well.")
            break
        elif total_sum== 53:
            print ("You are going on a trip, and you will receive it upon your return.  It will be found during your absence.")
            break
        elif total_sum== 54:
            print ("It is carried around, or otherwise being transferred from one place to another.  Recovery is certain, but it will take some time.")
            break
        elif total_sum== 55:
            print ("it was displaced by the movement of water or wind.  You will find it when you least expect it.")
            break
        elif total_sum == 56:
            print ("Retrace your steps now.  Even when you lost it several days ago, you passed by it a short while later.  Water is nearby.")
            break
        elif total_sum == 57:
            print ("You lost it, and you will find it during sporting activities.  In particular, look in the pants pockets of sports gear.")
            break
        elif total_sum == 58:
            print ("You are the victim of someone's greed or anger.   Your chances of getting it back are slim.")
            break
        elif total_sum == 59:
            print ("It is in a dry and dark place, probably a small cabinet,  Look around food or eating utensils.")
            break
        elif total_sum == 60:
            print ("There is no chance of recovery.")
            break
        elif total_sum == 61:
            print ("Look in the cellar or in some other place underneath the house.  It is exposed to the elements.")
            break
        elif total_sum == 62:
            print ("You lost is a considerable distance from the house, and you will not recover it.")
            break
        elif total_sum == 63:
            print ("The object is in a forgotten place of storage, surrounded by items you have not laid eyes on in some time.")
            break
        elif total_sum == 64:
            print ("There is no need to look for it.  You will find it when you clean or reorganize your house.")
            break
        elif total_sum == 65: 
            print ("You will pass by it in the next few hours.  Your chances of finding it, however, are not good.")
            break
        elif total_sum == 66:
            print ("Thievery is the cause of your loss.  The person who took it has a physical problem; either the hand or the foot is damaged.")
            break
        elif total_sum == 67:
            print ("A younger family member, probably female, will find it, and return it.")
            break
        elif total_sum == 68:
            print ("It was lost twice.  Someone has retrieved it, and lost it before returning it to you.  That someone will not admit to this.  A third person will find it and return it.")
            break
        elif total_sum == 69:
            print ("It is a considerable distance from your house.  Call friends or relatives you visited not too long ago.  It was found, but the honest finder does not know that it is yours.")
            break
        elif total_sum == 70:
            print ("You did not lose it. It is simply mislaid.  Look near study materials.  Think.")
            break
        elif total_sum == 71:
            print ("The object is close by.  You will find it when you relax.  It is near printed material.")
            break
        elif total_sum == 72:
            print ("Look in vases, bowls, or other containers that have an open top.")
            break
        elif total_sum == 73:
            print ("You should involve the police or another official.  It was most likely taken from you.")
            break
        elif total_sum == 74:
            print ("It will be returned to you by someone whom you have not respected, or whom you have treated with some injustice.")
            break
        elif total_sum == 75:
            print ("It will be returned to you, but it will be damaged.")
            break
        elif total_sum == 76:
            print ("It is in the kitchen or pantry.  Look near flour products.")
            break
        elif total_sum == 77:
            print ("Don't spend too much time searching.  It will be found and returned to you only after you do the potential finder a favor.")
            break
        elif total_sum == 78:
            print ("It is near animals.  It is damaged, and the chances of recovery are not good.")
            break
        elif total_sum == 79:
            print ("It is in a tin can or other metal container.")
            break
        elif total_sum == 80:
            print ("It was locked away with other items, and it is now in a container inside another container.  You will find it when you are not looking.")  
            break
        elif total_sum == 81:
            print ("It went out with the garbage; you will not be able to retrieve it. It's covered by dirt, and it will soon disintegrate.")
            break
        else:
            print "Thank you for visiting, %s." % (name)
            break


