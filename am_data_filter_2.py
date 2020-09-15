import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

if __name__ == "__main__":

    acceleration_x = []
    acceleration_y = []
    acceleration_z = []
    gyro_x = []
    gyro_y = []
    gyro_z = []

    with open('20200907_101415_705000/Roller_Data.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:

            line_count += 1
            if line_count > 2:
                acceleration_x.append(float(row[3]))
                acceleration_y.append(float(row[4]))
                acceleration_z.append(float(row[5]))
                gyro_x.append(float(row[6]))
                gyro_y.append(float(row[7]))
                gyro_z.append(float(row[8]))


    time = []
    count = 0

    print(len(acceleration_x))
    for _ in range(len(acceleration_x)):
        time.append(count)
        count += 1

    x = acceleration_x
    y3 = gaussian_filter1d(x, 1.5)
    y6 = gaussian_filter1d(x, 2.5)
    plt.figure(1)
    plt.plot(x, 'k', label='original data')
    plt.plot(y3, '--', label='filtered, sigma=1.5')
    plt.plot(y6, ':', label='filtered, sigma=2')
    plt.figure(2)

    plt.plot(y6)
    plt.figure(3)
    plt.plot(y3)
    plt.show()
    plt.show()

    # plt.figure(1)
    # plt.plot(time, data, 'b-', linewidth=1)
    # plt.xlabel('Time (millis)')
    # plt.ylabel('Acceleration (m/ss)')
    #
    # plt.figure(2)
    # plt.plot(time, gyro_data, 'b-', linewidth=1)
    # plt.xlabel('Time (millis)')
    # plt.ylabel('Gyro (rad/ss)')
    # plt.show()
    # plt.pause(10)

