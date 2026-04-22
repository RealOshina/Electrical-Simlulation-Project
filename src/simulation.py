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

class electrical_power:
    def __init__(self, values):
        pass

class electrical_energy:
    def __init__(self):
        pass

class kirchhoffs_current_law:
    def __init__(self, values):
        self.current_out = values[0]
        self.current_in = values[1:]

        for x in self.current_in:
            self.result = [self.current_out, x]
        
        self.check()
    def calculate_current_out(self):
        for x in self.current_in:
            self.current_out = sum(x)
            self.result = [self.current_out, x]
    def calculate_current_in(self):
        a = []
        b = []

        for i, x in enumerate(self.current_in):
            for z, y in enumerate(x):
                if y is None:
                    a.append((z))
        
        if len(a) < 2:
            self.result = [self.current_out, self.current_out]
        elif len(a) == 2:
            
            self.result = [self.current_out, []]
    def calculate_current_in_out(self):
        print("Calculate Current In and Out")
    def check(self):
        sort = []

        for x in self.current_in:
            if x is not None:
                sort.extend(x)
        current_in_none = any(x is None for x in sort)

        if self.current_out is None and current_in_none:
            self.calculate_current_in_out()
            print("a")
        elif not self.current_out is None and current_in_none:
            self.calculate_current_in()
            print("b")
        elif self.current_out is None and not current_in_none:
            self.calculate_current_out()
            print("c")
        else:
            print("Nothing to Calculate")
    def __str__(self):
        return str(self.result)

"""
a = [9, [None, 3]]

x = kirchhoffs_current_law(a)
print(x.result)
"""
"""
a = [None, 2.5, 4]

z = ohms_law(a)
print(z.result)
"""