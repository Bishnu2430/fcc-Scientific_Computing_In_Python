import copy
import random
# Consider using the modules imported above.

class Hat:
  # We will get a dictionary with all the k,v pairs passed as arguments
  def __init__(self, **kwargs ):
    self.contents = list()
    for k,v in kwargs.items() :
      for i in range(v):
        self.contents.append(k)

  def draw(self, amount_to_draw):
    return_list = list()
    if amount_to_draw <= len(self.contents):
      for j in range(amount_to_draw):
        item = random.choice(self.contents)
        return_list.append(item)
        self.contents.remove(item)
    else:
      return_list.extend(self.contents)
      self.contents.clear()
      return return_list
    return return_list
        
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  # In M we save the experiments that returned the desired result
  M = 0
  # For loop for each experiment
  for exp in range(num_experiments):
    # We need to create a copy of hat, otherwise, after each experiment the original hat will be modified
    new_hat = copy.deepcopy(hat)
    # Same as before for expected_ball
    new_expected_balls = copy.deepcopy(expected_balls)
    drew = new_hat.draw(num_balls_drawn)
    # In the copy of expected balls we subtract 1 to the values of the balls that were drawn
    for element in drew:
      if element in new_expected_balls:
        new_expected_balls[element] -= 1
    if all( x <= 0 for x in new_expected_balls.values() ):
      M += 1
  return M / num_experiments
  

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=1000)
print(probability)
