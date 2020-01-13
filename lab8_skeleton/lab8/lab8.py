import numpy as np

def convolution2d(x, kernel, stride=1):
    """
    Convolution 2D : Do Convolution on 'x' with filter = 'kernel', stride = 'stride'
    입력 x에 대해 'kernel'을 filter로 사용하여 2D Convolution을 수행하시오.
    [Input]
    x: 2D array
    - Shape : (Height, Width)
    kernel : 2D convolution filter
    - Shape : (Kernel size, Kernel size)
    stride : Stride size (default = 1)
    - dtype : int
    [Output]
    conv_out : convolution result
    - Shape : (Conv_Height, Conv_Width)
    - Conv_Height & Conv_Width can be calculated using 'Height', 'Width', 'Kernel size', 'Stride'
    """
    height, width = x.shape
    kernel_size = kernel.shape[0]
    conv_out = None
    # =============================== EDIT HERE ===============================
    # 결과 행렬 생성 zero
    out_row, out_col = ( int( (height - kernel_size) / stride ) + 1 ,
                        int( (width - kernel_size) / stride) + 1 )
    conv_out = np.zeros((out_row, out_col))
    for row in range(out_row):
        for col in range(out_col):
            # 커널 사이즈 추출: x에서 커널 사이즈 만큼 슬라이싱
            rows = row * stride
            cols = col * stride
            x_sub = x[rows : rows + kernel_size, cols : cols+kernel_size]
            # 커널과 x_sub와 행렬곱 계산 & 결과 저장
            result_mat = x_sub * kernel
            conv_out[row][col] = result_mat.sum()
    
    # =========================================================================
    return conv_out


if __name__ == '__main__':
    x = np.array([[1,0,0,0], [1,1,1,1], [0,1,0,0], [1,1,0,1]])
    kernel = np.array([[1,0,0], [0,1,1], [1,1,1]])

    x_ = np.array([[1,1,0,1,1], [0,1,0,0,1], [1,1,0,1,0], [0,0,1,1,1], [1,1,1,1,1]])
    kernel_ = np.array([[1,0,1], [1,1,1], [0,1,0]])

    y = convolution2d(x,kernel,stride=1)
    print(y)
