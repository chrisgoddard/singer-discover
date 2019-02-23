# Singer Discover Utility

Simply command line utility to take a [Singer](https://www.singer.io/)-specification JSON catalog file and select which streams and fields to include. Fields with "automatic" inclusion are included... er.. automatically.

## Installation

```
pip install https://github.com/chrisgoddard/singer-discover/archive/master.zip
```

## Use

Two ways of using this script.

First takes two filenames: input (--input, -i) and output (--output, -o). These can be the same

```
singer-discover --input catalog.json --output catalog.json
```

The second accepts the piped output of a tap in discover mode, making it a little more idiomatic with the rest of the Singer ecosystem.

```
tap-example --config config.json --discover | singer-discover -o catalog.json
```

_NOTE: This uses a bit of a hack to allow the interactive interface to appear after the script has accepted input from stdin. It worked for me, but please let me know if you see errors. First method should work for all._


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

