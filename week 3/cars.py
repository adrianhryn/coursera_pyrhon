import os
import csv


class CarBase:

    def __init__(self, car_type, brand, photo_file_name, carrying=None):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(CarBase):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = passenger_seats_count

    def __str__(self):
        return "car_type - {}, brand - {}, photo_file_name - {}, carrying - {}, passenger_seats_count -{}".format(
            self.car_type, self.brand, self.photo_file_name, self.carrying, self.passenger_seats_count
        )


class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, size):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        self.size = size.split("x")

        if len(size) == 0:
            self.body_length, self.body_width, self.body_height = 0, 0, 0
        else:
            size = size.split("x")
            self.body_length = float(size[0])
            self.body_width = float(size[1])
            self.body_height = float(size[2])

    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height

    def __str__(self):
        return "car_type - {}, brand - {}, photo_file_name - {}, carrying - {}, body_length -{}, body_width - {}, " \
               "body_height - {}".format(self.car_type, self.brand, self.photo_file_name, self.carrying,
                                         self.body_length, self.body_width, self.body_height)


class SpecMachine(CarBase):

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra

    def __str__(self):
        return "car_type - {}, brand - {}, photo_file_name - {}, carrying - {}, extra -{}".format(
            self.car_type, self.brand, self.photo_file_name, self.carrying, self.extra
        )


def get_car_list(csv_filename):
    with open(csv_filename, "r") as csv_to_read:
        car_list = []
        data = list(csv.reader(csv_to_read, delimiter=';'))
        colnames = data[0]
        print("colnames ", colnames)
        data = data[1:]
        print("Data", data)
        for i in data:
            if len(i) == 0:
                continue
            if i[0] == "car":
                car = Car(brand=i[colnames.index('brand')], photo_file_name=i[colnames.index('brand')],
                          carrying=i[colnames.index("carrying")], passenger_seats_count=i[colnames.index('passenger_seats_count')])

            elif i[0] == "truck":
                car = Truck(brand=i[colnames.index('brand')], photo_file_name=i[colnames.index('brand')],
                          carrying=i[colnames.index("carrying")], size=i[colnames.index("body_whl")])

            elif i[0] == "spec_machine":
                car = SpecMachine(brand=i[colnames.index('brand')], photo_file_name=i[colnames.index('brand')],
                          carrying=i[colnames.index("carrying")], extra=i[colnames.index('extra')])

            car_list.append(car)

        return car_list


cars = get_car_list("cars_data.csv")

for i in cars:
    print(i)