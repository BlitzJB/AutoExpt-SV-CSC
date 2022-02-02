### Usage
```py
# for normal scripts
Experiment('path_to_file.py', 'Amazing title', 'Incredible Datestring')


# if file needs use input, you will have to make a text file and put your console output in it
Experiment('path_to_file.py', 'Amazing title', 'Incredible Datestring', manual_output='path_to_the_text_file_you_made.txt')
```

### CLI Usage
You can run the cli.py to get an easy to use CLI

```cli.py [OPTIONS] FILE

Arguments:
  FILE  Path to the file to be processed  [required]

Options:
  --title TEXT
  --date TEXT
  --manual-output TEXT
  --help                          Show this message and exit.
```

Example: `python stack-1.py --title 'STACK 1' --date 1-2-2022`

```
NOTE: defaults to python in windows and python3 in linux so you might need to make aliases to make it work
```
