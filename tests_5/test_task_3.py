import pytest
import task_3

def test_import_plt():
    try:
        task_3.plt
    except AttributeError:
        pytest.fail("matplotlib.pyplot was not imported as plt")

def test_import_np():
    try:
        task_3.np
    except AttributeError:
        pytest.fail("numpy was not imported as np")

def test_import_newtons_method():
    try:
        task_3.newtons_method
    except AttributeError:
        pytest.fail("newtons_method was not imported from task_1")

def test_import_central_difference():
  try:
      task_3.central_difference
  except AttributeError:
      pytest.fail("central_difference was not imported from task_2")


def f(x):
    return x**3 - 3 * x + 2


@pytest.mark.mpl_image_compare
def test_plot_extreme_value():
    return task_3.plot_extreme_value(f, (-1.5, 0))
