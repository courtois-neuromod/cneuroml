# CNeuroML

[![container-build-push](
    https://github.com/courtois-neuromod/cneuroml/actions/workflows/container-build-push.yaml/badge.svg)](
        https://github.com/courtois-neuromod/cneuroml/actions/workflows/container-build-push.yaml)
[![docs-build-push](
    https://github.com/courtois-neuromod/cneuroml/actions/workflows/docs-build-push.yaml/badge.svg)](
        https://github.com/courtois-neuromod/cneuroml/actions/workflows/docs-build-push.yaml)
[![format-lint](
    https://github.com/courtois-neuromod/cneuroml/actions/workflows/format-lint.yaml/badge.svg)](
        https://github.com/courtois-neuromod/cneuroml/actions/workflows/format-lint.yaml)
[![typecheck-unittest](
    https://github.com/courtois-neuromod/cneuroml/actions/workflows/typecheck-unittest.yaml/badge.svg)](
        https://github.com/courtois-neuromod/cneuroml/actions/workflows/typecheck-unittest.yaml)
[![codecov](
    https://codecov.io/gh/courtois-neuromod/cneuroml/branch/main/graph/badge.svg?token=AN8GLFP9CB)](
        https://codecov.io/gh/courtois-neuromod/cneuroml)
[![code style: black](
    https://img.shields.io/badge/code%20style-black-000000.svg)](
        https://github.com/psf/black)

Full documentation available at [https://courtois-neuromod.github.io/cneuroml](
    https://courtois-neuromod.github.io/cneuroml/).


```
cneuroml
├─ .github
│  └─ workflows
│     ├─ container-build-push.yaml
│     ├─ container-build.yaml
│     ├─ docs-build-push.yaml
│     ├─ docs-build.yaml
│     ├─ format-lint.yaml
│     └─ typecheck-unittest.yaml
├─ .gitignore
├─ .pre-commit-config.yaml
├─ .yamllint.yaml
├─ LICENSE
├─ README.md
├─ cneuroml
│  ├─ __init__.py
│  ├─ app
│  │  └─ __init__.py
│  ├─ dl
│  │  ├─ __init__.py
│  │  └─ base
│  │     ├─ __init__.py
│  │     ├─ datamodule.py
│  │     ├─ datamodule_test.py
│  │     ├─ litmodule.py
│  │     └─ litmodule_test.py
│  └─ ne
│     └─ __init__.py
├─ cneuroml.egg-info
│  ├─ PKG-INFO
│  ├─ SOURCES.txt
│  ├─ dependency_links.txt
│  ├─ requires.txt
│  └─ top_level.txt
├─ containers
│  └─ deps
│     └─ run
│        └─ Containerfile
├─ docs
│  ├─ Contribution.rst
│  ├─ Execution.rst
│  ├─ Execution_On_a_Linux_machine.rst
│  ├─ Execution_On_a_Slurm_cluster.rst
│  ├─ Installation.rst
│  ├─ Installation_Common_to_all_machines.rst
│  ├─ Installation_On_a_Linux_machine.rst
│  ├─ Installation_On_a_Slurm_cluster.rst
│  ├─ Makefile
│  ├─ __init__.py
│  ├─ conf.py
│  ├─ index.rst
│  ├─ make.bat
│  └─ requirements.txt
├─ pyproject.toml
├─ pyreqs
│  ├─ core.txt
│  ├─ dl.txt
│  ├─ hpo.txt
│  ├─ hydra_run.txt
│  ├─ hydra_test.txt
│  ├─ jupyter.txt
│  ├─ ne.txt
│  ├─ test.txt
│  ├─ utils.txt
│  └─ wandb.txt
└─ renovate.json

```
cneuroml
├─ .github                                                                                                                    //
│  └─ workflows                                                                                                               //
│     ├─ container-build-push.yaml                                                                                            //
│     ├─ container-build.yaml                                                                                                 //
│     ├─ docs-build-push.yaml                                                                                                 //
│     ├─ docs-build.yaml                                                                                                      //
│     ├─ format-lint.yaml                                                                                                     //
│     └─ typecheck-unittest.yaml                                                                                              //
├─ .gitignore                                                                                                                 //
├─ .pre-commit-config.yaml                                                                                                    //
├─ .yamllint.yaml                                                                                                             //
├─ LICENSE                                                                                                                    //
├─ README.md                                                                                                                  //
├─ cneuroml                                                                                                                   //
│  ├─ __init__.py                                                                                                             //
│  ├─ app                                                                                                                     //
│  │  └─ __init__.py                                                                                                          //
│  ├─ dl                                                                                                                      //
│  │  ├─ __init__.py                                                                                                          //
│  │  └─ base                                                                                                                 //
│  │     ├─ __init__.py                                                                                                       //
│  │     ├─ datamodule.py                                                                                                     //
│  │     ├─ datamodule_test.py                                                                                                //
│  │     ├─ litmodule.py                                                                                                      //
│  │     └─ litmodule_test.py                                                                                                 //
│  └─ ne                                                                                                                      //
│     └─ __init__.py                                                                                                          //
├─ cneuroml.egg-info                                                                                                          //
│  ├─ PKG-INFO                                                                                                                //
│  ├─ SOURCES.txt                                                                                                             //
│  ├─ dependency_links.txt                                                                                                    //
│  ├─ requires.txt                                                                                                            //
│  └─ top_level.txt                                                                                                           //
├─ containers                                                                                                                 //
│  └─ deps                                                                                                                    //
│     └─ run                                                                                                                  //
│        └─ Containerfile                                                                                                     //
├─ docs                                                                                                                       //
│  ├─ Contribution.rst                                                                                                        //
│  ├─ Execution.rst                                                                                                           //
│  ├─ Execution_On_a_Linux_machine.rst                                                                                        //
│  ├─ Execution_On_a_Slurm_cluster.rst                                                                                        //
│  ├─ Installation.rst                                                                                                        //
│  ├─ Installation_Common_to_all_machines.rst                                                                                 //
│  ├─ Installation_On_a_Linux_machine.rst                                                                                     //
│  ├─ Installation_On_a_Slurm_cluster.rst                                                                                     //
│  ├─ Makefile                                                                                                                //
│  ├─ __init__.py                                                                                                             //
│  ├─ conf.py                                                                                                                 //
│  ├─ index.rst                                                                                                               //
│  ├─ make.bat                                                                                                                //
│  └─ requirements.txt                                                                                                        //
├─ pyproject.toml                                                                                                             //
├─ pyreqs                                                                                                                     //
│  ├─ core.txt                                                                                                                //
│  ├─ dl.txt                                                                                                                  //
│  ├─ hpo.txt                                                                                                                 //
│  ├─ hydra_run.txt                                                                                                           //
│  ├─ hydra_test.txt                                                                                                          //
│  ├─ jupyter.txt                                                                                                             //
│  ├─ ne.txt                                                                                                                  //
│  ├─ test.txt                                                                                                                //
│  ├─ utils.txt                                                                                                               //
│  └─ wandb.txt                                                                                                               //
├─ renovate.json                                                                                                              //
