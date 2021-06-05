import random


starter = ['Once upon a time in modern world, ', 'Once upon a time, ', 'Under the blue sky, ']
character1_girl = ['there lived a mermaid named ', 'there lived a princess named ', 'there lived a young businesswoman named ']
character1_boy = ['there lived a vampire boy named ', 'there lived a crown prince named ', 'there lived a young CEO named ']
background_girl = ['She was a spoiled kid before the family bancrupcy. ', 'She was bullied by her classmates. ', 'She was mocked for being a cleaning service.']
background_boy = ['He was a witness of his father suicide.', 'He was a poor street hawker. ', 'He used to badmouth everyone. ']
plot_girl = ['One day when she was eating, ', 'By the time she went to the mall, ', 'When she want to change herself, ']
plot_boy = ['One day when he was attacked, ', 'When he was staring at the road, ', 'By the time he reached the palace, ']
character2_boy = ['a kind boy approached, he named ', 'a handsome man came, he named ', 'the friend came, he named ']
character2_girl = ['a girl reach out her hand, she named  ', 'the girlfriend willing to risk everything, she named ', 'the girl from the dream appears, she named ']
ending_sad = ['That person let he/she being kidnapped. ', 'They dated, but their parents disagreed. ', 'One of them died in a car crash afterward. ']
ending_happy = ['They fell in love, and married. ', 'They are being friends forever. ', 'They live happily ever after. ']

gender1 = input("Select the gender of your protagonist:1. Boy (type boy) 2. Girl (type girl)")
name1 = input("Type their name: ")
gender2 = input("Select the gender of your second character 1. Boy (type boy) 2. Girl (type girl)")
name2 = input("Type their name: ")
ending = input("Select the ending of your choice: 1. Happy (type happy) 2. Sad (type sad)")
print(" ")

if gender1 == "boy":
  print(random.choice(starter)+random.choice(character1_boy)+name1+". ")
  print(random.choice(background_boy)+random.choice(plot_boy))
  if gender2== "boy":
    print(random.choice(character2_boy)+name2+". ")
    if ending =="happy":
      print(name2+". "+random.choice(ending_happy))
    elif ending =="sad":
      print(name2+". "+random.choice(ending_sad))

  elif gender2== "girl":
    print(random.choice(character2_girl)+name2+". ")
    if ending =="happy":
      print(random.choice(ending_happy))
    elif ending =="sad":
      print(random.choice(ending_sad))
  
elif gender1 == "girl":
  print(random.choice(starter)+random.choice(character1_girl)+name1+". ")
  print(random.choice(background_girl)+random.choice(plot_girl))
  if gender2== "boy":
    print(random.choice(character2_boy)+name2+". ")
    if ending =="happy":
      print(random.choice(ending_happy))
    elif ending =="sad":
      print(random.choice(ending_sad))

  elif gender2== "girl":
    print(random.choice(character2_girl)+name2+". ")
    if ending =="happy":
      print(random.choice(ending_happy))
    elif ending =="sad":
      print(random.choice(ending_sad))
