# Control Flows

# Control Flow -> flow through a particular decision progress.

# if statement

age = 19

# if age > 18:
#     print('You are the correct age to watch this film and can buy a ticket')
# if age < 18:
#     print('You are not old enough, you cannot buy a ticket to watch a film')

# elif and else
film_rating = "universal"

if film_rating.lower() == "universal":
    print('All age groups can watch this film')
elif film_rating.lower() == "pg":
    print('General viewing but parental guidance advised')
elif film_rating.lower() == "12" or film_rating.lower() == "12A":
    print('12 rated movies may not be suitable for those under 12, supervision is recommended')
elif film_rating.lower() == "15":
    print('Your must be 15 to watch 15 rated movies in the cinema')
elif film_rating.lower() == "18":
    print('Your must be 18 to watch 18 rated movies in the cinema')
else:
    print('This is not a correct rating, please use universal, pg, 12, 15, 18')