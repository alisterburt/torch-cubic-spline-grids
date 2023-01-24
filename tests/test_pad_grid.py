import torch

from torch_cubic_b_spline_grid import pad_grid


def test_pad_1d():
    grid = torch.arange(3)
    padded_grid = pad_grid.pad_grid_1d(grid)
    expected = torch.tensor([-1, 0, 1, 2, 3])
    assert torch.allclose(padded_grid, expected)


def test_pad_2d():
    grid = torch.tensor(
        [[0, 1],
         [2, 3]]
    ).view(2, 2, 1)
    padded_grid = pad_grid.pad_grid_2d(grid)
    expected = torch.tensor(
        [[-3, -2, -1, 0],
         [-1, 0, 1, 2],
         [1, 2, 3, 4],
         [3, 4, 5, 6]]
    ).view((4, 4, 1))
    assert torch.allclose(padded_grid, expected)


def test_pad_3d():
    grid = torch.tensor(
        [[[0, 1],
          [2, 3]],
         [[4, 5],
          [6, 7]]]
    ).view(2, 2, 2, 1)
    padded_grid = pad_grid.pad_grid_3d(grid)
    expected = torch.tensor(
        [[[-7, -6, -5, -4],
          [-5, -4, -3, -2],
          [-3, -2, -1, 0],
          [-1, 0, 1, 2]],

         [[-3, -2, -1, 0],
          [-1, 0, 1, 2],
          [1, 2, 3, 4],
          [3, 4, 5, 6]],

         [[1, 2, 3, 4],
          [3, 4, 5, 6],
          [5, 6, 7, 8],
          [7, 8, 9, 10]],

         [[5, 6, 7, 8],
          [7, 8, 9, 10],
          [9, 10, 11, 12],
          [11, 12, 13, 14]]]
    ).view(4, 4, 4, 1)
    assert torch.allclose(padded_grid, expected)


def test_pad_4d():
    grid = torch.tensor(
        [[[[0, 1],
           [2, 3]],
          [[4, 5],
           [6, 7]]],
         [[[8, 9],
           [10, 11]],
          [[12, 13],
           [14, 15]]]]
    ).view(2, 2, 2, 2, 1)
    padded_grid = pad_grid.pad_grid_4d(grid)
    expected = torch.tensor(
        [[[[-15, -14, -13, -12],
           [-13, -12, -11, -10],
           [-11, -10, -9, -8],
           [-9, -8, -7, -6]],
          [[-11, -10, -9, -8],
           [-9, -8, -7, -6],
           [-7, -6, -5, -4],
           [-5, -4, -3, -2]],
          [[-7, -6, -5, -4],
           [-5, -4, -3, -2],
           [-3, -2, -1, 0],
           [-1, 0, 1, 2]],
          [[-3, -2, -1, 0],
           [-1, 0, 1, 2],
           [1, 2, 3, 4],
           [3, 4, 5, 6]]],
         [[[-7, -6, -5, -4],
           [-5, -4, -3, -2],
           [-3, -2, -1, 0],
           [-1, 0, 1, 2]],
          [[-3, -2, -1, 0],
           [-1, 0, 1, 2],
           [1, 2, 3, 4],
           [3, 4, 5, 6]],
          [[1, 2, 3, 4],
           [3, 4, 5, 6],
           [5, 6, 7, 8],
           [7, 8, 9, 10]],
          [[5, 6, 7, 8],
           [7, 8, 9, 10],
           [9, 10, 11, 12],
           [11, 12, 13, 14]]],
         [[[1, 2, 3, 4],
           [3, 4, 5, 6],
           [5, 6, 7, 8],
           [7, 8, 9, 10]],
          [[5, 6, 7, 8],
           [7, 8, 9, 10],
           [9, 10, 11, 12],
           [11, 12, 13, 14]],
          [[9, 10, 11, 12],
           [11, 12, 13, 14],
           [13, 14, 15, 16],
           [15, 16, 17, 18]],
          [[13, 14, 15, 16],
           [15, 16, 17, 18],
           [17, 18, 19, 20],
           [19, 20, 21, 22]]],
         [[[9, 10, 11, 12],
           [11, 12, 13, 14],
           [13, 14, 15, 16],
           [15, 16, 17, 18]],
          [[13, 14, 15, 16],
           [15, 16, 17, 18],
           [17, 18, 19, 20],
           [19, 20, 21, 22]],
          [[17, 18, 19, 20],
           [19, 20, 21, 22],
           [21, 22, 23, 24],
           [23, 24, 25, 26]],
          [[21, 22, 23, 24],
           [23, 24, 25, 26],
           [25, 26, 27, 28],
           [27, 28, 29, 30]]]]
    ).view(4, 4, 4, 4, 1)
    assert torch.allclose(padded_grid, expected)
