import numpy as np
import tkinter as tk

class Satellite_in_Orbit:
    def __init__(self, center_mass, starting_position, starting_velocity, time, step):
        self.Gravity_constant = 6.67408e-11 # Jeyba mnel net
        self.starting_pos = starting_position # starting position te3 el satellite relative 3al terre
        self.starting_vel = starting_velocity # starting velocity te3 el satellite
        self.c_mass = center_mass
        self.step = step # bkabero kermel sarri3 el simulation (ma 3endo unite)
        self.end = time # kam yom el cycle baddo IN SECONDS
    
    def velocityX(self, posX, posY): #formula to find velocity
        return -(self.c_mass * self.Gravity_constant * posX) / ((posX ** 2 + posY ** 2) ** (3 / 2)) #Newton Law of universal gravitation: F=(G*m1*m2)/r^2
    def velocityY(self, posX, posY):
        return -(self.c_mass * self.Gravity_constant * posY) / ((posX ** 2 + posY ** 2) ** (3 / 2))
    def velocityXO(self, posX1, posY1, posX2, posY2): #formula to find velocity
        return -(self.c_mass * self.Gravity_constant * posX1) / ((posX1 ** 2 + posY1 ** 2) ** (3 / 2)) , -(self.c_mass * self.Gravity_constant * posX2) / ((posX2 ** 2 + posY2 ** 2) ** (3 / 2)) #Newton Law of universal gravitation: F=(G*m1*m2)/r^2
    def velocityYO(self, posX1, posY1, posX2, posY2):
        return -(self.c_mass * self.Gravity_constant * posY1) / ((posX1 ** 2 + posY1 ** 2) ** (3 / 2)) , -(self.c_mass * self.Gravity_constant * posY2) / ((posX2 ** 2 + posY2 ** 2) ** (3 / 2))
    
    
    def Find_All_K (self, posX, posY, velX, velY):
        # k1
        k1pos_x = velX
        k1pos_y = velY
        k1vel_x = self.velocityX(posX, posY)
        k1vel_y = self.velocityY(posX, posY)
        # k2
        k2pos_x = velX + (self.step * k1vel_x) / 2
        k2pos_y = velY + (self.step * k1vel_y) / 2
        k2vel_x = self.velocityX(posX + (self.step * k1pos_x) / 2, posY + (self.step * k1pos_y) / 2)
        k2vel_y = self.velocityY(posX + (self.step * k1pos_x) / 2, posY + (self.step * k1pos_y) / 2)
        # k3
        k3pos_x = velX + (self.step * k2vel_x) / 2
        k3pos_y = velY + (self.step * k2vel_y) / 2
        k3vel_x = self.velocityX(posX + (self.step * k2pos_x) / 2, posY + (self.step * k2pos_y) / 2)
        k3vel_y = self.velocityY(posX + (self.step * k2pos_x) / 2, posY + (self.step * k2pos_y) / 2) 
        # k4
        k4pos_x = velX + self.step * k3vel_x
        k4pos_y = velY + self.step * k3vel_y
        k4vel_x = self.velocityX(posX + self.step * k3pos_x, posY + self.step * k3pos_y)
        k4vel_y = self.velocityY(posX + self.step * k3pos_x, posY + self.step * k3pos_y)
        return [k1pos_x, k2pos_x, k3pos_x, k4pos_x], [k1pos_y, k2pos_y, k3pos_y, k4pos_y], [k1vel_x, k2vel_x, k3vel_x, k4vel_x], [k1vel_y, k2vel_y, k3vel_y, k4vel_y]
    def Find_All_KO (self, posX1, posY1, velX1, velY1, posX2, posY2, velX2, velY2):
        # k1
        k1pos_x1 = velX1
        k1pos_y1 = velY1
        k1vel_x1 = self.velocityXO(posX1, posY1)
        k1vel_y1 = self.velocityYO(posX1, posY1)
        # k2
        k2pos_x1 = velX1 + (self.step * k1vel_x1) / 2
        k2pos_y1 = velY1 + (self.step * k1vel_y1) / 2
        k2vel_x1 = self.velocityXO(posX1 + (self.step * k1pos_x1) / 2, posY1 + (self.step * k1pos_y1) / 2)
        k2vel_y1 = self.velocityYO(posX1 + (self.step * k1pos_x1) / 2, posY1 + (self.step * k1pos_y1) / 2)
        # k3
        k3pos_x1 = velX1 + (self.step * k2vel_x1) / 2
        k3pos_y1 = velY1 + (self.step * k2vel_y1) / 2
        k3vel_x1 = self.velocityXO(posX1 + (self.step * k2pos_x1) / 2, posY1 + (self.step * k2pos_y1) / 2)
        k3vel_y1 = self.velocityYO(posX1+ (self.step * k2pos_x1) / 2, posY1 + (self.step * k2pos_y1) / 2) 
        # k4
        k4pos_x1 = velX1 + self.step * k3vel_x1
        k4pos_y1 = velY1 + self.step * k3vel_y1
        k4vel_x1 = self.velocityXO(posX1 + self.step * k3pos_x1, posY1 + self.step * k3pos_y1)
        k4vel_y1 = self.velocityYO(posX1 + self.step * k3pos_x1, posY1 + self.step * k3pos_y1)
        # k1
        k1pos_x2 = velX2
        k1pos_y2 = velY2
        k1vel_x2 = self.velocityXO(posX2, posY2)
        k1vel_y2 = self.velocityYO(posX2, posY2)
        # k2
        k2pos_x2 = velX2 + (self.step * k1vel_x2) / 2
        k2pos_y2 = velY2 + (self.step * k1vel_y2) / 2
        k2vel_x2 = self.velocityXO(posX2 + (self.step * k1pos_x2) / 2, posY2 + (self.step * k1pos_y2) / 2)
        k2vel_y2 = self.velocityYO(posX2 + (self.step * k1pos_x2) / 2, posY2 + (self.step * k1pos_y2) / 2)
        # k3
        k3pos_x2 = velX2 + (self.step * k2vel_x2) / 2
        k3pos_y2 = velY2+ (self.step * k2vel_y2) / 2
        k3vel_x2 = self.velocityXO(posX2 + (self.step * k2pos_x2) / 2, posY2 + (self.step * k2pos_y2) / 2)
        k3vel_y2 = self.velocityYO(posX2 + (self.step * k2pos_x2) / 2, posY2 + (self.step * k2pos_y2) / 2) 
        # k4
        k4pos_x2 = velX2 + self.step * k3vel_x2
        k4pos_y2 = velY2 + self.step * k3vel_y2
        k4vel_x2 = self.velocityXO(posX2 + self.step * k3pos_x2, posY2 + self.step * k3pos_y2)
        k4vel_y2 = self.velocityYO(posX2 + self.step * k3pos_x2, posY2 + self.step * k3pos_y2)
        return [k1pos_x1, k2pos_x1, k3pos_x1, k4pos_x1], [k1pos_y1, k2pos_y1, k3pos_y1, k4pos_y1], [k1vel_x1, k2vel_x1, k3vel_x1, k4vel_x1], [k1vel_y1, k2vel_y1, k3vel_y1, k4vel_y1], [k1pos_x2, k2pos_x2, k3pos_x2, k4pos_x2], [k1pos_y2, k2pos_y2, k3pos_y2, k4pos_y2], [k1vel_x2, k2vel_x2, k3vel_x2, k4vel_x2], [k1vel_y2, k2vel_y2, k3vel_y2, k4vel_y2]
    
    
    def next_position(self, posX, posY, kpos_xlist, kpos_ylist): #The next time step.
        posX = posX + (self.step / 6) * (kpos_xlist[0] + 2 * kpos_xlist[1] + 2 * kpos_xlist[2] + kpos_xlist[3])
        posY = posY + (self.step / 6) * (kpos_ylist[0] + 2 * kpos_ylist[1] + 2 * kpos_ylist[2] + kpos_ylist[3])
        return posX, posY
    def next_velocity(self, velX, velY, kvel_xlist, kvel_ylist):
        velX = velX + (self.step / 6) * (kvel_xlist[0] + 2 * kvel_xlist[1] + 2 * kvel_xlist[2] + kvel_xlist[3])
        velY = velY + (self.step / 6) * (kvel_ylist[0] + 2 * kvel_ylist[1] + 2 * kvel_ylist[2] + kvel_ylist[3])
        return velX, velY
    def next_positionO(self, posX1, posY1, kpos_xlist1, kpos_ylist1, posX2, posY2, kpos_xlist2, kpos_ylist2): #The next time step.
        posX1 = posX1 + (self.step / 6) * (kpos_xlist1[0] + 2 * kpos_xlist1[1] + 2 * kpos_xlist1[2] + kpos_xlist1[3])
        posY1 = posY1 + (self.step / 6) * (kpos_ylist1[0] + 2 * kpos_ylist1[1] + 2 * kpos_ylist1[2] + kpos_ylist1[3])
        posX2 = posX2 + (self.step / 6) * (kpos_xlist2[0] + 2 * kpos_xlist2[1] + 2 * kpos_xlist2[2] + kpos_xlist2[3])
        posY2 = posY2 + (self.step / 6) * (kpos_ylist2[0] + 2 * kpos_ylist2[1] + 2 * kpos_ylist2[2] + kpos_ylist2[3])
        return posX1, posY1, posX2, posY2
    def next_velocityO(self, velX1, velY1, kvel_xlist1, kvel_ylist1, velX2, velY2, kvel_xlist2, kvel_ylist2):
        velX1 = velX1 + (self.step / 6) * (kvel_xlist1[0] + 2 * kvel_xlist1[1] + 2 * kvel_xlist1[2] + kvel_xlist1[3])
        velY1 = velY1 + (self.step / 6) * (kvel_ylist1[0] + 2 * kvel_ylist1[1] + 2 * kvel_ylist1[2] + kvel_ylist1[3])
        velX2 = velX2 + (self.step / 6) * (kvel_xlist2[0] + 2 * kvel_xlist2[1] + 2 * kvel_xlist2[2] + kvel_xlist2[3])
        velY2 = velY2 + (self.step / 6) * (kvel_ylist2[0] + 2 * kvel_ylist2[1] + 2 * kvel_ylist2[2] + kvel_ylist2[3])
        return velX1, velY1, velX2, velY2
    
    def time_Control(self):
        return np.linspace(0, self.end, int(self.end / self.step) + 1) #array 3endo nafes el step men starting time lal final time
    
    def orbit_track (self):  # x y components (position and velocity) of the ENTIRE simulation!
        posX, posY = self.starting_pos[0], self.starting_pos[1]
        velX, velY = self.starting_vel[0], self.starting_vel[1]
        time_list = self.time_Control()
        rx, ry = np.zeros(len(time_list)), np.zeros(len(time_list))
        rdotx, rdoty = np.zeros(len(time_list)), np.zeros(len(time_list))
        for i in range(0, len(time_list)):
            kpos_xlist, kpos_ylist, kvel_xlist, kvel_ylist = self.Find_All_K(posX, posY, velX, velY) #3abbet el lists of k
            posX, posY = self.next_position(posX, posY, kpos_xlist, kpos_ylist) #position of next time step
            velX, velY = self.next_velocity(velX, velY, kvel_xlist, kvel_ylist)
            rx[i], ry[i], rdotx[i], rdoty[i] = posX, posY, velX, velY #ma ken fi lzoum a3mol increment i   car in next_velocity 3ende +=
        return rx, ry, rdotx, rdoty
    def orbit_trackO (self):  # x y components (position and velocity) of the ENTIRE simulation!
        posX1, posY1 = self.starting_pos[0], self.starting_pos[1]
        velX1, velY1 = self.starting_vel[0], self.starting_vel[1]
        posX2, posY2 = self.starting_pos[0], self.starting_pos[1]
        velX2, velY2 = self.starting_vel[0], self.starting_vel[1]
        time_list = self.time_Control()
        rx1, ry1 = np.zeros(len(time_list)), np.zeros(len(time_list))
        rdotx1, rdoty1 = np.zeros(len(time_list)), np.zeros(len(time_list))
        rx2, ry2 = np.zeros(len(time_list)), np.zeros(len(time_list))
        rdotx2, rdoty2 = np.zeros(len(time_list)), np.zeros(len(time_list))
        for i in range(0, len(time_list)):
            kpos_xlist1, kpos_ylist1, kvel_xlist1, kvel_ylist1, kpos_xlist2, kpos_ylist2, kvel_xlist2, kvel_ylist2 = self.Find_All_KO(posX1, posY1, velX1, velY1, posX2, posY2, velX2, velY2) #3abbet el lists of k
            posX1, posY1, posX2, posY2 = self.next_positionO(posX1, posY1, kpos_xlist1, kpos_ylist1, posX2, posY2, kpos_xlist2, kpos_ylist2) #position of next time step
            velX1, velY1, velX2, velY2 = self.next_velocityO(velX1, velY1, kvel_xlist1, kvel_ylist1, velX2, velY2, kvel_xlist2, kvel_ylist2)
            rx1[i], ry1[i], rdotx1[i], rdoty1[i], rx2[i], ry2[i], rdotx2[i], rdoty2[i] = posX1, posY1, velX1, velY1, posX2, posY2, velX2, velY2
        return rx1, ry1, rdotx1, rdoty1, rx2, ry2, rdotx2, rdoty2

    def animation(rx, ry, rdotx, rdoty):
        root = tk.Tk() # create GUI window
        root.title("Satellite in Orbit Simulation")
        window_width = 500 # window dimensions
        window_height = 500
        centerX = window_width / 2 # centre of the window
        centerY = window_height / 2
        scaleX = (window_width - 100) / (2 * rx.max() - rx.min())  # rx>>>canvas donc 8iyaret el scale kermel chuf el animation mazbuta
        scaleY = (window_height - 100) / (2 * ry.max() - ry.min())
        #fixing the scale
        rx *= scaleX
        ry *= -scaleY
        rx += centerX
        ry += centerY
        window = tk.Canvas(root, width = window_width, height = window_height, bg = "#C0C0C0") # initializing canvas
        window.pack() # adjusting window dimensions to fit
        #drawing two circles (earth on the center and satellite on the orbit)
        radius_e = 20
        radius_s = 5
        x0e, y0e, x1e, y1e = centerX - radius_e, centerY - radius_e, centerX + radius_e, centerY + radius_e
        x0s, y0s, x1s, y1s = centerX, centerY, centerX, centerY
        earth = window.create_oval(x0e, y0e, x1e, y1e, fill = "blue", outline = "")
        satellite = window.create_oval(x0s, y0s, x1s, y1s, fill = "red", outline = "")
        #radial_line = window.create_line(centerX, centerY, centerX, centerY, fill = "white")
        earth_text = window.create_text(centerX + 15, centerY + 15, text = "EARTH", fill = "blue", anchor = "nw")  # fixed
        satellite_text = window.create_text(rx[0] + 10, ry[0] + 10, text = "SATELLITE", fill = "red", anchor = "s") #follows the orbit
        coordinates = [] # array of live positions
        for i in range(0, len(rdotx)):
            coordinates.append(rx[i])
            coordinates.append(ry[i])
        window.create_polygon(coordinates, outline = "blue", dash = ".", fill = "") #creates any polygon (mostly likeley an ellipse or circle)
        j = 0
        while j <= len(rdotx) + 1:
            if j == len(rdotx):
                j = 0
            window.coords(satellite, rx[j] - radius_s, ry[j] - radius_s, rx[j] + radius_s, ry[j] + radius_s) # steps through the satellite
            window.coords(satellite_text, rx[j], ry[j] - 10) # steps through satellite's text
            #window.coords(radial_line, centerX, centerY, rx[j], ry[j])
            distance = np.sqrt(((centerX - rx[j]) ** 2) + ((centerY - ry[j]) ** 2)) * 2 / (scaleX + scaleY) # determines the distance between the orbiting and central mass
            if distance < 6371e3:     # radius of the distance is smaller than radius of earth itself?!
                print("Unstable Orbit, Satellite has crashed!")
                #crash_label.config(text="Unstable Orbit, Satellite has crashed!", fg="red")
                window.create_text(250, 350, text = "Crash!", fill = "red", font= 30)
                break
            if distance > 8e7: #after this distance, the physicians won't be able to reover or even track the satellite
                print("Out of Orbit!")
                #crash_label.config(text="Unstable Orbit, Satellite has crashed!", fg="red")
                window.create_text(250, 350, text = "Out of orbit!", fill = "red", font= 30)
                break
            # displaying a live RK4
            velocity = np.sqrt(rdotx[j] ** 2 + rdoty[j] ** 2)
            velocity, distance = "%.4f" % velocity, "%.4f" % distance  # %.4f represents floating point rouded to 4
            orbital_rad = window.create_text(250, 450, text = "Orbital Raduis : " + distance + " m", fill = "blue")
            live_velocity = window.create_text(250, 470, text = "Satellite Velocity : " + velocity + " m/s", fill = "blue")
            window.after(1, window.update())
            window.delete(orbital_rad)
            window.delete(live_velocity)
            j += 1
        root.mainloop() # enter main loop to wait for the user even
    def animationO(rx1, ry1, rdotx1, rdoty1, rx2, ry2, rdotx2, rdoty2):
        root = tk.Tk() # create GUI window
        root.title("Satellite in Orbit Simulation")
        window_width = 500 # window dimensions
        window_height = 500
        centerX = window_width / 2 # centre of the window
        centerY = window_height / 2
        scaleX1 = (window_width - 100) / (2 * rx1.max() - rx1.min())  # rx>>>canvas donc 8iyaret el scale kermel chuf el animation mazbuta
        scaleY1 = (window_height - 100) / (2 * ry1.max() - ry1.min())
        #fixing the scale
        rx1 *= scaleX1
        ry1 *= -scaleY1
        rx1 += centerX
        ry1 += centerY
        scaleX2 = (window_width) / (2 * rx2.max() - rx2.min())  # rx>>>canvas donc 8iyaret el scale kermel chuf el animation mazbuta
        scaleY2 = (window_height) / (2 * ry2.max() - ry2.min())
        #fixing the scale
        rx2 *= scaleX2
        ry2 *= -scaleY2
        rx2 += centerX
        ry2 += centerY
        window = tk.Canvas(root, width = window_width, height = window_height, bg = "#C0C0C0") # initializing canvas
        window.pack() # adjusting window dimensions to fit
        #drawing two circles (earth on the center and satellite on the orbit)
        radius_e = 20
        radius_s1 = 5
        radius_s2 = 5
        x0e, y0e, x1e, y1e = centerX - radius_e, centerY - radius_e, centerX + radius_e, centerY + radius_e
        x0s, y0s, x1s, y1s = centerX, centerY, centerX, centerY
        earth = window.create_oval(x0e, y0e, x1e, y1e, fill = "blue", outline = "")
        satellite1 = window.create_oval(x0s, y0s, x1s, y1s, fill = "red", outline = "")
        satellite2 = window.create_oval(x0s, y0s, x1s, y1s, fill = "red", outline = "")
        #radial_line = window.create_line(centerX, centerY, centerX, centerY, fill = "white")
        earth_text = window.create_text(centerX + 15, centerY + 15, text = "EARTH", fill = "blue", anchor = "nw")  # fixed
        satellite_text1 = window.create_text(rx1[0] + 10, ry1[0] + 10, text = "SATELLITE1", fill = "red", anchor = "s") #follows the orbit
        coordinates1 = [] # array of live positions
        satellite_text2 = window.create_text(rx2[0] + 10, ry2[0] + 10, text = "SATELLITE2", fill = "red", anchor = "s") #follows the orbit
        coordinates2 = [] # array of live positions
        for i in range(0, len(rdotx1)):
            coordinates1.append(rx1[i])
            coordinates1.append(ry1[i])
        window.create_polygon(coordinates1, outline = "blue", dash = ".", fill = "") #creates any polygon (mostly likeley an ellipse or circle)
        for i in range(0, len(rdotx2)):
            coordinates2.append(rx2[i])
            coordinates2.append(ry2[i])
        window.create_polygon(coordinates2, outline = "blue", dash = ".", fill = "") #creates any polygon (mostly likeley an ellipse or circle)
        j1 = 0
        while j1 <= len(rdotx1) + 1 :
            if j1 == len(rdotx1):
                j1 = 0
            window.coords(satellite1, rx1[j1] - radius_s1, ry1[j1] - radius_s1, rx1[j1] + radius_s1, ry1[j1] + radius_s1) # steps through the satellite
            window.coords(satellite_text1, rx1[j1], ry1[j1] - 10) # steps through satellite's text
            window.coords(satellite2, rx2[j1] - radius_s2, ry2[j1] - radius_s2, rx2[j1] + radius_s2, ry2[j1] + radius_s2) # steps through the satellite
            window.coords(satellite_text2, rx2[j1], ry2[j1] - 10) # steps through satellite's text
            #window.coords(radial_line, centerX, centerY, rx[j], ry[j])
            distance1 = np.sqrt(((centerX - rx1[j1]) ** 2) + ((centerY - ry1[j1]) ** 2)) * 2 / (scaleX1 + scaleY1) # determines the distance between the orbiting and central mass
            distance2 = np.sqrt(((centerX - rx2[j1]) ** 2) + ((centerY - ry2[j1]) ** 2)) * 2 / (scaleX2 + scaleY2)
            if distance1 < 6371e3 or distance2 < 6371e3:     # radius of the distance is smaller than radius of earth itself?!
                print("Unstable Orbit, Satellite has crashed!")
                #crash_label.config(text="Unstable Orbit, Satellite has crashed!", fg="red")
                window.create_text(250, 350, text = "Crash!", fill = "red", font= 30)
                break
            if distance1 > 10e7 or distance2 > 10e7: #after this distance, the physicians won't be able to reover or even track the satellite
                print("Out of Orbit!")
                #crash_label.config(text="Unstable Orbit, Satellite has crashed!", fg="red")
                window.create_text(250, 350, text = "Out of orbit!", fill = "red", font= 30)
                break
            # displaying a live RK4
            velocity1 = np.sqrt(rdotx1[j1] ** 2 + rdoty1[j1] ** 2)
            velocity1, distance1 = "%.4f" % velocity1, "%.4f" % distance1  # %.4f represents floating point rouded to 4
            orbital_rad1 = window.create_text(350, 450, text = "Orbital Raduis S1: " + distance1 + " m", fill = "blue")
            live_velocity1 = window.create_text(350, 470, text = "Satellite Velocity S1 : " + velocity1 + " m/s", fill = "blue")
            window.after(1, window.update())
            window.delete(orbital_rad1)
            window.delete(live_velocity1)
            velocity2 = np.sqrt(rdotx2[j1] ** 2 + rdoty2[j1] ** 2)
            velocity2, distance2 = "%.4f" % velocity2, "%.4f" % distance2  # %.4f represents floating point rouded to 4
            orbital_rad2 = window.create_text(150, 450, text = "Orbital Raduis S2 : " + distance2 + " m", fill = "blue")
            live_velocity2 = window.create_text(150, 470, text = "Satellite Velocity S2 : " + velocity2 + " m/s", fill = "blue")
            window.after(1, window.update())
            window.delete(orbital_rad2)
            window.delete(live_velocity2)
            j1 += 1
        root.mainloop() # enter main loop to wait for the user even   
        
        
