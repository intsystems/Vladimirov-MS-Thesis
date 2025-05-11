import os, sys, pandas as pd
from pathlib import Path
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri


pandas2ri.activate()                       # R ⇄ pandas auto-conversion

# ---------------------------------------------------------------------
# 1.  ─── USER SETTINGS ───────────────────────────────────────────────
# ---------------------------------------------------------------------
FILENAMES = ("magic-irri", "arth150", "mehra-original")
N_ROWS = 5000
SEED = 42

# install.packages(
#   "https://cran.r-project.org/src/contrib/Archive/bnlearn/bnlearn_4.7.1.tar.gz",
#   repos = NULL, type = "source"
# )

for filename in FILENAMES:
    R_FILE = f"../data/{filename}.rds"         # .rds  or .rda
    # ---------------------------------------------------------------------
    
    # 2.  ─── load the network into R -------------------------------------
    R_FILE = Path(R_FILE).expanduser().resolve()
    
    if R_FILE.suffix.lower() == ".rds":
        ro.r(f'bn <- readRDS("{R_FILE.as_posix()}")')
    else:                                      # .rda
        ro.r(f'load("{R_FILE.as_posix()}")')   # creates object 'bn' inside R
    
    # Make sure bnlearn v4.7.1 is available
    ro.r('library(bnlearn)')                   # errors if package missing
    
    # 3.  ─── simulate N_ROWS i.i.d. rows ---------------------------------
    ro.r(f'set.seed({SEED})') 
    ro.r(f'df_sim <- rbn(bn, {N_ROWS})')
    
    # 4.  ─── pull into pandas and save CSV -------------------------------
    df = pandas2ri.rpy2py(ro.r('df_sim'))      # R → pandas
    csv_path = R_FILE.with_name(f"{R_FILE.stem}_sim{N_ROWS}.csv")
    df.to_csv(csv_path, index=False)
    
    print(f"✓ Generated {df.shape[0]}×{df.shape[1]} table → {csv_path}")
    
    arcs_df = pandas2ri.rpy2py(
        ro.r('as.data.frame(arcs(bn))')   # columns: "from" "to"
    )

    # 4-bis-a  save as edge-list CSV
    edges_csv = R_FILE.with_name(f"{R_FILE.stem}_edges.csv")
    arcs_df.to_csv(edges_csv, index=False)
    print(f"✓ Wrote edge list → {edges_csv}")

