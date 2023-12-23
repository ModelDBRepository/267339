# -*- coding: utf-8 -*-
"""
This is a network with 58 Neurons ispired by ippocampal circuitry
"""
# pragma: no cover

__author__ = 'Simone Coppolino'

#from hbp_nrp_cle.brainsim import simulator as sim
import nest
import hbp_nrp_cle.tf_framework as nrp
import numpy as np
import logging
from pyNN.nest import *
import pyNN.nest as sim
nest.SetKernelStatus({'dict_miss_is_error': False})
logger = logging.getLogger(__name__)

"Function for reading files"
def read(k,csv_file):
    import csv
    with open(csv_file,'rt') as infile:
        read = csv.reader(infile)
        rows = list(read)
        if(k == 0):
            m = (rows[1][2])
            new = m.replace(")","")
            new_bis = new.replace("]","")
            new_float = float(new_bis) #convert new_bis from string to float
            return new_float
        elif(k > 0):
            m = (rows[1][k+3])
            new = m.replace(")","")
            new_bis = new.replace("]","")
            new_float = float(new_bis)
            return new_float



       
       
       
       
# Following parameters were taken from Pynn default parameters (PyNN.com)
SENSORPARAMS = {'cm': 1.0,
                    'v_rest': -65.0,
                    'tau_m': 20.0,
                    'e_rev_E': 0.0,
                    'e_rev_I': -70.0,
                    'v_reset': -65.0,
                    'v_thresh': -50.0,
                    'tau_refrac': 1.0,
                    'tau_syn_E': 5.0,
                    'tau_syn_I': 5.0}




#syn_params = {'U' : 1.0, 'tau_rec': 10.0, 'tau_facil': 100.0}
cell_class = sim.IF_cond_alpha(**SENSORPARAMS)

#Static Synapse

#Synapse Sensor-Object
SYN_S_OJ = sim.StaticSynapse(weight = 0.1, delay = 0.1)
#Synapse HD-PC
SYN_S_HD = sim.StaticSynapse(weight = 0.05, delay = 0.1)
#Wrong path - Synapse
SYN_PF_E = sim.StaticSynapse(weight = 0.036, delay = 0.1)
SYN_PF_P = sim.StaticSynapse(weight = 0.03, delay = 0.1)

#Synapse Sensor-Persistent
SYN_B_MB = sim.StaticSynapse(weight = 0.03, delay = 0.1)
SYN_TURN = sim.StaticSynapse(weight = 0.0015, delay = 0.1)
SYN_TURN_B = sim.StaticSynapse(weight = 0.0018, delay = 0.1)
SYN_TURN_C = sim.StaticSynapse(weight = 0.005, delay = 0.1)

#ColorSynapses

SYN_R_0 = sim.StaticSynapse(weight = read(0,'angular_red.csv'), delay = 0.1)
SYN_R_1 = sim.StaticSynapse(weight = read(2,'angular_red.csv'), delay = 0.1)
SYN_R_2 = sim.StaticSynapse(weight = read(5,'angular_red.csv'), delay = 0.1)
SYN_R_3 = sim.StaticSynapse(weight = read(8,'angular_red.csv'), delay = 0.1)
SYN_R_4 = sim.StaticSynapse(weight = read(11,'angular_red.csv'), delay = 0.1)
SYN_R_5 = sim.StaticSynapse(weight = read(14,'angular_red.csv'), delay = 0.1)
SYN_R_6 = sim.StaticSynapse(weight = read(17,'angular_red.csv'), delay = 0.1)
SYN_R_7 = sim.StaticSynapse(weight = read(20,'angular_red.csv'), delay = 0.1)
SYN_R_8 = sim.StaticSynapse(weight = read(23,'angular_red.csv'), delay = 0.1)
SYN_R_9 = sim.StaticSynapse(weight = read(26,'angular_red.csv'), delay = 0.1)
SYN_R_10 = sim.StaticSynapse(weight = read(29,'angular_red.csv'), delay = 0.1)
SYN_R_11 = sim.StaticSynapse(weight = read(32,'angular_red.csv'), delay = 0.1)
SYN_R_12 = sim.StaticSynapse(weight = read(35,'angular_red.csv'), delay = 0.1)
SYN_R_13 = sim.StaticSynapse(weight = read(38,'angular_red.csv'), delay = 0.1)
SYN_R_14 = sim.StaticSynapse(weight = read(41,'angular_red.csv'), delay = 0.1)
SYN_R_15 = sim.StaticSynapse(weight = read(44,'angular_red.csv'), delay = 0.1)
SYN_R_16 = sim.StaticSynapse(weight = read(47,'angular_red.csv'), delay = 0.1)
SYN_R_17 = sim.StaticSynapse(weight = read(50,'angular_red.csv'), delay = 0.1)

SYN_B_0 = sim.StaticSynapse(weight = read(0,'angular_blue.csv'), delay = 0.1)
SYN_B_1 = sim.StaticSynapse(weight = read(2,'angular_blue.csv'), delay = 0.1)
SYN_B_2 = sim.StaticSynapse(weight = read(5,'angular_blue.csv'), delay = 0.1)
SYN_B_3 = sim.StaticSynapse(weight = read(8,'angular_blue.csv'), delay = 0.1)
SYN_B_4 = sim.StaticSynapse(weight = read(11,'angular_blue.csv'), delay = 0.1)
SYN_B_5 = sim.StaticSynapse(weight = read(14,'angular_blue.csv'), delay = 0.1)
SYN_B_6 = sim.StaticSynapse(weight = read(17,'angular_blue.csv'), delay = 0.1)
SYN_B_7 = sim.StaticSynapse(weight = read(20,'angular_blue.csv'), delay = 0.1)
SYN_B_8 = sim.StaticSynapse(weight = read(23,'angular_blue.csv'), delay = 0.1)
SYN_B_9 = sim.StaticSynapse(weight = read(26,'angular_blue.csv'), delay = 0.1)
SYN_B_10 = sim.StaticSynapse(weight = read(29,'angular_blue.csv'), delay = 0.1)
SYN_B_11 = sim.StaticSynapse(weight = read(32,'angular_blue.csv'), delay = 0.1)
SYN_B_12 = sim.StaticSynapse(weight = read(35,'angular_blue.csv'), delay = 0.1)
SYN_B_13 = sim.StaticSynapse(weight = read(38,'angular_blue.csv'), delay = 0.1)
SYN_B_14 = sim.StaticSynapse(weight = read(41,'angular_blue.csv'), delay = 0.1)
SYN_B_15 = sim.StaticSynapse(weight = read(44,'angular_blue.csv'), delay = 0.1)
SYN_B_16 = sim.StaticSynapse(weight = read(47,'angular_blue.csv'), delay = 0.1)
SYN_B_17 = sim.StaticSynapse(weight = read(50,'angular_blue.csv'), delay = 0.1)

