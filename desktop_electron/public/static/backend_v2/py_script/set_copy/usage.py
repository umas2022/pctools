import sys
sys.path.append("..")
from set_copy.quick_start import QuickStart


# qs.quick_start("compress_test")

json_set = {
    "pre_key":"compress_test"
}

qs = QuickStart(json_set=json_set)
qs.run()