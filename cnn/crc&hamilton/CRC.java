import java.util.Scanner;

public class CRC {


    public static String mod2div(String dividend, String divisor) {
        int pick = divisor.length();
        char[] tmp = dividend.substring(0, pick).toCharArray();
        int n = dividend.length();

        for (int i = pick; i < n; i++) {
            // If leftmost bit is '1', perform XOR with divisor
            if (tmp[0] == '1') {
                for (int j = 0; j < pick; j++) {
                    tmp[j] = (tmp[j] == divisor.charAt(j)) ? '0' : '1';
                }
            } else {
               
            }
            for (int k = 0; k < pick - 1; k++) tmp[k] = tmp[k + 1];
            tmp[pick - 1] = dividend.charAt(i);
        }

        if (tmp[0] == '1') {
            for (int j = 0; j < pick; j++) {
                tmp[j] = (tmp[j] == divisor.charAt(j)) ? '0' : '1';
            }
        }

        StringBuilder remainder = new StringBuilder();
        for (int i = 1; i < pick; i++) remainder.append(tmp[i]);
        return remainder.toString();
    }

    public static String computeCodeword(String data, String divisor) {
        int l = divisor.length() - 1;
        StringBuilder appended = new StringBuilder(data);
        for (int i = 0; i < l; i++) appended.append('0');

        String remainder = mod2div(appended.toString(), divisor);
        return data + remainder; 
    }

    
    public static boolean checkReceived(String received, String divisor) {
        String remainder = mod2div(received, divisor);
        // If remainder is all zeros -> no error detected
        for (int i = 0; i < remainder.length(); i++) {
            if (remainder.charAt(i) != '0') return false;
        }
        return true;
    }

    public static String flipBit(String s, int pos) {
        if (pos < 0 || pos >= s.length()) return s;
        char[] arr = s.toCharArray();
        arr[pos] = (arr[pos] == '0') ? '1' : '0';
        return new String(arr);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter dataword (binary string, e.g. 11010011101100):");
        String data = sc.nextLine().trim();
        System.out.println("Enter generator:");
        String divisor = sc.nextLine().trim();

        if (!data.matches("[01]+") || !divisor.matches("[01]+")) {
            System.err.println("Error: only binary strings (0/1) are allowed.");
            sc.close();
            return;
        }
        if (divisor.length() < 2) {
            System.err.println("Error: divisor must be at least 2 bits (degree >= 1).");
            sc.close();
            return;
        }

        // Sender computes the codeword
        String codeword = computeCodeword(data, divisor);
        System.out.println("\n=== SENDER ===");
        System.out.println("Dataword:    " + data);
        System.out.println("Generator:   " + divisor);
        System.out.println("Computed codeword (data + CRC): " + codeword);

        // Simulate transmission: ask whether to inject error
        System.out.println("\nSimulate transmission error? (y/n):");
        String ans = sc.nextLine().trim().toLowerCase();
        String received = codeword;
        if (ans.equals("y") || ans.equals("yes")) {
            System.out.println("Enter bit position to flip (0-based from left, 0.. " + (codeword.length()-1) + "):");
            int pos = -1;
            try {
                pos = Integer.parseInt(sc.nextLine().trim());
            } catch (NumberFormatException e) {
                pos = -1;
            }
            if (pos >= 0 && pos < codeword.length()) {
                received = flipBit(codeword, pos);
                System.out.println("Introduced error at position " + pos);
            } else {
                System.out.println("Invalid position, no error injected.");
            }
        } else {
            System.out.println("No error injected.");
        }

        // Receiver checks the received frame
        System.out.println("\n=== RECEIVER ===");
        System.out.println("Received frame: " + received);
        boolean ok = checkReceived(received, divisor);
        if (ok) {
            System.out.println("Result: No error detected (remainder is 0).");
        } else {
            System.out.println("Result: Error detected (non-zero remainder).");
        }

        sc.close();
    }
}