def run_simulationGeo():
    # Retrieve values from entry boxes
    earth_mass = float(run_parametersGeo.earth_mass_entry.get())
    orbital_radius = float(run_parametersGeo.orbital_radius_entry.get())
    satellite_velocity = float(run_parametersGeo.satellite_velocity_entry.get())
    multiplier = float(run_parametersGeo.multiplier_entry.get()) # defines the amount of days the simulation should run through
    catalyse = float(run_parametersGeo.catalyse_entry.get())
    # Run simulation with user-provided parameters
    day = 24 * 60 * 60 # seconds
    earth_radius = 6371e3 # jeyba mnel net (in meters)
    satellite_mass = 6000 # hiye akid akid akid negligeable bel nesbe lal ared
    satellite = Satellite_in_Orbit(earth_mass, [0, orbital_radius], [satellite_velocity, 0], (multiplier * day), (catalyse))
    rx, ry, rdotx, rdoty = satellite.orbit_track() # initializing points of the entire simulation
    Satellite_in_Orbit.animation(rx, ry, rdotx, rdoty) # animating this track
def run_simulationISS():
    # Retrieve values from entry boxes
    earth_mass = float(run_parametersISS.earth_mass_entry.get())
    orbital_radius = float(run_parametersISS.orbital_radius_entry.get())
    satellite_velocity = float(run_parametersISS.satellite_velocity_entry.get())
    multiplier = float(run_parametersISS.multiplier_entry.get()) # defines the amount of days the simulation should run through
    catalyse = float(run_parametersISS.catalyse_entry.get())
    # Run simulation with user-provided parameters
    day = 24 * 60 * 60 # seconds
    earth_radius = 6371e3 # jeyba mnel net (in meters)
    satellite_mass = 450000 # hiye akid akid akid negligeable bel nesbe lal ared
    satellite = Satellite_in_Orbit(earth_mass, [0, orbital_radius], [satellite_velocity, 0], (multiplier * day), (catalyse))
    rx, ry, rdotx, rdoty = satellite.orbit_track() # initializing points of the entire simulation
    Satellite_in_Orbit.animation(rx, ry, rdotx, rdoty) # animating this track    
