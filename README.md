
# CoMoDO
Codebase for working with Configurable Morphology Distance Operator function

## Getting Started
Clone the repository in your local directory using `git clone git@github.com:namitjuneja/CoMoDO.git`

### Usage
```
from comodo import compute_distance  

compute_distance(x, y, image_set_directory, query_image_filename)  
```

`compute_distanc` returns the image from `image_set_directory`  which has the least distance from the `query_image_filename`

Here `x` and `y` are the width and height of the images passed to the compute_distance function.



## Citation

```
@INPROCEEDINGS{Juneja2021,
    author = {Juneja, N. and Zola, J. and Chandola, V. and Wodo, O.},
    title = {Graph-based Strategy for Establishing Morphology Similarity},
    booktitle = {International Conference on Scientific and Statistical Database Management (SSDBM)},
    pages = {169--180},
    year = {2021},
    doi = {10.1145/3468791.3468819}
}
```
