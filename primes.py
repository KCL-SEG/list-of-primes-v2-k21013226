"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

#number of primes - how many primes to print out
#if 0 or negative then raise Value error 



def is_prime(n):
   if n <= 1:
      return False
   else:
      for i in range(2, n):       
         if n % i == 0:          
            return False
   return True


def primes(number_of_primes):
    list = []

    complete = False
    current_num = 2

    if number_of_primes <= 0:
        raise ValueError("number of primes must be bigger than 0")
    else:
        while complete == False:

            if len(list)== number_of_primes:
                complete = True
            else:
                if is_prime(current_num)==True:
                    list.append(current_num)
                current_num = current_num + 1
           
                
        
    return list