SYN_K_0 = sim.StaticSynapse(weight = read(0,'angular_black.csv'), delay = 0.1)
SYN_K_1 = sim.StaticSynapse(weight = read(2,'angular_black.csv'), delay = 0.1)
SYN_K_2 = sim.StaticSynapse(weight = read(5,'angular_black.csv'), delay = 0.1)
SYN_K_3 = sim.StaticSynapse(weight = read(8,'angular_black.csv'), delay = 0.1)
SYN_K_4 = sim.StaticSynapse(weight = read(11,'angular_black.csv'), delay = 0.1)
SYN_K_5 = sim.StaticSynapse(weight = read(14,'angular_black.csv'), delay = 0.1)
SYN_K_6 = sim.StaticSynapse(weight = read(17,'angular_black.csv'), delay = 0.1)
SYN_K_7 = sim.StaticSynapse(weight = read(20,'angular_black.csv'), delay = 0.1)
SYN_K_8 = sim.StaticSynapse(weight = read(23,'angular_black.csv'), delay = 0.1)
SYN_K_9 = sim.StaticSynapse(weight = read(26,'angular_black.csv'), delay = 0.1)
SYN_K_10 = sim.StaticSynapse(weight = read(29,'angular_black.csv'), delay = 0.1)
SYN_K_11 = sim.StaticSynapse(weight = read(32,'angular_black.csv'), delay = 0.1)
SYN_K_12 = sim.StaticSynapse(weight = read(35,'angular_black.csv'), delay = 0.1)
SYN_K_13 = sim.StaticSynapse(weight = read(38,'angular_black.csv'), delay = 0.1)
SYN_K_14 = sim.StaticSynapse(weight = read(41,'angular_black.csv'), delay = 0.1)
SYN_K_15 = sim.StaticSynapse(weight = read(44,'angular_black.csv'), delay = 0.1)
SYN_K_16 = sim.StaticSynapse(weight = read(47,'angular_black.csv'), delay = 0.1)
SYN_K_17 = sim.StaticSynapse(weight = read(50,'angular_black.csv'), delay = 0.1)

SYN_G_0 = sim.StaticSynapse(weight = read(0,'angular_green.csv'), delay = 0.1)
SYN_G_1 = sim.StaticSynapse(weight = read(2,'angular_green.csv'), delay = 0.1)
SYN_G_2 = sim.StaticSynapse(weight = read(5,'angular_green.csv'), delay = 0.1)
SYN_G_3 = sim.StaticSynapse(weight = read(8,'angular_green.csv'), delay = 0.1)
SYN_G_4 = sim.StaticSynapse(weight = read(11,'angular_green.csv'), delay = 0.1)
SYN_G_5 = sim.StaticSynapse(weight = read(14,'angular_green.csv'), delay = 0.1)
SYN_G_6 = sim.StaticSynapse(weight = read(17,'angular_green.csv'), delay = 0.1)
SYN_G_7 = sim.StaticSynapse(weight = read(20,'angular_green.csv'), delay = 0.1)
SYN_G_8 = sim.StaticSynapse(weight = read(23,'angular_green.csv'), delay = 0.1)
SYN_G_9 = sim.StaticSynapse(weight = read(26,'angular_green.csv'), delay = 0.1)
SYN_G_10 = sim.StaticSynapse(weight = read(29,'angular_green.csv'), delay = 0.1)
SYN_G_11 = sim.StaticSynapse(weight = read(32,'angular_green.csv'), delay = 0.1)
SYN_G_12 = sim.StaticSynapse(weight = read(35,'angular_green.csv'), delay = 0.1)
SYN_G_13 = sim.StaticSynapse(weight = read(38,'angular_green.csv'), delay = 0.1)
SYN_G_14 = sim.StaticSynapse(weight = read(41,'angular_green.csv'), delay = 0.1)
SYN_G_15 = sim.StaticSynapse(weight = read(44,'angular_green.csv'), delay = 0.1)
SYN_G_16 = sim.StaticSynapse(weight = read(47,'angular_green.csv'), delay = 0.1)
SYN_G_17 = sim.StaticSynapse(weight = read(50,'angular_green.csv'), delay = 0.1)

SYN_Y_0 = sim.StaticSynapse(weight = read(0,'angular_yellow.csv'), delay = 0.1)
SYN_Y_1 = sim.StaticSynapse(weight = read(2,'angular_yellow.csv'), delay = 0.1)
SYN_Y_2 = sim.StaticSynapse(weight = read(5,'angular_yellow.csv'), delay = 0.1)
SYN_Y_3 = sim.StaticSynapse(weight = read(8,'angular_yellow.csv'), delay = 0.1)
SYN_Y_4 = sim.StaticSynapse(weight = read(11,'angular_yellow.csv'), delay = 0.1)
SYN_Y_5 = sim.StaticSynapse(weight = read(14,'angular_yellow.csv'), delay = 0.1)
SYN_Y_6 = sim.StaticSynapse(weight = read(17,'angular_yellow.csv'), delay = 0.1)
SYN_Y_7 = sim.StaticSynapse(weight = read(20,'angular_yellow.csv'), delay = 0.1)
SYN_Y_8 = sim.StaticSynapse(weight = read(23,'angular_yellow.csv'), delay = 0.1)
SYN_Y_9 = sim.StaticSynapse(weight = read(26,'angular_yellow.csv'), delay = 0.1)
SYN_Y_10 = sim.StaticSynapse(weight = read(29,'angular_yellow.csv'), delay = 0.1)
SYN_Y_11 = sim.StaticSynapse(weight = read(32,'angular_yellow.csv'), delay = 0.1)
SYN_Y_12 = sim.StaticSynapse(weight = read(35,'angular_yellow.csv'), delay = 0.1)
SYN_Y_13 = sim.StaticSynapse(weight = read(38,'angular_yellow.csv'), delay = 0.1)
SYN_Y_14 = sim.StaticSynapse(weight = read(41,'angular_yellow.csv'), delay = 0.1)
SYN_Y_15 = sim.StaticSynapse(weight = read(44,'angular_yellow.csv'), delay = 0.1)
SYN_Y_16 = sim.StaticSynapse(weight = read(47,'angular_yellow.csv'), delay = 0.1)
SYN_Y_17 = sim.StaticSynapse(weight = read(50,'angular_yellow.csv'), delay = 0.1)

