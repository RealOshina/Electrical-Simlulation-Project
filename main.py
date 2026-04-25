from electricalsim import Loader, Circuit, Solver
from electricalsim import VoltageSource, Resistor

def main():
    data = Loader.open_file("data/2026-19-4_circuit_1.json")
    try:
        circuit = Circuit(data)
        print(circuit)
    except ValueError as e:
        print(e)

    solver = Solver(circuit)

if __name__ == "__main__":
    main()  