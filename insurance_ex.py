# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name + " is "+ str(estimated_cost) + " dollars.")
  return estimated_cost

def difference_insurance_cost(person1, person2):
  difference_cost = person1 - person2
  print("The difference in insurance cost is " + str(difference_cost) + " dollars.")

# Estimate Maria's insurance cost

maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0, "Maria") 

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(35, 1, 22.2, 0, 1, "Omar")

# Estimate Carlos's insurance cost
carlos_insurance_cost = calculate_insurance_cost(26, 1, 23.4, 0, 0, "Carlos")

# Function to calculate the difference in insurance cost between two persons
difference_insurance_cost(maria_insurance_cost, carlos_insurance_cost)
