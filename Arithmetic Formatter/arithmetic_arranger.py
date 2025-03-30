# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
import re

def arithmetic_arranger(problems, show=False):

  # Check if parts has more than 5 problems
  if len(problems) > 5:
    print("Error: Too many problems.")
    return "Error: Too many problems."

  all_num1 = list()
  all_num2 = list()
  all_lines = list()
  all_signs = list()
  results = list()
  parts = list()
  for i in range(len(problems)):
    parts.append(problems[i].split())
    all_num1.append(parts[i][0])
    all_num2.append(parts[i][2])
    all_signs.append(parts[i][1])
    # Check if other than + or - was used
    if not re.search('\+|\-', parts[i][1]):

      print("Error: Operator must be '+' or '-'.")
      return "Error: Operator must be '+' or '-'."

    #Numbers must only contain digits.
    if len(parts[i][0]) > 4 or len(parts[i][2]) > 4:
      print("Error: Numbers cannot be more than four digits.")
      return "Error: Numbers cannot be more than four digits."

    #Numbers must only contain digits
    try:
      num1 = int(parts[i][0])
      num2 = int(parts[i][2])
    except:
      print("Error: Numbers must only contain digits.")
      return "Error: Numbers must only contain digits."

    #Section to calculate the results
    if all_signs[i] == '+':
      result = num1 + num2
    else:
      result = num1 - num2
    results.append(str(result))

    # Get the number of lines at the bottom of the result
    num_of_lines = max(len(all_num1[i]), len(all_num2[i])) + 2

    lines = ''
    for i in range(num_of_lines):
      lines += '-'
    all_lines.append(lines)

  #Part to give back the string with the correct format
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  
  for j in range(len(results)):
    num_sp = len(all_lines[j]) - 1 - len(all_num2[j])
    sp_total = ' ' * num_sp
    print(sp_total)
    if j < len(results) - 1:
      line1 += f"{' ' * (len(all_lines[j]) - len(all_num1[j])) + all_num1[j] + '    ' }"
      line2 += f"{all_signs[j] + sp_total + all_num2[j] + '    ' }"
      line3 += f"{all_lines[j] + '    ' }"
      line4 += f"{' ' * (len(all_lines[j]) - len(results[j])) + results[j] + '    ' }"
    else:
      line1 += f"{' ' * (len(all_lines[j]) - len(all_num1[j])) + all_num1[j] }"
      line2 += f"{all_signs[j] + sp_total + all_num2[j]}"
      line3 += f"{all_lines[j] }"
      line4 += f"{' ' * (len(all_lines[j]) - len(results[j])) + results[j] }" 
      
  if show:
    arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
  else:
    arranged_problems = line1 + '\n' + line2 + '\n' + line3 
    
  return arranged_problems


print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
