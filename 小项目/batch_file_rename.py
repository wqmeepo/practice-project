import argparse
import os


def batch_rename(work_dir, old_ext, new_ext):
    # files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        if old_ext == file_ext:
            new_file = split_file[0] + new_ext
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, new_file)
            )
        print("rename is done")


def get_parser():
    parser = argparse.ArgumentParser(description='批量修改文件后缀名，请在脚本后输入目录地址')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='目录地址')
    parser.add_argument('old_ext', metavar='OLD_DIR', type=str, nargs=1, help='旧后缀')
    parser.add_argument('new_ext', metavar='NEW_DIR', type=str, nargs=1, help='新后缀')
    return parser


def main():
    paser = get_parser()
    args = vars(paser.parse_args())
    print(args)
    word_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext

    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(word_dir, old_ext, new_ext)


if __name__ == '__main__':
    main()
