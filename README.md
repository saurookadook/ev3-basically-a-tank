# EV3 Brick Program - Basically-A-Tank

## Overview

Some kinda program for some kind of tanky creation of mine with LEGO, the EV3Brick, and Python 🫠

---

## General Dev

### Versions
- Python: 3.5.3
- Poetry: 1.1.13 (_only compatible with >=3.8.1_)

To get your local environment setup, fun the following:

```shell
$ poetry config cache-dir ./.poetry-cache
$ poetry install
```

If you're using VS Code, you should additionally create a local `.vscode` folder with a `settings.json` file and add the following:
```json
{
    "python.analysis.extraPaths": [
        // replace `ev3-basically-a-tank-aBCDEFGH-py3.8` with the name of the similarly-located folder from your local poetry cache directory
        "./.poetry-cache/virtualenvs/ev3-basically-a-tank-aBCDEFGH-py3.8/lib/python3.8/site-packages"
    ]
}
```


- [Connecting to EV3dev Using SSH](https://www.ev3dev.org/docs/tutorials/connecting-to-ev3dev-with-ssh/)

```bash
$ ssh robot@ev3dev.local
```
_default password is `maker`_


Printing to VS Code terminal:
- https://github.com/ev3dev/ev3dev/issues/1307

---

### Debugging Snippets

```python
all_motors = list_devices("dc-motor", "*")

print(("-" * 30) + " all_motors " + ("-" * 30), file=sys.stderr)
    for motor in all_motors:
        print(motor, file=sys.stderr)
        motor_members = getmembers(motor)
        for member_tup in motor_members:
            name, value = member_tup
            print("name: {}".format(name), file=sys.stderr)
            print("value: {}".format(value), file=sys.stderr)


```

---

### Quirks

- https://stackoverflow.com/questions/57483794/python-shlex-no-closing-quotations-error-how-to-deal-with
- [\[Question\] How can we ev3devBrowser.download.exclude multiple patterns? #104](https://github.com/ev3dev/vscode-ev3dev-browser/issues/104)
    - **answer**: use `ev3devBrowser.download.exclude: "GlobPattern"` _(see [Glob-Patterns](https://github.com/ev3dev/vscode-ev3dev-browser/wiki/Glob-Patterns))_
    - _suggested:_ `"ev3devBrowser.download.exclude": "{**/.*/*,**/tests/*}",`

---

### Resources

- [ev3dev-lang-python](https://github.com/ev3dev/ev3dev-lang-python)
- [python-ev3dev-testfs](https://github.com/pybricks/python-ev3dev-testfs)
- [Mindstorms EV3 - Building Instructions](https://education.lego.com/en-us/product-resources/mindstorms-ev3/downloads/building-instructions)
