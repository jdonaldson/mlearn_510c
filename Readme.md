# MLEARN 510C - Supplementary Notebooks
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdonaldson/mlearn_510c/HEAD)


## Copy Code and Install the Notebook Environment

### Install and Use Git
Install Git, using the instructions  [here](https://git-scm.com/downloads)

Copy the code to your local system with:

```
$> git clone https://github.com/jdonaldson/mlearn_510c.git
```

This will be our working directory, so switch into it:

```
$> cd mlearn_510c
```

### Install and Use Anaconda
Install Anaconda, using the instructions [here](https://docs.anaconda.com/anaconda/install/).

Anaconda will set our python environment (the python runtime and libraries).
Use this command to create the environment (remember to run this from inside
the mlearn510 working directory.

```
$> conda create -f environment.yml
```

This creates a conda environment called "mlearn510".  To use this environment
we need to activate it:

```
$> conda activate mlearn510
```

(you will need to do this each time you start a new shell)

The session is active until you terminate your shell.  You can manually
close it with:

```
$> conda deactivate
```


### Launch Jupyter Notebooks

Launch the jupyter notebooks with the following command:

```
$> jupyter notebook
```

The jupyter notebook should load inside a new web page in your default browser.

Using the jupyter browser interface, navigate to the "notebooks" directory to
view individual notebooks


