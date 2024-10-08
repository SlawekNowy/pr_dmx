import os
import subprocess
import sys
import stat
from sys import platform
from pathlib import Path

# util_dmx
git_clone_commit(
    "util_dmx",
    external_libs_dir +"/util_dmx",
    "https://github.com/Silverlan/util_dmx.git",
    "2d9c0789be25c29cc02c1a385b8baea112765f58"
)


cmake_args.append("-DPME_EXTERNAL_LIB_LOCATION=" +external_libs_dir)
cmake_args.append("-DPME_EXTERNAL_LIB_BIN_LOCATION=" +external_libs_bin_dir)
cmake_args.append("-DPME_THIRD_PARTY_LIB_LOCATION=" +third_party_libs_dir)

additional_build_targets.append("pr_dmx")
