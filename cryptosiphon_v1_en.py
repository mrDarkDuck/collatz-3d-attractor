import sys

# Remove Python's limit on integer string conversion for arbitrary-precision math
sys.set_int_max_str_digits(100000)

# Monolinguistic notification messages
MESSAGES = {
    "start": "1. Original plaintext: '{text}'\n",
    "cipher": "2. Ciphertext (Massive Z-coordinate of the attractor):\n{cipher}\n",
    "key_size": "3. Private trajectory key size (bits): {size}",
    "key_frag": "   Vacant space phase log fragment: {frag}...\n",
    "decrypt": "4. Mirror world decryption result: '{text}'",
    "err_decrypt": "[Decryption Error: Topological Siphon Collapse]",
    "err_route": "[Siphon Collapse]: Fake or corrupted key trajectory detected!"
}


class TopologicalSiphonCipher:
    def __init__(self, steps=111):
        """
        Initialize the cipher. 
        steps = avalanche depth (111 steps = number 27 resonance configuration).
        """
        self.steps = steps

    def _text_to_int(self, text: str) -> int:
        """Convert plaintext string to a single massive bitwise passport"""
        encoded_bytes = text.encode('utf-8')
        return int.from_bytes(encoded_bytes, byteorder='big')

    def _int_to_text(self, number: int) -> str:
        """Convert bitwise passport back to plaintext string"""
        try:
            byte_length = (number.bit_length() + 7) // 8
            decoded_bytes = number.to_bytes(byte_length, byteorder='big')
            return decoded_bytes.decode('utf-8')
        except Exception:
            return MESSAGES["err_decrypt"]

    def encrypt(self, plain_text: str) -> dict:
        """
        Forward path (Avalanche wedge). 
        Encrypts text into a chaotic spatial coordinate using bitwise shifts.
        """
        n = self._text_to_int(plain_text)
        
        # Guarantee that the seed number is odd to force launch the avalanche
        padding_bit = 0
        if n % 2 == 0:
            n = (n << 1) + 1
            padding_bit = 1
            
        trajectory_log = []
        current = n
        
        # Process the number through the siphon to generate carry wave chaos
        for _ in range(self.steps):
            if current % 2 != 0:
                # Avalanche wedge: T(n) = (n << 1) + n + 1 (3n + 1 equivalent via shifts)
                current = (current << 1) + current + 1
                trajectory_log.append(1)  # Phase 1: Avalanche
            else:
                # Blue dive: structural division by 2
                current = current // 2
                trajectory_log.append(0)  # Phase 0: Dissipation
                
        return {
            "ciphertext": current,
            "private_key_path": trajectory_log,
            "padding_bit": padding_bit
        }

    def decrypt(self, cipher_data: dict) -> str:
        """
        Reverse path (Mirror operator). 
        Unwinds the spiral using the vacant phase trajectory map.
        """
        current = cipher_data["ciphertext"]
        path = cipher_data["private_key_path"]
        padding_bit = cipher_data["padding_bit"]
        
        # Unwind strictly backward from the edge of the inverse tree
        for phase in reversed(path):
            if phase == 0:
                # Reverse blue dive: restore parity by multiplying by 2
                current = current * 2
            else:
                # Reverse mirror avalanche wedge: (n - 1) / 3 with route integrity check
                if (current - 1) % 3 != 0:
                    raise ValueError(MESSAGES["err_route"])
                current = (current - 1) // 3
                
        # Remove padding bit if it was applied
        if padding_bit == 1:
            current = current >> 1
            
        return self._int_to_text(current)


# ==========================================
# PROTOTYPE VALIDATION RUN
# ==========================================
if __name__ == "__main__":
    # Test secret dataset (International verification payload)
    secret_data = "mrDarkDuck. collatz-3d-attractor v4.0.0. Sealed project verification."
    
    print(MESSAGES["start"].format(text=secret_data))
    
    # Initialize the Topological Siphon engine
    siphon = TopologicalSiphonCipher(steps=111)
    
    # Execute forward encryption path
    encrypted_packet = siphon.encrypt(secret_data)
    
    print(MESSAGES["cipher"].format(cipher=encrypted_packet['ciphertext']))
    print(MESSAGES["key_size"].format(size=len(encrypted_packet['private_key_path'])))
    print(MESSAGES["key_frag"].format(frag=encrypted_packet['private_key_path'][:20]))
    
    # Execute reverse mirror decryption path
    decrypted_data = siphon.decrypt(encrypted_packet)
    
    print(MESSAGES["decrypt"].format(text=decrypted_data))
