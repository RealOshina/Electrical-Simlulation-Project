from electricalsim import Loader, Circuit, Solver, Simulation

def main():
    data = Loader.open_file("data/2026-19-4_circuit_1.json")
    try:
        circuit = Circuit(data)
        print(circuit.result)
    except ValueError as e:
        print(e)
        return
    
    solver = Solver(circuit)
    print(solver.result)
    
    simulation = Simulation(solver.result)
    time = 1
    while time <= 6:
        simulation.simulate(time)
        print(simulation.result)
        #print(solver.result)
        time += 1
 
if __name__ == "__main__":
    main()