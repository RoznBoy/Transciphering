def mix_columns(state):
    for i in range(4):
        s0 = state[0][i]
        s1 = state[1][i]
        s2 = state[2][i]
        s3 = state[3][i]

        state[0][i] = gf_mul8(s0, 0x02) ^ gf_mul8(s1, 0x03) ^ s2 ^ s3
        state[1][i] = s0 ^ gf_mul8(s1, 0x02) ^ gf_mul8(s2, 0x03) ^ s3
        state[2][i] = s0 ^ s1 ^ gf_mul8(s2, 0x02) ^ gf_mul8(s3, 0x03)
        state[3][i] = gf_mul8(s0, 0x03) ^ s1 ^ s2 ^ gf_mul8(s3, 0x02)

    return state

def gf_mul8(a, b):
    result = 0
    while b: # b가 0이 아닌 동안에만 반복
        print('b',hex(b))
        if b & 1: # b의 최하위 비트가 1인 경우에만 실행
            result ^= a
            print('res', hex(result))
        print('befor shift', hex(a))
        a <<= 1
        print('after shift', hex(a))
        if a & 0x100: # a의 최상위 비트가 1인 경우
            a ^= 0x11B # AES에서 사용하는 다항식 x^8 + x^4 + x^3 + x + 1과 XOR 연산, 제일 앞에 1이 생기는거 방지 하기 위해 1 추가
            print('최상위 비트 확인', hex(a))
        b >>= 1
    return result

def print_state(state):
    for row in state:
        print([hex(byte) for byte in row])

# 테스트
plaintext = b"HelloAES12345678" #문자열 리터럴 앞에 b를 붙이면 해당 문자열이 바이트 문자열
key = b"secretkey1234567"
state = [[plaintext[i + 4 * j] for i in range(4)] for j in range(4)]
print("Original State:")
print_state(state)

# MixColumns 적용
state = mix_columns(state)

print("\nState after MixColumns:")
print_state(state)

print('============= mult test =============')
a = 0x1a  # 10110111
b1 = 0x0b  # 00000011
b2 = 0x02  # 00000010
result1 = gf_mul8(a, b1)
print('===============')
result2 = gf_mul8(a, b2)
print('===============')
print('a :', hex(a))
print('b1 :', hex(b1))
print('b2 :', hex(b2))
print("Multiplication Result:", hex(result1))
print("Multiplication Result:", hex(result2))

def gf_mul8(a, b):
    result = 0
    while b: # b가 0이 아닌 동안에만 반복
        if b & 1: # b의 최하위 비트가 1인 경우에만 실행
            result ^= a
        a <<= 1 # a를 왼쪽으로 1비트씩 시프트
        if a & 0x100: # a의 최상위 비트가 1인 경우
            a ^= 0x11b # AES에서 사용하는 기약 다항식과 XOR 연산
        b >>= 1 # b를 오른쪽으로 1비트씩 시프트
    return result

# 예제: 갈루아 필드에서의 곱셈 연산을 테스트합니다.
a = 0xb7  # 입력 숫자 a
b = 0x02  # 입력 숫자 b
result = gf_mul8(a, b)  # gf_mul8 함수를 사용하여 두 숫자의 곱셈을 계산합니다.
print("Multiplication Result:", hex(result))  # 곱셈 결과를 출력합니다.
