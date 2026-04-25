class Solver:
    def __init__(self, circuit):
        self.nodes = circuit.nodes
        self.components = circuit.result
        
        self.ground_node = {}
        self.known_voltage = {}
        self.unknown_voltage = {}

        self.identify_node(self.components, self.nodes)
        self.calculate_unknowVoltage(self.components)
        current = self.ohms_law(self.components)
        self.power_calculation(self.components, current)
    def identify_node(self, components, nodes):
        for component in components:
            if "voltage" in component:
                if component["n1"] in nodes and component["n2"] in nodes:
                    if component["n1"] < component["n2"]:
                        self.ground_node[component["n1"]] = 0
                        self.known_voltage[component["n2"]] = component["voltage"]
                    else:
                        self.known_voltage[component["n1"]] = component["voltage"]
                        self.ground_node[component["n2"]] = 0
            else:
                for n in [component["n1"], component["n2"]]:
                    if n not in self.ground_node and n not in self.known_voltage:
                        self.unknown_voltage[n] = None
        #print(self.ground_node)
        #print(self.known_voltage)
        #print(self.unknown_voltage)
    def calculate_unknowVoltage(self, components):
        neighbor_voltage = {}

        for node in self.unknown_voltage:
            sum_conductance = 0
            sum_current = 0
            for component in components:
                if component["n1"] == node or component["n2"] == node:
                    #print("a", component, node)
                    if component["n1"] == node:
                        neighbor_node = component["n2"]
                    else:
                        neighbor_node = component["n1"]

                    if neighbor_node == component["n1"] or neighbor_node == component["n2"]:
                        if neighbor_node in self.ground_node:
                            neighbor_voltage[neighbor_node] = 0
                        elif neighbor_node in self.known_voltage:
                            neighbor_voltage[neighbor_node] = self.known_voltage[neighbor_node]
                    if "resistance" in component:
                        sum_conductance += 1 / component["resistance"]
                        sum_current += neighbor_voltage[neighbor_node] / component["resistance"]
                        #print(sum_conductance, sum_current)

            a = sum_current / sum_conductance
            self.unknown_voltage[node] = a
            #print(a)
            #print(self.unknown_voltage)
    def ohms_law(self, components):
        all_voltage = {}

        all_voltage.update(self.ground_node)
        all_voltage.update(self.known_voltage)
        all_voltage.update(self.unknown_voltage)

        currents = []

        for component in components:
            if "resistance" in component:
                current = (all_voltage[component["n1"]] - all_voltage[component["n2"]]) / component["resistance"]
                currents.append(current)
                #print(current)

        return currents
        #print(all_voltage)
    def power_calculation(self, components, currents):
        power = 0
        current_index = 0
        if currents is not None:
            for component in components:
                if "resistance" in component:
                    i = currents[current_index]
                    power += (i ** 2) * component["resistance"]
                    current_index += 1
                   
            print(power)
            print(current_index)
            print(currents)
        else:
            raise ValueError("Current can't be None")