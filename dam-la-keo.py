import random
n=int(input('How manay times do you want to play? '))
for i in range(n):
    win=0
    lose=0
    player=input('select: dam - la - keo :')   # play select
    if player !='dam' and player !='la' and player !='keo':
        print('Your selection is incorrect. Pleae choose again')
        player=input('select: dam - la - keo :')
    computer=random.randint(0,2)  # computer select
    if computer == 0:
        computer='dam'
    elif computer ==1:
        computer = 'la'
    else:
        computer = 'keo'

    # Show select
    print('------')
    print('Your select is: ',player)
    print('Computer select is: ',computer)
    if player=='dam':
        if computer == 'dam':
            print('reconcile')
        elif computer == 'la':
            print('Win')
            win+=1
        else:
            print('Lose')
            lose+=1
    elif player == 'la':
        if computer == 'la':
            print('reconcile')
        elif computer == 'keo':
            print('Win')
            win+=1
        else:
            print('reconcile')
            lose+=1
    else:
        if computer == 'keo':
            print('reconcile')
        elif computer == 'dam':
            print('Win')
            win+=1
        else:
            print('Lose')
            lose+=1
if win>lose:
    print('You are win')
elif win<lose:
    print('You are lose')
else:
    print('You are reconcile')