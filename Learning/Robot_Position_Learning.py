@nrp.MapRobotSubscriber("position", Topic('gazebo/model_states', gazebo_msgs.msg.ModelStates))
@nrp.MapVariable("robot_index", global_key="robot_index", initial_value = None)
@nrp.MapVariable("angular_x",scope=nrp.GLOBAL)
@nrp.MapVariable("angular_y",scope=nrp.GLOBAL)
@nrp.MapVariable("angular_z",scope=nrp.GLOBAL)
@nrp.MapVariable("angular_w",scope=nrp.GLOBAL)
@nrp.MapVariable("position_x",scope=nrp.GLOBAL)
@nrp.MapVariable("position_y",scope=nrp.GLOBAL)
@nrp.MapVariable("position_z",scope=nrp.GLOBAL)
@nrp.MapVariable("t0",scope=nrp.GLOBAL)
@nrp.MapVariable("t1",scope=nrp.GLOBAL)
@nrp.MapVariable("t2",scope=nrp.GLOBAL)
@nrp.MapVariable("t3",scope=nrp.GLOBAL)
@nrp.MapVariable("roll",scope=nrp.GLOBAL)
@nrp.MapVariable("pitch",scope=nrp.GLOBAL)
@nrp.MapVariable("yaw",scope=nrp.GLOBAL)
@nrp.MapVariable("angle",scope=nrp.GLOBAL)
@nrp.Robot2Neuron()
def Robot_Position_Learning (t,position,position_x,position_y,position_z,robot_index,angle,t0,t1,t2,t3,roll,pitch,yaw,angular_x,angular_y,angular_z,angular_w):
    import math
    import numpy as np
    robot_index.value = position.value.name.index('husky')
    
    angular_x.value = position.value.pose[robot_index.value].orientation.x
    angular_y.value = position.value.pose[robot_index.value].orientation.y
    angular_z.value = position.value.pose[robot_index.value].orientation.z
    angular_w.value = position.value.pose[robot_index.value].orientation.w
    position_x.value = position.value.pose[robot_index.value].position.x
    position_y.value = position.value.pose[robot_index.value].position.y
    position_z.value = position.value.pose[robot_index.value].position.z
    t0 = 2.0 * (angular_w.value * angular_x.value + angular_y.value * angular_z.value)
    t1 = 1.0 - 2.0 * (angular_x.value * angular_x.value + angular_y.value * angular_y.value)
    roll.value = math.atan2(t0,t1)
    t2 = 2.0 * (angular_w.value * angular_y.value - angular_z.value * angular_x.value)
    t2 = 1.0 if t2 > 1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch.value = math.asin(t2)
    t3 = 2.0 * (angular_w.value * angular_z.value + angular_x.value * angular_y.value)
    t4 = 1.0 - 2.0 * (angular_y.value * angular_y.value + angular_z.value * angular_z.value)
    yaw.value = math.atan2(t3, t4)
    pi = 22.0/7.0
    angle.value = ((yaw.value)/(2*pi))*360
    if angle.value < 0:
        angle.value = angle.value + 360

    