class ohms_law:
    def __init__(self, voltage, current, resistance):
        self.voltage = voltage
        self.current = current
        self.resistance = resistance
    def calculate_voltage(self):
        # V = I x R
        self.voltage = self.current * self.resistance
        print(self.voltage)
    def calculate_current(self):
        # I = V / R
        self.current = self.voltage / self.resistance
        print(self.current)
    def calculate_resistance(self):
        # R = V / I
        self.resistance = self.voltage / self.current
        print(self.resistance)

class electrical_energy:
    def __init__(self, energy, power, time, voltage, current, capacitance, resistance, charge):
        self.energy = energy
        self.power = power
        self.time = time
        self.voltage = voltage
        self.current = current
        self.capacitance = capacitance
        self.resistance = resistance
        self.charge = charge
    #def calculate_

x = ohms_law(None, 2.5, 2)
x.calculate_voltage()

y = ohms_law(5, None, 2)
y.calculate_current()

z = ohms_law(5, 2.5, None)
z.calculate_resistance()