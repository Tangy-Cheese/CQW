
import numpy as np
import matplotlib.pyplot as plt

def plot_3d_entanglement(ent_file, selected_W=None):
    """
    Loads the aggregated 3D entanglement file and plots entanglement entropy vs. time.
    Expects:
      - "times": array of shape (num_times,)
      - Keys "W=0.0", etc., each mapping to an array of shape (num_times,)
    """
    data = np.load(ent_file, allow_pickle=True)
    if "times" not in data:
        print("Error: 'times' not found.")
        return
    times = data["times"]
    if selected_W is None:
         selected_W = [k for k in data.keys() if k.startswith("W=")]
    plt.figure(figsize=(10,6))
    for w_str in sorted(selected_W, key=lambda x: float(x[2:])):
         arr = data[w_str]
         if arr is None or arr.ndim != 1:
              print(f"Skipping {w_str}: unexpected shape {np.shape(arr)}")
              continue
         plt.plot(times, arr, label=w_str)
    plt.xlabel("Time (t)")
    plt.ylabel("Entanglement Entropy (nats)")
    plt.ylim(1.45,2.1)
    plt.title("3D Entanglement Entropy vs. Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    ent_file = rf"C:\Users\Louis\Physics_Project\Programming\Report(Hopefully)\aggregated_3D_entanglementFINAL_Proper1.npz"
    plot_3d_entanglement(ent_file)
