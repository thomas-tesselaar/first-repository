#This will implement a function which checks if a password is valid or not
#In order to be valid, one of two criteria must be met
'''
 - Compsed of 5 or more non-repeating words
 - Each word must be seperated by a space
 - Words must be at least three letters
 - Includes only alphabetical characters
'''
#OR
'''
 - At least 12 characters long
 - Contains at least one uppercase and one lowercase letter
 - Contains at least one number
 - Contains at least one fo the following symbols: ~!@#$%^&*()_+=
 - No character may be used more than three times in a row
 '''

def check_typeI_password(string pword):
  



def check_typeII_password(string pword):
  #Check that it contains at least 12 characters
  if(len(pword)<12):
    return False
  
  #Check for an uppercase letter
  if(pword.lower()==pword):
    return False
  #Check for a lowercase letter
  elif(pword.upper()==pword):
    return False

  #Check for at least one number
  if

def check_password(string password):
  
  if(check_typeI_password(password)):
    return True
  
  elif(check_typeII_password(password)):
    return True
  
  else:
    return False


