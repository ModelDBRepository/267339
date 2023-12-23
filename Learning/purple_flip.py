@nrp.MapVariable("violet_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("violet_right",initial_value = 0, scope = nrp.GLOBAL)
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
def purple_flip (t,violet_left,violet_right,turn_bis,vision_blu,vision_red,vision_black,vision_green,vision_cyan,vision_yellow,vision_purple,vision_indaco):
    if(turn_bis.value == 0 and (vision_blu.value == 0 and vision_red.value == 0 and vision_black.value == 0 and vision_green.value == 0 and vision_cyan.value == 0 and vision_yellow.value == 0 and vision_indaco.value == 0)):
        if (violet_left.value > 0.001 and violet_right.value > 0.001):
            return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(1.0,0,0))
        if(violet_left.value < 0.001 and violet_right.value > 0.001):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-4))
        if(violet_left.value > 0.001 and violet_right.value < 0.001):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,4))