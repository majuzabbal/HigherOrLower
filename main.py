import random
from game_data import data
from art import logo, vs
from replit import clear

def get_correct_answer(compare_a, compare_b):
  followers_a = int(compare_a['follower_count'])
  followers_b = int(compare_b['follower_count'])

  if(followers_a > followers_b):
    correct_answer = 'a'
  else:
    correct_answer = 'b'

  return correct_answer

def get_compare_b(compare_a):
  compare_b = random.choice(data)

  while(compare_a == compare_b):
    compare_b = random.choice(data)
  
  return compare_b

def game():
  score = 0
  end_of_the_game = False
  compare_a = random.choice(data)
  print(logo)

  while not end_of_the_game:
    compare_b = get_compare_b(compare_a)

    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")

    print(vs)

    print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")

    correct_answer = get_correct_answer(compare_a, compare_b)

    user_answer = input("Who has more followers? Type 'A' or 'B': ")
    user_answer = user_answer.lower()

    clear()
    print(logo)

    if(user_answer == correct_answer):
      score += 1
      print(f"You're right! Current score: {score}.")
      compare_a = compare_b
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      end_of_the_game = True

game()
