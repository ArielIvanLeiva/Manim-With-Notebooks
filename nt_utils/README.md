# Notebook Utils
This is a simple library for simplifying exporting jupyter notebooks (and intended for using it while running a notebook).

## Usage
The next script will create a python script called "scene.py" by taking in order all code cells from example.ipynb that are tagged with "export" or "export_mee_too" igoring those who are tagged with some of the ignored_tags.

```python
from nt_utils import export_cells

export_cells("example.ipynb", "ouput_file.py", tags=["export", "export_me_too"], ignored_tags=["ignore"])
```

## Example use case
Imagine you have a lot of code cells for a [Manim](https://www.manim.community/) animation scene and want all of them to be imported except the last cell, which is for running the Manim rendering.

Your last cell could look like this:

```python

from subprocess import run
from nt_utils import export_cells

export_cells("example.ipynb", "scene.py", tags=[], ignored_tags=["ignore"])

output = run("manim -pqm scene.py SceneName".split(), capture_output=True)
print(output.stdout.decode("utf-8"))
print(output.stderr.decode("utf-8"))

```

So that every code cell is imported (that's what **"tags=[]" means**) except for the one tagged "ignore" (and the Manim simulation is run in this case).

**WARNING:** If you are not careful and forget to specify the "ignore" tag to this last cell, you can easily end up having an infinite loop.