#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

def run_tests():
    print("========================================")
    print(" 1. CAS CLASSIQUES (Normal cases)")
    print("========================================")
    
    # Circle Area & Perimeter
    circle = Circle(radius=5)
    print(f"[Circle r=5] Area: {circle.area()} | Perimeter: {circle.perimeter()}")
    shape_info(circle)
    print()

    # Rectangle Area & Perimeter
    rect = Rectangle(width=4, height=7)
    print(f"[Rectangle 4x7] Area: {rect.area()} | Perimeter: {rect.perimeter()}")
    shape_info(rect)
    print()

    print("========================================")
    print(" 2. CAS LIMITES : ZÉRO (Zero dimensions)")
    print("========================================")
    
    # Circle 0 Radius
    circle_zero = Circle(radius=0)
    print(f"[Circle r=0] Area: {circle_zero.area()} | Perimeter: {circle_zero.perimeter()}")
    shape_info(circle_zero)
    print()

    # Rectangle 0 dimensions
    rect_zero = Rectangle(width=0, height=0)
    print(f"[Rectangle 0x0] Area: {rect_zero.area()} | Perimeter: {rect_zero.perimeter()}")
    shape_info(rect_zero)
    print()

    print("========================================")
    print(" 3. CAS LIMITES : NÉGATIFS (Negative dimensions)")
    print("========================================")
    
    # Circle negative radius
    try:
        circle_neg = Circle(radius=-5)
        print(f"[Circle r=-5] Area: {circle_neg.area()} | Perimeter: {circle_neg.perimeter()}")
        shape_info(circle_neg)
    except Exception as e:
        print(f"[Circle r=-5] Exception levée : {e}")
    print()

    # Rectangle negative dimensions
    try:
        rect_neg = Rectangle(width=-4, height=-7)
        print(f"[Rectangle -4x-7] Area: {rect_neg.area()} | Perimeter: {rect_neg.perimeter()}")
        shape_info(rect_neg)
    except Exception as e:
        print(f"[Rectangle -4x-7] Exception levée : {e}")
    print()

if __name__ == "__main__":
    run_tests()