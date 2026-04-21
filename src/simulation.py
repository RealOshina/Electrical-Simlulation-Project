class ohms_law:
    def __init__(self, values):
        self.voltage, self.current, self.resistance = values
        self.calculate()
    def calculate_voltage(self):
        return self.current * self.resistance
    def calculate_current(self):
        return self.voltage / self.resistance
    def calculate_resistance(self):
        return self.voltage / self.current
    def calculate(self):
        if self.voltage is None and self.current is not None and self.resistance is not None: 
            self.voltage = self.calculate_voltage()
        elif self.current is None and self.voltage is not None and self.resistance is not None: 
            self.current = self.calculate_current()
        elif self.resistance is None and self.voltage is not None and self.current is not None: 
            self.resistance = self.calculate_resistance()

        self.result = [self.voltage, self.current, self.resistance]
    def __str__(self):
        return str(self.result)

class kirchhoffs_current_law:
    def __init__(self, values):
        self.current_out = values[0]
        self.current_in = values[1:]
        
        self.check()
    def calculate_current_out(self):
        print("Calculate Current Out")
    def calculate_current_in(self):
        print("Calculate Current In")
    def calculate_current_in_out(self):
        print("Calculate Current In and Out")
    def check(self):
        sort = []

        for x in self.current_in:
            print(x)
            if x is not None:
                sort.extend(x)

        current_in_none = any(x is None for x in sort)

        if self.current_out is None and current_in_none:
            self.calculate_current_in_out()
        elif not self.current_out is None and current_in_none:
            self.calculate_current_in()
        elif self.current_out is None and not current_in_none:
            self.calculate_current_out()
    def calculate(self):
        pass

a = [None, [2, 2]]

x = kirchhoffs_current_law(a)

"""
a = [None, 2.5, 4]

z = ohms_law(a)
print(z.result)
"""