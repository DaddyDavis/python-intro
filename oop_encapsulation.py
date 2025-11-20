import hashlib

class SecureHasher:
    """
    A class that securely generates hashes. 
    It encapsulates (protects) the sensitive internal hash object.
    """
    
    # The double underscore makes this property 'private' and protected
    def __init__(self, algorithm="sha256"):
        self.__hash_object = hashlib.new(algorithm)
        self.algorithm = algorithm
    
    # Public Method: The ONLY way to input data
    def update_data(self, data):
        """Forces users to input data through this control method."""
        if isinstance(data, str):
            data = data.encode('utf-8')
        print(f"[CONTROL]: Updating {self.algorithm} with new data...")
        self.__hash_object.update(data)
    
    # Public Method: The ONLY way to retrieve the final hash
    def get_final_hash(self):
        """Retrieves the final hash digest."""
        return self.__hash_object.hexdigest()

    # Public Method: For demonstration only
    def __cheat_print_private_data(self):
        print(f"\n[DANGER!]: Accessing protected data directly: {self.__hash_object}")


# --- APPLICATION LOGIC (Creating the Secure Tool) ---

print("--- SECURE PASSWORD HASH GENERATOR (SHA256) ---")

# 1. Create the Hasher Object
password_hasher = SecureHasher()

# 2. Get User Input
user_input = input("\nEnter a password to hash: ")

# 3. Use the public, safe method to input the data
password_hasher.update_data(user_input)

# 4. Try to break the encapsulation (This will fail!)
# try:
#     # This line attempts to access the protected data directly
#     print(f"Direct Access Attempt: {password_hasher.__hash_object}")
# except AttributeError as e:
#     print(f"\n[SECURITY FAIL]: ERROR! Attempt to access private data was blocked: {e}")

# 5. Use the public, safe method to retrieve the result
final_hash = password_hasher.get_final_hash()

print("\n--- REPORT ---")
print(f"Original Text: {user_input}")
print(f"Final Hash ({password_hasher.algorithm}): {final_hash}")

## 2. Run and Verify