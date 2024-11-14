class ROBIN:
    def __init__(self):
        self.conversion_orchestrator = ConversationOrchestrator()
        self.context_agent = ContextAgent()
        self.collaborative_agent = CollaborativeAgent()
        self.responder_agent = ResponderAgent()
        self.follow_up_agent = FollowUpAgent()

    def generate_reply(self, message):
        if self.conversion_orchestrator.need_investigation(message):
            if self.conversion_orchestrator.can_automate_context(message):
                return self.process_with_context(message)
            else:
                return self.process_without_context(message)
        else:
            return self.responder_agent.generate_response(message)

    def process_with_context():
        context = self.context_agent.extract_context(message)
        


    def process_without_context():