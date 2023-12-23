import hbp_nrp_cle.tf_framework as nrp
#@nrp.MapSpikeSource("angular_cell", nrp.map_neurons(range(0,6), lambda i: nrp.brain.angular_cells[i]), nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_0",nrp.brain.head_direction_cells[0:1],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_1",nrp.brain.head_direction_cells[1:2],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_2",nrp.brain.head_direction_cells[2:3],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_3",nrp.brain.head_direction_cells[3:4],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_4",nrp.brain.head_direction_cells[4:5],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_5",nrp.brain.head_direction_cells[5:6],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_6",nrp.brain.head_direction_cells[6:7],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_7",nrp.brain.head_direction_cells[7:8],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_8",nrp.brain.head_direction_cells[8:9],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_9",nrp.brain.head_direction_cells[9:10],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_10",nrp.brain.head_direction_cells[10:11],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_11",nrp.brain.head_direction_cells[11:12],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_12",nrp.brain.head_direction_cells[12:13],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_13",nrp.brain.head_direction_cells[13:14],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_14",nrp.brain.head_direction_cells[14:15],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_15",nrp.brain.head_direction_cells[15:16],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_16",nrp.brain.head_direction_cells[16:17],nrp.poisson)
@nrp.MapSpikeSource("head_direction_cells_17",nrp.brain.head_direction_cells[17:18],nrp.poisson)
@nrp.MapVariable("angle",scope=nrp.GLOBAL)
@nrp.Robot2Neuron()
def propagate_angular_cells_spike (t,angle,head_direction_cells_0,head_direction_cells_1,head_direction_cells_2,head_direction_cells_3,head_direction_cells_4,head_direction_cells_5,head_direction_cells_6,head_direction_cells_7,head_direction_cells_8,head_direction_cells_9,head_direction_cells_10,head_direction_cells_11,head_direction_cells_12,head_direction_cells_13,head_direction_cells_14,head_direction_cells_15,head_direction_cells_16,head_direction_cells_17):
    
        
        if (angle.value <= 20 and angle.value > 0):
            head_direction_cells_0.rate = 8000
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0
        
        if (angle.value <= 40 and angle.value > 20):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 8000
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0

        
        if (angle.value <= 60 and angle.value > 40):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 8000
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0

            
        if (angle.value <= 80 and angle.value > 60):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 8000
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0
            
        if (angle.value <= 100 and angle.value > 80):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 8000
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0
            
        if (angle.value <= 120 and angle.value > 100):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 8000
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0
            
        if (angle.value <= 140 and angle.value > 120):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 8000
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0

       
        if (angle.value <= 160 and angle.value > 140):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 8000
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0
        
        if (angle.value <= 180 and angle.value > 160):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 8000
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0
            
        if (angle.value <= 200 and angle.value > 180):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 8000
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0

        
        if (angle.value <= 220 and angle.value > 200):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 8000
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0
            
        if (angle.value <= 240 and angle.value > 220):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 8000
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0

        
        if (angle.value <= 260 and angle.value > 240):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 8000
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0
        
        if (angle.value <= 280 and angle.value > 260):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 8000
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0
        
        if (angle.value <= 300 and angle.value > 280):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 8000
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0
        
        if (angle.value <= 320 and angle.value > 300):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 8000
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 0.0
        
        if (angle.value <= 340 and angle.value > 320):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 8000
            head_direction_cells_17.rate = 0.0
        
        if (angle.value <= 360 and angle.value > 340):
            head_direction_cells_0.rate = 0.0
            head_direction_cells_1.rate = 0.0
            head_direction_cells_2.rate = 0.0
            head_direction_cells_3.rate = 0.0
            head_direction_cells_4.rate = 0.0
            head_direction_cells_5.rate = 0.0
            head_direction_cells_6.rate = 0.0
            head_direction_cells_7.rate = 0.0
            head_direction_cells_8.rate = 0.0
            head_direction_cells_9.rate = 0.0
            head_direction_cells_10.rate = 0.0
            head_direction_cells_11.rate = 0.0
            head_direction_cells_12.rate = 0.0
            head_direction_cells_13.rate = 0.0
            head_direction_cells_14.rate = 0.0
            head_direction_cells_15.rate = 0.0
            head_direction_cells_16.rate = 0.0
            head_direction_cells_17.rate = 8000

    