

# Author: Xinzhang Xiong xpx5059@psu.edu
# Collaborator:Alexander Barr ajb7463@psu.edu
# Collaborator:Jeremy Hoheneder jjh549@psu.edu
# Collaborator:Luke Heckman luke@psu.edu
# Section: 1
# Breakout: 15

def sum_n(n):
  n = int(n)
  
  if(n==1):
    return(1)
  elif(n==0):
    return(0)
  elif(n>1):
   return(n+sum_n(n-1))
  else:
   return(1)

def print_n(s,n):
  n = int(n)
  if(n>=1):
    n = n-1
    return(f"{s}{print_n(s,n)}")
  else:
    return("")

def run():
  n = input("Enter an int: ")
  print(f"sum is {sum_n(n)}.")
  s = input("Enter a string: ")
  print(f"{print_n(s,n)}")

if __name__ == "__main__":
  run()