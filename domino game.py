import random

#Here we get the initial data for the game
def generate_starting_set():
    side_one = []
    side_two = []

    for i in range(7):
        side_one.append(i) 
        side_two.append(i)

    final_list = []

    for el in side_one:
        for i in side_two:
            x = [el,i]
            x.sort()
            if x not in final_list:
                final_list.append(x)
    return final_list

def random_split_begining(list_of_dominos):
    stock_number = 14
    player_1 = 7
    player_2 = 7

    random.shuffle(list_of_dominos)

    stock_pieces = []

    for _ in range(stock_number):
        x = list_of_dominos.pop()
        stock_pieces.append(x)
    
    computer_pieces = []

    for _ in range(player_1):
        x = list_of_dominos.pop()
        computer_pieces.append(x)

    player_pieces = []

    for _ in range(player_2):
        x = list_of_dominos.pop()
        player_pieces.append(x)

    return stock_pieces, computer_pieces, player_pieces

def domino_snake(stock_pieces, computer_pieces, player_pieces):
    
    snakes = [[6,6],[5,5]]

    max_domino = []
    while True:
        for el in snakes:
            if el in player_pieces:
                first_move = 'computer'
                max_domino.append(el)
                player_pieces.remove(el)                
                break
            elif el in computer_pieces:                
                first_move = 'player'
                max_domino.append(el)
                computer_pieces.remove(el)                
                break
            else: 
                first_move = 'reshuffle'
                
        break

    if first_move != 'reshuffle':
        max_domino.sort()
        snake = [max_domino[0]]
    else:
      snake = 'nothing'
 
    return first_move, snake, player_pieces, computer_pieces
    




#organizing first info together


def initial_info():
    
    list_of_dominos = generate_starting_set()
    stock_pieces, computer_pieces, player_pieces = random_split_begining(list_of_dominos)
    first_move, snake, player_pieces, computer_pieces = domino_snake( stock_pieces, computer_pieces, player_pieces)
    return stock_pieces, first_move, snake, player_pieces, computer_pieces
    
def start_or_reshuffle(first_move):
  if first_move == 'reshuffle':
    print('Sorry, we have to reshuffle!')
    return False

def move_one(first_move, computer_pieces,player_pieces):
    if first_move == 'player':
      sign_top = 'Computer pieces: 6'    
      length = len(player_pieces)
      pieces =  player_pieces
      sign_bottom = "Status: It's your turn to make a move. Enter your command."
    else:
      sign_top ='Computer pieces: 7'         
      length = len(player_pieces)
      pieces =  player_pieces
      sign_bottom = 'Status: Computer is about to make a move. Press Enter to continue...'
    return sign_top,length,pieces,sign_bottom 

def move_all_others(played, computer_pieces,player_pieces):
    if played == 'computer':
      sign_top = 'Computer pieces: '+str(len(computer_pieces))   
      length = len(player_pieces)
      pieces =  player_pieces
      
    else:
      sign_top ='Computer pieces: '+str(len(computer_pieces))            
      length = len(player_pieces)
      pieces =  player_pieces
      
    return sign_top,length,pieces, 
  

  


#actions
def print_header(stock_pieces):
  line = '='*70
  print(line)
  print('Stock size:',len(stock_pieces)) 
  
def first_moving(sign_top,length,pieces,sign_bottom, snake):
  print(f'{sign_top}\n')
  
  print(f'{snake[0]}\n')
  
  print('Your pieces:')
  
  count = 1
  for i in range(length):
    print(f'{count}:{pieces[count-1]}')
    count += 1

  print(f'\n{sign_bottom}')

def display_main(sign_top,length,pieces, snake):
    print(f'{sign_top}\n')
  
    
    if len(snake)>6:
     
      part_num_1 = snake[0:3]
      part_1 = ''.join(map(str, part_num_1))
      part_num_2 = snake[-3:]
      part_2 = ''.join(map(str, part_num_2))
      print(f'{part_1}...{part_2}\n')
      
    else:
      whole = ''.join(map(str, snake))
      print(f'{whole}\n')
    
    print('Your pieces:')
    
    count = 1
    for i in range(length):
      print(f'{count}:{pieces[count-1]}')
      count += 1


    # print(f'\n{sign_bottom}')


  
