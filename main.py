import json
import math

# Read data
with open("data.json", "r") as file:
    data = json.load(file)

warehouses = data["warehouses"]
agents = data["agents"]
packages = data["packages"]


# Find distance between two points
def distance(p1, p2):
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2
    )


# Assign packages to nearest agent
assigned = {}

for agent in agents:
    assigned[agent] = []

for package in packages:

    warehouse = warehouses[package["warehouse"]]

    nearest = None
    shortest = float("inf")

    for agent in agents:

        d = distance(agents[agent], warehouse)

        if d < shortest:
            shortest = d
            nearest = agent

    assigned[nearest].append(package)


# Deliver packages
report = {}

for agent in agents:

    position = agents[agent]
    total = 0

    for package in assigned[agent]:

        warehouse = warehouses[package["warehouse"]]
        destination = package["destination"]

        # Agent goes to warehouse
        total += distance(position, warehouse)

        # Agent goes to destination
        total += distance(warehouse, destination)

        position = destination

    count = len(assigned[agent])

    if count > 0:
        efficiency = total / count
    else:
        efficiency = 0

    report[agent] = {
        "packages_delivered": count,
        "total_distance": round(total, 2),
        "efficiency": round(efficiency, 2)
    }


# Find best agent
best_agent = min(
    report,
    key=lambda agent: report[agent]["efficiency"]
)

report["best_agent"] = best_agent


# Save report
with open("report.json", "w") as file:
    json.dump(report, file, indent=4)


print("Package assignments:")

for agent in assigned:
    print(agent, ":", [p["id"] for p in assigned[agent]])

print("\nBest agent:", best_agent)
print("report.json created!")