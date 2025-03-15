class Guest:
  def __init__(self, name):
    self.name = name
    self.total_score = 0

def get_rating(question):
  while True:
    try:
      rating = int(input(question + " (1-5): "))
      if 1 <= rating <= 5:
        return rating
      else:
        print("Please enter a number between 1 to 5")
    except ValueError:
      print("Enter a valid number")

def rate_guest(guest):
  print(f"{guest.name}:")
  guest.total_score = get_rating("How close are you to this person? (1 = acquaintance, 5 = Family/Bffs)")

def main():
  print("Wedding Guest List Builder")
  guests = []

  while True:
    name = input("Enter guest name (TYPE: 'done' to finish): ").strip()

    if name.lower() == 'done':
      break
    guest = Guest(name)
    rate_guest(guest)
    guests.append(name)

  # Show the list
  print("\nYour guests:")

  for i in range(1, len(guests)+1):
    print(f"{i}. {guests[i-1]}")

if __name__ == "__main__":
  main()