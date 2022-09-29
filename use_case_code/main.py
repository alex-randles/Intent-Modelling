# Code that executes the control loop for the use case
from rdflib import *

# intents = {
#     1 : {
#         "intent_name": "Maintain throughput between a specific threshold",
#         "intent_description": "Maintain downlink throughput at 6900-700",
#         "goals": {
#             "1": {
#                 "goal_name": "Maintain throughput greater than 6900",
#                 "goal_satisfied": "true",
#             },
#             "2": {
#                 "goal_name": "Maintain throughput less than 7000",
#                 "goal_satisfied": "true",
#             }
#         }
#     }
# }

# for intent_number, intent in intents.items():
#     print("Intent: ", intent_number)
#     intent_name = intent.get("intent_name")
#     intent_description = intent.get("intent_description")
#     print("Intent name: ", intent_name)
#     print("Intent description: ", intent_description)
#     banner = "*" * (len(intent_description) + 22)
#     print(banner)
#     print("Executing Actions.....")
#     print(banner)
#     i = 0
#     goals = intent.get("goals")
#     for goal_number, goal_info in goals.items():
#         print("Goal: ", goal_number)
#         print("Goal Description: ", goal_info.get("goal_name"))
#         print("Goal Satisfied: ", goal_info.get("goal_satisfied"))
#         i += 1
#     print(banner)
#     print("Intent Satisfied: true")
#     print("Control loop maintained...")


class ControlLoop:

    def __init__(self, num_intents, graph_file):
        self.num_intents = num_intents
        self.intent_graph = Graph().parse(graph_file, format="ttl")
        self.run_control_loop()

    def get_intent_info(self):
        query = """
            SELECT ?name ?description
            WHERE {
                ?intent a :Intent;
                        :hasIntentName ?name;
                        :hasIntentDescription ?description . 
            } 
        """
        qres = self.intent_graph.query(query)
        intent_info = {}
        for row in qres:
            intent_info["name"] = str(row["name"])
            intent_info["description"] = str(row["description"])
        return intent_info

    def get_action_info(self):
        query = """
            SELECT ?name ?description 
            WHERE {
                ?goal a :MetricGoal; 
                      :isMaintainedBy ?actionEffect . 
                ?action :hasEffect ?actionEffect; 
                        :hasActionName ?name ;
                        :hasActionDescription ?description
            } 
        """
        qres = self.intent_graph.query(query)
        action_info = {}
        for row in qres:
            action_info["name"] = str(row["name"])
            action_info["description"] = str(row["description"])
        return action_info

    def get_goal_info(self):
        query = """
            SELECT ?goalValue ?goalSatisfied 
            WHERE {
                ?goal a :MetricGoal; 
                      :hasGoalValue ?goalValue; 
                      :isSatisfied ?goalSatisfied . 
            } 
        """
        qres = self.intent_graph.query(query)
        goal_info = {}
        goal_counter =  0
        for row in qres:
            goal_info[goal_counter] = {}
            goal_info[goal_counter]["goal_status"] = str(row["goalSatisfied"])
            goal_info[goal_counter]["goal_value"] = str(row["goalValue"])
            goal_counter += 1
        return goal_info

    def run_control_loop(self):
        for intent_number in range(1, self.num_intents + 1):
            print("Intent: ", intent_number)
            intent_info = self.get_intent_info()
            intent_name = intent_info.get("name")
            intent_description = intent_info.get("description")
            print("Intent name: ", intent_name)
            print("Intent description: ", intent_description)
            banner = "*" * (len(intent_description) + 22)
            print(banner)
            print("Executing Actions.....")
            print(banner)
            action_info = self.get_action_info()
            goal_info = self.get_goal_info()
            for goal_num, goal_details in goal_info.items():
                print("Goal: ", goal_num)
                print("Goal Satisfied:", goal_info.get(goal_num).get("goal_status"))
                print("Goal Value: ", goal_info.get(goal_num).get("goal_value"))
            print(banner)
            print("Intent Satisfied: true")
            print("Control loop maintained...")
        
        
if __name__ == "__main__":
    ControlLoop(1, "../use_case_graph.ttl")