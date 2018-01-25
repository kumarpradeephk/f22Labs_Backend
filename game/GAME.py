import random
from random import randint
import string
#RANDOM STRING GENERATOR 
def generate_random_str(randomNum):
  randomString=''.join([random.choice(string.ascii_uppercase) for _ in range(randomNum)])
  return randomString

#PROCESS_BOTH_STRING
def process_both_string(randomString,userStr,randomNum):
  exact_matchNo=0
  for i in range(randomNum):
    if randomString[i]==userStr[i]:
      exact_matchNo=exact_matchNo+1
      
  randomString_hash={}
  userStr_hash={}
  for i in range(randomNum):
    counts=0
    counts=randomString.count(randomString[i])
    randomString_hash[randomString[i]]=counts
    counts=0
    counts=userStr.count(userStr[i])
    userStr_hash[userStr[i]]=counts
  
  match_val=0
  for k in userStr_hash.keys():
    if k in randomString_hash.keys():
      if randomString_hash[k]>=userStr_hash[k]:
        match_val=match_val+userStr_hash[k]
      else:
        match_val=match_val+randomString_hash[k]
  
  char_match=match_val-exact_matchNo
  print("Number of charcter matches with EXACT_POSITION:= " + str(exact_matchNo))
  print("Number of charcter matches with WRONG_POSITION:= " + str(char_match))

#DRIVER_PROGRAMME  
rNum=randint(2,10);
#USER GUESSING STATS
randString=generate_random_str(rNum)
usrStr=input("enter string of length "+ str(rNum)+ ":-")
print(".......PLAYER GUESSING STATS........")
process_both_string(randString,usrStr,rNum)
print("SYSTEM GENERETED:- " + randString)
print("USER ENTERED STRING:- " + usrStr)

print("---------------------------------------------------")
#SYSTEM GUESSING STATS
Sys_randString=generate_random_str(rNum)
Sys_user_String=generate_random_str(rNum)
print(".......SYSTEM GUESSING STATS........")
process_both_string(Sys_randString,Sys_user_String,rNum)
print("SYSTEM GENERETED ACTUAL:- " + Sys_randString)
print("SYSTEM GENERETED GUESSED:- " + Sys_user_String)