#Game

def firsy_display(stock_pieces, first_move, snake, player_pieces, computer_pieces):
  print_header(stock_pieces)
  sign_top,length,pieces,sign_bottom = move_one(first_move, computer_pieces,player_pieces)
  first_moving(sign_top,length,pieces,sign_bottom,snake)
  return stock_pieces, snake,computer_pieces

def display(stock_pieces, snake, player_pieces, computer_pieces,played):
  print_header(stock_pieces)
  sign_top,length,pieces = move_all_others(played, computer_pieces,player_pieces)
  display_main(sign_top,length,pieces, snake)



def check_player_input(player_pieces):
      available_pieces = len(player_pieces)
      while True:
        try:
            while True:
                choice = int(input())
                if abs(choice) > available_pieces:
                   print("Invalid input. Please try again.")
                else:
                  return choice, False
            break
        except ValueError:
             print("Invalid input. Please try again.")

def check_rules_player_input(snake, player_pieces):
    
    while True:
        choice = check_player_input(player_pieces)[0]
        if choice > 0:
            choice_working = choice - 1
            move_1 = abs(choice_working)
            piece = player_pieces[move_1]

            if snake[-1][1] == piece[0]:
                return piece,choice, False
            elif snake[-1][1] == piece[1]:
                piece.reverse()
                return piece, choice, False
            else:
                print("Illegal move. Please try again.")
        elif choice < 0:
            choice_working = choice + 1
            move_1 = abs(choice_working)
            piece = player_pieces[move_1]

            if snake[0][0] == piece[0]:
                piece.reverse()
                return piece, choice, False
            elif snake[0][0] == piece[1]:
                
                return piece, choice, False
            else:
                print("Illegal move. Please try again.")
        else:
            return 'none',choice, False

def check_rules_computer_input(snake, pieces):
  input()

  
  # input()
  possible_positive_moves = []
  possible_negative_moves = []
  all_moves = []
  all_moves_clean = []
  for i in pieces:
    piece = i
    if snake[-1][1] == piece[0]:
      possible_positive_moves.append(piece)
      is_reversed = (False, piece)
      all_moves.append(is_reversed)
    elif snake[-1][1] == piece[1]:
      piece.reverse()
      possible_positive_moves.append(piece)
      is_reversed = (True, piece)
      all_moves.append(is_reversed)
      
         
  for i in pieces:
    piece = i
    if snake[0][0] == piece[0]:
       piece.reverse()
       possible_negative_moves.append(piece)
       is_reversed = (True, piece)
       all_moves.append(is_reversed)
    elif snake[0][0] == piece[1]:
       possible_negative_moves.append(piece)
       is_reversed = (False, piece)
       all_moves.append(is_reversed)
   

  for el in all_moves:
    all_moves_clean.append(el[1])

 

        
  dict_numbers = {0:0,1:0,2:0,3:0,4:0,5:0,6:0}

  if len(all_moves_clean) > 0:
      for card in all_moves_clean:
        for num in card:
          dict_numbers[num] += 1
      for card in snake:
        for num in card:
          dict_numbers[num] += 1

      dict_with_moves = []
      for i in all_moves_clean:
        first = i[0]
        second = i[1]
        number = dict_numbers[first] + dict_numbers[second]
        dict_with_moves.append(number)
    
      maximum_index = dict_with_moves.index(max(dict_with_moves))
    
      piece_to_play = all_moves_clean[maximum_index]
      if piece_to_play in piece_to_play:
        side = 'right'
      else:
        side = 'left'

      action = 'move'
       

      if all_moves[maximum_index][0] == False:
        orientation = 'not_reversed'
      else:
        orientation = 'reversed'
       
      return piece_to_play,side,action, orientation
 
  else:
    return 'none','none', 'skip', 'none'
    
    
      # while True:
          # possible_positive_moves = []
          
          # number_0f_pieces = len(computer_pieces)
          # negative = -(number_0f_pieces)
          # choice = random.randint(negative,number_0f_pieces)
          # choice = check_player_input(pieces)[0]
          # for i in len(pieces):
          #   # POSITIVE CHOICE
          #   piece = pieces[i]
          #   if snake[-1][1] == piece[0]:
          #     possible_moves.append(piece)
          #         # return piece,choice, False
          #   elif snake[-1][1] == piece[1]:
          #     piece.reverse()
          #     possible_moves.append(piece)    
          #         # return piece, choice, False
          # for i in len(pieces):



          # if choice > 0:
          #     choice_working = choice - 1
          #     move_1 = abs(choice_working)
              

            
              
          # elif choice < 0:
          #     choice_working = choice + 1
          #     move_1 = abs(choice_working)
          #     piece = pieces[move_1]

          #     if snake[0][0] == piece[0]:
          #         piece.reverse()
          #         return piece, choice, False
          #     elif snake[0][0] == piece[1]:
                  
          #         return piece, choice, False
             
        # else:
        #     return 'none',choice, False            

