
from face import recong_face    #或者import face然后 face.recong_face         没有import face.recong_face
from upperbody import recong_upperebody
from lowerbody import recong_lower




rootdir = 'kodenshi'
recong_upperebody(rootdir)
recong_face(rootdir)
recong_lower(rootdir)
