
# ===== Event Management System =====

class Participant:

    def __init__(self, participant_id, name, phone):
        self.participant_id = participant_id
        self.name = name
        self.phone = phone

    def display(self):
        print(f"{self.participant_id}\t"
              f"{self.name}\t"
              f"{self.phone}")


class Event:

    def __init__(self, event_id, event_name, event_type, event_date, venue, organizer, ticket_price):
        self.event_id = event_id
        self.event_name = event_name
        self.event_type = event_type
        self.event_date = event_date
        self.venue = venue
        self.organizer = organizer
        self.ticket_price = ticket_price
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def remove_participant(self, participant):
        if participant in self.participants:
            self.participants.remove(participant)

    def display(self):
        print(f"{self.event_id}\t"
              f"{self.event_name}\t"
              f"{self.event_type}\t"
              f"{self.event_date}\t"
              f"{self.venue}\t"
              f"{self.organizer}\t"
              f"{self.ticket_price:.2f}\t"
              f"{len(self.participants)}\t"
              )

    def calculate_revenue(self):
        return len(self.participants) * self.ticket_price


class EventManagementSystem:

    def __init__(self):
        self.events = []

    # Find event
    def find_event(self, event_id):
        for event in self.events:
            if event.event_id == event_id:
                return event
        return None

    # Find Participant
    def find_participant(self, event, participant_id):
        for participant in event.participants:
            if participant.participant_id == participant_id:
                return participant
        return None

    # Add Event
    def add_event(self):
        try:
            event_id = int(input("Enter Event ID: "))
        except ValueError:
            print("Invalid Event ID. Enter a number.")
            return

        if event_id <= 0:
            print("Event ID must be positive.")
            return

        if self.find_event(event_id):
            print("This Event ID is already in use.")
            return

        event_name = input("Enter Event Name: ").strip()
        event_type = input("Enter Event Type: ").strip()
        event_date = input("Enter Event Date: ").strip()
        venue = input("Enter Venue: ").strip()
        organizer = input("Enter Organizer Name: ").strip()

        if not event_name or not event_type or not event_date or not venue or not organizer:
            print("Event details cannot be empty.")
            return

        try:
            ticket_price = float(input("Enter Ticket Price: "))
        except ValueError:
            print("Invalid ticket price. Enter a number.")
            return

        if ticket_price < 0:
            print("Ticket price cannot be negative.")
            return

        event = Event(event_id, event_name, event_type,
                      event_date, venue, organizer, ticket_price)

        self.events.append(event)
        print("Event created successfully.")

    # View Events
    def view_events(self):
        if not self.events:
            print("No events available.")
            return

        print("\nID\tName\tType\tDate\tVenue\t"
              "Organizer\tPrice\tParticipants")
        print("-" * 110)

        for event in self.events:
            event.display()

    # Search Event
    def search_event(self):
        try:
            event_id = int(input("Enter Event ID: "))
        except ValueError:
            print("Invalid Event ID. Enter a number.")
            return

        event = self.find_event(event_id)

        if event:
            print("\nEvent Information")
            print("---------------------------------")
            print("Event ID:", event.event_id)
            print("Event Name:", event.event_name)
            print("Event Type:", event.event_type)
            print("Event Date:", event.event_date)
            print("Venue:", event.venue)
            print("Organizer:", event.organizer)
            print("Ticket Price:", event.ticket_price)
            print("Registered Participants:", len(event.participants))
        else:
            print("No matching event found.")

    # Register Participant
    def register_participant(self):
        try:
            event_id = int(input("Enter Event ID: "))
        except ValueError:
            print("Invalid Event ID. Enter a number.")
            return

        event = self.find_event(event_id)

        if event:
            try:
                participant_id = int(input("Enter Participant ID: "))
            except ValueError:
                print("Invalid Participant ID. Enter a number.")
                return

            if participant_id <= 0:
                print("Participant ID must be positive.")
                return

            if self.find_participant(event, participant_id):
                print("This participant is already registered for this event.")
                return

            name = input("Enter Participant Name: ").strip()
            phone = input("Enter Phone Number: ").strip()

            if not name or not phone:
                print("Participant name and phone cannot be empty.")
                return

            participant = Participant(participant_id, name, phone)
            event.add_participant(participant)

            print("Registration completed successfully.")
            print("Ticket Price:", event.ticket_price)
        else:
            print("No matching event found.")

    # View Participants
    def view_participants(self):
        try:
            event_id = int(input("Enter Event ID: "))
        except ValueError:
            print("Invalid Event ID. Enter a number.")
            return

        event = self.find_event(event_id)

        if event:
            if not event.participants:
                print("No participants registered for this event.")
                return

            print("\nID\tName\tPhone")
            print("----------------------------------------")

            for participant in event.participants:
                participant.display()
        else:
            print("No matching event found.")

    # Cancel Registration
    def cancel_registration(self):
        try:
            event_id = int(input("Enter Event ID: "))
        except ValueError:
            print("Invalid Event ID. Enter a number.")
            return

        event = self.find_event(event_id)

        if event:
            try:
                participant_id = int(input("Enter Participant ID: "))
            except ValueError:
                print("Invalid Participant ID. Enter a number.")
                return

            participant = self.find_participant(event, participant_id)

            if participant:
                event.remove_participant(participant)
                print("Registration cancelled successfully.")
            else:
                print("Participant not found in this event.")
        else:
            print("No matching event found.")

    # Update Event
    def update_event(self):
        try:
            event_id = int(input("Enter Event ID: "))
        except ValueError:
            print("Invalid Event ID. Enter a number.")
            return

        event = self.find_event(event_id)

        if event:
            print("\nLeave input blank to keep the current value.")

            name = input(f"Event Name [{event.event_name}]: ").strip()
            venue = input(f"Venue [{event.venue}]: ").strip()
            date = input(f"Date [{event.event_date}]: ").strip()

            if name:
                event.event_name = name

            if venue:
                event.venue = venue

            if date:
                event.event_date = date

            print("Event details updated successfully.")
        else:
            print("No matching event found.")

    # Calculate Revenue
    def calculate_revenue(self):
        try:
            event_id = int(input("Enter Event ID: "))
        except ValueError:
            print("Invalid Event ID. Enter a number.")
            return

        event = self.find_event(event_id)

        if event:
            revenue = event.calculate_revenue()

            print("\n==== Event Revenue ====")
            print("Event Name:", event.event_name)
            print("Registered Participants:", len(event.participants))
            print("Ticket Price:", f"{event.ticket_price:.2f}")
            print("Total Revenue:", f"{revenue:.2f}")
        else:
            print("No matching event found.")

    # Delete Event
    def delete_event(self):
        try:
            event_id = int(input("Enter Event ID: "))
        except ValueError:
            print("Invalid Event ID. Enter a number.")
            return

        event = self.find_event(event_id)

        if event:
            self.events.remove(event)
            print("Event removed successfully.")
        else:
            print("No matching event found.")


# ===================== Main Program =======================

system = EventManagementSystem()

while True:

    print("\n=======================================")
    print("       Event Planner & Registration")
    print("=======================================")
    print("1. Create Event")
    print("2. View All Events")
    print("3. Search Event")
    print("4. Register Participant")
    print("5. View Participants")
    print("6. Cancel Registration")
    print("7. Update Event")
    print("8. Calculate Event Revenue")
    print("9. Delete Event")
    print("10. Exit")

    try:
        choice = int(input("Select an option: "))
    except ValueError:
        print("Invalid choice. Enter a number from 1 to 10.")
        continue

    if choice == 1:
        system.add_event()
    elif choice == 2:
        system.view_events()
    elif choice == 3:
        system.search_event()
    elif choice == 4:
        system.register_participant()
    elif choice == 5:
        system.view_participants()
    elif choice == 6:
        system.cancel_registration()
    elif choice == 7:
        system.update_event()
    elif choice == 8:
        system.calculate_revenue()
    elif choice == 9:
        system.delete_event()
    elif choice == 10:
        print("Thank you for using the system. Goodbye!")
        break
    else:
        print("Invalid choice. Select an option from 1 to 10.")
