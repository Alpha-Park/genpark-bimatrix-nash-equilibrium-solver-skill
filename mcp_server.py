import json
import sys
from client import BimatrixGameSolver

def handle_rpc(line):
    try:
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        rid = req.get("id")
        
        if method == "tools/list":
            tools = [
                {"name": "solve_game", "description": "Find pure and mixed Nash equilibria"}
            ]
            return json.dumps({"jsonrpc": "2.0", "id": rid, "result": {"tools": tools}})
        elif method == "tools/call":
            tname = params.get("name")
            args = params.get("arguments", {})
            if tname == "solve_game":
                solver = BimatrixGameSolver(args["payoff_p1"], args["payoff_p2"])
                pure = solver.find_pure_nash()
                mixed = solver.solve_2x2_mixed_nash()
                return json.dumps({"jsonrpc": "2.0", "id": rid, "result": {"pure_nash": pure, "mixed_nash": mixed}})
    except Exception as e:
        return json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}})

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(handle_rpc(line.strip()), flush=True)
