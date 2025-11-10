# Essaying
Password generator and manager: two-in-one.

# Overview

> This application (a.k.a. a Python script) provides a unique approach towards storing a user's passwords by serving as a password generator with **a consistent output**.

This is the further development of my earlier idea: long time ago I used to store my passwords in a large text file that consisted of **purely random text**;
but various key words were scattered around this file, so that when searching for them via `Ctrl+F` I was able to locate the beginning
and the ending of a particular password (the keywords are unique for each password and something unobvious, of course).

Now, I've made an automated version of this approach.

# How it works

- Upon the first launch of `passwords.py`, the `essay.txt` file is generated. This file consists of a large amount of randomly generated character sequences. The randomness depends on the time (milliseconds, to be exact) when you generate this file;
- Afterwards, this file will be used to retrieve passwords in a deterministic manner; as long as the file is the same, the output will remain the same;
- The app works as a command line utility: you enter some text (e.g. the name of the site and your log-in username), you click `Enter` and receive your password;
- The password is calculated as follows:
  - The input text is converted to an integer hashcode;
  - This hashcode is used as a random seed;
  - Given this seed, the `random()` fuction returns the start index of the password in the `essay.txt` file;
  - The password length is always 20 characters - they are added to the start index to get the end index.

Besides, some _keyword_ will be provided along with the password; it is a random word from the `names.txt` file. It can be used to have a vague understanding of whether the password is correct
(each password will have its own _name_ word assigned to it, but different passwords may share the same keyword). The keyword feature is also handy when running on a mobile device, because it is easier to copy the password this way.

# How to use
Download archive (or `git clone` if you feel like you're a cool hacker).

Run `passwords.py`.

Enter some text (your username, some web site name, the date you create this password - anything; all characters are allowed, including white spaces, digits and any special symbols).

This is your password, enjoy.

# Q/A

1. Why would you want that?
   - I use it to generate the password once, and then share it between all devices without the need for any sort of synchronization (you just need to share the `essay.txt` between devices only once).
2. Is it safe?
   - As long as no one has access to your PC (`essay.txt` specifically), sure, it's safe.
3. Can it be run on any platform?
   - **Any platform that has Python interpreter installed and running** (yes, mobile devices too). This is the reason I do not compile it to an executable: to provide portability.
4. Any serious drawbacks?
   - See the next section.

# Things that should be taken into account

- If you lose `essay.txt`, you lose everything.
- You must install Python interpreter (version 3.x.x) to run the program.
- The prompt is case-sensitive.
- At the moment, there is a small chance that the `random()` will throw `OutOfBounds` if the (random) starting index is a way-too-big number. Need to fix it! But hasn't happened to me yet!
- There may be some problem with changing (updating) your passwords. You may want to add a date of the password creation into input prompt; but then you may easily forget it.

To solve the latter problem, `notes.py` comes along with `passwords.py`. It is a simple note encryption tool: when you run it for the first time, a simple `.txt` note file is generated.
Then you may fill it with some notes about _when_ you created the password, _how_ can you retrieve it again, etc. When you run it again, the note is encrypted (you must provide **yet another password**
to encrypt it). Enter the same password again - and the note is decrypted.

You should be warned that, if someone tries to decrypt the note with a wrong password, **no exceptions will be thrown**; instead, **you'll just lose your note**.

So let's be real: **don't use `notes.py` unless you really want to**; it's just an experimental tool.

It will be better if you use some third-party utility to store the passwords input prompts (the ones you enter to retrieve your password). **Telegram** (for synchronization over devices) or a plain `.txt` file on your PC (for safety), for example.

# Screenshots

_Upon launch, you enter your prompt:_

<img width="816" height="355" alt="image" src="https://github.com/user-attachments/assets/d34cd189-a08a-4e15-8876-46562a67b5ec" />

_Then, when you tap Enter:_

<img width="690" height="261" alt="image" src="https://github.com/user-attachments/assets/d0c2f4ed-0736-471c-b154-e99be1681838" />
