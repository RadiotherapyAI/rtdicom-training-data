import subprocess
import pathlib


HERE = pathlib.Path(__file__).parent


def main():
    paths = HERE.glob("**/*.dcm")
    counts_to_upload_per_step = 500

    while True:
        block_of_paths = list(next(paths) for _ in range(counts_to_upload_per_step))
        relative_block = [str(path.relative_to(HERE)) for path in block_of_paths]
        
        subprocess.check_output(['git', 'add'] + relative_block)

        try:
            subprocess.check_output(['git', 'commit', '-m', 'automated bulk data commit'])
            subprocess.check_output(['git', 'push'])
        except subprocess.CalledProcessError:
            continue
        


if __name__ == "__main__":
    main()
