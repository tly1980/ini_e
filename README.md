# INI file enhancer

A tool to help you manipulate ini files.

## Why ?

Essentially, an ini files is nothing but just a dictionary. Most modern languages shiped with a ini configuartion lib that help you read / modify ini files.

However this is not the case with a lot of *nix shells . Wouldn't it be nice if there is a command line tool to make ini files modifying easier.

`INI file enhancer` is exactly a tool for ini manipulation, it allows you add / update / delete a item of a ini files, what is more than that, to extends multiple ini files into one new ini file.

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
1. Remove `a=A` in `[sec]`
2. add `new_item=NEW` to `[sec]`
3. update `a2` in `[sec2]` to `haha`

`ini_e.py a.ini b.ini --del sec.a --set sec.new_item=NEW sec2.a2=haha`

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