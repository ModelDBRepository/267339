@nrp.MapVariable("blue_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("blue_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("blue",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("turn_f",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("turn_bis",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_blu",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_red",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_black",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_green",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_turquoise",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_yellow",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_purple",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_indaco",initial_value = 0,scope = nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def follow_blue (t,blue_left,blue_right,blue,turn_f,vision_blu,vision_red,vision_black,vision_green,vision_turquoise,vision_yellow,vision_purple,vision_indaco,turn_bis):
    if(turn_f.value == 0 and turn_bis.value == 0 and(vision_red.value == 0 and vision_black.value == 0 and vision_green.value == 0 and vision_turquoise.value == 0 and vision_purple.value == 0 and vision_indaco.value == 0 and vision_yellow.value == 0)):
        if (blue_left.value > 0.0001 and blue_right.value > 0.0014):
            vision_blu.value = 1
            return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(1.0,0,0))
        if(blue_left.value < 0.0001 and blue_right.value > 0.0014):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-4))
        if(blue_left.value > 0.0001 and blue_right.value < 0.0014):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,4))