def computer_move(stock_pieces,computer_pieces,snake):
    played = 'computer'
    next_play = 'player'
    piece,side,action,orientation = check_rules_computer_input(snake, computer_pieces)

    if orientation == 'reversed':
      original_piece = piece.reverse()
    else:
      original_piece = piece
    
    
      
    # if choice < 0:
    #     side = 'left'
    #     choice = choice + 1
    #     action = 'move'
    # elif choice > 0:
    #     side = 'right'
    #     choice = choice - 1
    #     action = 'move'
    # else:
    #     action = 'skip'
       
    # choice = abs(choice) 
      
    if action == 'move':
          can_play = True
          if (side == 'left'):                
                snake.insert(0, piece)
                # print(f'computer pieces 1:{computer_pieces}')
                computer_pieces.remove(original_piece)
                # print(f'computer pieces 2:{computer_pieces}')
                return stock_pieces, computer_pieces, snake,next_play,played,can_play
                 
          else:
            # print(f'computer pieces 1:{computer_pieces}')
            snake.append(piece)
            computer_pieces.pop(original_piece)
            # print(f'computer pieces 2:{computer_pieces}')
            return stock_pieces, computer_pieces, snake,next_play,played,can_play
             
    else:
          if len(stock_pieces)>0:
            pieces_in_stock = len(stock_pieces)-1
            ran = random.randint(0, pieces_in_stock)
            # print(f'computer pieces 1:{computer_pieces}')
            el = stock_pieces.pop(ran)
            # print(f'computer pieces 2:{computer_pieces}')
            computer_pieces.append(el)
            can_play = True
            return stock_pieces, computer_pieces, snake,next_play,played,can_play
          else:
            stock_pieces = stock_pieces
            computer_pieces = computer_pieces
            snake = snake
            next_play = next_play
            played = played
            can_play = False
            return stock_pieces, computer_pieces, snake, next_play, played,can_play
          
              

def player_move(stock_pieces,player_pieces,snake):
    played = 'player'
    next_play = 'computer'
    # choice = check_player_input(player_pieces)[0]
    piece_to_play, choice, status = check_rules_player_input(snake,player_pieces)

    if choice < 0:
        side = 'left'
        choice = choice + 1
        action = 'move'
    elif choice > 0:
        side = 'right'
        choice = choice - 1
        action = 'move'
    else:
        action = 'skip'
       
    choice = abs(choice) 
      
    if action == 'move':
          can_play = True
          if (side == 'left'):                
                snake.insert(0,piece_to_play)
                player_pieces.pop(choice)
                return stock_pieces, player_pieces, snake,next_play,played,can_play
                
          else:
            
            snake.append(piece_to_play)
            player_pieces.pop(choice)
            return stock_pieces, player_pieces, snake,next_play,played,can_play
            
    else:
          if len(stock_pieces)>0:
            pieces_in_stock = len(stock_pieces)-1
            ran = random.randint(0, pieces_in_stock)
            el = stock_pieces.pop(ran)
            player_pieces.append(el)
            can_play = True
            return stock_pieces, player_pieces, snake,next_play,played,can_play
          else:
            stock_pieces = stock_pieces
            player_pieces = player_pieces
            snake = snake
            next_play = next_play
            played = played
            can_play = False
            return stock_pieces, player_pieces, snake, next_play, played,can_play
    
 
