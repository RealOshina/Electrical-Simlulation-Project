from .loader import Loader
from ..components import capacitor
from ..components import current_source
from ..components import diode
from ..components import inductor
from ..components import resistor
from ..components import transistor
from ..components import voltage_source

_VALID_COMPONENT = {
    "capacitor": capacitor,
    "current_source": current_source,
    "diode": diode,
    "inductor": inductor,
    "resistor": resistor,
    "transistor": transistor,
    "voltage_source": voltage_source
}

class Circuit:
    def __init__(self, data):
        self.data = data
        self.node = data["nodes"]
        self.components = data["components"]
        self.valid_check()
    def valid_check(self):
        """
        for component in self.components:
            for key in _VALID_COMPONENT:
                if component["type"] == key:
                    print("a")
                else:
                    print("b")
            print(component, key)
        """
        for component in self.components:
            for key in _VALID_COMPONENT:
                print(key)
            if component["type"] == _VALID_COMPONENT:
                print("a")
            else:
                print("b")
            print(component, component["type"])