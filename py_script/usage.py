from sp_manager import SpManager

sm = SpManager()
# sm.quick_start("samu_image_compress")
# sm.quick_start("samu_video_compress")

# json_set = {
#     "path_in": r"D:\s-linux\project\test_file\test_in",
#     "path_out": r"D:\s-linux\project\test_file\test_out"
# }
# sm.run_copy_merge(json_set=json_set)

json_set = {
    "pre_key":"samu_compress_test"
}
sm.quick_start(json_set=json_set)