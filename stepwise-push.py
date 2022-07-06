# Copyright (C) 2022 Radiotherapy AI Pty Ltd

# Licensed under the Apache License, Version 2.0 (the "License"); you
# may not use this file except in compliance with the License. You may
# obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.


import subprocess
import pathlib

import typer

HERE = pathlib.Path(__file__).parent

def main(module: str):
    module_path = HERE.joinpath(module)

    paths = module_path.glob("**/*.dcm")
    counts_to_upload_per_step = 500

    while True:
        block_of_paths = []
        for _ in range(counts_to_upload_per_step):
            try:
                path = next(paths)
            except StopIteration:
                break

            block_of_paths.append(str(path.relative_to(module_path)))
        
        subprocess.check_output(['git', 'add'] + block_of_paths, cwd=module_path)

        try:
            subprocess.check_output(['git', 'commit', '-m', 'automated bulk data commit'], cwd=module_path)
            subprocess.check_output(['git', 'push'], cwd=module_path)
        except subprocess.CalledProcessError:
            continue
        


if __name__ == "__main__":
    typer.run(main)
