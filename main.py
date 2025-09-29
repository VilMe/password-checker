def check_password(password: str):
    with open('passwords.text', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()
        print(common_passwords)

    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f'{password}: ❌(#{i})')
            return
        
    print(f'{password}: ✅ (Unique), go ahead and use it, make my day!!')


def main():
    check_password('abc123')

if __name__ == '__main__':
    main()