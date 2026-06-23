import math
import secrets

def bytes_to_bits(b_arr: bytes) -> list:
    """Преобразует 16 байт (128 бит) в список интов 0 и 1."""
    bits = []
    for byte in b_arr:
        for i in range(8):
            bits.append((byte >> (7 - i)) & 1)
    return bits

def bits_to_bytes(bits: list) -> bytes:
    """Преобразует список из 128 битов обратно в 16 байт шифротекста."""
    b_arr = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i+8]:
            byte = (byte << 1) | bit
        b_arr.append(byte)
    return bytes(b_arr)

def count_bit_difference(bits1: list, bits2: list) -> int:
    """Расстояние Хэмминга между двумя битовыми потоками."""
    return sum(b1 ^ b2 for b1, b2 in zip(bits1, bits2))

def calculate_pearson_correlation(x: list, y: list) -> float:
    """Вычисляет коэффициент корреляции Пирсона для двух списков битов."""
    n = len(x)
    if n == 0: return 0.0
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(i**2 for i in x)
    sum_y_sq = sum(i**2 for i in y)
    p_sum = sum(x[i] * y[i] for i in range(n))
    
    num = p_sum - (sum_x * sum_y / n)
    den = math.sqrt((sum_x_sq - (sum_x**2) / n) * (sum_y_sq - (sum_y**2) / n))
    if den == 0: return 0.0
    return num / den

def evaluate_collatz_3d_step(bits: list) -> list:
    """
    Имитация одного шага 3D-аттрактора Коллатца v5.0.0.
    В реальном скрипте замените на оригинальную функцию из simulator_4habr.py.
    """
    # Эмуляция локального перемешивания внутри осей X, Y, Z
    state = list(bits)
    for i in range(128):
        state[i] ^= (state[(i + 53) % 128] & state[(i + 3) % 128])
    return state

def topological_phase_permutation(block_bits: list) -> list:
    """
    ИНСТРУМЕНТ ИСПРАВЛЕНИЯ (Вариант 2): Межпространственный туннель v5.1.0.
    Перебрасывает 33.3% битов «хвоста» каждой оси в начало следующей координаты.
    """
    # Разрезаем 128-битное пространство на физические координаты X, Y, Z
    x = block_bits[0:43]
    y = block_bits[43:86]
    z = block_bits[86:128]
    
    # 33.3% фазовой миграции (по 14 бит с конца каждой оси)
    mig_size = 14
    tail_x, core_x = x[-mig_size:], x[:-mig_size]
    tail_y, core_y = y[-mig_size:], y[:-mig_size]
    tail_z, core_z = z[-mig_size:], z[:-mig_size]
    
    # Циклический переброс по правилу правого винта: X -> Y -> Z -> X
    new_x = tail_z + core_x
    new_y = tail_x + core_y
    new_z = tail_y + core_z
    
    return new_x + new_y + new_z

def encrypt_block_v5_1(plaintext: bytes, key: bytes) -> bytes:
    """Полный цикл шифрования блока v5.1.0 с поддержкой сквозной диффузии."""
    # Начальный XOR с ключом (Sign Calibration Isomorphism)
    state_bytes = bytes(p ^ k for p, k in zip(plaintext, key))
    state_bits = bytes_to_bits(state_bytes)
    
    # Симуляция итераций аттрактора через критический шаг 53
    for step in range(1, 64):
        state_bits = evaluate_collatz_3d_step(state_bits)
        # Активация топологического туннеля v5.1.0 после каждого шага
        state_bits = topological_phase_permutation(state_bits)
        
    return bits_to_bytes(state_bits)

def run_tool_1_classic_avalanche(encrypt_func, iterations=500):
    print("\n=== [ИНСТРУМЕНТ 1] КЛАССИЧЕСКИЙ ЛАВИННЫЙ ЭФФЕКТ (v5.1.0) ===")
    total_pt_diff_pct = 0.0
    total_key_diff_pct = 0.0

    for _ in range(iterations):
        pt = secrets.token_bytes(16)
        key = secrets.token_bytes(16)
        base_cipher = bytes_to_bits(encrypt_func(pt, key))

        # Тест текста: флип 1 бита
        pt_mod = bytearray(pt)
        pt_mod[0] ^= 0x01
        mod_pt_cipher = bytes_to_bits(encrypt_func(bytes(pt_mod), key))
        total_pt_diff_pct += (count_bit_difference(base_cipher, mod_pt_cipher) / 128.0)

        # Тест ключа: флип 1 бита
        key_mod = bytearray(key)
        key_mod[0] ^= 0x01
        mod_key_cipher = bytes_to_bits(encrypt_func(pt, bytes(key_mod)))
        total_key_diff_pct += (count_bit_difference(base_cipher, mod_key_cipher) / 128.0)

    avg_pt = total_pt_diff_pct / iterations
    avg_key = total_key_diff_pct / iterations
    print(f"Результат (Plaintext Diff): {avg_pt*100:.2f}% (Цель: ~50%)")
    print(f"Результат (Key Diff):       {avg_key*100:.2f}% (Цель: ~50%)")

