n = int( input() )

for i in range( n ):
    word = input()
    new = [*word]
 
    s = str(len(new)-2) 

    if len(new) > 10:
        print(new[0] + s + new[-1])    
    else:
        print(word)
