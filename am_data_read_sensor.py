__author__ = "Edward J. C. Ashenbert"
__version__ = "1.0.1"
__status__ = "20200827_1625"

import csv
import matplotlib.pyplot as plt
import cv2
import numpy as np

if __name__ == "__main__":

    acceleration_x = []
    acceleration_y = []
    acceleration_z = []
    gyro_x = []
    gyro_y = []
    gyro_z = []
    time = []

    with open('test_sensor_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for index, row in enumerate(csv_reader):
            if index != 0:
                time.append(float(row[0]))
                acceleration_x.append(float(row[1]))
                acceleration_y.append(float(row[2]))
                acceleration_z.append(float(row[3]))
                gyro_x.append(float(row[4]))
                gyro_y.append(float(row[5]))
                gyro_z.append(float(row[6]))

    sample_data = 10000
    count = 0
    image = np.zeros((500, 500))

    while True:
        cv2.imshow("image", image)
        print(count)
        time_min = sample_data * count
        time_max = sample_data * (count + 1)
        count += 1
        plt.figure()
        plt.plot(time[time_min:time_max], acceleration_x[time_min:time_max], 'b-', linewidth=1)
        plt.title("Something")
        plt.xlabel('Time (millis)')
        plt.ylabel('Acceleration (cm/s)')
        plt.legend(['Acceleration', 'Time'], loc=2)
        plt.show()
        cv2.waitKey()
