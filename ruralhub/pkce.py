import random
import string
import base64
import hashlib

def generate_pkce_code():
    # Generate a random code_verifier
    code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))
    
    # Generate the code_challenge from the code_verifier
    code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')

    return code_verifier, code_challenge

if __name__ == "__main__":
    verifier, challenge = generate_pkce_code()
    print(f"Code Verifier: {verifier}")
    print(f"Code Challenge: {challenge}")
