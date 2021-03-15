
## Introduction to JSON Web Tokens

JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA or ECDSA.

## What is the JSON Web Token structure?
In its compact form, JSON Web Tokens consist of three parts separated by dots (.), which are:

- Header
- Payload
- Signature

## When should you use JSON Web Tokens?

Here are some scenarios where JSON Web Tokens are useful:

### Authorization
This is the most common scenario for using JWT. Once the user is logged in, each subsequent request will include the JWT, allowing the user to access routes, services, and resources that are permitted with that token. Single Sign On is a feature that widely uses JWT nowadays, because of its small overhead and its ability to be easily used across different domains.

### Information Exchange
JSON Web Tokens are a good way of securely transmitting information between parties. Because JWTs can be signed—for example, using public/private key pairs—you can be sure the senders are who they say they are. Additionally, as the signature is calculated using the header and the payload, you can also verify that the content hasn't been tampered with.

For more details please check [https://jwt.io/introduction]

# About the JWT Library
This python library will help out in case you are planning to inject some JWT security checks in your automation scripts using Robot Framework.

All you have to do [After you have Robot framework environment is ready] is adding the jwt lib to your robot framework settings so you can use the keywords instead of using the CLI to run the jwt commands.

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
       
For more details on how to use each keywork please check  [https://myjwt.readthedocs.io/en/latest/examples.html#modify-your-jwt] 

# Refrences 
- https://myjwt.readthedocs.io/en/latest/
- https://github.com/mBouamama/MyJWT
- https://jwt.io/