def check_victory(player_pieces, computer_pieces, played, snake):
    msg1 = '\nStatus: The game is over. You won!'
    msg2 = '\nStatus: The game is over. The computer won!'
    msg3 = "\nStatus: The game is over. It's a draw!"
    msg4 = "Status: It's your turn to make a move. Enter your command."
    msg5 = 'Status: Computer is about to make a move. Press Enter to continue...'
    
    if len(player_pieces) < 1 or len(computer_pieces) < 1:
        if played == 'player':
           print(msg1)
        else:
           print(msg2)
        return False
        
    elif snake[0][0] == snake[-1][1]:
      number = []
      for i in snake:
          for num in i:
              number.append(num)
      num_count = number.count(snake[0][0])
      if num_count > 7:
           print(msg3)
           return False
    
    if played == 'player':
           print()
           print(msg5)
          
    else:
           print()
           print(msg4)
            
   

    # return True            
       
def check_the_draw(can_play_1, can_play_2,stock_pieces):
  msg3 = "\nStatus: The game is over. It's a draw!"
  if stock_pieces == 0 and can_play_1 ==  False and can_play_2 == False:
    print (msg3)
    return False



def circle(first_move, stock_pieces,computer_pieces,snake,player_pieces):
    if first_move == 'computer':
      while True :
        stock_pieces, computer_pieces, snake, next_play,played,can_play_1 = computer_move(stock_pieces, computer_pieces, snake)
        display(stock_pieces, snake, player_pieces, computer_pieces,played)
        check = check_victory(player_pieces, computer_pieces, played, snake)
        if check == False:
          break
        draw = check_the_draw(can_play_1, can_play_2,stock_pieces)
        if draw == False:
          break

        stock_pieces, player_pieces, snake, next_play,played,can_play_2 = player_move(stock_pieces, player_pieces, snake)
        display(stock_pieces, snake, player_pieces, computer_pieces,played)
        check = check_victory(player_pieces, computer_pieces, played, snake)
        if check == False:
          break
        draw = check_the_draw(can_play_1, can_play_2,stock_pieces)
        if draw == False:
          break
    else:
      while True :
        stock_pieces, player_pieces, snake, next_play,played,can_play_1 = player_move(stock_pieces, player_pieces, snake)
        display(stock_pieces, snake, player_pieces, computer_pieces,played)
        check = check_victory(player_pieces, computer_pieces, played, snake)
        if check == False:
          break
        draw = check_the_draw(can_play_1, can_play_2,stock_pieces)
        if draw == False:
          break

        stock_pieces, computer_pieces, snake, next_play,played,can_play_2 = computer_move(stock_pieces, computer_pieces, snake)
        display(stock_pieces, snake, player_pieces, computer_pieces,played)
        check = check_victory(player_pieces, computer_pieces, played, snake)
        if check == False:
          break
        draw = check_the_draw(can_play_1, can_play_2,stock_pieces)
        if draw == False:
          break
        

stock_pieces, first_move, snake, player_pieces, computer_pieces = initial_info()
x = start_or_reshuffle(first_move)


if x != False:
      stock_pieces, snake, computer_pieces = firsy_display(stock_pieces, first_move, snake, player_pieces, computer_pieces)
      # game = check_victory(player_pieces, computer_pieces, played, snake)
      circle(first_move, stock_pieces,computer_pieces,snake,player_pieces)
      