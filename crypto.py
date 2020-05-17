import subprocess

def encrypt_symetric(key, filename):
    cmd = 'gpg --armor -o - --symmetric --passphrase "{}" --pinentry-mode loopback {}'.format(key, filename)
    return subprocess.check_output(cmd, shell=True)

def decrypt_symetric(key, stdin):
    cmd = 'gpg --armor -o - --passphrase "{}" --pinentry-mode loopback -'.format(key)
    return subprocess.check_output(cmd, stdin=stdin, shell=True).decode("utf-8")
