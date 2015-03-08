import jediduck.duck as d

print "start duck"

def react_to_death_star(object):
    try:
        object.quack()
    except:
        print "Not a Duck"

    try:
        object.force()
    except:
        print "Not a Jedi Duck"
    
    print "\n"

# Create jedi ducks and actor
obi_duck = d.JediDuck("Obi")
anakin_duck = d.DarkDuck("Anakin")
actor = d.Actor()

# check if all are jedi ducks
react_to_death_star(obi_duck)
react_to_death_star(anakin_duck)
react_to_death_star(actor)

#add some lambdas to boost coolness
print(obi_duck.jedi_modulus(range(1,217,1)))