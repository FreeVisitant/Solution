import random
import string
import config_client

def generate_chains(num_chains):
    """
    Generates a specified number of random strings and writes them to a file.
    
    :param num_chains: The number of strings to generate
    """
    def generate_chain_f(length, num_spaces):
        """
        Generates a random string of a specified length and number of spaces.
        Ensures that spaces are not consecutive and do not appear at the start or end of the string.
        
        :param length: The length of the string
        :param num_spaces: The number of spaces in the string
        :return: The generated string, or None if it was not possible to generate a valid string
        """
        # Check if it's possible to generate a string with the specified parameters
        if length - num_spaces < num_spaces + 2:
            return None

        # Randomly choose positions for the spaces, ensuring they are not consecutive
        spaces_positions = sorted(random.sample(range(1, length - 1), num_spaces))
        for i in range(1, len(spaces_positions)):
            while spaces_positions[i] - spaces_positions[i-1] <= 1:
                spaces_positions[i] += 1
            if spaces_positions[i] >= length - 1:
                return None

        # Generate the string, inserting spaces and random characters
        chain = ""
        for i in range(length):
            if i in spaces_positions:
                chain += " "
            else:
                chain += random.choice(string.ascii_letters + string.digits)
        return chain

    # Open the file for writing and generate the strings
    with open(config_client.CHAINS_FILE_PATH, 'w') as f:
        for _ in range(num_chains):
            length = random.randint(50, 100)
            num_spaces = random.randint(3, 5)
            chain = generate_chain_f(length, num_spaces)
            if chain:
                f.write(chain + "\n")

if __name__ == "__main__":
    # Generate the strings when the script is run directly
    generate_chains(config_client.NUM_CHAINS_TO_GENERATE)