def run_simulationGPS():
    # Retrieve values from entry boxes
    earth_mass = float(run_parametersGPS.earth_mass_entry.get())
    orbital_radius = float(run_parametersGPS.orbital_radius_entry.get())
    satellite_velocity = float(run_parametersGPS.satellite_velocity_entry.get())
    multiplier = float(run_parametersGPS.multiplier_entry.get()) # defines the amount of days the simulation should run through
    catalyse = float(run_parametersGPS.catalyse_entry.get())
    # Run simulation with user-provided parameters
    day = 24 * 60 * 60 # seconds
    earth_radius = 6371e3 # jeyba mnel net (in meters)
    satellite_mass = 1080 # hiye akid akid akid negligeable bel nesbe lal ared
    satellite = Satellite_in_Orbit(earth_mass, [0, orbital_radius], [satellite_velocity, 0], (multiplier * day), (catalyse))
    rx, ry, rdotx, rdoty = satellite.orbit_track() # initializing points of the entire simulation
    Satellite_in_Orbit.animation(rx, ry, rdotx, rdoty) # animating this track
def run_simulationO():
    # Retrieve values from entry boxes for the first satellite
    earth_mass = float(run_parametersO.earth_mass_entry.get())
    orbital_radius = float(run_parametersO.orbital_radius_entry.get())
    satellite_velocity = float(run_parametersO.satellite_velocity_entry.get())
    multiplier = float(run_parametersO.multiplier_entry.get())  # defines the amount of days the simulation should run through
    catalyse = float(run_parametersO.catalyse_entry.get())
    # Run simulation with user-provided parameters for the first satellite
    day = 24 * 60 * 60  # seconds
    satellite_mass = 350000  # hiye akid akid akid negligeable bel nesbe lal ared
    satellite1 = Satellite_in_Orbit(earth_mass, [0, orbital_radius], [satellite_velocity, 0], (multiplier * day), catalyse)

    # Retrieve values from entry boxes for the second satellite
    orbital_radius2 = float(run_parametersO.orbital_radius_entry2.get())
    satellite_velocity2 = float(run_parametersO.satellite_velocity_entry2.get())
    # Run simulation with user-provided parameters for the second satellite
    satellite2 = Satellite_in_Orbit(earth_mass, [0, orbital_radius2], [satellite_velocity2, 0], (multiplier * day), catalyse)

    # Get orbit tracks for both satellites
    rx1, ry1, rdotx1, rdoty1 = satellite1.orbit_track()
    rx2, ry2, rdotx2, rdoty2 = satellite2.orbit_track()

    # Animate the tracks of both satellites
    Satellite_in_Orbit.animationO(rx1, ry1, rdotx1, rdoty1, rx2, ry2, rdotx2, rdoty2)
    
    
    
