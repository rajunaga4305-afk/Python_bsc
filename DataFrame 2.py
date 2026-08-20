import pandas as pd
d1={
"Name":["yashu","nagaraju","janu"],
"Age":[18,45,14]
}
d2=pd.DataFrame(d1)
print(d2)
print(d2["Age"].mean())