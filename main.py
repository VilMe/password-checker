def check_password(password: str):
    with open('passwords.text', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f'{password}: ❌(#{i})')
            return
        
    print(f'{password}: ✅ (Unique), go ahead and use it, make my day!!')


def main():
    user_password: str = input('Enter a password: ')
    check_password(user_password)

if __name__ == '__main__':
    main()