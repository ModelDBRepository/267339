@nrp.MapRobotSubscriber("position", Topic('gazebo/model_states', gazebo_msgs.msg.ModelStates))
@nrp.MapVariable("robot_index", global_key="robot_index", initial_value = None)
@nrp.MapVariable("position_x",scope=nrp.GLOBAL)
@nrp.MapVariable("position_y",scope=nrp.GLOBAL)
@nrp.MapVariable("position_z",scope=nrp.GLOBAL)
@nrp.MapVariable("position_w",scope=nrp.GLOBAL)
@nrp.MapVariable("posizione_x",scope=nrp.GLOBAL)
@nrp.MapVariable("posizione_y",scope=nrp.GLOBAL)
@nrp.MapVariable("t0",scope=nrp.GLOBAL)
@nrp.MapVariable("t1",scope=nrp.GLOBAL)
@nrp.MapVariable("t2",scope=nrp.GLOBAL)
@nrp.MapVariable("t3",scope=nrp.GLOBAL)
@nrp.MapVariable("roll",scope=nrp.GLOBAL)
@nrp.MapVariable("pitch",scope=nrp.GLOBAL)
@nrp.MapVariable("yaw",scope=nrp.GLOBAL)
@nrp.MapVariable("var_angle",scope=nrp.GLOBAL)
@nrp.Robot2Neuron()
def Robot_Position_Learning (t,position,position_x,position_y,position_z,position_w,robot_index,var_angle,t0,t1,t2,t3,roll,pitch,yaw,posizione_x,posizione_y):
    import math
    import numpy as np
    robot_index.value = position.value.name.index('husky')
    
    position_x.value = position.value.pose[robot_index.value].orientation.x
    position_y.value = position.value.pose[robot_index.value].orientation.y
    position_z.value = position.value.pose[robot_index.value].orientation.z
    position_w.value = position.value.pose[robot_index.value].orientation.w
    posizione_x.value = position.value.pose[robot_index.value].position.x
    posizione_y.value = position.value.pose[robot_index.value].position.y
    t0 = 2.0 * (position_w.value * position_x.value + position_y.value * position_z.value)
    t1 = 1.0 - 2.0 * (position_x.value * position_x.value + position_y.value * position_y.value)
    roll.value = math.atan2(t0,t1)
    t2 = 2.0 * (position_w.value * position_y.value - position_z.value * position_x.value)
    t2 = 1.0 if t2 > 1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch.value = math.asin(t2)
    t3 = 2.0 * (position_w.value * position_z.value + position_x.value * position_y.value)
    t4 = 1.0 - 2.0 * (position_y.value * position_y.value + position_z.value * position_z.value)
    yaw.value = math.atan2(t3, t4)
    pi = 22.0/7.0
    var_angle.value = ((yaw.value)/(2*pi))*360
    if var_angle.value < 0:
        var_angle.value = var_angle.value + 360
   