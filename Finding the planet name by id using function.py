id = input ('Enter the id of the planet :')

def planet(i) :
    planet = {'1':'mercury','2' : 'Venus','3' :'Earth','4': 'Mars' ,'5' : 'Jupiter' ,'6' :'saturn','7' :'uranus','8' :'Neptune','9' :'Pluto' } 
    ans = planet.get(i,'ID NOT FOUND')
    print ('The planet name for the entered key is :',ans )

planet(id)

