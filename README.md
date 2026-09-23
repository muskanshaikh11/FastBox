# FastBox Mystery Delivery System

## What is included
- `main.py` - complete Python solution
- `data.json` - assignment sample input
- `report.json` - generated output
- `test_cases/` - supplied test cases
- `test_results.json` - test results

## How to run

Open a terminal in this folder and run:

    python main.py

To test another input file:

    python main.py test_cases/test_case_1.json

The program creates `report.json`.

## Logic
1. Read JSON using Python's `json` module.
2. Calculate Euclidean distance.
3. Assign each package to the closest agent based on agent-to-warehouse distance.
4. Deliver packages in their JSON order.
5. For each package, travel from the agent's current position to the warehouse, then to the destination.
6. Update the agent's current position to the destination.
7. Efficiency = total distance / packages delivered.
8. Lowest efficiency value is reported as `best_agent`.
9. Exact ties use the first agent in JSON order.

The program supports both the PDF dictionary format and the supplied `base_case.json` list format.
