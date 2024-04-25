def add_round_key(state, round_key):
    """
    AddRoundKey transformation in AES.
    """
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i][j]
            
    # output state는 10진수로 출력 됨
    return state

def print_state(state):
    """
    Helper function to print the state matrix.
    """
    for row in state:
        print([hex(byte) for byte in row])
    print()

# 테스트
plaintext = b"HelloAES12345678" #문자열 리터럴 앞에 b를 붙이면 해당 문자열이 바이트 문자열
key = b"secretkey1234567"

state = [[plaintext[i + 4 * j] for i in range(4)] for j in range(4)]
round_key = [[key[i + 4 * j] for i in range(4)] for j in range(4)]

print("Original State:")
print_state(state)

print("\nRound Key:")
print_state(round_key)

# AddRoundKey 적용
state = add_round_key(state, round_key)

print(state)

print("\nState after AddRoundKey:")
print_state(state)
print(state)
