from shooter_calculator import ProjectileSolver

def main():
    solver = ProjectileSolver(delta_x=3, delta_y=3.5)
    solver.set_initial_guess(v0_guess=10, theta_guess=55)
    
    result = solver.solve()
    
    theta_optimal, v0_optimal = result
    
    print(f"Optimal launch angle (degrees): {theta_optimal}")
    print(f"Optimal initial velocity: {v0_optimal}")


if __name__ == "__main__":
    main()