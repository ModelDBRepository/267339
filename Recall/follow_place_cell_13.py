@nrp.MapSpikeSink("Place_13",nrp.brain.place_cells[13:14],nrp.spike_recorder)
@nrp.MapSpikeSink("brown_left_output", nrp.brain.wall_neuron[1:2],nrp.spike_recorder)
@nrp.MapSpikeSink("brown_right_output", nrp.brain.wall_neuron[0:1],nrp.spike_recorder)
@nrp.MapVariable("var_angle",scope=nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def follow_place_cell_13 (t,Place_13,brown_left_output,brown_right_output,var_angle):
    
    if(brown_left_output.spiked and brown_right_output.spiked):
        return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(-2,0,0))
    elif (brown_left_output.spiked):
        return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(1,0,0),angular=geometry_msgs.msg.Vector3(0,0,4))
    elif (brown_right_output.spiked):
        return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(1,0,0),angular=geometry_msgs.msg.Vector3(0,0,-4))
    
    if Place_13.spiked:
            if(var_angle.value <= 280 and var_angle.value >260):
                return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(1,0,0))
            elif(var_angle.value <= 260 and var_angle.value > 100):
                return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.0))
            elif(var_angle.value <= 100 and var_angle.value > 0):
                return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.0))
            elif(var_angle.value <= 360 and var_angle.value > 280):
                return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.0))