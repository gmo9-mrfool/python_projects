print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#count_l,count_o,count_v,count_e=0,0,0,0
new_name_1=name1.lower()
new_name_2=name2.lower()
count_l=new_name_1.count('l') + new_name_2.count('l')
count_o=new_name_1.count('o') + new_name_2.count('o')
count_v=new_name_1.count('v') + new_name_2.count('v')
count_e=new_name_1.count('e') + new_name_2.count('e')
total_love=count_l+count_o+count_v+count_e
#count_t,count_r,count_u,count_e2=0,0,0,0
count_t=new_name_1.count('t')+new_name_2.count('t')
count_r=new_name_1.count('r')+new_name_2.count('r')
count_u=new_name_1.count('u')+new_name_2.count('u')
count_e2=new_name_1.count('e')+new_name_2.count('e')
total_true=count_t+count_r+count_u+count_e2

love_score=int(str(total_true)+str(total_love))
if love_score<10 or love_score>90:
  print(f'Your score is **{love_score}**, you go together like coke and mentos.')
elif love_score>40 and love_score<50:
  print(f'Your score is {love_score}, you are alright together.')
else:
  print(f'Your score is {love_score}.')