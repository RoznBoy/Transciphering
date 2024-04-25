from itertools import combinations

def SBOX_coeff(Sbox):
    coefficient = []
    coefficient.append(Sbox[0])
    # print(len(coefficient), coefficient)
    # print('================= combination =================')
    ind = 1
    # 주어진 범위
    numbers = range(1, 9)

    # 1개씩 combination 생성
    flag1 = ind
    # print('check flag : ', flag1)
    combinations_list1 = list(combinations(numbers, 1))
    for combination in combinations_list1:
        # # print(combination)
        new = 2**(combination[0]-1)
        # print(new, hex(Sbox[new]), Sbox[new], coefficient[0])

        coefficient.append(Sbox[new]-coefficient[0])
        ind += 1
        # # print()
    # print(len(coefficient), coefficient)
    # print('set index :', ind)
    # print('================= combination =================')
    # 2개씩 combination 생성
    flag2 = ind
    # print('check flag : ', flag2)
    combinations_list2 = list(combinations(numbers, 2))
    for combination in combinations_list2:
        # # print(combination)
        new = 2**(combination[0]-1)+2**(combination[1]-1)
        # # print(new, hex(Sbox[new]), Sbox[new], coefficient[combination[0]], coefficient[combination[1]], coefficient[0])
        one = coefficient[combination[0]]+coefficient[combination[1]]
        # # print('res : ', Sbox[new]-(one+coefficient[0]))
        coefficient.append(Sbox[new]-(one+coefficient[0]))
        ind += 1
        # # print()
    # print(len(coefficient), coefficient)
    # print('set index :', ind)
    # print('================= combination =================')
    # 3개씩 combination 생성
    flag3 = ind
    # print('check flag : ', flag3)
    combinations_list3 = list(combinations(numbers, 3))
    for combination in combinations_list3:
        # # print(combination)
        new = 2**(combination[0]-1)+2**(combination[1]-1)+2**(combination[2]-1)
        # # print(new, hex(Sbox[new]), Sbox[new], coefficient[combination[0]], coefficient[combination[1]], coefficient[combination[2]], coefficient[0])
        one = coefficient[combination[0]]+coefficient[combination[1]]+coefficient[combination[2]]
        # # print('one :', one)
        sub_comb2 = list(combinations(combination, 2)) # check 2 combination
        two = 0
        for subComb in sub_comb2:
            # # print(subComb)
            comb_ind = combinations_list2.index(subComb)
            # # print('comb_ind :', comb_ind)
            comb_ind += flag2
            # # print('comb_ind+flag :', comb_ind)
            two += coefficient[comb_ind]
            # # print('two : ', two)

        # # print('res : ', Sbox[new]-(one+two+coefficient[0]))
        # # print()
        coefficient.append(Sbox[new]-(one+two+coefficient[0]))
        ind += 1
        # # print()
    # print(len(coefficient), coefficient)
    # print('set index :', ind)
    # print()
    # print('================= combination =================')
    # 4개씩 combination 생성
    flag4 = ind
    # print('check flag : ', flag4)
    combinations_list4 = list(combinations(numbers, 4))
    for combination in combinations_list4:
        # print(combination)
        new = 2**(combination[0]-1)+2**(combination[1]-1)+2**(combination[2]-1)+2**(combination[3]-1)
        # # print(new, hex(Sbox[new]), Sbox[new+1], coefficient[combination[0]], coefficient[combination[1]], coefficient[combination[2]], coefficient[combination[3]], coefficient[0])
        one = coefficient[combination[0]]+coefficient[combination[1]]+coefficient[combination[2]]+coefficient[combination[3]]
        # print('one :', one)
        # print()
        sub_comb2 = list(combinations(combination, 2)) # check 2 combination
        two = 0
        for subComb in sub_comb2:
            # print(subComb)
            comb_ind = combinations_list2.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag2
            # print('comb_ind+flag :', comb_ind)
            two += coefficient[comb_ind]
            # print('two : ', two)
        # print()
        sub_comb3 = list(combinations(combination, 3)) # check 3 combination
        three = 0
        for subComb in sub_comb3:
            # print(subComb)
            comb_ind = combinations_list3.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag3
            # print('comb_ind+flag :', comb_ind)
            three += coefficient[comb_ind]
            # print('three : ', three)

        # print()
        # print('res : ', Sbox[new]-(one+two+three+coefficient[0]))
        # print()
        coefficient.append(Sbox[new]-(one+two+three+coefficient[0]))
        ind += 1
        # # print()
    # print(len(coefficient), coefficient)
    # print('set index :', ind)
    # print()
    # print('================= combination =================')
    # 5개씩 combination 생성
    flag5 = ind
    # print('check flag : ', flag5)
    combinations_list5 = list(combinations(numbers, 5))
    for combination in combinations_list5:
        # print(combination)
        new = 2**(combination[0]-1)+2**(combination[1]-1)+2**(combination[2]-1)+2**(combination[3]-1)+2**(combination[4]-1)
        # print(new, hex(Sbox[new]), Sbox[new+1], coefficient[combination[0]], coefficient[combination[1]], coefficient[combination[2]], coefficient[combination[3]], coefficient[0])
        one = coefficient[combination[0]]+coefficient[combination[1]]+coefficient[combination[2]]+coefficient[combination[3]]+coefficient[combination[4]]
        # print('one :', one)
        # print()
        sub_comb2 = list(combinations(combination, 2)) # check 2 combination
        two = 0
        for subComb in sub_comb2:
            # print(subComb)
            comb_ind = combinations_list2.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag2
            # print('comb_ind+flag :', comb_ind)
            two += coefficient[comb_ind]
            # print('two : ', two)
        # print()
        sub_comb3 = list(combinations(combination, 3)) # check 3 combination
        three = 0
        for subComb in sub_comb3:
            # print(subComb)
            comb_ind = combinations_list3.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag3
            # print('comb_ind+flag :', comb_ind)
            three += coefficient[comb_ind]
            # print('three : ', three)
        # print()
        sub_comb4 = list(combinations(combination, 4)) # check 4 combination
        four = 0
        for subComb in sub_comb4:
            # print(subComb)
            comb_ind = combinations_list4.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag4
            # print('comb_ind+flag :', comb_ind)
            four += coefficient[comb_ind]
            # print('four : ', four)
            
        # print()
        # print('res : ', Sbox[new]-(one+two+three+four+coefficient[0]))
        # print()
        coefficient.append(Sbox[new]-(one+two+three+four+coefficient[0]))
        ind += 1
        # # print()
    # print(len(coefficient), coefficient)
    # print('set index :', ind)
    # print('================= combination =================')
    # 6개씩 combination 생성
    flag6 = ind
    # print('check flag : ', flag6)
    combinations_list6 = list(combinations(numbers, 6))
    for combination in combinations_list6:
        # print(combination)
        new = 2**(combination[0]-1)+2**(combination[1]-1)+2**(combination[2]-1)+2**(combination[3]-1)+2**(combination[4]-1)+2**(combination[5]-1)
        # print(new, hex(Sbox[new]), Sbox[new+1], coefficient[combination[0]], coefficient[combination[1]], coefficient[combination[2]], coefficient[combination[3]], coefficient[0])
        one = coefficient[combination[0]]+coefficient[combination[1]]+coefficient[combination[2]]+coefficient[combination[3]]+coefficient[combination[4]]+coefficient[combination[5]]
        # print('one :', one)
        # print()
        sub_comb2 = list(combinations(combination, 2)) # check 2 combination
        two = 0
        for subComb in sub_comb2:
            # print(subComb)
            comb_ind = combinations_list2.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag2
            # print('comb_ind+flag :', comb_ind)
            two += coefficient[comb_ind]
            # print('two : ', two)
        # print()
        sub_comb3 = list(combinations(combination, 3)) # check 3 combination
        three = 0
        for subComb in sub_comb3:
            # print(subComb)
            comb_ind = combinations_list3.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag3
            # print('comb_ind+flag :', comb_ind)
            three += coefficient[comb_ind]
            # print('three : ', three)
        # print()
        sub_comb4 = list(combinations(combination, 4)) # check 4 combination
        four = 0
        for subComb in sub_comb4:
            # print(subComb)
            comb_ind = combinations_list4.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag4
            # print('comb_ind+flag :', comb_ind)
            four += coefficient[comb_ind]
            # print('four : ', four)
        # print()
        sub_comb5 = list(combinations(combination, 5)) # check 5 combination
        five = 0
        for subComb in sub_comb5:
            # print(subComb)
            comb_ind = combinations_list5.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag5
            # print('comb_ind+flag :', comb_ind)
            five += coefficient[comb_ind]
            # print('five : ', five)

        # print()
        # print('res : ', Sbox[new]-(one+two+three+four+five+coefficient[0]))
        # print()
        coefficient.append(Sbox[new]-(one+two+three+four+five+coefficient[0]))
        ind += 1
        # # print()
    # print(len(coefficient), coefficient)
    # print('set index :', ind)
    # print()
    # print('================= combination =================')
    # 7개씩 combination 생성
    flag7 = ind
    # print('check flag : ', flag7)
    combinations_list7 = list(combinations(numbers, 7))
    for combination in combinations_list7:
        # print(combination)
        new = 2**(combination[0]-1)+2**(combination[1]-1)+2**(combination[2]-1)+2**(combination[3]-1)+2**(combination[4]-1)+2**(combination[5]-1)+2**(combination[6]-1)
        # print(new, Sbox[new+1], coefficient[combination[0]], coefficient[combination[1]], coefficient[combination[2]], coefficient[combination[3]], coefficient[0])
        one = coefficient[combination[0]]+coefficient[combination[1]]+coefficient[combination[2]]+coefficient[combination[3]]+coefficient[combination[4]]+coefficient[combination[5]]+coefficient[combination[6]]
        # print('one :', one)
        # print()
        sub_comb2 = list(combinations(combination, 2)) # check 2 combination
        two = 0
        for subComb in sub_comb2:
            # print(subComb)
            comb_ind = combinations_list2.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag2
            # print('comb_ind+flag :', comb_ind)
            two += coefficient[comb_ind]
            # print('two : ', two)
        # print()
        sub_comb3 = list(combinations(combination, 3)) # check 3 combination
        three = 0
        for subComb in sub_comb3:
            # print(subComb)
            comb_ind = combinations_list3.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag3
            # print('comb_ind+flag :', comb_ind)
            three += coefficient[comb_ind]
            # print('three : ', three)
        # print()
        sub_comb4 = list(combinations(combination, 4)) # check 4 combination
        four = 0
        for subComb in sub_comb4:
            # print(subComb)
            comb_ind = combinations_list4.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag4
            # print('comb_ind+flag :', comb_ind)
            four += coefficient[comb_ind]
            # print('four : ', four)
        # print()
        sub_comb5 = list(combinations(combination, 5)) # check 5 combination
        five = 0
        for subComb in sub_comb5:
            # print(subComb)
            comb_ind = combinations_list5.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag5
            # print('comb_ind+flag :', comb_ind)
            five += coefficient[comb_ind]
            # print('five : ', five)
        # print()
        sub_comb6 = list(combinations(combination, 6)) # check 6 combination
        six = 0
        for subComb in sub_comb6:
            # print(subComb)
            comb_ind = combinations_list6.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag6
            # print('comb_ind+flag :', comb_ind)
            six += coefficient[comb_ind]
            # print('six : ', six)

        # print()
        # print('res : ', Sbox[new]-(one+two+three+four+five+six+coefficient[0]))
        # print()
        coefficient.append(Sbox[new]-(one+two+three+four+five+six+coefficient[0]))
        ind += 1
        # # print()
    # print(len(coefficient), coefficient)
    # print('set index :', ind) 
    # print()
    # print('================= combination =================')
    # 8개씩 combination 생성
    combinations_list8 = list(combinations(numbers, 8))
    for combination in combinations_list8:
        # # print(combination)
        # # print(combination[0], combination[1], combination[2], combination[3], combination[4], combination[5], combination[6], combination[7])
        new = 2**(combination[0]-1)+2**(combination[1]-1)+2**(combination[2]-1)+2**(combination[3]-1)+2**(combination[4]-1)+2**(combination[5]-1)+2**(combination[6]-1)+2**(combination[7]-1)
        # # print(new)
        # # print(Sbox[new])
        # # print(coefficient[combination[0]], coefficient[combination[1]], coefficient[combination[2]], coefficient[combination[3]], coefficient[4], coefficient[5], coefficient[6], coefficient[7])
        one = coefficient[combination[0]]+coefficient[combination[1]]+coefficient[combination[2]]+coefficient[combination[3]]+coefficient[combination[4]]+coefficient[combination[5]]+coefficient[combination[6]]+coefficient[combination[7]]
        # print('one :', one)
        # print()
        sub_comb2 = list(combinations(combination, 2)) # check 2 combination
        two = 0
        for subComb in sub_comb2:
            # print(subComb)
            comb_ind = combinations_list2.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag2
            # print('comb_ind+flag :', comb_ind)
            two += coefficient[comb_ind]
            # print('two : ', two)
        # print()
        sub_comb3 = list(combinations(combination, 3)) # check 3 combination
        three = 0
        for subComb in sub_comb3:
            # print(subComb)
            comb_ind = combinations_list3.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag3
            # print('comb_ind+flag :', comb_ind)
            three += coefficient[comb_ind]
            # print('three : ', three)
        # print()
        sub_comb4 = list(combinations(combination, 4)) # check 4 combination
        four = 0
        for subComb in sub_comb4:
            # print(subComb)
            comb_ind = combinations_list4.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag4
            # print('comb_ind+flag :', comb_ind)
            four += coefficient[comb_ind]
            # print('four : ', four)
        # print()
        sub_comb5 = list(combinations(combination, 5)) # check 5 combination
        five = 0
        for subComb in sub_comb5:
            # print(subComb)
            comb_ind = combinations_list5.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag5
            # print('comb_ind+flag :', comb_ind)
            five += coefficient[comb_ind]
            # print('five : ', five)
        # print()
        sub_comb6 = list(combinations(combination, 6)) # check 6 combination
        six = 0
        for subComb in sub_comb6:
            # print(subComb)
            comb_ind = combinations_list6.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag6
            # print('comb_ind+flag :', comb_ind)
            six += coefficient[comb_ind]
            # print('six : ', six)
        # print()
        sub_comb7 = list(combinations(combination, 7)) # check 7 combination
        seven = 0
        for subComb in sub_comb7:
            # print(subComb)
            comb_ind = combinations_list7.index(subComb)
            # print('comb_ind :', comb_ind)
            comb_ind += flag7
            # print('comb_ind+flag :', comb_ind)
            seven += coefficient[comb_ind]
            # print('seven : ', seven)

        # print()
        # print('res : ', Sbox[new]-(one+two+three+four+five+six+seven+coefficient[0]))
        # print()
        coefficient.append(Sbox[new]-(one+two+three+four+five+six+seven+coefficient[0]))
        ind += 1
        # # print()
    # print(len(coefficient), coefficient)
    # print('set index :', ind)
    return coefficient
    
