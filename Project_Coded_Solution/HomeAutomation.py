class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Light turned on")

    def turn_off(self):
        self.is_on = False
        print("Light turned off")


class Thermostat:
    def __init__(self):
        self.temperature = 25

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Temperature set to {temperature}°C")

    def get_temperature(self):
        return self.temperature


class SmartHomeAutomation:
    def __init__(self):
        self.light = Light()
        self.thermostat = Thermostat()

    def control_light(self, command):
        if command == "on":
            self.light.turn_on()
        elif command == "off":
            self.light.turn_off()

    def control_thermostat(self, temperature):
        self.thermostat.set_temperature(temperature)

    def get_thermostat_temperature(self):
        return self.thermostat.get_temperature()


# Sample usage of the home automation system
home = SmartHomeAutomation()

home.control_light("on")
home.control_thermostat(22)

current_temperature = home.get_thermostat_temperature()
print(f"Current temperature: {current_temperature}°C")

home.control_light("off")
