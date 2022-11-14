import unittest
from modules.Car import Car
from modules.Engine import Engine
from modules.Gearbox import GearBox

engine1 = Engine(2)
engine2 = Engine(4)
gearbox1 = GearBox(6)
gearbox2 = GearBox(5)

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Red", "Micra", engine1, gearbox1)
        self.car32 = Car("Blue", "Prelude", engine2, gearbox2)

    def test_car_has_colour(self):
        self.assertEqual("Blue", self.car32.colour)

    def test_car_has_model(self):
        self.assertEqual("Prelude", self.car32.model)

    def test_car_engine_volume(self):
        self.assertEqual(2, self.car.engine.volume)

    def test_how_many_gears(self):
        self.assertEqual(6, self.car.gearbox.num_of_gears)

    def test_colour_can_change(self):
        self.car.colour = "Green"
        self.assertEqual("Green", self.car.colour)

    def test_model_can_change(self):
        self.car.model = "Viper"
        self.assertEqual("Viper", self.car.model)



       
        