def run_parametersGeo():
    root = tk.Tk()
    root.title("Orbit Simulation Parameters")
    # Label and entry box for Earth mass
    earth_mass_label = tk.Label(root, text="Earth Mass (kg):")
    earth_mass_label.grid(row=0, column=0)
    run_parametersGeo.earth_mass_entry = tk.Entry(root)
    run_parametersGeo.earth_mass_entry.grid(row=0, column=1)
    run_parametersGeo.earth_mass_entry.insert(tk.END, "5.972e24")  # Default value
    # Label and entry box for Orbital radius
    orbital_radius_label = tk.Label(root, text="Orbital Radius (m):")
    orbital_radius_label.grid(row=1, column=0)
    run_parametersGeo.orbital_radius_entry = tk.Entry(root)
    run_parametersGeo.orbital_radius_entry.grid(row=1, column=1)
    run_parametersGeo.orbital_radius_entry.insert(tk.END, "42157000")  # Default value
    # Label and entry box for Satellite velocity
    satellite_velocity_label = tk.Label(root, text="Satellite Velocity (m/s):")
    satellite_velocity_label.grid(row=2, column=0)
    run_parametersGeo.satellite_velocity_entry = tk.Entry(root)
    run_parametersGeo.satellite_velocity_entry.grid(row=2, column=1)
    run_parametersGeo.satellite_velocity_entry.insert(tk.END, "3070")  # Default value
    # Label and entry box for multiplier velocity
    multiplier_label = tk.Label(root, text="Number of days:")
    multiplier_label.grid(row=3, column=0)
    run_parametersGeo.multiplier_entry = tk.Entry(root)
    run_parametersGeo.multiplier_entry.grid(row=3, column=1)
    run_parametersGeo.multiplier_entry.insert(tk.END, "1")  # Default value
    # Label and entry box for rapidly simulation
    catalyse_label = tk.Label(root, text="Step:")
    catalyse_label.grid(row=4, column=0)
    run_parametersGeo.catalyse_entry = tk.Entry(root)
    run_parametersGeo.catalyse_entry.grid(row=4, column=1)
    run_parametersGeo.catalyse_entry.insert(tk.END, "10")
    # Button to run simulation
    run_button = tk.Button(root, text="Run Simulation", command=run_simulationGeo)
    run_button.grid(row=5, columnspan=2)
    # Label for crash message
    # crash_label = tk.Label(root, text="")
    #crash_label.grid(row=4, columnspan=2)
    root.mainloop()
    run_simulationGeo()
    pass
