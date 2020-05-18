import numpy as np
from colormath.color_objects import sRGBColor, HSLColor
from colormath.color_conversions import convert_color
from sklearn.preprocessing import PolynomialFeatures
import joblib

def modify_rgb(rgb_tuple, level=0.5,pipe=[]):
    rgb = rgb_int_to_float(rgb_tuple)
    rgb_class = sRGBColor(rgb[0], rgb[1], rgb[2])
    hsl = convert_color(rgb_class, HSLColor).get_value_tuple()
    intensity = get_intensity(int(hsl[0]),pipe)
    new_hsl = convert(hsl, intensity, level,pipe)
    new_hsl = HSLColor(new_hsl[0],new_hsl[1],new_hsl[2])
    new_rgb = convert_color(new_hsl, sRGBColor).get_value_tuple()
    new_rgb_int = rgb_float_to_int(new_rgb)
    return new_rgb_int

def get_intensity(x,pipe):
    
    n = len(pipe.coef_[0])
    exponents = np.array([*range(0, n, 1)])
    list_x = np.array([x]*n)
    return pipe.predict([np.array(np.power(list_x,exponents))])[0][0]

def convert(rgb_tuple, intensity, level,pipe):
    return (rgb_tuple[0], brigthness_level(rgb_tuple[1],intensity,level,pipe), rgb_tuple[2])
        
def brigthness_level(color, downgrade, level,pipe):
    if(downgrade < 0 or color >= 260):
        downgrade = 0
    return (color*level)*(1 + downgrade)

def rgb_int_to_float(rgb_int):
    return (float(rgb_int[0]/255.00000), float(rgb_int[1]/255.00000),  float(rgb_int[2]/255.00000))

def rgb_float_to_int(rgb):
    return (int(rgb[0]*255), int(rgb[1]*255),  int(rgb[2]*255))