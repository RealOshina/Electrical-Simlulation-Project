class Simulation:
    def __init__(self, values):
        self.values = values
        #self.time = time
        self.step = 0
        self.result = None
    def simulate(self, time):
        self.step += 1
        
        self.result = {
            "step": self.step,
            "time": time,
            "power": self.values["power"],
            "energy": self.values["power"] * time
        }