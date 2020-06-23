from Crypto.PublicKey import RSA

def createPEM():
    private_key = RSA.generate(1024);
    h = open('privatekey.pem' , 'wb+');
    h.write(private_key.exportKey('PEM'))
    h.close()

    public_key = private_key.public_key()
    h = open('publickey.pem' , 'wb+')
    h.write(public_key.exportKey('PEM'))
    h.close()
createPEM()
