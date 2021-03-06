# Canalyse

Analyse [CURP](https://curp.jp/) result.

## Install

Canalyse require python 3.6 or more upper version.

```console
pip install canalyse
```

## Usage

### as a CLI

Verify statistical quantity of data

The variance should be grater than:

```console
canalyse conductivity --quantity=variance --grater-than 2.0e-5 conductivity.dot
```

The variance should be less than:

```console
canalyse conductivity --quantity=variance --less-than 2.0e-4 conductivity.dot
```

You can use `--quantity` option:

| Option   | description                |
| -------- | -------------------------- |
| variance | variance of data           |
| average  | average of data            |
| std      | standard deviation of data |

### as a Python package

```python
from canalyse.parser import (
    ConductivityParser,
    ConductivityFormatter
)

conductivity_file = "conductivity.dot"
parser = ConductivityParser()
df = parser.run(conductivity_file)
formatter = ConductivityFormatter()
new_df = formatter.run(df)
```

and you can see the frame of `new_df` :

```console
      source     target  conductivity  source_number source_residue  target_number target_residue
0  00001_MET  00036_PHE      0.017448              1            MET             36            PHE
1  00001_MET  00005_GLU      0.021499              1            MET              5            GLU
2  00001_MET  00004_ASP      0.012439              1            MET              4            ASP
```
