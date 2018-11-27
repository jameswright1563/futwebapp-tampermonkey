from app.requirements.requirements_builder import RequirementsBuilder
from app.solver import Solver

parameters = {
    "chemistry": 100,
    "team_rating": 85,
    "max_costs": 100000,
    "formation": '442'
}
requirements = RequirementsBuilder(**parameters)

# Returns a player and position dict for the given formation
results = Solver(requirements=requirements).solve(strategy='genetic')