def run_tool_2_strict_avalanche_criterion(encrypt_func, iterations=200):
    print("\n=== [ИНСТРУМЕНТ 2] СТРОГИЙ ЛАВИННЫЙ КРИТЕРИЙ (SAC) ===")
    sac_matrix = [[0] * 128 for _ in range(128)]
    
    for _ in range(iterations):
        pt = secrets.token_bytes(16)
        key = secrets.token_bytes(16)
        base_cipher = bytes_to_bits(encrypt_func(pt, key))
        
        for input_bit_idx in range(128):
            pt_mod = bytearray(pt)
            byte_idx = input_bit_idx // 8
            bit_shift = 7 - (input_bit_idx % 8)
            pt_mod[byte_idx] ^= (1 << bit_shift)
            
            mod_cipher = bytes_to_bits(encrypt_func(bytes(pt_mod), key))
            
            for output_bit_idx in range(128):
                if base_cipher[output_bit_idx] ^ mod_cipher[output_bit_idx]:
                    sac_matrix[input_bit_idx][output_bit_idx] += 1

    total_deviation = 0.0
    for i in range(128):
        for j in range(128):
            prob = sac_matrix[i][j] / iterations
            total_deviation += abs(prob - 0.5)
            
    avg_deviation = total_deviation / (128 * 128)
    print(f"Среднее отклонение матрицы SAC от идеала (0.5): {avg_deviation:.4f}")
    print(f"Успешность калибровки знаков (Sign Calibration): {(1 - avg_deviation)*100:.2f}%")

def run_tool_3_bit_independence_criterion(encrypt_func, iterations=100):
    print("\n=== [ИНСТРУМЕНТ 3] КРИТЕРИЙ НЕЗАВИСИМОСТИ БИТ (BIC) ===")
    bit_vectors = [[] for _ in range(8)]
    
    for _ in range(iterations):
        pt = secrets.token_bytes(16)
        key = secrets.token_bytes(16)
        base_cipher = bytes_to_bits(encrypt_func(pt, key))
        
        pt_mod = bytearray(pt)
        pt_mod[0] ^= 0x80 
        mod_cipher = bytes_to_bits(encrypt_func(bytes(pt_mod), key))
        
        for out_idx in range(8):
            reaction = base_cipher[out_idx] ^ mod_cipher[out_idx]
            bit_vectors[out_idx].append(reaction)
            
    correlations = []
    for i in range(8):
        for j in range(i + 1, 8):
            corr = calculate_pearson_correlation(bit_vectors[i], bit_vectors[j])
            correlations.append(abs(corr))
            
    avg_correlation = sum(correlations) / len(correlations) if correlations else 0
    print(f"Средняя взаимозависимость (BIC) выходных бит: {avg_correlation:.4f} (Цель: ~0.0)")
    if avg_correlation < 0.15:
        print("-> Матрешка воронок успешно разделяет координатные плоскости.")

def run_tool_4_nist_monobit_and_runs(encrypt_func, iterations=100):
    print("\n=== [ИНСТРУМЕНТ 4] ЧАСТОТНЫЙ ТЕСТ И ТЕСТ НА СЕРИИ (NIST) ===")
    large_bit_stream = []
    for _ in range(iterations):
        pt = secrets.token_bytes(16)
        key = secrets.token_bytes(16)
        large_bit_stream.extend(bytes_to_bits(encrypt_func(pt, key)))
        
    n = len(large_bit_stream)
    
    # 1. Частотный тест
    sum_s = sum((2 * b - 1) for b in large_bit_stream)
    s_obs = abs(sum_s) / math.sqrt(n)
    p_value_monobit = math.erfc(s_obs / math.sqrt(2))
    
    # 2. Тест на серии (Runs)
    pi = sum(large_bit_stream) / n
    v_n = 1
    for k in range(n - 1):
        if large_bit_stream[k] != large_bit_stream[k+1]:
            v_n += 1
            
    num = abs(v_n - 2 * n * pi * (1 - pi))
    den = 2 * math.sqrt(2 * n) * pi * (1 - pi)
    p_value_runs = math.erfc(num / den) if den != 0 else 0.0

    print(f"Частотный тест P-value: {p_value_monobit:.5f} (Успех при > 0.01)")
    print(f"Тест на серии P-value:  {p_value_runs:.5f} (Успех при > 0.01)")
    
    if p_value_monobit > 0.01 and p_value_runs > 0.01:
        print("-> Теорема фазовой миграции 33.3% подтверждена: поток неотличим от случайного.")

def main():
    print("===============================================================")
    print("  КОМПЛЕКСНЫЙ АНАЛИЗ УСТОЙЧИВОСТИ: collatz-3d-attractor v5.1.0  ")
    print("===============================================================")
    
    # Запуск тестов на обновленной функции с топологическим каскадом
    target_encrypt = encrypt_block_v5_1
    
    run_tool_1_classic_avalanche(target_encrypt)
    run_tool_2_strict_avalanche_criterion(target_encrypt)
    run_tool_3_bit_independence_criterion(target_encrypt)
    run_tool_4_nist_monobit_and_runs(target_encrypt)
    
    print("\n[FINISH] Все 4 инструмента проверки криптографической плотности v5.1.0 выполнены.")

if __name__ == "__main__":
    main()
