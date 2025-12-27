class ConversationMemory:
    def __init__(self):
        self.last_intent = None
        self.last_budget = None
        self.last_results = None

    def update(self, intent = None, budget = None, results = None):
        if intent is not None:
            self.last_intent = intent
        if budget is not None:
            self.last_budget = budget
        if results is not None:
            self.last_results = results

    def reset(self):
        self.last_intent = None
        self.last_budget = None
        self.last_results = None
   