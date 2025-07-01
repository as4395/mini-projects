import random
import string
import logging

logging.basicConfig(
    filename='fuzzing.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def random_string(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def target_function(input_data):
    """
    Example vulnerable function that crashes on certain inputs.
    For demonstration, crashes if '!' is in input.
    """
    if '!' in input_data:
        raise ValueError("Invalid character '!' detected!")
    # Simulate processing
    return input_data[::-1]

def fuzz(iterations=1000):
    for i in range(iterations):
        test_input = random_string(random.randint(5, 15))
        try:
            result = target_function(test_input)
            logging.info(f"Iteration {i}: Success with input: {test_input}")
        except Exception as e:
            logging.error(f"Iteration {i}: Crash with input: {test_input} - Exception: {e}")

if __name__ == "__main__":
    print("Starting fuzzing...")
    fuzz()
    print("Fuzzing complete. Check fuzzing.log for details.")
