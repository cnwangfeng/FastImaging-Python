from fastimgproto.tests.fixtures.image import (
    evaluate_model_on_pixel_grid,
    gaussian_point_source,
    uncorrelated_gaussian_noise_background
)
import fastimgproto.sourcefind.detect as detect
import numpy as np


def test_basic_source_detection():
    ydim = 128
    xdim = 64
    img = uncorrelated_gaussian_noise_background((ydim, xdim))
    bright_src = gaussian_point_source(x_centre=32, y_centre=64, amplitude=5.0)
    faint_src = gaussian_point_source(x_centre=64, y_centre=64, amplitude=3.5)
    img += evaluate_model_on_pixel_grid(img.shape, bright_src)
    img += evaluate_model_on_pixel_grid(img.shape, faint_src)

    srcs = detect.extract_sources(img, detection_n_sigma=4.5,
                                  analysis_n_sigma=3)
    # We expect to detect the bright source, but not the faint one.
    assert len(srcs) == 1
    pixel_idx, pixel_value = srcs[0]
    y_idx, x_idx = pixel_idx
    assert np.abs(y_idx - bright_src.y_mean) <0.5
    assert np.abs(x_idx - bright_src.x_mean) < 0.5
