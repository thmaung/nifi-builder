#### Table of Contents

1. [Overview](#overview)
2. [Setup](#setup)
3. [Usage - Configuration options and etc](#usage)

### Overview

This rake task will build the Apache NiFi downloaded from https://nifi.incubator.apache.org/download.html

### Setup

* Ensure simp-rack-helpers rubygem is installed.

### Usage

* rake clean
* rake build:rpm[path_to_tar.gz,mock_environment]
