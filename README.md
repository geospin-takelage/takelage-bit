[![takelage image](https://github.com/geospin-takelage/takelage-bit/actions/workflows/build_test_project_nightly.yml/badge.svg)](https://github.com/geospin-takelage/takelage-bit/actions/workflows/build_test_project_nightly.yml)
[![ansible roles](https://github.com/geospin-takelage/takelage-bit/actions/workflows/build_test_roles_nightly.yml/badge.svg)](https://github.com/geospin-takelage/takelage-bit/actions/workflows/build_test_roles_nightly.yml)
[![docker image](https://img.shields.io/docker/v/takelage/bitboard?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelage/bitboard)
[![license](https://img.shields.io/github/license/geospin-takelage/takelage-bit?label=License&color=blueviolet)](https://github.com/geospin-takelage/takelage-bit/blob/main/LICENSE)

# takelage-bit

*takelage-bit* is bit server to facilitate collaboration
using the takelage devops workflow.
The takelage devops workflow helps devops engineers
build, test and deploy os images.

A *takelage-bit* docker container called *bitboard* is published on 
[Docker Hub](https://hub.docker.com/r/takelage/bitboard).
It contains a 
[public ssh key pair](ansible/roles/takel-bit-server/files)
so it is usable for testing purposes only!

## Framework

The takelage devops framework consists of these projects:

| App | Description |
| --- | ----------- |
| *[takelage-doc](https://github.com/geospin-takelage/takelage-doc)* | takelage documentation |
| *[takelage-dev](https://github.com/geospin-takelage/takelage-dev)* | takelage development environment |
| *[takelage-var](https://github.com/geospin-takelage/takelage-var)* | takelage test plugin |
| *[takelage-cli](https://github.com/geospin-takelage/takelage-cli)* | takelage command line interface |
| *[takelage-bit](https://github.com/geospin-takelage/takelage-bit)* | takelage bit server | 
| *[takelage-img-takelbase](https://github.com/geospin-takelage/takelage-img-takelbase)* | takelage takelbase image | 
| *[takelage-img-takelslim](https://github.com/geospin-takelage/takelage-img-takelslim)* | takelage takelbase image | 
| *[takelage-img-multipostgres](https://github.com/geospin-takelage/takelage-img-multipostgres)* | takelage multipostgres image | 

## bit

[bit](https://github.com/teambit/bit) is a 
[git](https://git-scm.com) extension.
bit is not meant to replace git.
You may think of bit as a git powered clipboard manager
with versioning and central storage.
For open source projects you may use [bit.dev](https://bit.dev)
as your central bit storage.
For software testing or private use you may use a *bitboard* server
created with this project.

Both bit and git are in their core free and open source tools.
Around these tools both free and non-free infrastructure has emerged.
git sparked projects like [GitHub](https://github.com) and 
[GitLab](https://gitlab.com) while bit has been
developed by Cocycles, the company behind 
[bit.dev](https://bit.dev).

bit.dev's intended audience is the javascript community and
they also host the best resources for bit: 
the [bit docs](https://docs.bit.dev/docs/faq).

The takelage devops workflow uses the open source parts of bit.
The bit part of takelage is targeting devops engineers.
It enables them to share parts of their git repositories.
And they may inject private data into open source projects.
