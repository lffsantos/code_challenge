This library using Python 3.5

[![Current version at PyPI](https://img.shields.io/pypi/v/postcodeuk.svg)](https://pypi.python.org/pypi/postcodeuk)

# PostCodeUK

## Instalation
```
pip install postcodeuk
```

## Documentation
``` python
In [1]: from postcodeuk import PostCodeUk

In [2]: post = PostCodeUk('invalid')

In [3]: post.is_valid()
Out[3]: False

In [4]: post = PostCodeUk('WV164EH')

In [5]: post.is_valid()
Out[5]: True

In [6]: post.get_inward()
Out[6]: '4EH'

In [7]: post.get_outward()
Out[7]: 'WV16'

In [8]: post.radom_postcode()
Out[8]: 'G1S 9GS'

In [9]: PostCodeUk.radom_postcode()
Out[9]: 'TD4Y 1SS'

In [10]: PostCodeUk.find_all_in_text('example of text with postcodes A7 7AA and other code A8 9BB ',['A7 7AA'])
Out[10]: ['A7 7AA']

In [11]: PostCodeUk.find_all_in_text('example of text with postcodes A7 7AA and other code A8 9BB ',['A7 8AA'])
Out[11]: []

In [12]: PostCodeUk.find_all_in_text('example of text with postcodes A7 7AA and other code A8 9BB ')
Out[12]: ['A7 7AA', 'A8 9BB']

```

- Explore this package using iPython
- Have fun!