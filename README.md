# PPM - PROTECTED PASSWORD MANAGER

**PPM** is a software application created in order to provide security, privacy, and optimization of passwords on a small scale level. It was initially designed as a simple python project that could be used as a refrence or showcase alongside other projects. It has now become a fair use for me and likely will be for a long duration as it helps keep passwords in one place and hashed (SHA256) for security. 

The format of the database information is as **follows**:


   `Note:` NUM can also be identified as ID Integer


   `Note:` TYPE can either be GA, VA, OA, or IA


   `Note:` Name is often used for VA or OA accounts, it can also be N/A
   

| NUM(ID)| EMAIL             |PASSWORD       |TYPE   |NAME   |
|:-------|:-----------------:|:--------------|:------|:------|
| 1      | example@gmail.com |ABCDEabcde123  |GA     |N/A    |


Each and every information will pass through a database check & input, they will often return in the form of lines of **string** & **integer** values:

```javascript
{
 'NUM': 1,
 'EMAIL': 'example@gmail.com',
 'PASSWORD': 'AABBCCDDaabbccdd11',
 'TYPE': 'GA',
 'NAME': 'Allis' or N/A
}
```

# HASHING PASSWORDS - sha256.py

**Hashing** is fairly important when it comes privacy and protection against hackers who often obtain access to relational databases. Within PPM, there is an option to hash the passwords that you have provided. Hashing the passwords will prevent hackers from obtaining string encoded values of passwords for each email that you may have, or anything of that equivalent.

After utilizing the hashing feature, you will be provided with a folder PASSWORDS (can be changed to something more subtle) where there will be a file containing your passwords and hashed passwords in the following order:


   `password` : `hashed password`


From there, hashing the passwords will also hash the passwords within the database. You can however, use the .txt file in folder PASSWORDS to use for other purposes later. 
