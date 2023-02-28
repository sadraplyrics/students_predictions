import re
import pandas as pd
#profiles = ["ling", "inf", "econ", "france"]
def test_per_1(filename: str, pattern: str):
    matches_arr = []
    with open(filename, "r") as rus:
        text_file = rus.read()
        matches = pattern.finditer(text_file)
        for match in matches:
            matches_arr.append(match.group(0).split(" "))
    for i in matches_arr:
        print(i)

def column(mathces: list, i:int):
    return([row[i] for row in mathces])

def exctract_csv(year: int, number_of_docs: int, pattern: str):
    for i in range(1, number_of_docs+1):
        matches_arr = []
        with open(f"rus_trans_{year}_{i}.txt", 'r') as rus:
            text_file = rus.read()
            matches = pattern.finditer(text_file)
            for match in matches:
                matches_arr.append(match.group(0).split(" "))

        out_df = pd.DataFrame({"name1": column(matches_arr, 1),
                                   "name2": column(matches_arr, 2),
                                   "name3": column(matches_arr, 3),
                                   "scores": column(matches_arr, 4)})
        out_df.to_csv(f"final_{year}_{i}.csv")

if __name__ == "__main__":
    pattern = re.compile(r"(\d+|\|)\.\s.+")
    exctract_csv(2018, 4, pattern)
    






