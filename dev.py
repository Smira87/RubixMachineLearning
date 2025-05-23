import pyray as pr
import configs
from rubik import Rubik

pr.init_window(configs.window_w, configs.window_h, "Building Rubik's Cube")

rubik_cube = Rubik()

pr.set_target_fps(configs.fps)

while not pr.window_should_close():

    pr.update_camera(configs.camera, pr.CameraMode.CAMERA_THIRD_PERSON)

    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    pr.begin_mode_3d(configs.camera)
    pr.draw_grid(20, 1.0)

    # Draw every cube of a Rubik's Cube

    for i, cube in enumerate(rubik_cube.cubes):
        for cube_part in cube:
            position = pr.Vector3(cube[0].center[0], cube[0].center[1], cube[0].center[2])
            print(cube[0].center)

            pr.draw_model(cube_part.model,
                          position,
                          2,
                          cube_part.face_color)


    pr.end_mode_3d()

    pr.end_drawing()

pr.close_window()