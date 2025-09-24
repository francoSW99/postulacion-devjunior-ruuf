from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    wp=panel_width
    hp=panel_height
    wr=roof_width
    hr=roof_height
    #CASO CRITICO: Paneles mas grandes que el techo 
    if (wp>wr or hp>hr) and (wp>hr or hp>wr):
        final=0
    else:
        #CASO 1: Paneles en vertical, de "pie"
        #a)cuantas paneles caben en el ancho del techo
        pv_in_r_w=wr//wp
        #b)cuantas paneles caben en el alto del techo
        pv_in_r_h=hr//hp
        #c)cuantos paneles caben en el techo
        pv_in_r=pv_in_r_w*pv_in_r_h


        #CASO 2: Paneles en horizontal, "acostados"
        #a)cuantas paneles caben en el ancho del techo
        ph_in_r_w=wr//hp
        #b)cuantas paneles caben en el alto del techo
        ph_in_r_h=hr//wp
        #c)cuantos paneles caben en el techo
        ph_in_r=ph_in_r_w*ph_in_r_h

        final=max(pv_in_r,ph_in_r)

    return final


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