# Rijndael S-Box
#        0     1     2     3     4     5     6     7     8     9     a     b     c     d     e     f
s_box = [
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
    ]

s_box_inverse = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]


# print('========================')
# 주어진 값
#### value 순서 : x0 x1 x2 x3 x4 x5 x6 x7 -> 잘 확인해야한다 ###
values = [0, 0, 1, 0, 0, 1, 0, 0]

# 가능한 모든 조합을 생성하여 값을 만듦
combined_values = [1]
for r in range(1, len(values) + 1):
    for combo in combinations(values, r):
        # # print(combo)
        product = 1
        for element in combo:
            # # print(element)
            if isinstance(element, int):
                product *= element
        combined_values.append(product)
    # print(combined_values)

########################################################
###################### 결과 출력 #########################
########################################################

# print(len(combined_values))
# print('combuned value :', combined_values)
coeff = SBOX_coeff(s_box)
print('coefficient list :', coeff)
result = 0
for i in range(len(coeff)):
    res = coeff[i]*combined_values[i]
    # if res != 0:
        # print(res)
    result += res
print('final SBOX result : ', result, hex(result))

'''

# 기약 다항식을 사용하여 정수를 Galois Field GF(2^8)의 값으로 변환하는 함수
def int_to_gf256(element):

    # 기약 다항식을 활용하여 나머지 연산을 구해주는 과정 구현
    
    primitive = 0x11b
    primitive = format(primitive, 'b')
    # print('primitive', primitive, type(primitive), len(primitive))

    # 주어진 정수를 이진수로 표현
    binary_str = format(element, 'b')
    # print('input', binary_str, type(binary_str), len(binary_str))

    # 이진수의 길이가 8보다 작으면 앞에 0을 채워서 8비트로 만듦
    if len(binary_str) < 8:
        binary_str = '0' * (8 - len(binary_str)) + binary_str

    # 8비트가 넘는 경우 모듈러 연산을 통해 값을 변환
    while len(binary_str) > 8:
        # print('primitive str length :', len(primitive))
        primitive_long = primitive.ljust(len(binary_str),'0')
        # print('zfill primitive', primitive_long, type(primitive_long), len(primitive_long))

        # XOR 연산 수행
        binary_str = int(binary_str,2) ^ int(primitive_long,2)
        binary_str = format(binary_str, 'b')
        # print('xor result', binary_str, type(binary_str))

    # 변환된 이진수를 정수로 반환
    return int(binary_str, 2)


# 예시: 300을 Galois Field GF(2^8)로 변환
element = 1686
gf_element = int_to_gf256(element)
print("Galois Field GF(2^8)에서의 값:", gf_element, hex(gf_element))


####### 첫번째 변환 : 양수든 음수든 연산 먼저 하고나서 기약 방정식 확용 #######
def to_gf256(coefficient):
    coeff_binary = []
    for i in range(len(coefficient)):
        # bin = format(coeff[i], 'b')
        # coeff_binary.append(bin)
        # coeff_binary.append(bin(coeff[i]))
        if coeff[i] > 0: # 양수 -> 기약 다항식 활용
            a = int_to_gf256(coefficient[i])
            a = format(a, '08b')
            coeff_binary.append(a)
        else: # 음수 -> 2의 보수로 변환 후 기약다항식
            # a = format(coeff[i], 'b')
            
            # 음의 정수를 양의 정수로 변환하여 이진수로 표현
            abs_num_binary = bin(abs(coefficient[i]))

            # 양의 정수를 2의 보수로 변환
            a = int(bin((int(abs_num_binary, 2) ^ 0b11111111) + 1),2)
            # a = int_to_gf256(a)
            a = format(a, '08b')
            coeff_binary.append(a)
    print('coefficient to binary : ', coeff_binary)
    return coeff_binary

coeff_binary = to_gf256(coeff)
# 각 element에서 1의 개수를 구하는 코드
count_list = [bin_str.count('1') for bin_str in coeff_binary]

print("각 element에서 1의 개수:", sum(count_list), count_list)

result = 0
for i in range(len(coeff_binary)):
    res = int(coeff_binary[i],2)*combined_values[i]
    # print(res)
    result += res
    if res != 0:
        print(res, coeff_binary[i])
result %= 256
print('final SBOX result : ', result, hex(result))

first = []
second = []
third = []
fourth = []
fifth = []
sixth = []
seventh = []
eighth = []
for i in range(len(coeff_binary)):
    first.append(int(coeff_binary[i][0]))
    second.append(int(coeff_binary[i][1]))
    third.append(int(coeff_binary[i][2]))
    fourth.append(int(coeff_binary[i][3]))
    fifth.append(int(coeff_binary[i][4]))
    sixth.append(int(coeff_binary[i][5]))
    seventh.append(int(coeff_binary[i][6]))
    eighth.append(int(coeff_binary[i][7]))

print('1st list : ',first.count(1),first)
print('2nd list : ',second.count(1),second)
print('3rd list : ',third.count(1),third)
print('4th list : ',fourth.count(1),fourth)
print('5th list : ',fifth.count(1),fifth)
print('6th list : ',sixth.count(1),sixth)
print('7th list : ',seventh.count(1),seventh)
print('8th list : ',eighth.count(1),eighth)
'''
