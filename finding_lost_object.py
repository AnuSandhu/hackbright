# introducing how items will be found via numerology.
#print ("Finding lost objects with the help of numbers is an old and proven method of tapping into your subconscious.  As with other aspects of life where the relationship between cause and effect is obscured, doubts have no effect on the reality of what takes place.  Hence, if you find it difficult to create a nine-digit number, perhaps because you feel too self-conscious, changing your mind ten times in the process, remember that no matter how you reach the final number, it is the number that tells all.  Period.")
print 'I am here to help you.'
# interaction with client, asks for name.
# questions if item lost?
 #asks person if they lost an object.

name = raw_input('Tell me your name. ')
response = raw_input( "%s, Have you lost any object? Please answer with a yes or no.  " % (name))
digits = []

#check for response and return response
while True: 
    
    if response == "no":
        print "Thank you for visiting, %s." % (name)
        break        
    if response == "yes":
        print "%s, Concentrate on lost object and" % (name)
        number = raw_input("input  a nine-digit number:" )     
        total_sum = sum(int(x) for x in number.strip())
        print total_sum
        if total_sum  == 6:
            print"It is near cleaning material or footgear.  Be careful not to blame someone else."
            break
        elif total_sum == 7:
            print"It is near items of clothing."
            break
        elif total_sum == 8: 
            print "Someone you dislike will deliver it to you."
            break
        elif total_sum  == 9:
            print "It is in the possession of a young person, but this person is not aware of that.  It will be presented to you innocently as a gift."
            break
        elif total_sum == 10:
            print"Look for it in the room you occupy most during your waking hours; not necessarily in your own house."
            break
        elif total_sum == 11:
            print "The object is close to a large body of water, such as a lake, pond, or ocean."
            break
        elif total_sum == 12:
            print "It is in a safe place, and you will find it while looking for something else.  It is better not to look for it."
            break
        elif total_sum == 13:
            print "It is in your clothes closet, possibly in a box containing shoes or a hat."
            break
        elif total_sum  == 14:
            print "It is under water.  You may need a plumber to recover it. If the object is made of cloth, look among your umbrellas, coats, and head or neck gear."
            break
        else:
            print "Thank you for visiting, %s." % (name)
            break



 

   	

