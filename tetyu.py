# Création d'un dictionnaire de correspondance pour notre langue inventée
mapping = {
    'a': 'z', 'b': 'x', 'c': 'v', 'd': 't', 'e': 'r',
    'f': 'p', 'g': 'n', 'h': 'l', 'i': 'j', 'j': 'h',
    'k': 'f', 'l': 'd', 'm': 'b', 'n': 'y', 'o': 'w',
    'p': 'u', 'q': 's', 'r': 'q', 's': 'o', 't': 'm',
    'u': 'k', 'v': 'i', 'w': 'g', 'x': 'e', 'y': 'c',
    'z': 'a'
}

def encrypt(message):
    """
    Fonction pour crypter un message
    """
    encrypted_message = ''
    for char in message.lower():
        if char in mapping:
            encrypted_message += mapping[char]
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message):
    """
    Fonction pour décrypter un message
    """
    decrypted_message = ''
    for char in encrypted_message.lower():
        if char in mapping.values():
            for key, value in mapping.items():
                if value == char:
                    decrypted_message += key
                    break
        else:
            decrypted_message += char
    return decrypted_message

def main():
    print("Bienvenue dans le programme de cryptage/décryptage de messages dans la langue tetyu !")
    choice = input("Voulez-vous crypter (1) ou décrypter (2) un message? ")

    if choice == '1':
        message = input("Entrez le message à crypter: ")
        encrypted_message = encrypt(message)
        print("Le message crypté est:", encrypted_message)
    elif choice == '2':
        encrypted_message = input("Entrez le message à décrypter: ")
        decrypted_message = decrypt(encrypted_message)
        print("Le message décrypté est:", decrypted_message)
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")

if __name__ == "__main__":
    main()

print("Dev by Paul5225")
