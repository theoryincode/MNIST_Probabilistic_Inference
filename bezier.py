import numpy as np

def bezier(control_points):
    """Returns list of points on cubic Bezier curve of given by control_points,
       for later use in cv2.polylines().
       control_points is an np.array."""
    t=np.linspace(0,1,101,endpoint=True,dtype=np.float64)
    points=np.zeros((len(t),2),dtype=np.float64)
    for idx, ti in enumerate(t):
        tmp=(1.0-ti)**3.0*control_points[0] + \
        3.0*(1.0-ti)**2.0*ti*control_points[1] + \
        3.0*(1.0-ti)*ti**2.0*control_points[2] + \
        ti**3.0*control_points[3]
        points[idx]=tmp
    return points    
