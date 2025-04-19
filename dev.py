import pyray as pr
import configs

pr.init_window(configs.window_w, configs.window_h, "Building Rubik's Cube")

pr.set_target_fps(configs.fps)

while not pr.window_should_close():

    pr.update_camera(configs.camera, pr.CameraMode.CAMERA_ORBITAL)

    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    pr.begin_mode_3d(configs.camera)

    pr.end_mode_3d()
    pr.end_drawing()

pr.close_window()