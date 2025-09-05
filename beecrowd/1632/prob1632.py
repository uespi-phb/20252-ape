
special_chars = 'AaEeIiOoSs'

use_cases = int(input())
while use_cases > 0:
    use_cases -= 1
    
    password = input()

    permutations = 1
    for char in password:
        if char in special_chars:
            char_perms = 3
        else:
            char_perms = 2
            
        permutations *= char_perms

    print(permutations)