def run_parametersISS():
    root = tk.Tk()
    root.title("Orbit Simulation Parameters")
    # Label and entry box for Earth mass
    earth_mass_label = tk.Label(root, text="Earth Mass (kg):")
    earth_mass_label.grid(row=0, column=0)
    run_parametersISS.earth_mass_entry = tk.Entry(root)
    run_parametersISS.earth_mass_entry.grid(row=0, column=1)
    run_parametersISS.earth_mass_entry.insert(tk.END, "5.972e24")  # Default value
    # Label and entry box for Orbital radius
    orbital_radius_label = tk.Label(root, text="Orbital Radius (m):")
    orbital_radius_label.grid(row=1, column=0)
    run_parametersISS.orbital_radius_entry = tk.Entry(root)
    run_parametersISS.orbital_radius_entry.grid(row=1, column=1)
    run_parametersISS.orbital_radius_entry.insert(tk.END, "7131000")  # Default value
    # Label and entry box for Satellite velocity
    satellite_velocity_label = tk.Label(root, text="Satellite Velocity (m/s):")
    satellite_velocity_label.grid(row=2, column=0)
    run_parametersISS.satellite_velocity_entry = tk.Entry(root)
    run_parametersISS.satellite_velocity_entry.grid(row=2, column=1)
    run_parametersISS.satellite_velocity_entry.insert(tk.END, "7670")  # Default value
    # Label and entry box for multiplier velocity
    multiplier_label = tk.Label(root, text="Number of days:")
    multiplier_label.grid(row=3, column=0)
    run_parametersISS.multiplier_entry = tk.Entry(root)
    run_parametersISS.multiplier_entry.grid(row=3, column=1)
    run_parametersISS.multiplier_entry.insert(tk.END, "0.1")  # Default value
    # Label and entry box for rapidly simulation
    catalyse_label = tk.Label(root, text="Step:")
    catalyse_label.grid(row=4, column=0)
    run_parametersISS.catalyse_entry = tk.Entry(root)
    run_parametersISS.catalyse_entry.grid(row=4, column=1)
    run_parametersISS.catalyse_entry.insert(tk.END, "10")
    # Button to run simulation
    run_button = tk.Button(root, text="Run Simulation", command=run_simulationISS)
    run_button.grid(row=5, columnspan=2)
    # Label for crash message
    # crash_label = tk.Label(root, text="")
    #crash_label.grid(row=4, columnspan=2)
    root.mainloop()
    run_simulationISS()
    pass

