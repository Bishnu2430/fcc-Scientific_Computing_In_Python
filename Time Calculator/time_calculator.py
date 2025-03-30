def add_time(start, duration, starting_day = ''):

  start_parts = start.split()
  duration_parts = duration.split(':')
  start_parts_num = start_parts[0].split(':')

  hours = int(start_parts_num[0]) + int(duration_parts[0])
  minutes = int(start_parts_num[1]) + int(duration_parts[1])
  days_after_starting = 0
  time = start_parts[1]

  # Calculate hour and minutes
  if minutes >= 60:
    minutes -= 60
    hours += 1 

  while hours >= 12:
    if time == 'AM':
      if hours >12:
        hours -= 12
        time = 'PM'
      else:
        time = 'PM'
        break
    elif time == 'PM':
      if hours >12:
        days_after_starting += 1
        hours -= 12
        time = 'AM'
      else:
        days_after_starting += 1
        time = 'AM'
        break
  
  #First check that the day is a string
  days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
  final_day = ''
  if starting_day != '' and starting_day.lower() in days:
    starting_day = starting_day.lower()
    index = (days.index(starting_day) + days_after_starting) % 7
    final_day = f', {days[index].capitalize()}'
  
   
  # Change int to str 
  minutes_str = str(minutes)
  if len(minutes_str) == 1:
    minutes_str = '0' + str(minutes)
  hours_str = str(hours)


  # Part to create the string to return
  if days_after_starting < 1:
    new_time = hours_str + ':' + minutes_str  + f' {time}' + final_day 
  elif  days_after_starting == 1:
    new_time = hours_str + ':' + minutes_str  + f' {time}' + final_day + ' (next day)'
  else:
    new_time = hours_str + ':' + minutes_str  + f' {time}' + final_day + f" ({days_after_starting} days later)"
    
  return new_time

print(add_time("11:55 AM", "1:00",'Monday'),)