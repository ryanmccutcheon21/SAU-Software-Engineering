class TrespassAlert:
    def __init__(self):
        self.alerts = []

    def add_alert(self, message):
        self.alerts.append(message)
        self.notify_users(message)

    def notify_users(self, message):
        # Implement your notification mechanism here
        # This could involve sending emails, push notifications, or triggering alarms
        print("Alert: {}".format(message))

# Example usage
alert_system = TrespassAlert()
alert_system.add_alert("Unidentified person detected at the front door.")
