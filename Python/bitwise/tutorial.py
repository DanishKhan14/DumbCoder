"""
Theory:

>>, <<, ^, &, |, ~

Two's Complement binary for Negative Integers:

A negative number, -x, is written using the bit
pattern for (x-1) with all of the bits complemented
(switched from 1 to 0 or 0 to 1). So -1 is complement(1 - 1) = complement(0) = "11111111"

Python uses INFINITE number of bits.
Thus the number -5 is treated by bitwise operators as if it were written "...1111111111111111111011".
"""



# Single Bit Operations

    # testBit() returns a nonzero result, 2**offset, if the bit at 'offset' is one.

    def testBit(int_type, offset):
        mask = 1 << offset
        return(int_type & mask)

    # setBit() returns an integer with the bit at 'offset' set to 1.

    def setBit(int_type, offset):
        mask = 1 << offset
        return(int_type | mask)

   # clearBit() returns an integer with the bit at 'offset' cleared.

    def clearBit(int_type, offset):
        mask = ~(1 << offset)
        return(int_type & mask)

    # toggleBit() returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0.

    def toggleBit(int_type, offset):
        mask = 1 << offset
        return(int_type ^ mask)



############ LowerSet ############

    def lowestSet(int_type):
        low = (int_type & -int_type)
        lowBit = -1
        while (low):
            low >>= 1
            lowBit += 1
            return(lowBit)

############ Bit Count ###########

    def bitLenCount(int_type):
        length = 0
        count = 0
        while (int_type):
            count += (int_type & 1)
            length += 1
            int_type >>= 1
        return(length, count)



    def bitCount(int_type):
        count = 0
        while(int_type):
            int_type &= int_type - 1
            count += 1
        return(count)

############ Parity ##############

    def parityOf(int_type):
        parity = 0
        while (int_type):
            parity = ~parity
            int_type = int_type & (int_type - 1)
        return(parity)

