# Coined-Quantum-Walks

> ⚠️ This is the original version of my Quantum Walks project.  
> I’m currently working on a complete rewrite with improved structure and explanations and optimised codes/scripts

## Project Structure

```text
Coined-Quantum-Walks/
├── src/                     # Core simulation scripts
│   ├── 1D_runs/             # 1D quantum walk runs
│   │   ├── run_1d_example.py
│   │   ├── 1d_ee.py         # Entanglement entropy scripts
│   │   ├── 1d_fidelity.py   # State fidelity scripts
│   │   └── 1D_PV.py         # Participation value scripts
│   ├── 2D_runs/             # 2D quantum walk runs
│   │   ├── run_2d_example.py
│   │   ├── 2d_ee.py
│   │   ├── 2d_fidelity.py
│   │   └── 2d_pv.py
│   └── 3D_runs/             # 3D quantum walk runs
│       ├── run_3d_example.py
│       ├── 3d_ee.py
│       ├── 3d_fidelity.py
│       └── 3d_pv.py
│
├── plotters/                # Scripts for generating plots
│   ├── 1D_plotting/          # 1D plots
│   │   ├── 1D_EE_plot.py
│   │   ├── 1D_SF_plot.py
│   │   └── 1D_PV_plot.py
│   ├── 2D_plotting/          # 2D plots
│   │   ├── 2D_EE_plot.py
│   │   ├── 2D_SF_plot.py
│   │   └── 2D_PV_plot.py
│   └── 3D_plotting/          # 3D plots
│       ├── 3D_EE_plot.py
│       ├── 3D_SF_plot.py
│       └── 3D_PV_plot.py
│
├── HPC_jobs/                # SLURM scripts for HPC clusters
│   ├── 1D_jobs/
│   │   ├── 1D_EE_job.sh
│   │   ├── 1D_SF_job.sh
│   │   └── 1D_PV_job.sh
│   ├── 2D_jobs/
│   │   ├── 2D_EE.sh
│   │   ├── 2d_SF.sh
│   │   └── 2D_PV.sh
│   └── 3D_jobs/
│       ├── 3D_EE.sh
│       ├── 3D_SF.sh
│       └── 3D_PV.sh
│
├── output/                  # Simulation results
│   ├── data/                # Raw simulation data
│   └── logs/                # HPC and simulation logs
│
├── LICENSE                  # MIT License
└── README.md
