# Made using the following video: https://youtu.be/hqSnruUe3tA
# I did not derive or implement any of the original code above


import numpy as np
import matplotlib.pyplot as plt



def quadratic_variation(B):
    return np.cumsum(np.power(np.diff(B, axis=0, prepend=0.), 2), axis=0)
    

def main():

    n = int(input("[Suggested: 10,000] Enter integer number of timesteps: "))
    d = int(input("[Suggested: 10-100] Enter integer number of simulations: "))
    T = 1.

    times = np.linspace(0., T, n)
    
    dt = times[1] - times[0]
    dB = np.sqrt(dt) * np.random.normal(size=(n-1, d))

    B0 = np.zeros(shape=(1, d))
    B = np.concatenate((B0, np.cumsum(dB, axis=0)) , axis=0)

    plt.plot(times, B)
    plt.plot(times, quadratic_variation(B))
    plt.show()



    
if __name__ == '__main__':
    main()
