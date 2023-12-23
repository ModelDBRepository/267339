@nrp.MapVariable("yellow_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("yellow_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("yellow",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("turn_f",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("turn_bis",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_blu",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_red",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_black",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_green",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_cyan",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_yellow",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_purple",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_indaco",initial_value = 0,scope = nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def follow_yellow (t,yellow_left,yellow_right,yellow,turn_f,vision_blu,vision_red,vision_black,vision_green,vision_cyan,vision_yellow,vision_purple,vision_indaco,turn_bis):
    if(turn_f.value == 0 and turn_bis.value == 0 and  (vision_cyan.value == 0 and vision_blu.value == 0 and vision_green.value == 0 and vision_black.value == 0 and vision_purple.value == 0 and vision_indaco.value == 0 and vision_red.value == 0)):
        if (yellow_left.value > 0.001 and yellow_right.value > 0.0016):
            vision_yellow.value = 1
            return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(1.0,0,0))
        if(yellow_left.value < 0.001 and yellow_right.value > 0.0016):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2))
        if(yellow_left.value > 0.001 and yellow_right.value < 0.0016):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2))