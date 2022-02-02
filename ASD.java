import java.util.Arrays;

public class ASD {
    public static void main(String[] args) {
        // int[] arr = {9,8,13,16,2,5,17,14,12,6,7};
        int[] arr = { 10, 16, 0, 14, 4, 12, 1, 19, 2, 9, 15 };
        spt(arr);
    }

    static void spt(int[] arr) {

        System.out.println(Arrays.toString(arr));

        int l = 1;
        int r = arr.length - 1;
        int tmp;

        while (l <= r) {
            while ((l <= r) && (arr[r] > arr[0]))
                --r;
            while ((l <= r) && (arr[l] < arr[0]))
                ++l;

            if (l < r) {
                tmp = arr[l];
                arr[l] = arr[r];
                arr[r] = tmp;
                ++l;
                --r;
            }
        }

        if (r > 0) {
            tmp = arr[0];
            arr[0] = arr[r];
            arr[r] = tmp;
        }

        System.out.println(Arrays.toString(arr));
        System.out.println("r = " + r);
        System.out.println("val r = " + arr[r]);
    }

    void swap(int[] arr, int l, int r) {

    }
}