import java.util.Scanner;

public class GeneralHammingCode {

    // Function to calculate number of parity bits required
    static int calculateParityBits(int m) {
        int r = 0;
        while (Math.pow(2, r) < (m + r + 1)) {
            r++;
        }
        return r;
    }

    // Function to generate Hamming code
    static int[] encode(int[] data) {
        int m = data.length;                 // number of data bits
        int r = calculateParityBits(m);      // number of parity bits
        int totalBits = m + r;

        int[] codeword = new int[totalBits + 1]; // 1-based indexing

        // Fill data bits into positions that are not powers of 2
        int j = 0;
        for (int i = 1; i <= totalBits; i++) {
            if ((i & (i - 1)) != 0) { // not a power of 2
                codeword[i] = data[j++];
            }
        }

        // Calculate parity bits
        for (int i = 0; i < r; i++) {
            int parityPos = (1 << i);
            int parity = 0;
            for (int k = 1; k <= totalBits; k++) {
                if (((k >> i) & 1) == 1 && k != parityPos) {
                    parity ^= codeword[k];
                }
            }
            codeword[parityPos] = parity;
        }

        return codeword;
    }

    // Function to check and correct errors in received codeword
    static void decode(int[] received) {
        int totalBits = received.length - 1;
        int r = (int) (Math.log(totalBits) / Math.log(2)) + 1;

        // Calculate syndrome
        int errorPos = 0;
        for (int i = 0; i < r; i++) {
            int parityPos = (1 << i);
            int parity = 0;
            for (int k = 1; k <= totalBits; k++) {
                if (((k >> i) & 1) == 1) {
                    parity ^= received[k];
                }
            }
            if (parity != 0) {
                errorPos += parityPos;
            }
        }

        if (errorPos == 0) {
            System.out.println("✅ No error detected.");
        } else {
            System.out.println("⚠ Error detected at position: " + errorPos);
            received[errorPos] ^= 1; // Correct the error
            System.out.print("Corrected codeword: ");
            for (int i = 1; i <= totalBits; i++) System.out.print(received[i]);
            System.out.println();
        }

        // Extract original data bits
        System.out.print("Decoded dataword: ");
        for (int i = 1; i <= totalBits; i++) {
            if ((i & (i - 1)) != 0) { // not a power of 2
                System.out.print(received[i]);
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input data bits
        System.out.println("Enter dataword (binary string, e.g., 1011): ");
        String input = sc.nextLine().trim();

        if (!input.matches("[01]+")) {
            System.out.println(" Invalid input! Use only 0s and 1s.");
            return;
        }

        int n = input.length();
        int[] data = new int[n];
        for (int i = 0; i < n; i++) {
            data[i] = input.charAt(i) - '0';
        }

        // Sender: Encode
        int[] codeword = encode(data);
        System.out.print("Encoded Hamming codeword: ");
        for (int i = 1; i < codeword.length; i++) System.out.print(codeword[i]);
        System.out.println();

        // Transmission: optional error
        System.out.println("Do you want to introduce an error? (y/n): ");
        String ans = sc.nextLine().trim().toLowerCase();
        if (ans.equals("y")) {
            System.out.println("Enter error position (1 to " + (codeword.length - 1) + "): ");
            int pos = sc.nextInt();
            if (pos >= 1 && pos < codeword.length) {
                codeword[pos] ^= 1;
                System.out.print("Received codeword with error: ");
            }
        } else {
            System.out.print("Received codeword: ");
        }
        for (int i = 1; i < codeword.length; i++) System.out.print(codeword[i]);
        System.out.println();

        // Receiver: Decode
        decode(codeword);

        sc.close();
    }
}