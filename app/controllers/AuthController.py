import hashlib, string, random


class AuthController:

    def encrypt(self, password):
        salt = "".join(random.sample(string.ascii_letters, 32))
        new_password = password + salt
        return hashlib.md5(new_password.encode()).hexdigest(), salt
