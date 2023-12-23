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
#import neo
#from quantities import ms
nest.SetKernelStatus({'dict_miss_is_error': False})
logger = logging.getLogger(__name__)
nest.ResetKernel()

#sim.setup(timestep=0.1)

"""
Initializes PyNN with the minimal neuronal network
"""


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
SYN_F_IN = sim.StaticSynapse(weight = 0.013, delay = 0.1)
SYN_TURN = sim.StaticSynapse(weight = 0.02811, delay = 0.1)
SYN_TURN_F = sim.StaticSynapse(weight = 0.0275, delay = 0.1)
SYN_TURN_C = sim.StaticSynapse(weight = 0.005, delay = 0.1)
SYN_TURN_B = sim.StaticSynapse(weight = 0.0285, delay = 0.1)
SYN_DEP = sim.StaticSynapse(weight = 0.003, delay = 0.1)
SYN_WL = sim.StaticSynapse(weight = 3.0, delay = 0.1)
SYN_WR = sim.StaticSynapse(weight = 3.0, delay = 0.1)

#Inhibition and activation Synapse
SYN_D_IN = sim.StaticSynapse(weight = 0.1, delay = 0.1)
SYN_D = sim.StaticSynapse(weight = 4.5, delay = 0.1)
#Inhibitory-Inhibitory Synapse 
SYN_D_D = sim.StaticSynapse(weight = 9.0, delay = 0.1)
SYN_DK = sim.StaticSynapse(weight = 1.0, delay = 0.1)
SYN_M = sim.TsodyksMarkramSynapse(weight=0.3, delay= 20.0, U=0.5, tau_rec=100.0, tau_facil=10.0)
SYN_M_2 = sim.TsodyksMarkramSynapse(weight=0.2, delay= 55.0, U=0.5, tau_rec=100.0, tau_facil=10.0)
SYN_D_S = sim.StaticSynapse(weight = 12.0, delay = 0.1)
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
#Pynn STDP rule 

#STDP Rule for Potentiation/Depression simultaneous phase
standard = STDPMechanism(
          weight=0.007,  
          delay="3.5",
          dendritic_delay_fraction=1,
          timing_dependence=SpikePairRule(tau_plus=13.0, tau_minus=30.0,
                                          A_plus=0.2, A_minus=0.12),
          weight_dependence=AdditiveWeightDependence(w_min=0.0, w_max=0.04))


standard_persistent = STDPMechanism(
          weight=0.007,
          delay="5.5",
          dendritic_delay_fraction=1,
          timing_dependence=SpikePairRule(tau_plus=15.0, tau_minus=30.0,
                                          A_plus=0.2, A_minus=0.12),
          weight_dependence=AdditiveWeightDependence(w_min=0.0, w_max=0.04))




#Red-Connection

