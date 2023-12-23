@nrp.MapVariable("turn_f",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("turn_bis",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("turn_ter",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("choice", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("starting_time", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("flag", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("start_choice", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("vision_blu",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_red",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_black",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_green",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_cyan",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_yellow",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_purple",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("vision_indaco",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("second_obj",initial_value = 0,scope = nrp.GLOBAL)
@nrp.Neuron2Robot(Topic('/husky/husky/cmd_vel', geometry_msgs.msg.Twist))
def turn (t,turn_f, choice,start_choice,flag,starting_time,turn_bis,turn_ter,vision_blu,vision_red,vision_black,vision_green,vision_cyan,vision_yellow,vision_purple,vision_indaco,second_obj):
    if(turn_f.value == 1 and flag.value == 0):
        starting_time.value = t
        flag.value = 1
    if(turn_bis.value == 1 and flag.value == 0):
        starting_time.value = t
        flag.value = 1
        
    if(turn_f.value == 1 and choice.value == 0):
        if(t < starting_time.value + 10.5):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.0))
        elif(t > starting_time.value + 10.5):
            vision_blu.value = 0
            vision_red.value = 0
            vision_black.value = 0
            vision_green.value = 0
            vision_yellow.value = 0
            vision_indaco.value = 0
            vision_purple.value = 0
            vision_cyan.value = 0
            start_choice.value = 1
            flag.value = 0

    
    if(turn_f.value == 1 and (choice.value == 2 or choice.value == 5)):
        if(turn_ter.value == 0):
            if(second_obj.value == 0):
                if (t < starting_time.value + 1.3):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-3.0))
                if (t > starting_time.value + 1.3 and t < starting_time.value + 3.0):
                    return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(3.5,0,0))
                if (t > starting_time.value + 3.0 and t < starting_time.value + 4.0):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.5))
            if(second_obj.value == 1):
                if (t < starting_time.value + 1.3):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.5))
                if (t > starting_time.value + 1.3 and t < starting_time.value + 4.0):
                    return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(4.0,0,0))
        if(turn_ter.value == 1):
            if(second_obj.value == 0):
                if (t < starting_time.value + 1.2):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.3))
                if (t > starting_time.value + 1.2 and t < starting_time.value + 3.0):
                    return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(3.5,0,0))
            if(second_obj.value == 1):
                if (t < starting_time.value + 1.2):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.3))
                if (t > starting_time.value + 1.2 and t < starting_time.value + 3.0):
                    return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(3.5,0,0))
        if(t > starting_time.value + 4.0):
            if(second_obj.value == 1):
                second_obj.value = 0
            else:
                second_obj.value = 1
            vision_blu.value = 0
            vision_red.value = 0
            vision_black.value = 0
            vision_green.value = 0
            vision_yellow.value = 0
            vision_indaco.value = 0
            vision_purple.value = 0
            vision_cyan.value = 0
            turn_f.value = 0
            flag.value = 0
 
    
    if(turn_f.value == 1 and choice.value == 3):
        if(turn_ter.value == 0):
            if(second_obj.value == 0):
                if (t < starting_time.value + 1.2):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.3))
                if (t > starting_time.value + 1.2 and t < starting_time.value + 3.0):
                    return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(3.0,0,0))
            if(second_obj.value == 1):
                if (t < starting_time.value + 1.2):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.5))
                if (t > starting_time.value + 1.2 and t < starting_time.value + 3.0):
                    return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(4.5,0,0))
                if(t > starting_time.value + 3.0 and t < starting_time.value + 3.5):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.0))
        if(turn_ter.value == 1):
            if(second_obj.value == 0):
                if (t < starting_time.value + 1.2):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.35))
                if (t > starting_time.value + 1.2 and t < starting_time.value + 3.5):
                    return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(4.0,0,0))
                if (t > starting_time.value + 3.0 and t < starting_time.value + 3.5):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-3.5))
                if(t > starting_time.value + 3.5 and t < starting_time.value + 4.0):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(4.0,0,0))
                #if(t > starting_time.value + 4.0 and t < starting_time.value + 4.5):
                    #return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(4.0,0,-3.5))
            if(second_obj.value == 1):
                if (t < starting_time.value + 1.2):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.3))
                if (t > starting_time.value + 1.2 and t < starting_time.value + 3.0):
                    return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(3.5,0,0))
        if(t > starting_time.value + 4.0):
            if(second_obj.value == 1):
                second_obj.value = 0
            else:
                second_obj.value = 1
            vision_blu.value = 0
            vision_red.value = 0
            vision_black.value = 0
            vision_green.value = 0
            vision_yellow.value = 0
            vision_indaco.value = 0
            vision_purple.value = 0
            vision_cyan.value = 0
            turn_f.value = 0
            flag.value = 0
    
    if(turn_f.value == 1 and choice.value == 4):
        if(turn_ter.value == 0):
            if(second_obj.value == 0):
                if (t < starting_time.value + 1.0):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.3))
                if (t > starting_time.value + 1.0 and t < starting_time.value + 2.5):
                    return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(4.0,0,0))
                if(t > starting_time.value + 2.5 and t < starting_time.value + 3.5):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,1.5))
            if(second_obj.value == 1):
                if (t < starting_time.value + 1.0):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.5))
                if (t > starting_time.value + 1.0 and t < starting_time.value + 2.5):
                    return geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(3.5,0,0))
        if(turn_ter.value == 1):
            if(second_obj.value == 0):
                if (t < starting_time.value + 1.0):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.4))
                if (t > starting_time.value + 1.0 and t < starting_time.value + 2.5):
                    return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(4.0,0,0))
                if(t > starting_time.value + 2.5 and t < starting_time.value + 3.5):
                    return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(4.5,0,0))
                    
                if (t > starting_time.value + 3.5 and t < starting_time.value + 4.5):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-3.6))
                    
            if(second_obj.value == 1):
                if (t < starting_time.value + 1.0):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,-2.5))
                if (t > starting_time.value + 1.0 and t < starting_time.value + 2.5):
                    return geometry_msgs.msg.Twist(linear = geometry_msgs.msg.Vector3(3.5,0,0))
                if(t > starting_time.value + 2.5 and t < starting_time.value + 3.5):
                    return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,3.5))
        if (t > starting_time.value + 3.5):
            if(second_obj.value == 0):
                second_obj.value = 1
            else:
                second_obj.value = 0
            vision_blu.value = 0
            vision_red.value = 0
            vision_black.value = 0
            vision_green.value = 0
            vision_yellow.value = 0
            vision_indaco.value = 0
            vision_purple.value = 0
            vision_cyan.value = 0
            turn_f.value = 0
            flag.value = 0
    

    
    if(turn_bis.value == 1):
        if (t < starting_time.value + 4.0):
            return geometry_msgs.msg.Twist(angular=geometry_msgs.msg.Vector3(0,0,2.0))
        if (t > starting_time.value + 4.0):
            vision_blu.value = 0
            vision_red.value = 0
            vision_black.value = 0
            vision_green.value = 0
            vision_yellow.value = 0
            vision_indaco.value = 0
            vision_purple.value = 0
            vision_cyan.value = 0
            turn_bis.value = 0
            flag.value = 0