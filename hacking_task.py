import zipfile

# final submission of hacking task



# Using this to extract the passwords into a list
with open('rockyou.txt', 'r') as f:
        file_contents = f.read()
        contents_list = file_contents.split('\n')

for i in contents_list:
    pswd = i
    try:
        with zipfile.ZipFile('enc.zip') as file:
            file.extractall(pwd = bytes(pswd, 'utf-8'))
        print(f'zipfile was extracted with password:{pswd}')
        break
    except zipfile.BadZipFile:
        print('zipfile provided was invalid or corruputed.')
    except RuntimeError as e:
        print(f'The following error has occurred: {e} ')
    except Exception as e:
        print(f"password {pswd} did not work({e})")
