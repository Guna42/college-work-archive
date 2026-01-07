import math

# Function to calculate number of parity bits required
def calculate_parity_bits(m):
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r

# Function to generate Hamming code
def encode(data):
    m = len(data)                  # number of data bits
    r = calculate_parity_bits(m)   # number of parity bits
    total_bits = m + r

    codeword = [0] * (total_bits + 1)  # 1-based indexing

    # Fill data bits into positions that are not powers of 2
    j = 0
    for i in range(1, total_bits + 1):
        if (i & (i - 1)) != 0:  # not a power of 2
            codeword[i] = data[j]
            j += 1

    # Calculate parity bits
    for i in range(r):
        parity_pos = 1 << i
        parity = 0
        for k in range(1, total_bits + 1):
            if ((k >> i) & 1) == 1 and k != parity_pos:
                parity ^= codeword[k]
        codeword[parity_pos] = parity

    return codeword

# Function to check and correct errors in received codeword
def decode(received):
    total_bits = len(received) - 1
    r = int(math.log2(total_bits)) + 1

    # Calculate syndrome
    error_pos = 0
    for i in range(r):
        parity_pos = 1 << i
        parity = 0
        for k in range(1, total_bits + 1):
            if ((k >> i) & 1) == 1:
                parity ^= received[k]
        if parity != 0:
            error_pos += parity_pos

    if error_pos == 0:
        print("No error detected.")
    else:
        print(f"Error detected at position: {error_pos}")
        received[error_pos] ^= 1
        print("Corrected codeword: ", end="")
        print("".join(str(received[i]) for i in range(1, total_bits + 1)))

    # Extract original data bits
    print("Decoded dataword: ", end="")
    for i in range(1, total_bits + 1):
        if (i & (i - 1)) != 0:  # not a power of 2
            print(received[i], end="")
    print()

def main():
    # Input data bits
    inp = input("Enter dataword (binary string, e.g., 1011): ").strip()

    if not all(c in "01" for c in inp):
        print("Invalid input! Use only 0s and 1s.")
        return

    data = [int(c) for c in inp]

    # Sender: Encode
    codeword = encode(data)
    print("Encoded Hamming codeword: ", end="")
    print("".join(str(codeword[i]) for i in range(1, len(codeword))))

    # Transmission: optional error
    ans = input("Do you want to introduce an error? (y/n): ").strip().lower()
    if ans == "y":
        pos = int(input(f"Enter error position (1 to {len(codeword)-1}): "))
        if 1 <= pos < len(codeword):
            codeword[pos] ^= 1
            print("Received codeword with error: ", end="")
        else:
            print("Invalid position, no error introduced.")
            print("Received codeword: ", end="")
    else:
        print("Received codeword: ", end="")

    print("".join(str(codeword[i]) for i in range(1, len(codeword))))

    # Receiver: Decode
    decode(codeword)

if __name__ == "_main_":main()