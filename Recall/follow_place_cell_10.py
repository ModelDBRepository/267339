@nrp.MapSpikeSink("Place_10",nrp.brain.place_cells[10:11],nrp.spike_recorder)
@nrp.MapSpikeSink("brown_left_output", nrp.brain.wall_neuron[1:2],nrp.spike_recorder)
@nrp.MapSpikeSink("brown_right_output", nrp.brain.wall_neuron[0:1],nrp.spike_recorder)
@nrp.MapVariable("var_angle",scope=nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def follow_place_cell_10 (t,Place_10,brown_left_output,brown_right_output,var_angle):
    
    if(brown_left_output.spiked and brown_right_output.spiked):
        return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(-2,0,0))
    elif (brown_left_output.spiked):
        return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(1,0,0),angular=geometry_msgs.msg.Vector3(0,0,4))
    elif (brown_right_output.spiked):
        return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(1,0,0),angular=geometry_msgs.msg.Vector3(0,0,-4))
    
    if Place_10.spiked:
            if(var_angle.value <= 220 and var_angle.value >200):
                return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(1,0,0))
            elif(var_angle.value <= 200 and var_angle.value >40):
                return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.0))
            elif(var_angle.value <= 40 and var_angle.value > 0):
                return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.0))
            elif(var_angle.value <= 360 and angle.value > 220):
                return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.0))