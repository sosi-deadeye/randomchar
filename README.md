# randomchar

## What is `randomchar` ?
This module is designed to make the task of generating random strings as easy as calling a function.
To generate a password all you have to do is call `randomchar.password(8)` where 8 is the required length of the password.
Normally, to do this without randomchar you will have to write verbose code of up to 5 lines or more, randomchar shortens that up to one short line,

# Installation
This package has not been released to the Python Package Index (yet).

## Usage
```python
import randomchar

randomchar.letter(5)
#returns a sequence of 5 random characters
randomchar.digit(9)
#returns a sequence of 9 random digits
randomchar.symbol(3)
#returns a sequence of 3 random symbols
randomchar.password(8)
#returns a secure sequence of 8 characters

randomchar.letter()
#returns a single random letter
randomchar.digit()
#returns a single random number
randomchar.symbol()
#returns a single random symbol
randomchar.all_ascii()
#returns a single random character

```

## `randomchar` functions
* `letter()` - This function returns a sequence of ramdom **letters**, if its called with out any arguments it returns just one random **letter**
* `lower_case()` - This function returns a sequence of ramdom **lowercase letters**, if its called with out any arguments it returns just one random **lowercase letter**
* `upper_case()` - This function returns a sequence of ramdom **uppercase letters**, if its called with out any arguments it returns just one random **uppercase letter**
* `digit()` - This function returns a sequence of ramdom **digits**, if its called with out any arguments it returns just one random **digit**
* `symbol()` - This function returns a sequence of ramdom **symbols**, if its called with out any arguments it returns just one random **symbol**
* `all_ascii()` - This function returns a sequence of ramdom **character**, if its called with out any arguments it returns just one random **character**
* `password()`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licences/mit/)
