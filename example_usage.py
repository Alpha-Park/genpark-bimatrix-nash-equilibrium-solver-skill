import sys
from client import BimatrixGameSolver

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

def run():
    print(">>> Demonstrating Bimatrix Nash Equilibrium Solver...")
    
    # Prisoner's Dilemma
    # Actions: 0=Cooperate, 1=Defect
    # u1, u2
    p1_pd = [[3, 0], [5, 1]]
    p2_pd = [[3, 5], [0, 1]]

    solver_pd = BimatrixGameSolver(p1_pd, p2_pd)
    psne = solver_pd.find_pure_nash()
    print(f"Prisoner's Dilemma Pure Nash: {psne}")
    assert psne == [(1, 1)] # Both Defect

    # Matching Pennies (Zero-Sum, Mixed Nash)
    p1_mp = [[1, -1], [-1, 1]]
    p2_mp = [[-1, 1], [1, -1]]
    solver_mp = BimatrixGameSolver(p1_mp, p2_mp)
    assert solver_mp.find_pure_nash() == []
    mixed = solver_mp.solve_2x2_mixed_nash()
    print(f"Matching Pennies Mixed Nash: {mixed}")
    assert mixed['p1_prob_row0'] == 0.5
    assert mixed['p2_prob_col0'] == 0.5

    print("[PASS] Bimatrix Nash Equilibrium Solver verified.")

if __name__ == "__main__":
    run()
