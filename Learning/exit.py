@nrp.MapVariable("green_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("green_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("green",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("turn_f",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("start_record",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_blu",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_red",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_black",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_green",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_cyan",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_yellow",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_purple",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_indaco",initial_value = 0,scope = nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def exit (t,green_left,green_right,green,turn_f,start_record,vision_blu,vision_black,vision_red,vision_cyan,vision_yellow,vision_purple,vision_indaco,vision_green):
    if(turn_f.value == 0 and (vision_red.value == 0 and vision_blu.value == 0 and vision_cyan.value == 0 and vision_purple.value == 0 and vision_indaco.value == 0 and vision_yellow.value == 0)):
        if(green.value > 0.25 and green.value < 0.3):
            start_record.value = 1
            return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(0.0,0,0))
        if (green_left.value > 0.0025 and green_right.value > 0.00018):
            vision_green.value = 1
            return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(1.0,0,0))
        if (green_left.value < 0.0025 and green_right.value > 0.00018):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.0))
        if(green_left.value > 0.0025 and green_right.value < 0.00018):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.0))