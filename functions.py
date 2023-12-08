def produce_default_dict(): #Fonction 1
    default_dict = {'root': 'password'}
    return default_dict

test = produce_default_dict() # Pour tester si ça marche
print(test)


def salutation(nom, age) :# Fonction 2
    texte = "Bonjour {nom}, vous avez actuellement {age} an{'s' if age != '0','1' else ''}."

salutation = salutation_1('gael', '24')
salutation = salutation_2('bébé', '0')

test_2 = salutation_1()
test_3 = salutation_2()
print(test_2)
print(test_3)

#apporter des resultats ici



def power_2(limit) :
    return [2**i for i in range(limit + 1)]

# Exemple d'utilisation
resultat = power_2(10)
print(resultat)



