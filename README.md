# Singer Discover Utility

Simply command line utility to take a [Singer](https://www.singer.io/)-specification JSON catalog file and select which streams and fields to include. Fields with "automatic" inclusion are included... er.. automatically.

## Installation

```
pip install https://github.com/chrisgoddard/singer-discover/archive/master.zip
```

## Use

```
singer-discover --catalog catalog.json
```

First select which streams to include

```
? Select Streams (<up>, <down> to move, <space> to select, <a> to toggle, <i> to invert)
> • stream_one
  ○ stream_two
  ○ stream_three
```

Hit enter. Then select the fields within each stream to include. Hit `a` to toggle select all. Automatically included fields are unselectable and annotated with (automatic)

```
? Select fields for stream: `stream_one` (<up>, <down> to move, <space> to select, <a> to toggle, <i> to invert)
> - id (automatic)
  • name
  ○ type
  ○ price
```

Hit enter, and the catalog file is updated with the field and stream `selected` properties updated.