SYN_T_0 = sim.StaticSynapse(weight = read(0,'angular_turquoise.csv'), delay = 0.1)
SYN_T_1 = sim.StaticSynapse(weight = read(2,'angular_turquoise.csv'), delay = 0.1)
SYN_T_2 = sim.StaticSynapse(weight = read(5,'angular_turquoise.csv'), delay = 0.1)
SYN_T_3 = sim.StaticSynapse(weight = read(8,'angular_turquoise.csv'), delay = 0.1)
SYN_T_4 = sim.StaticSynapse(weight = read(11,'angular_turquoise.csv'), delay = 0.1)
SYN_T_5 = sim.StaticSynapse(weight = read(14,'angular_turquoise.csv'), delay = 0.1)
SYN_T_6 = sim.StaticSynapse(weight = read(17,'angular_turquoise.csv'), delay = 0.1)
SYN_T_7 = sim.StaticSynapse(weight = read(20,'angular_turquoise.csv'), delay = 0.1)
SYN_T_8 = sim.StaticSynapse(weight = read(23,'angular_turquoise.csv'), delay = 0.1)
SYN_T_9 = sim.StaticSynapse(weight = read(26,'angular_turquoise.csv'), delay = 0.1)
SYN_T_10 = sim.StaticSynapse(weight = read(29,'angular_turquoise.csv'), delay = 0.1)
SYN_T_11 = sim.StaticSynapse(weight = read(32,'angular_turquoise.csv'), delay = 0.1)
SYN_T_12 = sim.StaticSynapse(weight = read(35,'angular_turquoise.csv'), delay = 0.1)
SYN_T_13 = sim.StaticSynapse(weight = read(38,'angular_turquoise.csv'), delay = 0.1)
SYN_T_14 = sim.StaticSynapse(weight = read(41,'angular_turquoise.csv'), delay = 0.1)
SYN_T_15 = sim.StaticSynapse(weight = read(44,'angular_turquoise.csv'), delay = 0.1)
SYN_T_16 = sim.StaticSynapse(weight = read(47,'angular_turquoise.csv'), delay = 0.1)
SYN_T_17 = sim.StaticSynapse(weight = read(50,'angular_turquoise.csv'), delay = 0.1)

# Persistent Synapses

SYN_PR_1 = sim.StaticSynapse(weight = read(0,'persistent_red.csv'), delay = 0.1)
SYN_PR_2 = sim.StaticSynapse(weight = read(2,'persistent_red.csv'), delay = 0.1)
SYN_PR_3 = sim.StaticSynapse(weight = read(5,'persistent_red.csv'), delay = 0.1)
SYN_PR_4 = sim.StaticSynapse(weight = read(8,'persistent_red.csv'), delay = 0.1)
SYN_PR_5 = sim.StaticSynapse(weight = read(11,'persistent_red.csv'), delay = 0.1)

SYN_PB_1 = sim.StaticSynapse(weight = read(0,'persistent_blue.csv'), delay = 0.1)
SYN_PB_2 = sim.StaticSynapse(weight = read(0,'persistent_blue_1.csv'), delay = 0.1)
SYN_PB_3 = sim.StaticSynapse(weight = read(2,'persistent_blue_1.csv'), delay = 0.1)
SYN_PB_4 = sim.StaticSynapse(weight = read(5,'persistent_blue_1.csv'), delay = 0.1)
SYN_PB_5 = sim.StaticSynapse(weight = read(8,'persistent_blue_1.csv'), delay = 0.1)

SYN_PK_1 = sim.StaticSynapse(weight = read(0,'persistent_black.csv'), delay = 0.1)
SYN_PK_2 = sim.StaticSynapse(weight = read(2,'persistent_black.csv'), delay = 0.1)
SYN_PK_3 = sim.StaticSynapse(weight = read(5,'persistent_black.csv'), delay = 0.1)
SYN_PK_4 = sim.StaticSynapse(weight = read(8,'persistent_black.csv'), delay = 0.1)
SYN_PK_5 = sim.StaticSynapse(weight = read(0,'persistent_black1.csv'), delay = 0.1)

SYN_PY_1 = sim.StaticSynapse(weight = read(0,'persistent_yellow.csv'), delay = 0.1)
SYN_PY_2 = sim.StaticSynapse(weight = read(2,'persistent_yellow.csv'), delay = 0.1)
SYN_PY_3 = sim.StaticSynapse(weight = read(0,'persistent_yellow1.csv'), delay = 0.1)
SYN_PY_4 = sim.StaticSynapse(weight = read(2,'persistent_yellow1.csv'), delay = 0.1)
SYN_PY_5 = sim.StaticSynapse(weight = read(5,'persistent_yellow1.csv'), delay = 0.1)

