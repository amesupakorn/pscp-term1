""" RuleofThree """

def main(num):
    """ RuleofThree """
    var_sell, var_size, var_ratio = 0, 0, 0
    for _ in range(num):
        sell = float(input())
        size = float(input())
        ratio = size/sell
        if ratio == var_ratio:
            if var_sell > sell:
                var_sell, var_size, var_ratio = sell, size, ratio
        elif ratio > var_ratio:
            var_sell, var_size, var_ratio = sell, size, ratio
    print("%.02f %.02f"% (var_sell, var_size))
main(int(input()))
