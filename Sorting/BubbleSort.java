import java.util.*;

class BubbleSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] ar = { 9, 3, 9, 2, 6, 0, 8, 4, 7, 1 };

        bubbleSort(ar);

        System.out.println(Arrays.toString(ar));

        sc.close();
    }

    private static void bubbleSort(int[] ar) {
        /*
         * Time Complexity: O(N^2)
         * Space Complexity: O(1)
         */
        for (int i = 0; i < ar.length; i++) {
            for (int j = i + 1; j < ar.length; j++) {
                if (ar[i] > ar[j]) {
                    ar[i] = ar[j] ^ ar[i] ^ (ar[j] = ar[i]);
                }
            }
        }

    }
}