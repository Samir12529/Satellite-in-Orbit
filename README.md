# Satellite in Orbit - RK4

This project simulates the orbits of different types of satellites around Earth, including Geostationary satellites, the International Space Station (ISS), and GPS satellites. It also provides an option to simulate two satellites with custom orbital parameters. The simulation is implemented in Python using the Runge-Kutta method (RK4) for numerical integration and Tkinter for the GUI.

Modifiying the initial velocity (or orbital raduius) slightly affect the eccentricity of the orbit, making it more elliptical. Changing the velocity even more can result in a hyperbolic orbit with satellite never returning (a message will pop up).

## GUI instructions

1. Choose the type of satellite orbit you wish to simulate from the dropdown menu.
2. Click "Choose parameters" to input specific parameters for the selected orbit (or you can keep the predifined parameters).
3. After entering the parameters, click "Run Simulation" to start the simulation.
4. The simulation will display the satellite's orbit over time.

## Future Improvements

- Add support for more complex orbital mechanics, such as the influence of the moon or other planets.
- Improve the GUI for a more intuitive user experience.
- Implement 3D visualization of the satellite orbits.