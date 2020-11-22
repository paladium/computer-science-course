def calculate_time(aircraft, distance):
  return distance / aircraft["speed"]

aircraft = {
  "speed": 500
}

print(calculate_time(aircraft, 1000))

wrong_input = {
  "name": "Test"
}
print(calculate_time(wrong_input, 2000))