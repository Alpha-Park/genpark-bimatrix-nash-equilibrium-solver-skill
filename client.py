class BimatrixGameSolver:
    """
    2-Player Normal Form Game Solver.
    Identifies all Pure Strategy Nash Equilibria (PSNE) and 2x2 Mixed Strategy Nash Equilibria.
    """
    def __init__(self, payoff_p1, payoff_p2):
        # payoff_p1[row][col], payoff_p2[row][col]
        self.u1 = payoff_p1
        self.u2 = payoff_p2
        self.num_rows = len(payoff_p1)
        self.num_cols = len(payoff_p1[0])

    def find_pure_nash(self):
        psne = []
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                # Check P1 best response: u1[r][c] >= u1[r_alt][c] for all r_alt
                is_p1_best = all(self.u1[r][c] >= self.u1[r_alt][c] for r_alt in range(self.num_rows))
                # Check P2 best response: u2[r][c] >= u2[r][c_alt] for all c_alt
                is_p2_best = all(self.u2[r][c] >= self.u2[r][c_alt] for c_alt in range(self.num_cols))

                if is_p1_best and is_p2_best:
                    psne.append((r, c))
        return psne

    def solve_2x2_mixed_nash(self):
        """Solves completely mixed Nash equilibrium for 2x2 games where indifference holds."""
        if self.num_rows != 2 or self.num_cols != 2:
            return None

        # P2 makes P1 indifferent: p * u1[0][0] + (1-p) * u1[0][1] = p * u1[1][0] + (1-p) * u1[1][1]
        # P1 makes P2 indifferent: q * u2[0][0] + (1-q) * u2[1][0] = q * u2[0][1] + (1-q) * u2[1][1]
        denom_q = (self.u2[0][0] - self.u2[0][1] - self.u2[1][0] + self.u2[1][1])
        if abs(denom_q) < 1e-9:
            return None
        q = (self.u2[1][1] - self.u2[1][0]) / denom_q

        denom_p = (self.u1[0][0] - self.u1[1][0] - self.u1[0][1] + self.u1[1][1])
        if abs(denom_p) < 1e-9:
            return None
        p = (self.u1[1][1] - self.u1[0][1]) / denom_p

        if 0.0 <= p <= 1.0 and 0.0 <= q <= 1.0:
            return {"p1_prob_row0": round(q, 4), "p2_prob_col0": round(p, 4)}
        return None
