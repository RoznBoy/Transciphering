import basicFunction as aes

def encrypt(plaintext, key):
    state = [[plaintext[i + 4 * j] for i in range(4)] for j in range(4)]
    
    # Number of words in the key
    words = len(key) // 4
    print('number of words :', words)
    
    # Number of rounds based on key size
    if words == 4:
        rounds = 10
    elif words == 6:
        rounds = 12
    else:
        rounds = 14
    print('number of round : ', rounds)
    
    round_keys = aes.key_expansion(key, words, rounds)
    print(0,words)
    aes.add_round_key(state, round_keys[0:words])

    for round_num in range(1, rounds):
        aes.substitute_bytes(state)
        aes.shift_rows(state)
        aes.mix_columns(state)
        print(round_num*words,(round_num+1)*words)
        aes.add_round_key(state, round_keys[round_num*words:(round_num+1)*words])

    aes.substitute_bytes(state)
    aes.shift_rows(state)
    aes.add_round_key(state, round_keys[rounds*words:])

    # 암호문 생성
    ciphertext = [state[i][j] for j in range(4) for i in range(4)]
    return bytes(ciphertext)

# 테스트
if __name__ == "__main__":
    # NIST AES-128 test vector 1 (Ch. C.1, p. 35)
    plaintext = bytearray.fromhex('6bc1bee22e409f96e93d7e117393172a')
    key = bytearray.fromhex('2b7e151628aed2a6abf7158809cf4f3c')
    expected_ciphertext = bytearray.fromhex('3ad77bb40d7a3660a89ecaf32466ef97')
    ciphertext = encrypt(plaintext, key)
    print(ciphertext.hex())
    # recovered_plaintext = aes_decryption(ciphertext, key)

    assert (ciphertext == expected_ciphertext)
    # assert (recovered_plaintext == plaintext)
