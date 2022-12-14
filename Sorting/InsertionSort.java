import java.util.*;

public class InsertionSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] ar = { 9, 3, 9, 2, 6, 0, 8, 4, 7, 1 };

        insertionSort(ar);

        System.out.println(Arrays.toString(ar));

        sc.close();
    }

    private static void insertionSort(int[] ar) {
        /*
         * Time Complexity: O(N^2)
         * Space Complexity: O(1)
         */
        for (int j = 1; j < ar.length; j++) {
            int curr = ar[j];
            int i = j - 1;
            while ((i > -1) && (ar[i] > curr)) {
                ar[i + 1] = ar[i];
                i--;
            }
            ar[i + 1] = curr;
        }

    }

}
