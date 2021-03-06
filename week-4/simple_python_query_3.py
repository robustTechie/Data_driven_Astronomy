# Write your query function here
import numpy as np

def query(fName1, fName2):
  # load stars with radius > 1
  stars = np.loadtxt(fName1, delimiter=',', usecols=(0,2))
  planets = np.loadtxt(fName2, delimiter=',', usecols=(0,5))
  
  output = []

  for star in stars:
    if star[1] > 1.0:
      
      for planet in planets:
        if planet[0] == star[0]:
          output.append([planet[1]/star[1]])
 
  unsorted = np.array(output)
  sorted_indexes = np.argsort(unsorted[:,0])
  return unsorted[sorted_indexes,:]



# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv', 'planets.csv')