SYN_PT_1 = sim.StaticSynapse(weight = read(0,'persistent_turquoise.csv'), delay = 0.1)
SYN_PT_2 = sim.StaticSynapse(weight = read(2,'persistent_turquoise.csv'), delay = 0.1)
SYN_PT_3 = sim.StaticSynapse(weight = read(5,'persistent_turquoise.csv'), delay = 0.1)
SYN_PT_4 = sim.StaticSynapse(weight = read(0,'persistent_turquoise1.csv'), delay = 0.1)
SYN_PT_5 = sim.StaticSynapse(weight = read(2,'persistent_turquoise1.csv'), delay = 0.1)
SYN_WL = sim.TsodyksMarkramSynapse(weight = 3.0, delay = 0.1)
SYN_WR = sim.TsodyksMarkramSynapse(weight = 3.0, delay = 0.1)

#Inhibition and activation Synapse
SYN_D_IN = sim.StaticSynapse(weight = 0.1, delay = 0.1)
SYN_D = sim.StaticSynapse(weight = 4.5, delay = 0.1)
#Inhibitory-Inhibitory Synapse 
SYN_D_D = sim.StaticSynapse(weight = 9.0, delay = 0.1)
SYN_DK = sim.StaticSynapse(weight = 1.0, delay = 0.1)
SYN_M = sim.TsodyksMarkramSynapse(weight=0.3, delay= 20.0, U=0.5, tau_rec=100.0, tau_facil=10.0)
SYN_M_2 = sim.TsodyksMarkramSynapse(weight=0.2, delay= 50.0, U=0.5, tau_rec=100.0, tau_facil=10.0)
SYN_D_S = sim.StaticSynapse(weight = 15.0, delay = 0.1)
SYN_D_S_1 = sim.StaticSynapse(weight = 12.0, delay = 0.1)
SYN_D_S_P = sim.StaticSynapse(weight = 40.0, delay = 0.1)


#Define the neural population
linear_sensor = sim.Population(size = 8, cellclass = cell_class)
sensor_neuron = sim.Population(size = 8, cellclass = cell_class)
error_neuron = sim.Population(size = 2, cellclass = cell_class)
wall_sensor = sim.Population(size = 2, cellclass = cell_class)
wall_neuron = sim.Population(size = 2, cellclass = cell_class)
persistent_neurons = sim.Population(size = 8, cellclass = cell_class)
object_cells = sim.Population(size = 6,cellclass = cell_class)
place_cells  = sim.Population(size = 18,cellclass = cell_class)
depression_cell = sim.Population(size = 11, cellclass = cell_class)
head_direction_cells = sim.Population(size = 18, cellclass = cell_class)
feedback = sim.Population(size = 1, cellclass = cell_class)
neurons = sensor_neuron + linear_sensor + persistent_neurons + object_cells + place_cells + head_direction_cells + wall_sensor + wall_neuron + depression_cell + feedback + error_neuron


#Red-Connection

