"""
one example:
index      0  1  2  3  4  5  6  7  8  9  10  11
value      5  9  3  2  1  0  2  3  3  1  0   0
farthest   5  10 10 10 10 10 10 10 11 11 11  11

    my thought -- scan from right to left.

        -- to reach index 11, we have to first reach (try best to jump forward)
            -- index 0, 0+5=5, no
            -- index 1, 1+9=10, no
            -- index 2, 2+3=5, no
            -- index 3, 3+2=5, no
            -- index 4, 4+1=5, no
            -- index 5, 5+0=5, no
            -- index 6, 6+2=8, no
            -- index 7, 7+3=10, no
            -- index 8, 8+3=11, yes!
            thus we have to first reach index 8.
        -- to reach index 8, we have to first reach (try best to jump forward)
            -- index 0, 0+5=5, no
            -- index 1, 1+9=10, yes
            thus we have to first reach index 1.
        -- to reach index 1, we have to first reach (try best to jump forward)
            -- index 0, 0+5=5, yes
            thus we have to first reach index 0.

        therefore, 3 steps in total.

    one issue i thought about.
        -- when scanning from left to right to search for the "viable" index, we take the first "viable" index.
           what if this first "viable" index is not reachable?

           for example:
           index  0  1  2  3  4  5  6  7  8  9  10  11
           value  1  6  5  4  3  2  1  3  3  1  1   0

           scanned from left to right, the first "viable" index is 8, the second "viable" index is 10.
           what if we cannot reach index 8 but we can reach index 10?
                -- silly question, lol
           will it take more steps to choose index 8 than 10?
                -- 8-->11 and 10-->11 both take 1 step
                -- will it take more steps to reach index 8 than 10?
                    -- the answer is **NO**.
                       if reaching index 10 takes **n** steps, we can definitely reach index 8 in **<=n** steps.

           therefore we have no problem to choose the first "viable" index.
           such is the correctness of the algorithm.
"""