def run_parametersGPS():
    root = tk.Tk()
    root.title("Orbit Simulation Parameters")
    # Label and entry box for Earth mass
    earth_mass_label = tk.Label(root, text="Earth Mass (kg):")
    earth_mass_label.grid(row=0, column=0)
    run_parametersGPS.earth_mass_entry = tk.Entry(root)
    run_parametersGPS.earth_mass_entry.grid(row=0, column=1)
    run_parametersGPS.earth_mass_entry.insert(tk.END, "5.972e24")  # Default value
    # Label and entry box for Orbital radius
    orbital_radius_label = tk.Label(root, text="Orbital Radius (m):")
    orbital_radius_label.grid(row=1, column=0)
    run_parametersGPS.orbital_radius_entry = tk.Entry(root)
    run_parametersGPS.orbital_radius_entry.grid(row=1, column=1)
    run_parametersGPS.orbital_radius_entry.insert(tk.END, "26571000")  # Default value
    # Label and entry box for Satellite velocity
    satellite_velocity_label = tk.Label(root, text="Satellite Velocity (m/s):")
    satellite_velocity_label.grid(row=2, column=0)
    run_parametersGPS.satellite_velocity_entry = tk.Entry(root)
    run_parametersGPS.satellite_velocity_entry.grid(row=2, column=1)
    run_parametersGPS.satellite_velocity_entry.insert(tk.END, "3873")  # Default value
    # Label and entry box for multiplier velocity
    multiplier_label = tk.Label(root, text="Number of days:")
    multiplier_label.grid(row=3, column=0)
    run_parametersGPS.multiplier_entry = tk.Entry(root)
    run_parametersGPS.multiplier_entry.grid(row=3, column=1)
    run_parametersGPS.multiplier_entry.insert(tk.END, "0.5")  # Default value
    # Label and entry box for rapidly simulation
    catalyse_label = tk.Label(root, text="Step:")
    catalyse_label.grid(row=4, column=0)
    run_parametersGPS.catalyse_entry = tk.Entry(root)
    run_parametersGPS.catalyse_entry.grid(row=4, column=1)
    run_parametersGPS.catalyse_entry.insert(tk.END, "10")  # Defaurun_parametersGPSInfo
    # Button to run simulation
    run_button = tk.Button(root, text="Run Simulation", command=run_simulationGPS)
    run_button.grid(row=5, columnspan=2)
    # Label for crash message
    # crash_label = tk.Label(root, text="")
    #crash_label.grid(row=4, columnspan=2)
    root.mainloop()
    run_simulationGPS()
    pass
