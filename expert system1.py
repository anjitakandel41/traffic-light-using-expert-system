import time

class TrafficLightSystem:
    def __init__(self):
        self.state = 'Red'

    def run(self):
        while True:
            if self.state == 'Red':
                print("🟥 Red Light - STOP")
                time.sleep(5)
                self.state = 'Green'

            elif self.state == 'Green':
                print("🟩 Green Light - GO")
                time.sleep(4)
                self.state = 'Yellow'

            elif self.state == 'Yellow':
                print("🟨 Yellow Light - SLOW DOWN")
                time.sleep(2)
                self.state = 'Red'

# Run the system
traffic_system = TrafficLightSystem()
try:
    traffic_system.run()
except KeyboardInterrupt:
    print("\nSystem stopped.")
