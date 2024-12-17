"""
2,4 ; bst 4 ; reg[B] = reg[A] % 8    -- take bottom 3 bits
1,2 ; bxl 2 ; reg[B] ^= 2            -- xor it with 2
7,5 ; cdv 5 ; reg[C] = reg[A] // 2^reg[B] -- at most you care about up to 7 bits back
4,3 ; bcx - ; reg[B] ^= reg[C]       -- xor bottom 3 bits
0,3 ; adv 3 ; reg[A] = reg[A] // 2^3 -- drop bottom 3 bits
1,7 ; bxl 7 ; reg[B] ^= 7            -- flip everything
5,5 ; out 5 ; print reg[B] % 8       -- take bottom 3 bits
3,0 ; jnz 0 ; GOTO 0 if nonzero A

0o6554636017
7^2 = 4
c = 0o6554636017 // 2**4

0 = 7 ^ reg[B]
0 = 7 ^ reg[B] ^ reg[C]
0 = 7 ^ reg[B] ^ (reg[A] >> reg[B])
0 = 7 ^ reg[B] ^ (reg[A] >> reg[B])

0 = 7 ^ (reg[A]&7^2) ^ (reg[A] >> (reg[A]&7^2))
0 = 7 ^ (reg[A]&7^2) ^ (reg[A] >> (reg[A]&7^2))

reg[B] = 
"""

# A consists of chunks of 8
code = [2,4,1,2,7,5,4,3,0,3,1,7,5,5,3,0]
reg = []