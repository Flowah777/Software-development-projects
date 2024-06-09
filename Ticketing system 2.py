import random
import string
class Ticket:
   # Class variables for ticket numbers and statistics
   ticketCounter = 2000
   openTickets = 0
   resolvedTickets = 0
   def __init__(self, staffID, creatorName, contactEmail, desc):
       # Initialize ticket with provided details
       self.ticketNo = Ticket.ticketCounter
       Ticket.ticketCounter += 1
       self.staffID = staffID
       self.creatorName = creatorName
       self.contactEmail = contactEmail
       self.desc = desc
       self.response = "Not Yet Provided."
       self.status = "Open"
       Ticket.openTickets += 1
       self.password = None
   def displayTicket(self):
       # Print ticket information
       print(f"Ticket Number: {self.ticketNo}")
       print(f"Ticket Creator: {self.creatorName}")
       print(f"Staff ID: {self.staffID}")
       print(f"Email Address: {self.contactEmail}")
       print(f"Description: {self.desc}")
       print(f"Response: {self.response}")
       if self.password:
           print(f"Password: {self.password}")
       print(f"Ticket Status: {self.status}\n")
   def submitResponse(self, response):
       # Submit a response and close the ticket
       self.response = response
       self.status = "Closed"
       Ticket.openTickets -= 1
       Ticket.resolvedTickets += 1
   def resolvePC(self):
       # Handle password change request and close ticket
       if "password change" in self.desc.lower():
           newPassword = self.generatePassword()
           self.response = f"Password changed to: {newPassword}"
           self.status = "Closed"
           Ticket.openTickets -= 1
           Ticket.resolvedTickets += 1
           self.password = newPassword
   def generatePassword(self):
       # Generate a new password using staff ID and creator name
       staffID_chars = self.staffID[:2]
       creatorName_chars = self.creatorName[:3]
       random_chars = ''.join(random.choices(string.ascii_letters, k=3))
       newPassword = staffID_chars + creatorName_chars + random_chars
       return newPassword
   def reopenTicket(self):
       # Reopen a closed ticket
       self.status = "Reopened"
       Ticket.openTickets += 1
       Ticket.resolvedTickets -= 1
   @classmethod
   def ticket_stats(cls):
       # Show statistics for all tickets
       return f"Tickets Created: {cls.ticketCounter - 2000}\nTickets Resolved: {cls.resolvedTickets}\nTickets To Solve: {cls.openTickets}"
def main():
   tickets = []
   while True:
       # Show menu options
       print("\nMenu:")
       print("1. Create Ticket")
       print("2. Resolve Ticket")
       print("3. Change Password (if Password Change Request)")
       print("4. View All Tickets")
       print("5. View Open Tickets")
       print("6. View Closed Tickets")
       print("0. Exit")
       choice = input("Enter your choice: ")
       if choice == "1":
           # Create a new ticket
           creatorName = input("Enter Creator Name: ")
           staffID = input("Enter Staff ID: ")
           contactEmail = input("Enter Email Address: ")
           desc = input("Enter Description: ")
           tickets.append(Ticket(staffID, creatorName, contactEmail, desc))
           print("Ticket Created Successfully.")
       elif choice == "2":
           # Resolve an existing ticket
           for i, ticket in enumerate(tickets, start=1):
               print(f"{i}. Ticket Number: {ticket.ticketNo} (Status: {ticket.status})")
           ticket_index = int(input("Enter the index of the ticket to resolve: ")) - 1
           if 0 <= ticket_index < len(tickets):
               response = input("Enter response for the selected ticket: ")
               tickets[ticket_index].submitResponse(response)
               print("Ticket resolved successfully.")
           else:
               print("Invalid ticket index.")
       elif choice == "3":
           # Resolve a password change request
           print("Open Tickets:\n")
           for i, ticket in enumerate(tickets, start=1):
               if ticket.status == "Open":
                   print(f"{i}. Ticket Number: {ticket.ticketNo} (Status: {ticket.status})")
           ticket_index = int(input("Enter the index of the Password Change Request to change the password: ")) - 1
           if 0 <= ticket_index < len(tickets):
               tickets[ticket_index].resolvePC()
               print("Password Changed Successfully.")
           else:
               print("Invalid ticket index.")
       elif choice == "4":
           # View all tickets
           print("\nAll Tickets:")
           for ticket in tickets:
               ticket.displayTicket()
           print("\nTicket Statistics: ")
           print(Ticket.ticket_stats())
       elif choice == "5":
           # View open tickets
           print("\nOpen Tickets:\n")
           for ticket in tickets:
               if ticket.status == "Open":
                   ticket.displayTicket()
           print("\nTicket Statistics: \n")
           print(Ticket.ticket_stats())
       elif choice == "6":
           # View closed tickets
           print("\nClosed Tickets:\n")
           for ticket in tickets:
               if ticket.status == "Closed":
                   ticket.displayTicket()
           print("\nTicket Statistics: \n")
           print(Ticket.ticket_stats())
       elif choice == "0":
           # Exit the program
           print("Exiting the Program")
           break
       else:
           print("Invalid Choice. Please Enter a Valid Option.")


if __name__ == "__main__":
    main()