def run_parametersO():
    root = tk.Tk()
    root.title("Orbit Simulation Parameters")
    # Label and entry box for Earth mass
    earth_mass_label = tk.Label(root, text="Earth Mass (kg):")
    earth_mass_label.grid(row=0, column=0)
    run_parametersO.earth_mass_entry = tk.Entry(root)
    run_parametersO.earth_mass_entry.grid(row=0, column=1)
    run_parametersO.earth_mass_entry.insert(tk.END, "5.972e24")  # Default value
    # Label and entry box for Orbital radius
    orbital_radius_label = tk.Label(root, text="Lower Orbital Radius (m):")
    orbital_radius_label.grid(row=4, column=0)
    run_parametersO.orbital_radius_entry = tk.Entry(root)
    run_parametersO.orbital_radius_entry.grid(row=4, column=1)
    #run_parametersO.orbital_radius_entry.insert(tk.END, "26571000")  # Default value
    # Label and entry box for Satellite velocity
    satellite_velocity_label = tk.Label(root, text="Higher Satellite Velocity (m/s):")
    satellite_velocity_label.grid(row=5, column=0)
    run_parametersO.satellite_velocity_entry = tk.Entry(root)
    run_parametersO.satellite_velocity_entry.grid(row=5, column=1)
    #run_parametersO.satellite_velocity_entry.insert(tk.END, "3873")  # Default value
    # Label and entry box for multiplier velocity
    multiplier_label = tk.Label(root, text="Number of days:")
    multiplier_label.grid(row=1, column=0)
    run_parametersO.multiplier_entry = tk.Entry(root)
    run_parametersO.multiplier_entry.grid(row=1, column=1)
    run_parametersO.multiplier_entry.insert(tk.END, "1")  # Default value
    # Label and entry box for rapidly simulation
    catalyse_label = tk.Label(root, text="Step:")
    catalyse_label.grid(row=2, column=0)
    run_parametersO.catalyse_entry = tk.Entry(root)
    run_parametersO.catalyse_entry.grid(row=2, column=1)
    run_parametersO.catalyse_entry.insert(tk.END, "10")
    # Button to run simulation
    run_button = tk.Button(root, text="Run Simulation", command=run_simulationO)
    run_button.grid(row=10, columnspan=2)
    # Label for crash message
    # crash_label = tk.Label(root, text="")
    #crash_label.grid(row=4, columnspan=2)
    # Label and entry box for Orbital radius
    orbital_radius_label2 = tk.Label(root, text="Higer Orbital Radius (m):")
    orbital_radius_label2.grid(row=7, column=0)
    run_parametersO.orbital_radius_entry2 = tk.Entry(root)
    run_parametersO.orbital_radius_entry2.grid(row=7, column=1)
    #run_parametersO.orbital_radius_entry.insert(tk.END, "26571000")  # Default value
    # Label and entry box for Satellite velocity
    satellite_velocity_label2 = tk.Label(root, text="Lower Satellite Velocity (m/s):")
    satellite_velocity_label2.grid(row=8, column=0)
    run_parametersO.satellite_velocity_entry2 = tk.Entry(root)
    run_parametersO.satellite_velocity_entry2.grid(row=8, column=1)
    #run_parametersO.satellite_velocity_entry.insert(tk.END, "3873")  # Default value
    root.mainloop()
    run_simulationO()
    pass


