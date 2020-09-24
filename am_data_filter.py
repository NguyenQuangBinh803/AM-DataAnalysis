import csv
import matplotlib.pyplot as plt
from Complementary_Filter import ComplementaryFilter

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

    filter = ComplementaryFilter(acceleration_x)
    filter.set_alpha(0.99)
    filter.low_pass_filter_data()

    data = []
    gyro_data = []

    for i in range(len(acceleration_x)):
        data.append([acceleration_x[i], acceleration_y[i], acceleration_z[i]])
        gyro_data.append([gyro_x[i],gyro_y[i], gyro_z[i]])

    plt.figure(1)
    plt.plot(time, filter.refined_sequence, 'b-', linewidth=1)
    plt.xlabel('Time (millis)')
    plt.ylabel('Acceleration (m/ss)')

    plt.figure(2)
    plt.plot(time, acceleration_x, 'b-', linewidth=1)
    plt.xlabel('Time (millis)')
    plt.ylabel('Gyro (rad/ss)')
    plt.show()
    plt.pause(10)