red_connection =sim.Projection(sensor_neuron[0:1],object_cells[0:1],OneToOneConnector(),SYN_S_OJ,receptor_type='excitatory')
red_linear_sensor = sim.Projection(sensor_neuron[0:1], feedback, OneToOneConnector(), SYN_TURN, receptor_type = 'excitatory')
sensor_red_connection = sim.Projection(sensor_neuron[0:1],persistent_neurons[0:1],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
inib_red_connection = sim.Projection(sensor_neuron[0:1],depression_cell[1:2],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
angular_red_connection = sim.Projection(object_cells[0:1],place_cells,AllToAllConnector(),standard,receptor_type = 'excitatory')
persistent_red_connection = sim.Projection(persistent_neurons[0:1],object_cells[1:6],AllToAllConnector(),standard_persistent)
loop_red_connection = sim.Projection(persistent_neurons[0:1], persistent_neurons[0:1], OneToOneConnector(), SYN_M_2, receptor_type = 'excitatory')
red_inibition = sim.Projection(depression_cell[1:2], persistent_neurons[1:5],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')

#Blue-Connection
blue_connection = sim.Projection(sensor_neuron[1:2],object_cells[1:2],OneToOneConnector(),SYN_S_OJ, receptor_type = 'excitatory')
blue_linear_sensor = sim.Projection(sensor_neuron[1:2], feedback, OneToOneConnector(), SYN_TURN, receptor_type = 'excitatory')
sensor_blue_connection = sim.Projection(sensor_neuron[1:2],persistent_neurons[1:2],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
inib_blue_connection = sim.Projection(sensor_neuron[1:2],depression_cell[8:9],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
angular_blue_connection = sim.Projection(object_cells[1:2],place_cells,AllToAllConnector(),standard)
persistent_blue_connection = sim.Projection(persistent_neurons[1:2],object_cells[0:1],OneToOneConnector(),standard_persistent)
persistent_blue1_connection = sim.Projection(persistent_neurons[1:2],object_cells[2:6],AllToAllConnector(),standard_persistent)
loop_blue_connection = sim.Projection(persistent_neurons[1:2], persistent_neurons[1:2], OneToOneConnector(), SYN_M_2, receptor_type = 'excitatory')
blue_inibition = sim.Projection(depression_cell[8:9], persistent_neurons[0:1],OneToOneConnector(), SYN_D_S, receptor_type = 'inhibitory')
blue_inibition_1 = sim.Projection(depression_cell[8:9], persistent_neurons[2:5],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')

#Yellow-Connection
yellow_connection = sim.Projection(sensor_neuron[2:3], object_cells[2:3], OneToOneConnector(),SYN_S_OJ,receptor_type='excitatory')
yellow_linear_sensor = sim.Projection(sensor_neuron[2:3], feedback, OneToOneConnector(), SYN_TURN, receptor_type = 'excitatory')
sensor_yellow_connection = sim.Projection(sensor_neuron[2:3],persistent_neurons[2:3],OneToOneConnector(), SYN_B_MB,receptor_type = 'excitatory')
inib_yellow_connection = sim.Projection(sensor_neuron[2:3],depression_cell[9:10],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
angular_yellow_connection = sim.Projection(object_cells[2:3], place_cells, AllToAllConnector(), standard)
persistent_yellow_connection = sim.Projection(persistent_neurons[2:3],object_cells[0:2],AllToAllConnector(),standard_persistent)
persistent_yellow1_connection = sim.Projection(persistent_neurons[2:3], object_cells[3:6],AllToAllConnector(),standard_persistent)
loop_yellow_connection = sim.Projection(persistent_neurons[2:3], persistent_neurons[2:3], OneToOneConnector(), SYN_M_2, receptor_type = 'excitatory')
yellow_inibition = sim.Projection(depression_cell[9:10], persistent_neurons[0:2],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')
yellow_inibition_1 = sim.Projection(depression_cell[9:10], persistent_neurons[3:5],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')

#Cyan-Connection
cyan_connection = sim.Projection(sensor_neuron[3:4],object_cells[3:4], OneToOneConnector(),SYN_S_OJ,receptor_type='excitatory')
sensor_cyan_connection = sim.Projection(sensor_neuron[3:4],persistent_neurons[3:4],OneToOneConnector(), SYN_B_MB,receptor_type = 'excitatory')
cyan_linear_sensor = sim.Projection(sensor_neuron[3:4],feedback,OneToOneConnector(), SYN_TURN,receptor_type = 'excitatory')
inib_cyan_connection = sim.Projection(sensor_neuron[3:4],depression_cell[10:11],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
angular_cyan_connection = sim.Projection(object_cells[3:4], place_cells, AllToAllConnector(), standard)
persistent_cyan_connection = sim.Projection(persistent_neurons[3:4],object_cells[0:3],AllToAllConnector(),standard_persistent)
persistent_cyan1_connection = sim.Projection(persistent_neurons[3:4], object_cells[4:6],AllToAllConnector(),standard_persistent)
loop_cyan_connection = sim.Projection(persistent_neurons[3:4], persistent_neurons[3:4], OneToOneConnector(), SYN_M_2, receptor_type = 'excitatory')
cyan_inibition = sim.Projection(depression_cell[10:11], persistent_neurons[0:3],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')
cyan_inibition_1 = sim.Projection(depression_cell[10:11], persistent_neurons[4:5],OneToOneConnector(), SYN_D_S, receptor_type = 'inhibitory')

#Black-Connection
black_connection = sim.Projection(sensor_neuron[4:5], object_cells[4:5], OneToOneConnector(), SYN_S_OJ, receptor_type = 'excitatory')
black_linear_sensor = sim.Projection(sensor_neuron[4:5],feedback,OneToOneConnector(), SYN_TURN,receptor_type = 'excitatory')
sensor_black_connection = sim.Projection(sensor_neuron[4:5],persistent_neurons[4:5],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
inib_black_connection = sim.Projection(sensor_neuron[4:5],depression_cell[2:3],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
angular_black_connection = sim.Projection(object_cells[4:5],place_cells,AllToAllConnector(),standard)
persistent_black_connection = sim.Projection(persistent_neurons[4:5],object_cells[0:4],AllToAllConnector(),standard_persistent)
persistent_black1_connection = sim.Projection(persistent_neurons[4:5],object_cells[5:6],AllToAllConnector(),standard_persistent)
loop_black_connection = sim.Projection(persistent_neurons[4:5], persistent_neurons[4:5], OneToOneConnector(), SYN_M_2, receptor_type = 'excitatory')
black_inibition = sim.Projection(depression_cell[2:3], persistent_neurons[0:4],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')

#Purple-Connection
purple_connection = sim.Projection(sensor_neuron[5:6], persistent_neurons[5:6], OneToOneConnector(), SYN_PF_P, receptor_type = 'excitatory')
purple_linear_sensor = sim.Projection(sensor_neuron[5:6],error_neuron[0:1],OneToOneConnector(), SYN_TURN,receptor_type = 'excitatory')
purple_loop = sim.Projection(persistent_neurons[5:6], persistent_neurons[5:6], OneToOneConnector(), SYN_M, receptor_type = 'excitatory')
purple_forgot_connection = sim.Projection(sensor_neuron[5:6], persistent_neurons[0:5], AllToAllConnector(), SYN_PF_E, receptor_type = 'excitatory')
purple_depression = sim.Projection(persistent_neurons[5:6], persistent_neurons[0:5], AllToAllConnector(),SYN_DK, receptor_type = 'inhibitory')

#Green-Connection
green_connection = sim.Projection(sensor_neuron[6:7],object_cells[5:6],OneToOneConnector(),SYN_S_OJ,receptor_type = 'excitatory')
inib_green_connection = sim.Projection(sensor_neuron[6:7],depression_cell[4:5],OneToOneConnector(),SYN_B_MB,receptor_type='excitatory')
angular_green_connection = sim.Projection(object_cells[5:6],place_cells,AllToAllConnector(),standard)
green_inibition = sim.Projection(depression_cell[4:5], persistent_neurons[0:5],AllToAllConnector(), SYN_D_S, receptor_type = 'inhibitory')

#-Connection
magenta_connection = sim.Projection(sensor_neuron[7:8], depression_cell[7:8], OneToOneConnector(), SYN_B_MB, receptor_type = 'excitatory')
magenta_linear_sensor = sim.Projection(sensor_neuron[7:8],error_neuron[1:2],AllToAllConnector(), SYN_TURN,receptor_type = 'excitatory')
magenta_depression = sim.Projection(depression_cell[7:8],persistent_neurons[0:6], AllToAllConnector(), SYN_D_D, receptor_type = 'inhibitory')

#Avoidance-Connection
wall_connection_right = sim.Projection(wall_sensor[0:1],wall_neuron[0:1],OneToOneConnector(),SYN_WR)
wall_connection_left = sim.Projection(wall_sensor[1:2],wall_neuron[1:2], OneToOneConnector(),SYN_WL)

#Inhibition&Angular-HD
depression_1 = sim.Projection(object_cells[0:6], depression_cell[0:1], AllToAllConnector(), SYN_D_IN, receptor_type = 'excitatory')
depression_2 = sim.Projection(depression_cell[0:1],object_cells[0:6], AllToAllConnector(), SYN_D,receptor_type = 'inhibitory')
depression_4 = sim.Projection(persistent_neurons[5:6],depression_cell[0:1], OneToOneConnector(), SYN_D_D, receptor_type = 'inhibitory')
depression_5 = sim.Projection(persistent_neurons[5:6],head_direction_cells[0:18], AllToAllConnector(), SYN_D, receptor_type = 'inhibitory')
hd_connection = sim.Projection(head_direction_cells, place_cells, OneToOneConnector(), SYN_S_HD,receptor_type = 'excitatory')

#TurnBackInibition
turnback_depression_1 = sim.Projection(persistent_neurons[0:5], depression_cell[3:4], AllToAllConnector(), SYN_TURN_C)
turnback_depression_2 = sim.Projection(depression_cell[3:4],place_cells, AllToAllConnector(), SYN_D_S_P,receptor_type = 'inhibitory')
turnback_depression_3 = sim.Projection(depression_cell[3:4],depression_cell[0:1], OneToOneConnector(), SYN_D,receptor_type = 'inhibitory')

   
circuit = neurons