def choose_parameters():
    selected_option = option_var.get()
    if selected_option == "Geostationary":
        run_button3 = tk.Button(root, text="Confirm Geo", width=15, height=5, command=run_parametersGeo)
        run_button3.grid(row=3, columnspan=2)
    elif selected_option == "ISS":
        run_button3 = tk.Button(root, text="Confirm ISS", width=15, height=5, command=run_parametersISS)
        run_button3.grid(row=3, columnspan=2)
    elif selected_option == "GPS":
        run_button3 = tk.Button(root, text="Confirm GPS", width=15, height=5, command=run_parametersGPS)
        run_button3.grid(row=3, columnspan=2)
    elif selected_option == "Custom":
        run_button3 = tk.Button(root, text="Confirm Custom", width=15, height=5, command=run_parametersO)
        run_button3.grid(row=3, columnspan=2)

# Create the first Tkinter window
root = tk.Tk()
root.title("Choose your satellite")

option_var = tk.StringVar(root)
option_var.set("Options")  # Default value
options = ["Geostationary", "ISS", "GPS", "Custom"]  # List of options
option_menu = tk.OptionMenu(root, option_var, *options)
option_menu.grid(row=0, columnspan=2)

run_button2 = tk.Button(root, text="Choose parameters", command=choose_parameters)
run_button2.grid(row=2, columnspan=2)

root.mainloop()