# INI file enhancer

A tool to help you manipulate ini files.

## Why ?

Essentially, an ini files is nothing but just a dictionary. Most modern languages shiped with a ini configuartion lib that help you read / modify ini files.

However this is not the case with a lot of *nix shells . Wouldn't it be nice if there is a command line tool to make ini files modifying easier ?  :)

[INI file enhancer](https://github.com/tly1980/ini_e) is exactly a tool for ini manipulation, it allows you add / update / delete a item of a ini files, what is more than that, to extends multiple ini files into one new ini file.

Powered by excellent python 2.x's [ConfigParser](https://docs.python.org/2/library/configparser.html#module-ConfigParser), `ini_e` managed to implment those features with a very small code footprint and without any dependencies or other 3rd party. 

## Installation

As no 3rd party lib dependencies, you can just download [ini_e](https://raw.githubusercontent.com/tly1980/ini_e/master/src/ini_e.py) to what ever folder appears in your [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) and chmod with executable permission and run it.

## Usages

`Usages` usaually look scared to me, I normally go directly to [Examples](#examples).

```
./ini_e.py --help
usage: A tool to alter ini config files. [-h] [--set SET [SET ...]]
                                         [--del DEL [DEL ...]] [-o OUT]
                                         [-v VERBOSE]
                                         ini [ini ...]

positional arguments:
  ini

optional arguments:
  -h, --help            show this help message and exit
  --set SET [SET ...]   Add item. Specify it in format
                        "SECTION.item_name=value"
  --del DEL [DEL ...]   To remove item would require format
                        "SECTION.item_name", "SECTION" if you want to remove
                        the whole section
  -o OUT, --out OUT     Where you wish to save the ini file to. If the
                        operations failed the existing file would not be
                        overwritten.
  -v VERBOSE, --verbose VERBOSE
                        Enable logging to info level, default is warnning
```

## Examples

### Examples 1 - Dctionary extends

Supposed you have `a.ini` 
```ini
[sec]
a=A
```
and `b.ini`
```ini
[sec]
b=B
b1=B1
```

If you want to merge them together, simply go `ini_e.py a.ini b.ini`, and you will have:
```ini
[sec]
a = A
b = B
b1 = B1
```

### Examples 2 - Dctionary extends

Supposed you have `a.ini` 
```ini
[sec]
a=A
common=A_C
```
and `b.ini`
```ini
[sec]
b=B
b1=B1
common=B_C
```

Run the same command `ini_e.py a.ini b.ini`, and you will see `common` value is overriden to `B_C`, as `b.ini` is the later one:
```ini
[sec]
a = A
common = B_C
b = B
b1 = B1
```

If you have a `c.ini` like
```ini
[sec]
common=C_C
```

Run `ini_e.py a.ini b.ini c.ini`, you will have
```ini
[sec]
a = A
common = C_C
b = B
b1 = B1
```

### Examples 3 - set and del

Supposed you'd have `a.ini` and `b.ini` as following
```ini
# a.ini
[sec]
a=A

[sec2]
a2=A2
```

```ini
[sec]
b=B

[sec2]
b2=B2
```

What I want is:

1. remove `a=A` in `[sec]`
2. add `new_item=NEW` to `[sec]`
3. update `a2` in `[sec2]` to `haha`

All those can be done within one command:

```ini_e.py a.ini b.ini --del sec.a --set sec.new_item=NEW sec2.a2=haha```

Output would be:
```ini
[sec]
b = B
new_item = NEW

[sec2]
a2 = haha
b2 = B2
```

Removing the whole section is possbile.

```ini_e.py a.ini --del sec2```

```ini
[sec]
a = A
```