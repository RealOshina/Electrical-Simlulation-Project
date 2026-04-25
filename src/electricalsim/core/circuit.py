from ..components.capacitor import Capacitor
from ..components.current_source import CurrentSource
from ..components.diode import Diode
from ..components.inductor import Inductor
from ..components.resistor import Resistor
from ..components.transistor import Transistor
from ..components.voltage_source import VoltageSource

_VALID_COMPONENT = {
    "capacitor": Capacitor,
    "current_source": CurrentSource,
    "diode": Diode,
    "inductor": Inductor,
    "resistor": Resistor,
    "transistor": Transistor,
    "voltage_source": VoltageSource
}

_COMPONENT = {
    "capacitor": "capacitance",
    "current_source": "current",
    "diode": "forward_voltage",
    "inductor": "inductance",
    "resistor": "resistance",
    "transistor": "hfe",
    "voltage_source": "voltage"
}

class Circuit:
    def __init__(self, data):
        self.data = data
        self.node = data["nodes"]
        self.components = data["components"]
        self.valid_check(self.components)
    def valid_check(self, components):
        self.result = []
        for component in components:
            component_type = component["type"]
            if component_type in _VALID_COMPONENT:
                #print("a", component_type)

                class_ = _VALID_COMPONENT[component_type]
                object = None
                
                a = {}

                for i, x in component.items():
                    if i != "type":
                        if i == "value":
                            i = _COMPONENT[component_type]
                        
                        a[i] = x
                        object = {i: x}
                        
                        #print(object, i, a)
                
                self.result.append(a)
                object = class_(**{i:x})
                #print(self.result)
            else:
                raise ValueError(f"Unknown component type: {component_type}")
    def __str__(self):
        return str(self.result)