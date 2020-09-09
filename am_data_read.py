import csv
import matplotlib.pyplot as plt
if __name__ == "__main__":

    acceleration_x = []
    acceleration_y = []
    acceleration_z = []
    gyro_x = []
    gyro_y = []
    gyro_z = []

    with open('test_roller_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row[1] == '4':
                acceleration_x.append(float(row[3]))
                acceleration_y.append(float(row[4]))
                acceleration_z.append(float(row[5]))
                gyro_x.append(float(row[6]))
                gyro_y.append(float(row[7]))
                gyro_z.append(float(row[8]))

    time = []
    count = 0
    for _ in range(len(acceleration_x)):
        time.append(count)
        count += 1


    plt.figure()
    plt.plot(time, acceleration_x, 'b-', linewidth=1)
    plt.title("Biểu đồ thời gian xác lập góc quay của động cơ thời gian lấy mẫu là 2ms")
    plt.xlabel('Time (millis)')
    plt.ylabel('Acceleration (cm/s)')
    plt.legend(['Acceleration', 'Time'], loc=2)
    plt.show()
    plt.pause(10)

