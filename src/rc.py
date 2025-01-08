import numpy as np
from PIL import Image, ImageTk
import copy

class rc:
    front = np.zeros((3,3))+1
    top = np.zeros((3,3))+2
    bottom = np.zeros((3,3))+3
    right = np.zeros((3,3))+4
    left = np.zeros((3,3))+5
    back = np.zeros((3,3))+6

    def handle_back_left(self):
        temp = copy.copy(self.top[0])
        self.top[0] = self.left[:,0][::-1]
        self.left[:,0] = self.bottom[2]
        self.bottom[2] = self.right[:,2][::-1]
        self.right[:,2] = temp

        temp = copy.copy(self.back[2,1:])
        self.back[2,1:] = self.back[1:,0]
        self.back[1:,0] = self.back[0,:2][::-1]
        self.back[0,:2] = self.back[:2,2]
        self.back[:2,2] = temp[::-1]

    def handle_back_right(self):
        temp = copy.copy(self.top[0])
        self.top[0] = self.right[:,2]
        self.right[:,2] = self.bottom[2][::-1]
        self.bottom[2] = self.left[:,0]
        self.left[:,0] = temp[::-1]

        temp = copy.copy(self.back[2,1:])
        self.back[2,1:] = self.back[:2,2][::-1]
        self.back[:2,2] = self.back[0,:2]
        self.back[0,:2] = self.back[1:,0][::-1]
        self.back[1:,0] = temp

    def handle_top_left(self):
        temp = copy.copy(self.front[0])
        self.front[0] = self.left[0]
        self.left[0] = self.back[0]
        self.back[0] = self.right[0]
        self.right[0] = temp

        temp = copy.copy(self.top[2,1:])
        self.top[2,1:] = self.top[1:,0]
        self.top[1:,0] = self.top[0,:2][::-1]
        self.top[0,:2] = self.top[:2,2]
        self.top[:2,2] = temp[::-1]

    def handle_top_right(self):
        temp = copy.copy(self.front[0])
        self.front[0] = self.right[0]
        self.right[0] = self.back[0]
        self.back[0] = self.left[0]
        self.left[0] = temp

        temp = copy.copy(self.top[2,1:])
        self.top[2,1:] = self.top[:2,2][::-1]
        self.top[:2,2] = self.top[0,:2]
        self.top[0,:2] = self.top[1:,0][::-1]
        self.top[1:,0] = temp

    def handle_left_up(self):
        temp = copy.copy(self.top[:,0])
        self.top[:,0] = self.front[:,0]
        self.front[:,0] = self.bottom[:,0]
        self.bottom[:,0] = self.back[:,2][::-1]
        self.back[:,2] = temp[::-1]

        temp = copy.copy(self.left[2,1:])
        self.left[2,1:] = self.left[1:,0]
        self.left[1:,0] = self.left[0,:2][::-1]
        self.left[0,:2] = self.left[:2,2]
        self.left[:2,2] = temp[::-1]

    def handle_left_down(self):
        temp = copy.copy(self.top[:,0])
        self.top[:,0] = self.back[:,2][::-1]
        self.back[:,2] = self.bottom[:,0][::-1]
        self.bottom[:,0] = self.front[:,0]
        self.front[:,0] = temp

        temp = copy.copy(self.left[2,1:])
        self.left[2,1:] = self.left[:2,2][::-1]
        self.left[:2,2] = self.left[0,:2]
        self.left[0,:2] = self.left[1:,0][::-1]
        self.left[1:,0] = temp

    def handle_bottom_left(self):
        temp = copy.copy(self.front[2])
        self.front[2] = self.right[2]
        self.right[2] = self.back[2]
        self.back[2] = self.left[2]
        self.left[2] = temp

        temp = copy.copy(self.bottom[2,1:])
        self.bottom[2,1:] = self.bottom[1:,0]
        self.bottom[1:,0] = self.bottom[0,:2][::-1]
        self.bottom[0,:2] = self.bottom[:2,2]
        self.bottom[:2,2] = temp[::-1]

    def handle_bottom_right(self):
        temp = copy.copy(self.front[2])
        self.front[2] = self.left[2]
        self.left[2] = self.back[2]
        self.back[2] = self.right[2]
        self.right[2] = temp

        temp = copy.copy(self.bottom[2,1:])
        self.bottom[2,1:] = self.bottom[:2,2][::-1]
        self.bottom[:2,2] = self.bottom[0,:2]
        self.bottom[0,:2] = self.bottom[1:,0][::-1]
        self.bottom[1:,0] = temp

    def handle_right_up(self):
        temp = copy.copy(self.top[:,2])
        self.top[:,2] = self.front[:,2]
        self.front[:,2] = self.bottom[:,2]
        self.bottom[:,2] = self.back[:,0][::-1]
        self.back[:,0] = temp[::-1]

        temp = copy.copy(self.right[2,1:])
        self.right[2,1:] = self.right[:2,2][::-1]
        self.right[:2,2] = self.right[0,:2]
        self.right[0,:2] = self.right[1:,0][::-1]
        self.right[1:,0] = temp

    def handle_right_down(self):
        temp = copy.copy(self.top[:,2])
        self.top[:,2] = self.back[:,0][::-1]
        self.back[:,0] = self.bottom[:,2][::-1]
        self.bottom[:,2] = self.front[:,2]
        self.front[:,2] = temp

        temp = copy.copy(self.right[2,1:])
        self.right[2,1:] = self.right[1:,0]
        self.right[1:,0] = self.right[0,:2][::-1]
        self.right[0,:2] = self.right[:2,2]
        self.right[:2,2] = temp[::-1]

    def handle_front_left(self):
        temp = copy.copy(self.top[2])
        self.top[2] = self.right[:,0]
        self.right[:,0] = self.bottom[0][::-1]
        self.bottom[0] = self.left[:,2]
        self.left[:,2] = temp[::-1]

        temp = copy.copy(self.front[2,1:])
        self.front[2,1:] = self.front[1:,0]
        self.front[1:,0] = self.front[0,:2][::-1]
        self.front[0,:2] = self.front[:2,2]
        self.front[:2,2] = temp[::-1]

    def handle_front_right(self):
        temp = copy.copy(self.top[2])
        self.top[2] = self.left[:,2][::-1]
        self.left[:,2] = self.bottom[0]
        self.bottom[0] = self.right[:,0][::-1]
        self.right[:,0] = temp

        temp = copy.copy(self.front[2,1:])
        self.front[2,1:] = self.front[:2,2][::-1]
        self.front[:2,2] = self.front[0,:2]
        self.front[0,:2] = self.front[1:,0][::-1]
        self.front[1:,0] = temp

    def assemble(self):
        cube = np.zeros((11,15))
        cube[4:7,0:3]=self.back
        cube[4:7,4:7]=self.left
        cube[4:7,8:11]=self.front
        cube[4:7,12:15]=self.right
        cube[0:3,8:11]=self.top
        cube[8:11,8:11]=self.bottom

        image = np.kron(cube, np.ones((50,50)))
        image_rgb = np.zeros((550,750,3))
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                match image[x,y]:
                    case 1:image_rgb[x,y] = [255,255,255]
                    case 2:image_rgb[x,y] = [255,0,0]
                    case 3:image_rgb[x,y] = [0,255,0]
                    case 4:image_rgb[x,y] = [0,0,255]
                    case 5:image_rgb[x,y] = [255,255,0]
                    case 6:image_rgb[x,y] = [255,122,0]

        image = Image.fromarray(image_rgb.astype(np.uint8), mode='RGB')
        image = ImageTk.PhotoImage(image=image)
        return image