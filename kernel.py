import sys
import cv2 as cv
import numpy as np

def main(argv):
    window_name = 'filter2D Demo'
    
    imageName = argv[0] if len(argv) > 0 else 'lena.jpg'
    # Loads an image
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: filter2D.py [image_name -- default lena.jpg] \n')
        return -1
    
    ddepth = -1
    
    ind = 0
    while True:
        # Define a custom kernel for edge detection
        custom_kernel = np.array([[-1, -1, -1],
                                  [-1,  8, -1],
                                  [-1, -1, -1]], dtype=np.float32)
        
        kernel_size = custom_kernel.shape[0]
        
        dst = cv.filter2D(src, ddepth, custom_kernel)
        
        cv.imshow(window_name, dst)
        c = cv.waitKey(500)
        if c == 27:
            break
        ind += 1
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
