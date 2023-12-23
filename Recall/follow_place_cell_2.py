@nrp.MapSpikeSink("Place_2",nrp.brain.place_cells[2:3],nrp.spike_recorder)
@nrp.MapSpikeSink("brown_left_output", nrp.brain.wall_neuron[1:2],nrp.spike_recorder)
@nrp.MapSpikeSink("brown_right_output", nrp.brain.wall_neuron[0:1],nrp.spike_recorder)
@nrp.MapVariable("var_angle",scope=nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def follow_place_cell_2 (t,Place_2,brown_left_output,brown_right_output,var_angle):
    
    if(brown_left_output.spiked and brown_right_output.spiked):
        return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(-2,0,0))
    elif (brown_left_output.spiked):
        return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(1,0,0),angular=geometry_msgs.msg.Vector3(0,0,4))
    elif (brown_right_output.spiked):
        return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(1,0,0),angular=geometry_msgs.msg.Vector3(0,0,-4))
    
    if Place_2.spiked:
        if(var_angle.value <= 60 and var_angle.value > 40):
            return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(1,0,0))
        elif(var_angle.value <= 40 or var_angle.value > 240):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.0))
        elif(var_angle.value <= 240 and var_angle.value > 60):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.0))