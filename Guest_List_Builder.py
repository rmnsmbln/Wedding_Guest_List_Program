class Guest:
  def __init__(self, name):
    self.name = name
    self.scores = {}
    self.total_score = 0

def get_rating(question, weight):
  while True:
    try:
      rating = int(input(question + " (1-5): "))
      if 1 <= rating <= 5:
        return rating * weight
      else:
        print("Please enter a number between 1 to 5")
    except ValueError:
      print("Enter a valid number")

def rate_guest(guest):
  print(f"{guest.name}:")
  guest.scores['closeness'] = get_rating(
    "How close are you to this person? (1 = acquaintance, 5 = Family/Bffs)", 5
  )
  guest.scores['contact'] = get_rating(
    "How often do you see or talk to them? (1 = Never, 5 = Daily)", 4
  )
  guest.scores['importance'] = get_rating(
    "How important are they to the wedding? (1 = Not much, 5 = Essential)", 7
  )
  guest.scores['Vibe'] = get_rating(
    "Would your wedding be more fun with them around?", 4
  )
  guest.total_score = sum(guest.scores.values()) # Add up total scores

def main():
  print("Wedding Guest List Builder")
  guests = []

  while True:
    name = input("Enter guest name (TYPE: 'done' to finish): ").strip()

    if name.lower() == 'done':
      break
    guest = Guest(name)
    rate_guest(guest)
    guests.append(guest)

  # Sort by score (Highest First)
  guests.sort(key=lambda x: x.total_score, reverse=True)

  # Show the top 200 guest
  print("\nYour Top 200 guests:")
  print("-" * 40)

  for i in range(200):
    if i < len(guests):
      guest = guests[i]
      print(f"{i + 1}. {guest.name:<20} Score: {guest.total_score}")
    else:
      break

if __name__ == "__main__":
  main()