red_connection = sim.Projection(sensor_neuron[0:1],object_cells[0:1],OneToOneConnector(),SYN_S_OJ,receptor_type='excitatory')
red_linear_sensor = sim.Projection(linear_sensor[0:1], feedback, OneToOneConnector(), SYN_TURN, receptor_type = 'excitatory')
sensor_red_connection = sim.Projection(sensor_neuron[0:1],persistent_neurons[0:1],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
inib_red_connection = sim.Projection(sensor_neuron[0:1],depression_cell[1:2],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
angular_red_connection_0 = sim.Projection(object_cells[0:1],place_cells[0:1],OneToOneConnector(),SYN_R_0,receptor_type = 'excitatory')
angular_red_connection_1 = sim.Projection(object_cells[0:1],place_cells[1:2],OneToOneConnector(),SYN_R_1,receptor_type = 'excitatory')
angular_red_connection_2 = sim.Projection(object_cells[0:1],place_cells[2:3],OneToOneConnector(),SYN_R_2,receptor_type = 'excitatory')
angular_red_connection_3 = sim.Projection(object_cells[0:1],place_cells[3:4],OneToOneConnector(),SYN_R_3,receptor_type = 'excitatory')
angular_red_connection_4 = sim.Projection(object_cells[0:1],place_cells[4:5],OneToOneConnector(),SYN_R_4,receptor_type = 'excitatory')
angular_red_connection_5 = sim.Projection(object_cells[0:1],place_cells[5:6],OneToOneConnector(),SYN_R_5,receptor_type = 'excitatory')
angular_red_connection_6 = sim.Projection(object_cells[0:1],place_cells[6:7],OneToOneConnector(),SYN_R_6,receptor_type = 'excitatory')
angular_red_connection_7 = sim.Projection(object_cells[0:1],place_cells[7:8],OneToOneConnector(),SYN_R_7,receptor_type = 'excitatory')
angular_red_connection_8 = sim.Projection(object_cells[0:1],place_cells[8:9],OneToOneConnector(),SYN_R_8,receptor_type = 'excitatory')
angular_red_connection_9 = sim.Projection(object_cells[0:1],place_cells[9:10],OneToOneConnector(),SYN_R_9,receptor_type = 'excitatory')
angular_red_connection_10 = sim.Projection(object_cells[0:1],place_cells[10:11],OneToOneConnector(),SYN_R_10,receptor_type = 'excitatory')
angular_red_connection_11 = sim.Projection(object_cells[0:1],place_cells[11:12],OneToOneConnector(),SYN_R_11,receptor_type = 'excitatory')
angular_red_connection_12 = sim.Projection(object_cells[0:1],place_cells[12:13],OneToOneConnector(),SYN_R_12,receptor_type = 'excitatory')
angular_red_connection_13 = sim.Projection(object_cells[0:1],place_cells[13:14],OneToOneConnector(),SYN_R_13,receptor_type = 'excitatory')
angular_red_connection_14 = sim.Projection(object_cells[0:1],place_cells[14:15],OneToOneConnector(),SYN_R_14,receptor_type = 'excitatory')
angular_red_connection_15 = sim.Projection(object_cells[0:1],place_cells[15:16],OneToOneConnector(),SYN_R_15,receptor_type = 'excitatory')
angular_red_connection_16 = sim.Projection(object_cells[0:1],place_cells[16:17],OneToOneConnector(),SYN_R_16,receptor_type = 'excitatory')
angular_red_connection_17 = sim.Projection(object_cells[0:1],place_cells[17:18],OneToOneConnector(),SYN_R_17,receptor_type = 'excitatory')
persistent_red_connection_0 = sim.Projection(persistent_neurons[0:1],object_cells[1:2],OneToOneConnector(),SYN_PR_1)
persistent_red_connection_1 = sim.Projection(persistent_neurons[0:1],object_cells[2:3],OneToOneConnector(),SYN_PR_2)
persistent_red_connection_2 = sim.Projection(persistent_neurons[0:1],object_cells[3:4],OneToOneConnector(),SYN_PR_3)
persistent_red_connection_3 = sim.Projection(persistent_neurons[0:1],object_cells[4:5],OneToOneConnector(),SYN_PR_4)
persistent_red_connection_4 = sim.Projection(persistent_neurons[0:1],object_cells[5:6],OneToOneConnector(),SYN_PR_5)
loop_red_connection = sim.Projection(persistent_neurons[0:1], persistent_neurons[0:1], OneToOneConnector(), SYN_M_2, receptor_type = 'excitatory')
red_inibition = sim.Projection(depression_cell[1:2], persistent_neurons[1:5],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')

#Blue-Connection
blue_connection = sim.Projection(sensor_neuron[1:2],object_cells[1:2],OneToOneConnector(),SYN_S_OJ, receptor_type = 'excitatory')
blue_linear_sensor = sim.Projection(linear_sensor[1:2], feedback, OneToOneConnector(), SYN_TURN, receptor_type = 'excitatory')
sensor_blue_connection = sim.Projection(sensor_neuron[1:2],persistent_neurons[1:2],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
inib_blue_connection = sim.Projection(sensor_neuron[1:2],depression_cell[8:9],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
angular_blue_connection_0 = sim.Projection(object_cells[1:2],place_cells[0:1],OneToOneConnector(),SYN_B_0)
angular_blue_connection_1 = sim.Projection(object_cells[1:2],place_cells[1:2],OneToOneConnector(),SYN_B_1)
angular_blue_connection_2 = sim.Projection(object_cells[1:2],place_cells[2:3],OneToOneConnector(),SYN_B_2)
angular_blue_connection_3 = sim.Projection(object_cells[1:2],place_cells[3:4],OneToOneConnector(),SYN_B_3)
angular_blue_connection_4 = sim.Projection(object_cells[1:2],place_cells[4:5],OneToOneConnector(),SYN_B_4)
angular_blue_connection_5 = sim.Projection(object_cells[1:2],place_cells[5:6],OneToOneConnector(),SYN_B_5)
angular_blue_connection_6 = sim.Projection(object_cells[1:2],place_cells[6:7],OneToOneConnector(),SYN_B_6)
angular_blue_connection_7 = sim.Projection(object_cells[1:2],place_cells[7:8],OneToOneConnector(),SYN_B_7)
angular_blue_connection_8 = sim.Projection(object_cells[1:2],place_cells[8:9],OneToOneConnector(),SYN_B_8)
angular_blue_connection_9 = sim.Projection(object_cells[1:2],place_cells[9:10],OneToOneConnector(),SYN_B_9)
angular_blue_connection_10 = sim.Projection(object_cells[1:2],place_cells[10:11],OneToOneConnector(),SYN_B_10)
angular_blue_connection_11 = sim.Projection(object_cells[1:2],place_cells[11:12],OneToOneConnector(),SYN_B_11)
angular_blue_connection_12 = sim.Projection(object_cells[1:2],place_cells[12:13],OneToOneConnector(),SYN_B_12)
angular_blue_connection_13 = sim.Projection(object_cells[1:2],place_cells[13:14],OneToOneConnector(),SYN_B_13)
angular_blue_connection_14 = sim.Projection(object_cells[1:2],place_cells[14:15],OneToOneConnector(),SYN_B_14)
angular_blue_connection_15 = sim.Projection(object_cells[1:2],place_cells[15:16],OneToOneConnector(),SYN_B_15)
angular_blue_connection_16 = sim.Projection(object_cells[1:2],place_cells[16:17],OneToOneConnector(),SYN_B_16)
angular_blue_connection_17 = sim.Projection(object_cells[1:2],place_cells[17:18],OneToOneConnector(),SYN_B_17)

persistent_blue_connection_0 = sim.Projection(persistent_neurons[1:2],object_cells[0:1],OneToOneConnector(),SYN_PB_1)
persistent_blue_connection_1 = sim.Projection(persistent_neurons[1:2],object_cells[2:3],OneToOneConnector(),SYN_PB_2)
persistent_blue_connection_2 = sim.Projection(persistent_neurons[1:2],object_cells[3:4],OneToOneConnector(),SYN_PB_3)
persistent_blue_connection_3 = sim.Projection(persistent_neurons[1:2],object_cells[4:5],OneToOneConnector(),SYN_PB_4)
persistent_blue_connection_4 = sim.Projection(persistent_neurons[1:2],object_cells[5:6],OneToOneConnector(),SYN_PB_5)
loop_blue_connection = sim.Projection(persistent_neurons[1:2], persistent_neurons[1:2], OneToOneConnector(), SYN_M_2, receptor_type = 'excitatory')
blue_inibition = sim.Projection(depression_cell[8:9], persistent_neurons[0:1],OneToOneConnector(), SYN_D_S, receptor_type = 'inhibitory')
blue_inibition_1 = sim.Projection(depression_cell[8:9], persistent_neurons[2:5],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')

#Yellow-Connection
yellow_connection = sim.Projection(sensor_neuron[2:3],object_cells[2:3], OneToOneConnector(),SYN_S_OJ,receptor_type='excitatory')
yellow_linear_sensor = sim.Projection(linear_sensor[2:3], feedback, OneToOneConnector(), SYN_TURN, receptor_type = 'excitatory')
sensor_yellow_connection = sim.Projection(sensor_neuron[2:3],persistent_neurons[2:3],OneToOneConnector(), SYN_B_MB,receptor_type = 'excitatory')
inib_yellow_connection = sim.Projection(sensor_neuron[2:3],depression_cell[9:10],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
angular_yellow_connection_0 = sim.Projection(object_cells[2:3], place_cells[0:1], OneToOneConnector(),SYN_Y_0)
angular_yellow_connection_1 = sim.Projection(object_cells[2:3], place_cells[1:2], OneToOneConnector(), SYN_Y_1)
angular_yellow_connection_2 = sim.Projection(object_cells[2:3], place_cells[2:3], OneToOneConnector(), SYN_Y_2)
angular_yellow_connection_3 = sim.Projection(object_cells[2:3], place_cells[3:4], OneToOneConnector(), SYN_Y_3)
angular_yellow_connection_4 = sim.Projection(object_cells[2:3], place_cells[4:5], OneToOneConnector(), SYN_Y_4)
angular_yellow_connection_5 = sim.Projection(object_cells[2:3], place_cells[5:6], OneToOneConnector(), SYN_Y_5)
angular_yellow_connection_6 = sim.Projection(object_cells[2:3], place_cells[6:7], OneToOneConnector(), SYN_Y_6)
angular_yellow_connection_7 = sim.Projection(object_cells[2:3], place_cells[7:8], OneToOneConnector(), SYN_Y_7)
angular_yellow_connection_8 = sim.Projection(object_cells[2:3], place_cells[8:9], OneToOneConnector(), SYN_Y_8)
angular_yellow_connection_9 = sim.Projection(object_cells[2:3], place_cells[9:10], OneToOneConnector(), SYN_Y_9)
angular_yellow_connection_10 = sim.Projection(object_cells[2:3], place_cells[10:11], OneToOneConnector(),SYN_Y_10)
angular_yellow_connection_11 = sim.Projection(object_cells[2:3], place_cells[11:12], OneToOneConnector(), SYN_Y_11)
angular_yellow_connection_12 = sim.Projection(object_cells[2:3], place_cells[12:13], OneToOneConnector(), SYN_Y_12)
angular_yellow_connection_13 = sim.Projection(object_cells[2:3], place_cells[13:14], OneToOneConnector(), SYN_Y_13)
angular_yellow_connection_14 = sim.Projection(object_cells[2:3], place_cells[14:15], OneToOneConnector(), SYN_Y_14)
angular_yellow_connection_15 = sim.Projection(object_cells[2:3], place_cells[15:16], OneToOneConnector(), SYN_Y_15)
angular_yellow_connection_16 = sim.Projection(object_cells[2:3], place_cells[16:17], OneToOneConnector(), SYN_Y_16)
angular_yellow_connection_17 = sim.Projection(object_cells[2:3], place_cells[17:18], OneToOneConnector(), SYN_Y_17)
persistent_yellow_connection_0 = sim.Projection(persistent_neurons[2:3],object_cells[0:1],OneToOneConnector(),SYN_PY_1)
persistent_yellow_connection_1 = sim.Projection(persistent_neurons[2:3],object_cells[1:2],OneToOneConnector(),SYN_PY_2)
persistent_yellow_connection_2 = sim.Projection(persistent_neurons[2:3],object_cells[3:4],OneToOneConnector(),SYN_PY_3)
persistent_yellow_connection_3 = sim.Projection(persistent_neurons[2:3],object_cells[4:5],OneToOneConnector(),SYN_PY_4)
persistent_yellow_connection_4 = sim.Projection(persistent_neurons[2:3], object_cells[5:6],OneToOneConnector(),SYN_PY_5)
loop_yellow_connection = sim.Projection(persistent_neurons[2:3], persistent_neurons[2:3], OneToOneConnector(), SYN_M_2, receptor_type = 'excitatory')
yellow_inibition = sim.Projection(depression_cell[9:10], persistent_neurons[0:2],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')
yellow_inibition_1 = sim.Projection(depression_cell[9:10], persistent_neurons[3:5],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')

#Cyan-Connection
cyan_connection = sim.Projection(sensor_neuron[3:4],object_cells[3:4], OneToOneConnector(),SYN_S_OJ,receptor_type='excitatory')
sensor_cyan_connection = sim.Projection(sensor_neuron[3:4],persistent_neurons[3:4],OneToOneConnector(), SYN_B_MB,receptor_type = 'excitatory')
cyan_linear_sensor = sim.Projection(linear_sensor[3:4],feedback,OneToOneConnector(), SYN_TURN_B,receptor_type = 'excitatory')
inib_cyan_connection = sim.Projection(sensor_neuron[3:4],depression_cell[10:11],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
angular_cyan_connection_0 = sim.Projection(object_cells[3:4], place_cells[0:1], OneToOneConnector(), SYN_T_0)
angular_cyan_connection_1 = sim.Projection(object_cells[3:4], place_cells[1:2], OneToOneConnector(), SYN_T_1)
angular_cyan_connection_2 = sim.Projection(object_cells[3:4], place_cells[2:3], OneToOneConnector(), SYN_T_2)
angular_cyan_connection_3 = sim.Projection(object_cells[3:4], place_cells[3:4], OneToOneConnector(), SYN_T_3)
angular_cyan_connection_4 = sim.Projection(object_cells[3:4], place_cells[4:5], OneToOneConnector(), SYN_T_4)
angular_cyan_connection_5 = sim.Projection(object_cells[3:4], place_cells[5:6], OneToOneConnector(), SYN_T_5)
angular_cyan_connection_6 = sim.Projection(object_cells[3:4], place_cells[6:7], OneToOneConnector(), SYN_T_6)
angular_cyan_connection_7 = sim.Projection(object_cells[3:4], place_cells[7:8], OneToOneConnector(), SYN_T_7)
angular_cyan_connection_8 = sim.Projection(object_cells[3:4], place_cells[8:9], OneToOneConnector(), SYN_T_8)
angular_cyan_connection_9 = sim.Projection(object_cells[3:4], place_cells[9:10], OneToOneConnector(), SYN_T_9)
angular_cyan_connection_10 = sim.Projection(object_cells[3:4], place_cells[10:11], OneToOneConnector(), SYN_T_10)
angular_cyan_connection_11 = sim.Projection(object_cells[3:4], place_cells[11:12], OneToOneConnector(), SYN_T_11)
angular_cyan_connection_12 = sim.Projection(object_cells[3:4], place_cells[12:13], OneToOneConnector(), SYN_T_12)
angular_cyan_connection_13 = sim.Projection(object_cells[3:4], place_cells[13:14], OneToOneConnector(), SYN_T_13)
angular_cyan_connection_14 = sim.Projection(object_cells[3:4], place_cells[14:15], OneToOneConnector(), SYN_T_14)
angular_cyan_connection_15 = sim.Projection(object_cells[3:4], place_cells[15:16], OneToOneConnector(), SYN_T_15)
angular_cyan_connection_16 = sim.Projection(object_cells[3:4], place_cells[16:17], OneToOneConnector(), SYN_T_16)
angular_cyan_connection_17 = sim.Projection(object_cells[3:4], place_cells[17:18], OneToOneConnector(), SYN_T_17)
persistent_cyan_connection_0 = sim.Projection(persistent_neurons[3:4],object_cells[0:1],OneToOneConnector(),SYN_PT_1)
persistent_cyan_connection_1 = sim.Projection(persistent_neurons[3:4],object_cells[1:2],OneToOneConnector(),SYN_PT_2)
persistent_cyan_connection_2 = sim.Projection(persistent_neurons[3:4],object_cells[2:3],OneToOneConnector(),SYN_PT_3)
persistent_cyan_connection_3 = sim.Projection(persistent_neurons[3:4],object_cells[4:5],OneToOneConnector(),SYN_PT_4)
persistent_cyan_connection_4 = sim.Projection(persistent_neurons[3:4], object_cells[5:6],OneToOneConnector(),SYN_PT_5)
loop_cyan_connection = sim.Projection(persistent_neurons[3:4], persistent_neurons[3:4], OneToOneConnector(), SYN_M_2, receptor_type = 'excitatory')
cyan_inibition = sim.Projection(depression_cell[10:11], persistent_neurons[0:3],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')
cyan_inibition_1 = sim.Projection(depression_cell[10:11], persistent_neurons[4:5],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')

#Black-Connection
black_connection = sim.Projection(sensor_neuron[4:5], object_cells[4:5], OneToOneConnector(), SYN_S_OJ, receptor_type = 'excitatory')
black_linear_sensor = sim.Projection(linear_sensor[4:5],feedback,OneToOneConnector(), SYN_TURN_B,receptor_type = 'excitatory')
sensor_black_connection = sim.Projection(sensor_neuron[4:5],persistent_neurons[4:5],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
inib_black_connection = sim.Projection(sensor_neuron[4:5],depression_cell[2:3],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
angular_black_connection_0 = sim.Projection(object_cells[4:5],place_cells[0:1],OneToOneConnector(),SYN_K_0)
angular_black_connection_1 = sim.Projection(object_cells[4:5],place_cells[1:2],OneToOneConnector(),SYN_K_1)
angular_black_connection_2 = sim.Projection(object_cells[4:5],place_cells[2:3],OneToOneConnector(),SYN_K_2)
angular_black_connection_3 = sim.Projection(object_cells[4:5],place_cells[3:4],OneToOneConnector(),SYN_K_3)
angular_black_connection_4 = sim.Projection(object_cells[4:5],place_cells[4:5],OneToOneConnector(),SYN_K_4)
angular_black_connection_5 = sim.Projection(object_cells[4:5],place_cells[5:6],OneToOneConnector(),SYN_K_5)
angular_black_connection_6 = sim.Projection(object_cells[4:5],place_cells[6:7],OneToOneConnector(),SYN_K_6)
angular_black_connection_7 = sim.Projection(object_cells[4:5],place_cells[7:8],OneToOneConnector(),SYN_K_7)
angular_black_connection_8 = sim.Projection(object_cells[4:5],place_cells[8:9],OneToOneConnector(),SYN_K_8)
angular_black_connection_9 = sim.Projection(object_cells[4:5],place_cells[9:10],OneToOneConnector(),SYN_K_9)
angular_black_connection_10 = sim.Projection(object_cells[4:5],place_cells[10:11],OneToOneConnector(),SYN_K_10)
angular_black_connection_11 = sim.Projection(object_cells[4:5],place_cells[11:12],OneToOneConnector(),SYN_K_11)
angular_black_connection_12 = sim.Projection(object_cells[4:5],place_cells[12:13],OneToOneConnector(),SYN_K_12)
angular_black_connection_13 = sim.Projection(object_cells[4:5],place_cells[13:14],OneToOneConnector(),SYN_K_13)
angular_black_connection_14 = sim.Projection(object_cells[4:5],place_cells[14:15],OneToOneConnector(),SYN_K_14)
angular_black_connection_15 = sim.Projection(object_cells[4:5],place_cells[15:16],OneToOneConnector(),SYN_K_15)
angular_black_connection_16 = sim.Projection(object_cells[4:5],place_cells[16:17],OneToOneConnector(),SYN_K_16)
angular_black_connection_17 = sim.Projection(object_cells[4:5],place_cells[17:18],OneToOneConnector(),SYN_K_17)
persistent_black_connection_1 = sim.Projection(persistent_neurons[4:5],object_cells[0:1],OneToOneConnector(),SYN_PK_1)
persistent_black_connection_2 = sim.Projection(persistent_neurons[4:5],object_cells[1:2],OneToOneConnector(),SYN_PK_2)
persistent_black_connection_3 = sim.Projection(persistent_neurons[4:5],object_cells[2:3],OneToOneConnector(),SYN_PK_3)
persistent_black_connection_4 = sim.Projection(persistent_neurons[4:5],object_cells[3:4],OneToOneConnector(),SYN_PK_4)
persistent_black_connection_5 = sim.Projection(persistent_neurons[4:5],object_cells[5:6],OneToOneConnector(),SYN_PK_5)
loop_black_connection = sim.Projection(persistent_neurons[4:5], persistent_neurons[4:5], OneToOneConnector(), SYN_M_2, receptor_type = 'excitatory')
black_inibition = sim.Projection(depression_cell[2:3], persistent_neurons[0:4],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')

#Purple-Connection
purple_connection = sim.Projection(sensor_neuron[5:6], persistent_neurons[5:6], OneToOneConnector(), SYN_PF_P, receptor_type = 'excitatory')
purple_linear_sensor = sim.Projection(linear_sensor[5:6],error_neuron[0:1],OneToOneConnector(), SYN_TURN,receptor_type = 'excitatory')
purple_loop = sim.Projection(persistent_neurons[5:6], persistent_neurons[5:6], OneToOneConnector(), SYN_M, receptor_type = 'excitatory')
purple_forgot_connection = sim.Projection(sensor_neuron[5:6], persistent_neurons[0:5], AllToAllConnector(), SYN_PF_E, receptor_type = 'excitatory')
purple_forgot_connection_1 = sim.Projection(sensor_neuron[5:6], place_cells, AllToAllConnector(), SYN_D_S_P, receptor_type = 'inhibitory')
purple_depression = sim.Projection(persistent_neurons[5:6], persistent_neurons[0:5], AllToAllConnector(),SYN_DK, receptor_type = 'inhibitory')

#Green-Connection(This is the final connection)
green_connection = sim.Projection(sensor_neuron[6:7],object_cells[5:6],OneToOneConnector(),SYN_S_OJ,receptor_type = 'excitatory')
green_linear_sensor = sim.Projection(linear_sensor[6:7],feedback,OneToOneConnector(), SYN_TURN,receptor_type = 'excitatory')
angular_green_connection_0 = sim.Projection(object_cells[5:6],place_cells[0:1],OneToOneConnector(),SYN_G_0)
angular_green_connection_1 = sim.Projection(object_cells[5:6],place_cells[1:2],OneToOneConnector(),SYN_G_1)
angular_green_connection_2 = sim.Projection(object_cells[5:6],place_cells[2:3],OneToOneConnector(),SYN_G_2)
angular_green_connection_3 = sim.Projection(object_cells[5:6],place_cells[3:4],OneToOneConnector(),SYN_G_3)
angular_green_connection_4 = sim.Projection(object_cells[5:6],place_cells[4:5],OneToOneConnector(),SYN_G_4)
angular_green_connection_5 = sim.Projection(object_cells[5:6],place_cells[5:6],OneToOneConnector(),SYN_G_5)
angular_green_connection_6 = sim.Projection(object_cells[5:6],place_cells[6:7],OneToOneConnector(),SYN_G_6)
angular_green_connection_7 = sim.Projection(object_cells[5:6],place_cells[7:8],OneToOneConnector(),SYN_G_7)
angular_green_connection_8 = sim.Projection(object_cells[5:6],place_cells[8:9],OneToOneConnector(),SYN_G_8)
angular_green_connection_9 = sim.Projection(object_cells[5:6],place_cells[9:10],OneToOneConnector(),SYN_G_9)
angular_green_connection_10 = sim.Projection(object_cells[5:6],place_cells[10:11],OneToOneConnector(),SYN_G_10)
angular_green_connection_11 = sim.Projection(object_cells[5:6],place_cells[11:12],OneToOneConnector(),SYN_G_11)
angular_green_connection_12 = sim.Projection(object_cells[5:6],place_cells[12:13],OneToOneConnector(),SYN_G_12)
angular_green_connection_13 = sim.Projection(object_cells[5:6],place_cells[13:14],OneToOneConnector(),SYN_G_13)
angular_green_connection_14 = sim.Projection(object_cells[5:6],place_cells[14:15],OneToOneConnector(),SYN_G_14)
angular_green_connection_15 = sim.Projection(object_cells[5:6],place_cells[15:16],OneToOneConnector(),SYN_G_15)
angular_green_connection_16 = sim.Projection(object_cells[5:6],place_cells[16:17],OneToOneConnector(),SYN_G_16)
angular_green_connection_17 = sim.Projection(object_cells[5:6],place_cells[17:18],OneToOneConnector(),SYN_G_17)

#Magenta-Connection
magenta_connection = sim.Projection(sensor_neuron[7:8], depression_cell[7:8], OneToOneConnector(), SYN_B_MB, receptor_type = 'excitatory')
magenta_linear_sensor = sim.Projection(linear_sensor[7:8],error_neuron[1:2],AllToAllConnector(), SYN_TURN,receptor_type = 'excitatory')
magenta_depression = sim.Projection(depression_cell[7:8],persistent_neurons[0:6], AllToAllConnector(), SYN_D_D, receptor_type = 'inhibitory')

#Avoidance-Connection
wall_connection_right = sim.Projection(wall_sensor[0:1],wall_neuron[0:1],OneToOneConnector(),SYN_WR)
wall_connection_left = sim.Projection(wall_sensor[1:2],wall_neuron[1:2], OneToOneConnector(),SYN_WL)

#Inhibition&Angular-HD
depression_1 = sim.Projection(object_cells[0:6], depression_cell[0:1], AllToAllConnector(), SYN_D_IN, receptor_type = 'excitatory')
depression_2 = sim.Projection(depression_cell[0:1],object_cells[0:6], AllToAllConnector(), SYN_D,receptor_type = 'inhibitory')
depression_4 = sim.Projection(persistent_neurons[5:6],depression_cell[0:1], OneToOneConnector(), SYN_D_D, receptor_type = 'inhibitory')
depression_5 = sim.Projection(persistent_neurons[5:6],head_direction_cells[0:18], AllToAllConnector(), SYN_D, receptor_type = 'inhibitory')
#hd_connection = sim.Projection(head_direction_cells, place_cells, OneToOneConnector(), SYN_S_HD,receptor_type = 'excitatory')

#TurnBackInibition
sensor_depression_1 = sim.Projection(persistent_neurons[0:5], depression_cell[3:4], AllToAllConnector(), SYN_TURN_C)
sensor_depression_2 = sim.Projection(depression_cell[3:4],place_cells, AllToAllConnector(), SYN_D_S_P,receptor_type = 'inhibitory')
sensor_depression_3 = sim.Projection(depression_cell[3:4],depression_cell[0:1], OneToOneConnector(), SYN_D,receptor_type = 'inhibitory')

circuit = neurons