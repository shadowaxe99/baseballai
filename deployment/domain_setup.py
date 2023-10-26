```python
import os
from getpass import getpass
from OpenSSL import crypto

def create_self_signed_cert(cert_dir, cert_file, key_file, cert_country, cert_state, cert_city, cert_org, cert_ou, cert_cn):
    """
    If datacard.crt and datacard.key don't exist in cert_dir, create a new
    self-signed cert and keypair and write them into that directory.
    """

    if not os.path.exists(os.path.join(cert_dir, cert_file)) \
            or not os.path.exists(os.path.join(cert_dir, key_file)):

        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 2048)

        # create a self-signed cert
        cert = crypto.X509()
        cert.get_subject().C = cert_country
        cert.get_subject().ST = cert_state
        cert.get_subject().L = cert_city
        cert.get_subject().O = cert_org
        cert.get_subject().OU = cert_ou
        cert.get_subject().CN = cert_cn
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha256')

        open(os.path.join(cert_dir, cert_file), "wt").write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
        open(os.path.join(cert_dir, key_file), "wt").write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))

def main():
    cert_dir = input("Enter the directory to store the certificate and key: ")
    cert_file = "certificate.crt"
    key_file = "private.key"
    cert_country = "US"
    cert_state = "Massachusetts"
    cert_city = "Cambridge"
    cert_org = "MIT"
    cert_ou = "AI Lab"
    cert_cn = getpass("Enter your domain name: ")

    create_self_signed_cert(cert_dir, cert_file, key_file, cert_country, cert_state, cert_city, cert_org, cert_ou, cert_cn)

if __name__ == "__main__":
    main()
```