from pack_7 import mod_task4 as f1


def create_file_updated(**kwarg):
    for k , v in kwarg.items():
        f1.gen_files(ext= k, count= v)