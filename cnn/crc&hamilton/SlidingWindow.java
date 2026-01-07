import java.util.Random;

public class SlidingWindow {

    static Random random = new Random();

    // Sender function
    public static void sender(int totalFrames, int windowSize) {
        int base = 0; // first frame in window
        int nextFrame = 0; // next frame to send

        while (base < totalFrames) {
            // Send frames in window
            while (nextFrame < base + windowSize && nextFrame < totalFrames) {
                System.out.println("Sender: Sending Frame " + nextFrame);
                nextFrame++;
            }

            // Simulate ACKs from receiver
            int ack = receiver(base, nextFrame - 1);

            if (ack == -1) {
                System.out.println("Sender: Timeout! Resending from Frame " + base + "\n");
                nextFrame = base; // resend from base
            } else {
                System.out.println("Sender: ACK received for Frame " + ack + "\n");
                base = ack + 1; // slide window
            }
        }

        System.out.println("Sender: All frames sent successfully!");
    }

    // Receiver function
    public static int receiver(int start, int end) {
        // Simulate random ACK loss
        boolean ackLost = random.nextInt(10) < 3;

        if (ackLost) {
            System.out.println("Receiver: ACK lost! No ACK sent.");
            return -1; // ACK lost, sender must retransmit
        } else {
            int ack = end; // cumulative ACK (Go-Back-N)
            System.out.println("Receiver: Frames " + start + " to " + end + " received. Sending ACK for Frame " + ack);
            return ack;
        }
    }

    public static void main(String[] args) {
        int totalFrames = 10;   // Number of frames to send
        int windowSize = 4;     // Sliding window size
        sender(totalFrames, windowSize);
    }
}