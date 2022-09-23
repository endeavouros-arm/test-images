#!/usr/bin/env python3

import subprocess
import argparse
import datetime

today = datetime.date.today()

DATE = today.strftime("%Y%m%d")


def parse_function():
    global platform
    global itype
    global mod_rel
    parser = argparse.ArgumentParser(
        description="Python script to create EndeavourOS ARM images/rootfs"
    )
    parser.add_argument(
        "--platform",
        "-p",
        required=True,
        choices=["rpi", "odn", "pbp"],
        help="Choose platform",
    )
    # parser.add_argument(
    #     "--type",
    #     "-t",
    #     choices=["rootfs", "ddimg"],
    #     default="rootfs",
    #     help="Choose image type",
    # )
    parser.add_argument(
        "--mod",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Upload new image on same day",
    )
    args = parser.parse_args()

    platform = args.platform
    mod_rel = args.mod


def modify_release(img_name, rel_name):
    cmd = [
        "gh",
        "release",
        "upload",
        rel_name,
        img_name,
        img_name + ".sha512sum",
        "--clobber",
    ]
    out = subprocess.run(cmd, check=True)


def create_release(img_name, rel_name, rel_note):
    cmd = [
        "gh",
        "release",
        "create",
        rel_name,
        img_name,
        img_name + ".sha512sum",
        "-t",
        rel_name,
        "-F",
        rel_note,
        "-d",
    ]
    out = subprocess.run(cmd, check=True)
    cmd = ["gh", "release", "edit", rel_name, "--draft=false"]
    out = subprocess.run(cmd, check=True)


def main():
    parse_function()
    plat = platform
    if platform == "odn":
        plat = "odroid-n2"
    rel_name = f"image-{plat}-{DATE}"
    img_name = f"enosLinuxARM-{plat}-latest.tar.zst"
    rel_note = f"release-note-{plat}.md"
    if mod_rel:
        modify_release(img_name, rel_name)
    else:
        create_release(img_name, rel_name, rel_note)


if __name__ == "__main__":
    main()
