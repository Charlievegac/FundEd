import json
from json.decoder import JSONDecodeError

# List of payment plans with, dictionary within dictionary

#--------CLASSES---------#
#-----STUDENT CLASS------#
class Student():
  def __init__(self, name, password, net_worth, debt_amount, time_to_payment): 
    self.id = self.find_id() 
    self.name = name
    self.password = password
    self.net_worth = net_worth
    self.debt_amount = debt_amount
    self.time_to_payment = time_to_payment # Measured in month
    # IMPORTANT! Collects the information, to be sotred into a file using jstor
    self.info = {'name': self.name, 'password': self.password,'net_worth': self.net_worth, 'debt_amount': self.debt_amount, 'time_to_payment': self.time_to_payment}

  def store_info(self):
    # This will load the json file where I will be storing the students data
    student_data = {}
    with open("student_data.json", "r") as file:
      student_data = json.load(file)
    # New students data
    # if there is nothing in the file then create a dictionary named student_accounts
    print(student_data)
    if len(student_data) == 0:
      student_accounts = {'student_accounts': {}}
      student_data.update(student_accounts) # Add the data
      student_data['student_accounts'][self.id] = self.info
    elif not self.student_account_exist(): # check to see if the accoun exist in the account
      student_data['student_accounts'][self.id] = self.info  # Add the data
    with open("student_data.json", "w") as file:
       json.dump(student_data, file)
    
  def student_account_exist(self):
    student_data = {}
    with open("student_data.json", "r") as file:
      student_data = json.load(file)
    if self.id in student_data['student_accounts']:
        return True # The account already exist
    else:
      return False # The account does not exist, thus return false

  # when calling update_network_info also call the update_net_worth to determine if + or - amount
  def update_net_worth_info(self, amount): 
    student_data = {}
    with open("student_data.json", "r") as file:
      student_data = json.load(file)
    if f'student_{self.id}' in student_data['student_accounts']:
      student_data['student_accounts'][self.id]['net_worth'] = amount
      
  def find_id(self):
    # read json file find the largest if number and return curr + 1
    student_data = {}
    with open("student_data.json", "r") as file:
        student_data = json.load(file)
    id = len(student_data['student_accounts'])
    return id
    
  # ONLY IMPORTANT ONE
  def update_net_worth(self, amount):
    self.net_worth += amount
    
  def set_name(self, new_name):
    self.name = new_name 

  def print_loan_payment_plans(self):
    pass

  # def read_json(path):
  #   with open(path) as file_in:
  #       return json.load(file_in)