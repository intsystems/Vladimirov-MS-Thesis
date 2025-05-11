import pandas as pd
from pyEDM import CCM


motor_ccm_df = pd.read_csv("../data/motor_ccm_df.csv")

test_valid_df_res = CCM(
    dataFrame=motor_ccm_df,
    E=6,
    sample=2,
    embedded=True,
    columns=[f'motor_eeg_{i+1}' for i in range(6)],
    target="acc",
    showPlot=True,
    returnObject=True,
    libSizes="1000 1001",
    validLib=pd.Series([True] * 1000 + [False] * (len(motor_ccm_df) - 1000))
);

# motor_res.Project(sequential=True)
