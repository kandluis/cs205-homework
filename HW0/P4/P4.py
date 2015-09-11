import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

columns = { 'x_pos': 0,
            'y_pos': 1,
            'z_pos': 2,
            'x_vel': 3,
            'y_vel': 4,
            'z_vel': 5 }


if __name__ == '__main__':
    # Model parameters
    K = 121    # Number of times steps
    dt = 0.01  # Delta t
    c = 0.1    # Coefficient of drag
    g = -9.81  # Gravity
    # For constructing matrix B
    bx = 0
    by = 0
    bz = 0
    bvx = 0.25
    bvy = 0.25
    bvz = 0.1
    # For constructing matrix C
    rx = 1.0
    ry = 5.0
    rz = 5.0

    # Create 3D axes for plotting
    ax = Axes3D(plt.figure())

    #####################
    # Part 1:
    #
    # Load true trajectory and plot it
    # Normally, this data wouldn't be available in the real world
    #####################
    s_true = np.loadtxt("P4_trajectory.txt", delimiter=",")
    x_coords = s_true[:,columns['x_pos']]
    y_coords = s_true[:,columns['y_pos']]
    z_coords = s_true[:,columns['z_pos']]

    ax.plot(x_coords, y_coords, z_coords,
        '--b', label='True trajectory')

    #####################
    # Part 2:
    #
    # Read the observation array and plot it (Part 2)
    #####################
    s_measure = np.loadtxt("P4_measurements.txt", delimiter=",")
    C = np.diag([1.0 / rx, 1.0 / ry, 1.0 / rz])
    coords = np.dot(s_measure,C)
    x_coords = coords[:,columns['x_pos']]
    y_coords = coords[:,columns['y_pos']]
    z_coords = coords[:,columns['z_pos']]
    ax.plot(x_coords, y_coords, z_coords,
        '.g', label='Observed trajectory')

    #####################
    # Part 3:
    # Use the initial conditions and propagation matrix for prediction
    #####################

    # A = ?
    # a = ?
    # s = ?

    # Initial conditions for s0
    # Compute the rest of sk using Eq (1)

    # ax.plot(x_coords, y_coords, z_coords,
    #         '-k', label='Blind trajectory')

    #####################
    # Part 4:
    # Use the Kalman filter for prediction
    #####################

    # B = ?
    # C = ?

    # Initial conditions for s0 and Sigma0
    # Compute the rest of sk using Eqs (2), (3), (4), and (5)

    # ax.plot(x_coords, y_coords, z_coords,
    #         '-r', label='Filtered trajectory')

    # Show the plot
    ax.legend()
    plt.show()
