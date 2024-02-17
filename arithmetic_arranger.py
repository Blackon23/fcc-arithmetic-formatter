def arithmetic_arranger(problems, solution=False):

  #first requested error message
  if len(problems) > 5:
      return 'Error: Too many problems.'
  
  first_row = ''
  second_row = ''
  solution_row = ''
  dashes = ''
  spaces = 4 * ' '

  #for every calculation
  for problem in problems:
    #seperation of the operands and operator
      parts = problem.split()
      digit1 = parts[0]
      digit2 = parts[2]
      operator = parts[1]

      #requested rules
      if len(digit1) < 5 and len(digit2) < 5:
        if digit1.isdigit() and digit2.isdigit():
            if operator == '+':
                result = str(int(digit1) + int(digit2))
            elif operator == '-':
                result = str(int(digit1) - int(digit2))
            #second requested error message
            else:
                return "Error: Operator must be '+' or '-'."
        else:
          #third requested error message
            return "Error: Numbers must only contain digits."
      else:
        #fourth requested error message
        return 'Error: Numbers cannot be more than four digits.'
      
  
      #max distances for the corresponding spaces
      max_len = max(len(digit1), len(digit2))

      #creation of every row for every ploblem with the addiction of the standar spaces between the different calulations
      first_row += ' ' * (max_len + 2 - len(digit1)) + digit1 + spaces
      second_row += operator + ' ' * (max_len + 2 - len(digit2) - 1) + digit2 + spaces
      dashes += int(max_len + 2) * '-' + spaces
      solution_row += ' ' * (max_len + 2 - len(result)) + result + spaces
    
  #printing the rows
  if solution:
      arranged_problems = first_row.rstrip() + '\n' + second_row.rstrip() + '\n' + dashes.rstrip() + '\n' + solution_row.rstrip()
  else:
      arranged_problems = first_row.rstrip() + '\n' + second_row.rstrip() + '\n' + dashes.rstrip()
  
  return arranged_problems