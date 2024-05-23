import numpy as np

def calculate(x):
    if len(x) == 9:
      #Creating the matrix from the initial list
        matrix = np.matrix([x[:3], x[3:6], x[6:]])
        
      #Calculating the values from the matix axis
        mean_1 = np.mean(matrix, axis = 0).tolist()
        mean_ = np.mean(matrix, axis = 1).tolist() 
        mean_2 = [j for i in mean_ for j in i]
        mean_3 = np.mean(matrix).tolist()
        variance_1 = np.var (matrix, axis = 0).tolist()
        variance_ = np.var (matrix, axis = 1, ).tolist()
        variance_2 = [j for i in variance_ for j in i]
        variance_3 = np.var (matrix).tolist()
        standar_1 = np.std (matrix, axis = 0).tolist()
        standar_ = np.std (matrix, axis = 1).tolist()
        standar_2 = [j for i in standar_ for j in i]
        standar_3 = np.std (matrix).tolist()
        max_1 = np.max (matrix, axis = 0).tolist()
        max_ = np.max (matrix, axis = 1).tolist()
        max_2 = [j for i in max_ for j in i]
        max_3 = np.max (matrix).tolist()
        min_1 = np.min (matrix, axis = 0).tolist()
        min_ = np.min (matrix, axis = 1).tolist()
        min_2 = [j for i in min_ for j in i]
        min_3 = np.min (matrix).tolist()
        sum_1 = np.sum (matrix, axis = 0).tolist()
        sum_ = np.sum (matrix, axis = 1).tolist()
        sum_2 = [j for i in sum_ for j in i]
        sum_3 = np.sum (matrix).tolist()
        
       #Calculating the ditionary from the former results
        Result = {"mean":[mean_1, mean_2, mean_3], "variance":[variance_1, variance_2, variance_3], "standar deviation":[standar_1, standar_2, standar_3], "max": [max_1, max_2, max_3], "min": [min_1, min_2, min_3], "sum":[sum_1, sum_2, sum_3]}
        print(Result)
    else:
        print("List must contain nine numbers.")
