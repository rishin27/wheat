import json
import os
from argparse import ArgumentParser
import time


def main(args):
    if args.clean:
        os.system("rm -rf .kaggle")
        os.system("rm -rf ~/.kaggle")
    if not os.path.exists("./.kaggle"):
        os.mkdir("./.kaggle")
        token = ""
        with open("./.kaggle/kaggle.json", "w") as file:
            json.dump(token, file)
        if not os.path.exists("~/.kaggle/kaggle.json"):
            os.system("mkdir -p ~/.kaggle/")
            os.system("cp ./.kaggle/kaggle.json ~/.kaggle/kaggle.json")
        print("Kaggle Config Initialised")
    else:
        print("Kaggle Already Config Initialised")

    os.system(f"kaggle config set -n path -v {args.download_dir}")

    DL_DIR = "{args.download_dir}/datasets"

    if not os.path.exists(f"{DL_DIR}/{args.download}"):
        os.system(f"kaggle competitions download -c {args.download}")
    else:
        print("Dataset already Downloaded")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--download", default="huanghanchina/pascal-voc-2012")
    parser.add_argument("--download_dir", default="/content")
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args()
    main(args)