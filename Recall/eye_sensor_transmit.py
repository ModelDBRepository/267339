import sensor_msgs.msg
import numpy as np

@nrp.MapSpikeSource("red_sensor", nrp.brain.sensor_neuron[0:1], nrp.poisson,rng=1234)
@nrp.MapSpikeSource("blue_sensor",nrp.brain.sensor_neuron[1:2],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("yellow_sensor",nrp.brain.sensor_neuron[2:3],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("linear_red", nrp.brain.linear_sensor[0:1], nrp.poisson,rng=1234)
@nrp.MapSpikeSource("linear_blu",nrp.brain.linear_sensor[1:2],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("linear_yellow",nrp.brain.linear_sensor[2:3],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("linear_cyan",nrp.brain.linear_sensor[3:4],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("linear_black",nrp.brain.linear_sensor[4:5],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("linear_purple",nrp.brain.linear_sensor[5:6],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("linear_indigo",nrp.brain.linear_sensor[7:8],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("cyan_sensor",nrp.brain.sensor_neuron[3:4],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("black_sensor",nrp.brain.sensor_neuron[4:5],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("purple_sensor",nrp.brain.sensor_neuron[5:6],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("green_sensor",nrp.brain.sensor_neuron[6:7],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("indigo_sensor",nrp.brain.sensor_neuron[7:8],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("brown_left_sensor",nrp.brain.wall_sensor[0:1],nrp.poisson,rng=1234)
@nrp.MapSpikeSource("brown_right_sensor",nrp.brain.wall_sensor[1:2],nrp.poisson,rng=1234)
@nrp.MapVariable("red",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("blue",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("yellow",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("cyan",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("violet",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("black",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("green",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("indigo",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("brown_left", scope = nrp.GLOBAL)
@nrp.MapVariable("brown_right", scope = nrp.GLOBAL)
@nrp.Robot2Neuron()


def eye_sensor_transmit (t,red_sensor,blue_sensor,yellow_sensor,cyan_sensor,purple_sensor,green_sensor,indigo_sensor,black_sensor,brown_left_sensor,brown_right_sensor,brown_left,brown_right,linear_red,linear_blu,linear_yellow,linear_cyan,linear_purple,linear_black, linear_indigo,red,blue,black,green,yellow,cyan,violet,indigo):
    
    import numpy as np
   
    def gaussian ( x, mi, sig):
        return np.exp(-np.power(x-mi,2.) / ( 2 * np.power(sig,2.)))
    
    if(red.value < 0.3):
        red_sensor.rate = gaussian(red.value,0.055,0.07)*8005
    if(red.value > 0.3):
        red_sensor.rate = red.value
    if(blue.value < 0.3):
        blue_sensor.rate = gaussian(blue.value, 0.055, 0.07)*8005
    if(blue.value > 0.3):
        blue_sensor.rate = blue.value
    if(black.value < 0.3):
        black_sensor.rate = gaussian(black.value, 0.055, 0.07)*8005
    if(black.value > 0.3):
        black_sensor.rate = black.value
    if(yellow.value < 0.3):
        yellow_sensor.rate = gaussian(yellow.value, 0.055, 0.07)*8005
    if(yellow.value > 0.3):
        yellow_sensor.rate = yellow.value
    if(cyan.value < 0.3):
        cyan_sensor.rate = gaussian(cyan.value, 0.055, 0.07)*8005
    if(cyan.value > 0.3):
        cyan_sensor.rate = cyan.value
    purple_sensor.rate = gaussian(violet.value, 0.055, 0.07)*8005
    if(green.value < 0.3):
        green_sensor.rate = gaussian(green.value, 0.055, 0.07)*8005
    if(green.value > 0.3):
        green_sensor.rate = green.value
    indigo_sensor.rate = gaussian(indigo.value, 0.055, 0.07)*8500
    linear_red.rate = gaussian(red.value,0.005,0.005)*7500
    linear_blu.rate = gaussian(blue.value,0.005,0.005)*7500
    linear_yellow.rate = gaussian(yellow.value,0.005,0.0045)*7500
    linear_cyan.rate = gaussian(cyan.value,0.0045,0.005)*7500
    linear_purple.rate = gaussian(violet.value,0.005,0.005)*7500
    linear_black.rate = gaussian(black.value,0.005,0.005)*7500
    linear_indigo.rate = gaussian(indigo.value,0.005,0.005)*7500
    
    if(brown_left.value > 0.4):
        brown_left_sensor.rate = 8000
    elif(brown_left.value < 0.4):
        brown_left_sensor.rate = 0
    if(brown_right.value > 0.4):
        brown_right_sensor.rate = 8000
    if(brown_right.value < 0.4):
        brown_right_sensor.rate = 0