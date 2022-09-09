# Code that executes the control loop for the use case


intents = {
    1 : {
        "intent_name": "Maintain throughput between a specific threshold",
        "intent_description": "Maintain downlink throughput at 6900-700",
        "goals": {
            "1": {
                "goal_name": "Maintain throughput greater than 6900",
                "goal_satisfied": "true",
            },
            "2": {
                "goal_name": "Maintain throughput less than 7000",
                "goal_satisfied": "true",
            }
        }
    }
}

for intent_number, intent in intents.items():
    print("Intent: ", intent_number)
    intent_name = intent.get("intent_name")
    intent_description = intent.get("intent_description")
    print("Intent name: ", intent_name)
    print("Intent description: ", intent_description)
    banner = "*" * (len(intent_description) + 22)
    print(banner)
    print("Executing Actions.....")
    print(banner)
    i = 0
    goals = intent.get("goals")
    for goal_number, goal_info in goals.items():
        print("Goal: ", goal_number)
        print("Goal Description: ", goal_info.get("goal_name"))
        print("Goal Satisfied: ", goal_info.get("goal_satisfied"))
        i += 1
    print(banner)
    print("Intent Satisfied: true")
    print("Control loop maintained...")
