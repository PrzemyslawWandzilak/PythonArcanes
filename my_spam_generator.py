# Lets Iterate Generate Yield Enumerate folks!

# Iterator attack
def lets_iterate():
    my_list = ['Spam', 'Egg', 'SpamEgg']
    my_list_from_list = [e+e for e in my_list]
    
    print("\nLets iterate over Spam List of "
          + str(type(my_list_from_list)))
    for element in my_list_from_list:
        print element

# Generator attack
def lets_generate():
    my_list = ['Spam', 'Egg', 'SpamEgg']
    my_spam_generator = (e+e for e in my_list)
    
    print("\nLets iterate over my_spam_generator of " 
          + str(type(my_spam_generator)))
    for element in my_spam_generator:
        print element

# Yield attack
def yield_helper():
    my_list = ['Spam', 'Egg', 'SpamEgg']
    for e in my_list:
        yield e+e

def lets_yield():
    my_spam_generator = yield_helper()
    
    print("\nLets iterate over yielded my_spam_generator of"
          + str(type(my_spam_generator)))
    for element in my_spam_generator:
        print element

# Massive enumrate
def my_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

def lets_enumerate():
    my_list = ['Spam', 'Egg', 'SpamEgg']
    my_enum_generator = my_enumerate(my_list, start=50)
    
    print("\nLets enumerate over my_list returning "
          + str(type(my_enum_generator)))
    for n, elem in my_enum_generator: 
        print("[%d]:\"%s\"" % (n, elem))


def main():
    lets_iterate()
    lets_generate()
    lets_yield()
    lets_enumerate()

if __name__=='__main__':
    main()