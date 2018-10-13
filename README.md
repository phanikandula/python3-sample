# Sample Python 3 repo

Shows simple module that can generate Major keys (Music theory). See cli example below..


## Install python 3.6

[Anaconda](https://conda.io/docs/user-guide/getting-started.html) is one way to install python version you want

### Create environment for this project

`conda create -n python3-sample python=3.6`

### Activate environment

In Fish shell: `conda activate python3-sample`

or Bash: `activate python3-sample`

## Install the dependencies

`make install`

A few things to do with this project:

* install software: ```make install```
* test code: ```make test```
* lint code: ```make lint```
* run commandline tool:  

```bash
./cli.py --major C 
C,D,E,F,G,A,B,C

./cli.py --major Csh 
C#,D#,F,F#,G#,A#,C,C#
```

* run jupyter notebook:

```
jupyter notebook notebook.ipynb
```

* test jupyter notebook:

```
python -m pytest --nbval notebook.ipynb
```
