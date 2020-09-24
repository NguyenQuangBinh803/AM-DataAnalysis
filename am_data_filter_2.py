import csv

import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

if __name__ == "__main__":

    acceleration_x = []
    acceleration_y = []
    acceleration_z = []
    gyro_x = []
    gyro_y = []
    gyro_z = []

    with open('20200911_104456_202000/Roller_Data.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:

            line_count += 1
            if line_count > 2 and line_count < 500:
                acceleration_x.append(float(row[3]))
                acceleration_y.append(float(row[4]))
                acceleration_z.append(float(row[5]))
                gyro_x.append(float(row[6]))
                gyro_y.append(float(row[7]))
                gyro_z.append(float(row[8]))

    time = []
    count = 0

    print(len(acceleration_z))
    for _ in range(len(acceleration_z)):
        time.append(count)
        count += 1

    x = acceleration_z
    y3 = gaussian_filter1d(x, 1.5)
    y6 = gaussian_filter1d(x, 2.5)

    delta_t = 0.02
    sum_distance = 0
    distance = []
    for acc in acceleration_z:
        sum_distance += 1 / 2 * acc * delta_t ** 2
        distance.append(sum_distance*10)
    print(sum_distance)

    plt.figure(1)
    plt.plot(x, 'k', label='original data')
    plt.plot(y3, '--', label='filtered, sigma=1.5')
    plt.plot(y6, ':', label='filtered, sigma=2')
    plt.figure(2)

    plt.plot(distance)
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

