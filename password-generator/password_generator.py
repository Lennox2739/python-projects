import random
import string

class PasswordGenerator:
    def __init__(self):
        self.history = []
    
    def generate(self, length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
        """Generate a secure password."""
        characters = ""
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        
        if not characters:
            return None
        
        password = ''.join(random.choice(characters) for _ in range(length))
        self.history.append(password)
        return password

if __name__ == "__main__":
    generator = PasswordGenerator()
    password = generator.generate()
    print(f"Generated password: {password}")
