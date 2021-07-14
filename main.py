import random
import math


def random_num():
    """
    random_num generates a random number between 0 and 1.

    :return: A float in [0; 1]
    """
    return random.uniform(0.0, 1.0)


def approximate(num_points):
    """
    approximate will approximate the value of pi using a user-specified number of points on a unit square.

    :param num_points: Number of points to use.

    :return: The approximated value of pi.
    """
    # Step 1. Generate the desired amount of points.
    points = []

    for _ in range(num_points):
        points.append((random_num(), random_num()))
    
    # Step 2. Count the amount of points that is inside of the unit circle.
    points_inside = 0

    for point in points:
        # Pythagorean theorem
        if (math.sqrt(point[0]**2 + point[1]**2) <= 1.0):
            points_inside += 1

    # Step 3. Return the approximation of pi. We know that points_inside / points -> pi / 4 for infinitely many points, so return the fraction times 4.
    return (points_inside / len(points)) * 4 

def main():
    
    # Go into a loop waiting for user input specifying how many points should be used.
    while True:
        points = int(input("[*] Please enter the desired amount of points to use for the simulation: "))

        if (points < 1):
            print("[!] A positive number of points should be specified.")
            continue
        
        pi_approx = approximate(points)
        print("[+] The simulated value of pi: {}".format(pi_approx))

    

if __name__ == "__main__":
    main()