
test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    n, number = map(int, input().split())
    guesses = map(int, input().split())
    
    best_guess = 0
    best_diff = 200
    for k, guess in enumerate(guesses):
        diff = abs(guess - number)
        if diff < best_diff:
            best_diff = diff
            best_guess = k
    print(best_guess + 1)
