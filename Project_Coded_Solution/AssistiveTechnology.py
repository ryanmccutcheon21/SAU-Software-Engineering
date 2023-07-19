class AssistiveTechnology:
    def __init__(self):
        self.emergency_contacts = []

    def add_emergency_contact(self, contact_name, contact_number):
        # Add emergency contact information
        self.emergency_contacts.append({"name": contact_name, "number": contact_number})

    def detect_critical_situation(self, situation):
        # Simulating the detection of critical situations
        if situation == "emergency":
            self.trigger_emergency_assistance()
        elif situation == "handicap":
            self.assist_with_handicap()

    def trigger_emergency_assistance(self):
        # Send emergency alerts or notifications to the designated emergency contacts
        for contact in self.emergency_contacts:
            print(f"Sending emergency alert to {contact['name']} at {contact['number']}")

    def assist_with_handicap(self):
        # Perform specific assistance actions for handicap situations
        print("Assistance provided for handicap situation.")


# Sample usage of the AssistiveTechnology class
assistive_tech = AssistiveTechnology()
assistive_tech.add_emergency_contact("John Doe", "+123456789")
assistive_tech.add_emergency_contact("Jane Smith", "+987654321")

assistive_tech.detect_critical_situation("emergency")
assistive_tech.detect_critical_situation("handicap")
