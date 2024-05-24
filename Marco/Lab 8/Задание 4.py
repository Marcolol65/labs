class Train:
    def __init__(self, station, station2, time1, time2):
        self.station = station
        self.station2 = station2
        self.time1 = time1
        self.time2 = time2

    def __add__(self, other):
        if self.station2 == other.station and float(self.time2) < float(other.time1):
            new = Train(self.station, other.station2, self.time1, other.time2)
            return new
        else:
            print("Нелётная погодА")
            return None


t1 = Train("Волгоград", "Москва", "15.00", "9.00")
t2 = Train("Москва", "Сочи ", "10.00", "8.00")

new = t1 + t2

if new:
    print(
        f"Поезд из {new.station} в {new.station2} отправляется в {new.time1} и прибывает в {new.time2}")
