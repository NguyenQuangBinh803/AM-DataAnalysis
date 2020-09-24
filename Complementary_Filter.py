import numpy as np

class ComplementaryFilter:

    def __init__(self, sequence_of_data):
        self.sequence = sequence_of_data
        self.refined_sequence = []

        for _ in range(len(sequence_of_data)):
            self.refined_sequence.append(0.0)

        self.alpha = 0.1
        self.previous_data = 0
        self.current_data = 0
        self.current_raw_data = 0
        self.previous_raw_data = 0

    def set_alpha(self, alpha):
        self.alpha = alpha

    def low_pass_filter_data(self):

        for i in range(len(self.sequence)):
            self.current_raw_data = self.sequence[i]
            if i == 0:
                self.previous_data = 0
            else:
                self.previous_data = self.refined_sequence[i - 1]
            self.refined_sequence[i] = (1 - self.alpha) * self.current_raw_data + self.alpha * self.previous_data

    def high_pass_filter_data(self):
        self.previous_data = 0
        for i in range(len(self.sequence)):
            self.current_raw_data = self.sequence[i]
            if i == 0:
                self.previous_data = 0
            else:
                self.previous_data = self.refined_sequence[i - 1]

            self.refined_sequence[i] = (1 - self.alpha) * self.previous_data + (1 - self.alpha) * (self.current_raw_data - self.previous_raw_data)
            self.previous_raw_data = self.current_raw_data

