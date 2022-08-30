# PPM - PROTECTED PASSWORD MANAGER

**PPM** is a software application created in order to provide security, privacy, and optimization of passwords on a small scale level. It was initially designed as a simple python project that could be used as a refrence or showcase alongside other projects. It has now become a fair use for me and likely will be for a long duration as it helps keep passwords in one place and hashed (SHA256) for security. 

The format of the database information is as **follows**:

- NTKIM:


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