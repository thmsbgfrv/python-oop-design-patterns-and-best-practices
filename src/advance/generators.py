# def print_prev_and_current():
#     prev = 0  # Initialize the previous number
#     while True:
#         # Yield the initial state or the current state after receiving a value
#         current = yield f"Prev: {prev}, Current: {prev}"

#         # Print the previous and current values received
#         print(f"Prev: {prev}, Current: {current}")

#         # Update prev to be the current for the next iteration
#         prev = current


# # Usage
# gen = print_prev_and_current()
# print(next(gen))  # Start the generator; Output: "Prev: 0, Current: 0"

# # Send values to the generator and print the output
# print(gen.send(10))  # Output: "Prev: 0, Current: 10"
# print(gen.send(20))  # Output: "Prev: 10, Current: 20"
# print(gen.send(30))  # Output: "Prev: 20, Current: 30"
