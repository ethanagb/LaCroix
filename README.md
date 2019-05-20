**LaCroix Can Color Palettes for matplotlib**
====================================================================

[![Build Status](https://travis-ci.org/ethanagbaker/LaCroix.svg?branch=master)](https://travis-ci.org/ethanagbaker/lacroix)

Usage
-----
To install:

`pip install lacroix`

To import:
```
import lacroix
lacroix.set_palette('Pamplemousse')
```
and then all future plots will use the `Pamplemousse` palette.

To reset:

```
import matplotlib
matplotlib.rcdefaults()
```

You can plot all available palettes with `lacroix.available()`.

You can plot any number of palettes side-by-side with `lacroix.plot_palettes(*args)`.

For ease of integration with [seaborn](https://seaborn.pydata.org/index.html), you can return a list of colors from a palette and pass it as a `seaborn` palette:
```
berry = lacroix.colorList('Berry')
berry_sns = sns.color_palette(berry) #creates a seaborn palette.
```

See the [**Examples**](https://nbviewer.jupyter.org/github/ethanagbaker/LaCroix/blob/master/Examples.ipynb) notebook for usage cases. Palettes should be set after importing seaborn.

License
--------

This is licensed in the Creative Commons for Attribution and ShareAlike
purposes.
CC-BY-SA

Acknowledgements
--------
Package architecture modified from [wes](https://github.com/ljwolf/wampl)
