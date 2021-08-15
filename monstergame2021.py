floor0 = ['nothing','nothing','stairs up','nothing', 'a monster','nothing','sword']
floor1 = ['nothing' , 'key', 'stairs up','stairs down','paper','magic stones' ,'nothing']
floor2 = ['a monster' , 'stairs up','stairs down', 'nothing','sword', 'a monster','nothing']
floor3 = ['stairs down','stairs up door','nothing', 'big sword', 'nothing','sword','nothing']
floor4 = ['a big monster', 'nothing', 'stairs down', 'sword', 'magic stones','door','troll']
inventory = []
floors = [floor0, floor1, floor2,floor3,floor4]
floor = 0
room = 0
import random
x = [random.randint(1,10)] + [random.randint(1,10)] + [random.randint(1,10)] + [random.randint(1,10)]
gamestate = True
while gamestate == True:
    
    print('You are on floor' , floor +1 ,  ',You are in room' , room +1 , ', There is' , floors[floor][room])
    print(inventory)

    
    action = input('move, fight, grab, run away : ') 
    if action == 'move':
        direction = input('up, down, right, left : ')
        if direction == 'up':
            if floors[floor][room] == 'stairs up':
               floor += 1
            elif floors[floor][room] =='stairs up door':
                if 'key' in inventory:
                    floor += 1
                    inventory.remove('key')
                    floors[floor][room] = 'stairs up'
            else:
                print('can not')
        elif direction == 'down':
            if floors[floor][room] == 'stairs down':
                floor -= 1
            else:
                print('can not')
        elif direction == 'right':
            room += 1
            if floors[floor][room] == 'door':
                if paper in inventory:
                    room += 1
                    floors[floor][room] = 'nothing'
        elif direction == 'left':
            room -= 1
        elif floor > 4:
            print('can not')
        else:
            print('can not')

        
    elif action == 'grab':
        if floors[floor][room] == 'magic stones':
            inventory.append(floors[floor][room])
            floors[floor][room] = 'nothing'
        elif floors[floor][room] == 'sword':
            inventory.append(floors[floor][room])
            floors[floor][room] = 'nothing'
        elif floors[floor][room] == 'big sword':
            inventory.append(floors[floor][room])
            floors[floor][room] = 'nothing'
        elif floors[floor][room] == 'nothing':
            print('can not')
        elif floors[floor][room] == 'paper':
            print('the password is ', x)
            inventory.append(floors[floor][room])
            floors[floor][room] = 'nothing'
        elif floors[floor][room] == 'key':
            inventory.append(floors[floor][room])
            floors[floor][room] = 'nothing'
                               

    elif action == 'run away':
        if floors[floor][room] == 'a monster':
            room -=1
       

    
    elif action == 'fight':
        if floors[floor][room] == 'a monster':
            if 'sword' and 'magic stones' in inventory:
                print('monster is killed and dropped a key')
                inventory.remove('sword')
                inventory.append('key')
        elif floors[floor][room] == 'troll':
            if 'big sword' and 'magic stones' in inventory:
                print('troll killed')
                inventory.remove('magic stones')
        elif floors[floor][room] == 'a big monster':
            if 'big sword' and 'magic stones' in inventory:
                print('big monster is killed')
                print('you won')
                gamestate == False
            else:
                print('you died')
                gamestate == False
