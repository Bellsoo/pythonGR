#Echauffements
#fonction produce_default_dict
def produce_default_dict():
    default_dict = {'root': 'password'}
    return default_dict

test = produce_default_dict()
print(test)


#fonction salutation
def salutation(nom, age) :
    texte = "Bonjour {nom}, vous avez actuellement {age} an{'s' if age != '0','1' else ''}."
    return salutation

salutation1 = ('gael', '24')
print(salutation1)

salutation2 = ('bébé', '0')
print(salutation2)



#fonction power_2
def power_2(limit):
    i = 1
    while i <= limit:
        return 2**i

example1 = power_2(5)
print(example1)



#fonction check_ip_format
def check_ip_format(ip):
    format = ip.split('.')

    if len(format) != 4:
        return False

    else:
        return True

print(check_ip_format('10.0.0.0'))
print(check_ip_format('192.12.')) 

