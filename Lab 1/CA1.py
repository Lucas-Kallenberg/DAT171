# Computer assignment 1
# Av Lucas Kallenberg

import numpy as np
import matplotlib.pyplot as plt



def read_coordinate_file(filename):  # Create a function that reads the txtfile and rename it as file
    with open(filename, 'r') as file:
        lst =[]  # Create an empty list to store my arrays
        r =1
        line = file.readline()  # Read the first line before we remove all unwanted characters with the while loop
        while line:
            line = line.replace('{','')
            line = line.replace('}','')
            line = line.strip()
            line = line.split(',')  # Split the arrays in the , mark
            # Create a numpy array and then calculate x,y and convert them into floats
            # r * np.log(np.tan(np.pi / 4 + np.pi * float(line[0]) / 360))
            line = np.array([r*np.pi*float(line[1])/180,r*np.log(np.tan(np.pi/4+np.pi*float(line[0])/360))])
            lst.append(line)  # Save x,y into a list
            line = file.readline()
    arr = np.array(lst)  # Converts the list into a numpy array
    return arr

def plot_points(coord_list):
    coord = coord_list
    plt.scatter(coord[:,0],coord[:,1], s = 3, c= 'r')  # Plot the coords as points
    plt.show()

def construct_graph_connections(coord_list, radius):
    lst = []
    pun = []
    for n, a in enumerate(coord_list):  # We create a number infront of the arrays and then we loop over the arrays
        for i in range(n+1, len(coord_list)):  # Now we take the second array of the coord_list
            dist = np.linalg.norm(a - coord_list[i])  # Calculates the distance using pythagoras of the coords
            dist = np.array(dist)
            if dist >= radius:  # Checking if the coords distance is inside of the radius that is set
                lst.append(dist)
                pun.append([a,coord_list[i]])


    lst = np.array(lst) # Converting into numpy arrays
    pun = np.array(pun)
    return lst , pun





if __name__=='__main__':
    arr = read_coordinate_file('SampleCoordinates.txt')
    radius = 0.08
    # plot_points(arr)
    construct_graph_connections(arr,radius)

