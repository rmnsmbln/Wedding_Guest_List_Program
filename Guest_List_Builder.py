class Guest:
  def __init__(self):
    self.name = name
    self.total_score = 0

def main():
  print("Wedding Guest List Builder")
  guests = []

  while True:
    name = input("Enter guest name (TYPE: 'done' to finish): ")
    if name.lower() == 'done':
      break
    guests.append(name)

  # Show the list
  print("\nYour guests:")

  for i in range(1, len(guests)+1):
    print(f"{i}. {guests[i-1]}")

if __name__ == "__main__":
  main()