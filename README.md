
# Introduction to JSON Web Tokens

JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA or ECDSA.

## What is the JSON Web Token structure?
In its compact form, JSON Web Tokens consist of three parts separated by dots (.), which are:

- Header
- Payload
- Signature

# About the JWT Library

This library will help out in case you are planning to do some security checks in your JWT using Robot framework to inject the tests into your automation scripts.

All you have to do is adding the jwt lib to your robot framework settings so you can use the keywords instead of using the CLI to run the jwt commands.

    ### Library     ../Libraries/jwt.py


# Features

Below  are the list of the Keyword that are included in the jwt Library 

- Modify Your jwt

- None Vulnerabilty Check

- Sign Key

- Brute Force Signature

- RSA/HMAC Confusion

- Kid Injection

- Send your new Jwt to url

- Jku Vulnerability

- X5u Vulnerability


# Prerequisites 

- you have to install myjwt 

       pip install myjwt
       
For more details on how to use each keywork please check  https://myjwt.readthedocs.io/en/latest/examples.html#modify-your-jwt 

# Refrences 
- https://myjwt.readthedocs.io/en/latest/
- https://github.com/mBouamama/MyJWT
- https://jwt.io/
