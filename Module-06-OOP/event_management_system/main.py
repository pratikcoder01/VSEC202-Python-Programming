"""
Simple Event Management System using classes.
"""


class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location

    def __str__(self):
        return f"{self.name} on {self.date} at {self.location}"


class EventManager:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def list_events(self):
        if not self.events:
            print("No events available.")
        else:
            print("Upcoming events:")
            for i, e in enumerate(self.events, start=1):
                print(f"{i}. {e}")


manager = EventManager()

while True:
    print("\n=== Event Management System ===")
    print("1. Add event")
    print("2. View events")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter event name: ")
        date = input("Enter event date: ")
        location = input("Enter event location: ")
        event = Event(name, date, location)
        manager.add_event(event)
        print("Event added.")
    elif choice == "2":
        manager.list_events()
    elif choice == "3":
        print("Exiting Event Management System.")
        break
    else:
        print("Invalid choice.")
