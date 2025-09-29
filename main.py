def check_password(password: str):
    with open('passwords.text', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()
        print(common_passwords)

def main():
    check_password('abc123')

if __name__ == '__main__':
    main()