import datetime

class EnergyConsumptionMonitor:
    def __init__(self):
        self.usage_data = {}

    def add_usage(self, device, usage):
        timestamp = datetime.datetime.now()
        if device in self.usage_data:
            self.usage_data[device].append((timestamp, usage))
        else:
            self.usage_data[device] = [(timestamp, usage)]

    def get_total_usage(self, device):
        if device in self.usage_data:
            total_usage = sum(usage for _, usage in self.usage_data[device])
            return total_usage
        else:
            return 0

    def get_usage_history(self, device):
        if device in self.usage_data:
            return self.usage_data[device]
        else:
            return []

# Sample usage of the EnergyConsumptionMonitor class
monitor = EnergyConsumptionMonitor()

# Add usage data for a device
monitor.add_usage("Smart Light Bulb", 10)
monitor.add_usage("Smart Light Bulb", 15)
monitor.add_usage("Smart Thermostat", 5)

# Get the total usage for a device
total_usage = monitor.get_total_usage("Smart Light Bulb")
print("Total usage for Smart Light Bulb:", total_usage)

# Get the usage history for a device
usage_history = monitor.get_usage_history("Smart Light Bulb")
print("Usage history for Smart Light Bulb:")
for timestamp, usage in usage_history:
    print(timestamp, "-", usage)
