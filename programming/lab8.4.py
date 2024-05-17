class Train:
    def __init__(self, departure_point, destination, departure_time, arrival_time):
        self.departure_point = departure_point
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def __add__(self, other):
        if self.destination == other.departure_point and self.arrival_time < other.departure_time:
            return Train(self.departure_point, other.destination, self.departure_time, other.arrival_time)
        else:
            raise ValueError("Trains cannot be added due to mismatched destinations or arrival and departure times.")

# Пример использования:
train1 = Train("City A", "City B", "09:00", "12:00")
train2 = Train("City B", "City C", "13:00", "16:00")

try:
    combined_train = train1 + train2
    print("Combined Train: From", combined_train.departure_point, "to", combined_train.destination,
          "Departure:", combined_train.departure_time, "Arrival:", combined_train.arrival_time)
except ValueError as e:
    print(e)