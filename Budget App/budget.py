class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def __str__(self):
    symbols = 30 - len(self.category)
    final_text = ''
    for item in self.ledger:
      # Here we give the format for the description and the  amount 
      line = '{desc:<23}{amount:>7}\n'
      # Here whe assign the values to the format 
      final_text += line.format(desc= item["description"][0:23], amount = "{:.2f}".format(item["amount"]))
      # We know that the the string printed will be 30 characters long. 
    return f'''{"*" * int(symbols /2) + self.category + "*" * (symbols - int(symbols /2))}
{final_text}Total: {self.get_balance()}'''

  def check_funds(self, amount):
    if self.get_balance() < amount:
      return False
    else:
      return True

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item['amount']
    return balance

  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({"amount": amount * -1, "description": description})
      return True
    else:
      return False

  def transfer(self, amount, other_category):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {other_category.category}')
      other_category.deposit(amount, f'Transfer from {self.category}')
      return True
    else:
      return False

def create_spend_chart(categories):
  # To make the chart first we need to calculate the percentage of each category
  withdrawals_list = list()
  for cat in categories:
    withdrawals = 0
    for item in cat.ledger:
      if item["amount"] < 0:
        withdrawals += item["amount"]
    withdrawals_list.append(withdrawals)
  total = sum(withdrawals_list)
  percentages = list()
  for item in withdrawals_list:
    percentage = int((item / total) * 10)
    percentages.append(percentage)

  # Then we make a list tha will contain the 'o' of the chart. For example, line_text[1] contains 'o' at 10% level
  line_text = ['','' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'']
  for i in range(11):
    for per in percentages:
      if per >= i:
        line_text[i] += 'o  '
      else:
        line_text[i] += '   '

  # Now we need to get a list that will contain lists with the characters of each  category name
  name_lines = list()
  all_letters = list()
  largest = 0
  for cat in categories:
    cat_letters = [*cat.category]
    all_letters.append(cat_letters)
    if largest < len(cat.category):
      largest = len(cat.category)

  # Here we make a string called names that will contain the names of each category in the vertical format thet is needed 
  names = ''
  for j in range(largest):
    for i in range(len(all_letters)):
      try:
        names += '  ' + all_letters[i][j]
      except:
        names += '   '
      if i == len(all_letters) - 1 and j != largest - 1:
        names += '  \n   '
      elif i == len(all_letters) - 1 and j == largest - 1:
        names += '  '

  return f'''Percentage spent by category
100| {line_text[10]}
 90| {line_text[9]}
 80| {line_text[8]}
 70| {line_text[7]}
 60| {line_text[6]}
 50| {line_text[5]}
 40| {line_text[4]}
 30| {line_text[3]}
 20| {line_text[2]}
 10| {line_text[1]}
  0| {line_text[0]}
    {'-' * (len(line_text[0]) + 1)}
   {names}'''
