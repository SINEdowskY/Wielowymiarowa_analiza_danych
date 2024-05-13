## Here lies all ETLs (pipelines) between databases

### Installing Additional Packages

*Pip:*
```python
# Install a pip package in the current Jupyter kernel
import sys
!{sys.executable} -m pip install numpy
```

*Conda:*
```python
# Install a conda package in the current Jupyter kernel
import sys
%conda install --yes --prefix {sys.prefix} numpy
```
