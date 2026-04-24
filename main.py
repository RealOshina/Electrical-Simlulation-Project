from electricalsim import Loader, Circuit

def main():
    data = Loader.open_file("data/2026-19-4_circuit_1.json")
    circuit = Circuit(data)

if __name__ == "__main__":
    main()