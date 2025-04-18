# 🧊 Lattice-Based Particle Simulation

This Python script simulates a simple particle aggregation model using a vertical deposition mechanism and temperature-influenced diffusion via the Metropolis-Hastings algorithm. The simulation visualizes how particles settle and diffuse on a 2D lattice over increasing iterations.

---

## 📦 Features

- Simulates particle deposition on a 2D lattice.
- Uses a sigmoid-transformed Kelvin temperature to influence diffusion probability.
- Displays a series of subplots showing lattice states at different iteration milestones.
- Energy minimization using a Metropolis-Hastings approach.

---

## 🧪 How It Works

1. **Initialization:**
   - User inputs:
     - Lattice size (`L`)
     - Initial and maximum iteration counts
     - Temperature in Kelvins
     - Number of plots to visualize

2. **Temperature Mapping:**
   - Converts the input temperature to a simulation-friendly scale (0–10) using a sigmoid function.

3. **Particle Deposition:**
   - Particles drop from the top of the lattice and settle when blocked.
   - After each drop, diffusion attempts are made depending on local energy differences.

4. **Energy Calculation:**
   - Energy is defined as the number of occupied neighboring cells (up, down, left, right).

5. **Visualization:**
   - Subplots show the state of the lattice at various stages of the simulation.

---

## 📸 Sample Output

The script produces multiple grayscale plots, where white cells represent occupied positions and black ones are empty. Each subplot represents the lattice state at a different iteration count.

---

## ▶️ Requirements

- Python 3.x
- NumPy
- Matplotlib

Install dependencies using pip:

```bash
pip install numpy matplotlib
```
