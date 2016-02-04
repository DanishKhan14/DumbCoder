
"""
O(lg N) solution

Simply divide the input number as long as it's dividable by 2.

public boolean isPowerOfTwo(int n) {

        while(n > 1) {
            if(n % 2 != 0) {
                return false;
            }
            n /= 2;
        }
        return n == 1;
}
O(1) solution

This uses a bit of binary math and simple observation that if you have a power of 2 in binary then when you substract 1 from it you will have all lower order bits set to 1. ex. 8 in binary 1000 - 1 = 0111 so by doing AND of both values (N & (N - 1)) you should expect the result to be 0. This is only true for values that are the power of two.

public boolean isPowerOfTwo(int n) {

            return n > 0 && (n & n - 1) == 0;
}
O(1) - this can be considered constant, although it will vary on the actual type size and generally offer worse performance then both above solutions - (well we have to distinguish worse and best case - the base case is when the number is not power of 2, but the worse case is the oposite and we have to check all the bits of the input to verify that)

Another possibility is shifting and counting the number of ones.

public boolean isPowerOfTwo(int n) {

        int count = 0;
        for(int ind = 0; ind < 32; ind++) {
            if((n & (1 << ind)) != 0) {
                count++;
            }
        }
        return n > 0 && count == 1;
}
"""

